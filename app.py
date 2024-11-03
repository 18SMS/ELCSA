from flask import Flask, render_template, request, redirect, url_for
import plotly
import plotly.express as px
import json
import csv
import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib
from static.questuestions import preguntas
matplotlib.use('Agg')

app = Flask(__name__)

if not os.path.exists('static'):
    os.makedirs('static')

def obtener_ids_preguntas(preguntas_o_secciones):
    ids = []
    for item in preguntas_o_secciones:
        if 'id' in item:
            # Es una pregunta
            clave = f'P{item["id"]}'
            ids.append(clave)
            if 'condicional' in item:
                for condicion in item['condicional']:
                    if 'preguntas' in condicion:
                        ids.extend(obtener_ids_preguntas(condicion['preguntas']))
        elif 'preguntas' in item:
            # Es una sección
            ids.extend(obtener_ids_preguntas(item['preguntas']))
        else:
            print(f"Elemento inesperado sin 'id' ni 'preguntas': {item}")
    return ids



# En la función survey
todos_los_ids = obtener_ids_preguntas(preguntas)


@app.route('/', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        respuestas = {}

        def procesar_pregunta(pregunta):
            clave = f'P{pregunta["id"]}'
            valor = request.form.get(clave, '')
            respuestas[clave] = valor

            if 'condicional' in pregunta:
                valor_pregunta = valor
                for condicion in pregunta['condicional']:
                    mostrar_condicional = condicion['mostrar_condicional']
                    if valor_pregunta == mostrar_condicional:
                        if 'preguntas' in condicion:
                            for subpregunta in condicion['preguntas']:
                                procesar_pregunta(subpregunta)
                    else:
                        # Si la condición no se cumple, aseguramos que las subpreguntas tengan valores vacíos
                        if 'preguntas' in condicion:
                            for subpregunta in condicion['preguntas']:
                                clave_sub = f'P{subpregunta["id"]}'
                                respuestas[clave_sub] = ''  # Valor vacío

        # Obtener todos los IDs de preguntas
        todos_los_ids = obtener_ids_preguntas(preguntas)

        for seccion in preguntas:
            for pregunta in seccion['preguntas']:
                procesar_pregunta(pregunta)

        # Asegurar que todas las claves estén presentes en respuestas
        for clave in todos_los_ids:
            if clave not in respuestas:
                respuestas[clave] = ''

        # Guarda las respuestas en un archivo CSV con encabezados consistentes
        fieldnames = todos_los_ids
        file_exists = os.path.isfile('respuestas.csv')
        with open('respuestas.csv', 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow(respuestas)

        return redirect(url_for('resultado'))

    return render_template('survey.html', preguntas=preguntas)


@app.route('/resultado', methods=['GET'])
def resultado():
    return "Gracias por completar la encuesta."


@app.route('/admin', methods=['GET'])
def admin_dashboard():
    if not os.path.exists('respuestas.csv'):
        return "No hay datos para mostrar."

    # Cargar el CSV con los encabezados como textos de las preguntas
    df = pd.read_csv('respuestas.csv', encoding='utf-8')

    # Variables disponibles para filtrar
    filter_variables = [
        'Carrera que cursa',
        'Modalidad de estudios',
        'Semestre que cursa',
        'Edad',
        'Género',
        'Estado civil',
        'Lugar de residencia',
        '¿Con quién vives?'
    ]

    # Obtener opciones únicas para cada variable de filtro
    filter_options = {}
    for var in filter_variables:
        if var in df.columns:
            filter_options[var] = sorted(df[var].dropna().unique().tolist())
        else:
            filter_options[var] = []

    # Obtener valores seleccionados de los filtros
    filters = {}
    for var in filter_variables:
        selected_value = request.args.get(var)
        if selected_value:
            filters[var] = selected_value

    # Aplicar filtros al DataFrame
    filtered_df = df.copy()
    for var, value in filters.items():
        filtered_df = filtered_df[filtered_df[var] == value]

    # Si no hay datos después de aplicar los filtros
    if filtered_df.empty:
        return render_template('admin.html',
                               mensaje="No hay datos para mostrar con los filtros seleccionados.",
                               filter_variables=filter_variables,
                               filter_options=filter_options)

    # Usar 'df' como el DataFrame filtrado
    df = filtered_df

    # Calcular el promedio de edad
    if 'Edad' in df.columns:
        df['Edad'] = pd.to_numeric(df['Edad'], errors='coerce')
        if df['Edad'].notnull().any():
            promedio_edad = round(df['Edad'].mean(), 2)
        else:
            promedio_edad = 'No disponible'
    else:
        promedio_edad = 'No disponible'

    # Generar análisis por pregunta
    resultados_preguntas = []
    graficas_preguntas = []

    # Variables categóricas para tablas de contingencia
    variables_categoricas = []

    for columna in df.columns:
        conteo = df[columna].value_counts().dropna()
        total_respuestas = conteo.sum()

        if total_respuestas > 0 and len(conteo) > 1:
            # Crear gráfica interactiva con Plotly
            fig = px.bar(conteo, x=conteo.index.astype(str), y=conteo.values,
                         labels={'x': columna, 'y': 'Frecuencia'})
            fig.update_layout(title=columna, xaxis_title='', yaxis_title='Frecuencia')
            # Convertir la figura a JSON
            graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
            graficas_preguntas.append({'titulo': columna, 'grafica': graphJSON})
            variables_categoricas.append(columna)
        else:
            # Intentar convertir a numérico para análisis adicionales
            try:
                df[columna] = pd.to_numeric(df[columna], errors='coerce')
            except Exception as e:
                print(f"Error al convertir la columna {columna} a numérico: {e}")

    # Generar tablas de contingencia y heatmaps
    tablas_contingencia = []
    for i, var1 in enumerate(variables_categoricas):
        for var2 in variables_categoricas[i+1:]:
            tabla = pd.crosstab(df[var1], df[var2])
            if not tabla.empty and tabla.shape[0] > 1 and tabla.shape[1] > 1:
                # Crear heatmap con Plotly
                fig_heatmap = px.imshow(tabla.values,
                                        labels=dict(x=var2, y=var1, color='Frecuencia'),
                                        x=tabla.columns.astype(str).tolist(),
                                        y=tabla.index.astype(str).tolist(),
                                        text_auto=True,
                                        aspect="auto")
                fig_heatmap.update_layout(title=f'{var1} vs {var2}', xaxis_nticks=36)
                graphJSON_heatmap = json.dumps(fig_heatmap, cls=plotly.utils.PlotlyJSONEncoder)

                tablas_contingencia.append({
                    'titulo': f'{var1} vs {var2}',
                    'tabla': tabla.to_html(classes='table table-striped table-bordered'),
                    'heatmap': graphJSON_heatmap
                })

    # Análisis ELCSA
    elcsa_preguntas = [col for col in df.columns if col.startswith('ELCSA')]
    if elcsa_preguntas:
        df_elcsa = df[elcsa_preguntas].replace({'Sí': 1, 'No': 0, 'No sé': 0})
        df_elcsa = df_elcsa.apply(pd.to_numeric, errors='coerce').fillna(0)
        df['Total_ELCSA'] = df_elcsa.sum(axis=1)

        # Categorizar según el puntaje ELCSA
        categorias = ['Seguridad', 'Inseguridad leve', 'Inseguridad moderada', 'Inseguridad severa']
        df['Categoria'] = pd.cut(df['Total_ELCSA'], bins=[-1, 0, 3, 6, float('inf')], labels=categorias)

        # Contar la cantidad en cada categoría
        conteo_categorias = df['Categoria'].value_counts()
        total_respuestas = len(df)

        # Crear el análisis en texto
        analisis_texto = []
        for categoria, conteo in conteo_categorias.items():
            porcentaje = round((conteo / total_respuestas) * 100, 2)
            analisis_texto.append(f"{categoria}: {conteo} encuestados ({porcentaje}%)")

        # Crear gráfica de ELCSA con Plotly
        fig_elcsa = px.bar(conteo_categorias, x=conteo_categorias.index.astype(str), y=conteo_categorias.values,
                           labels={'x': 'Categoría', 'y': 'Número de encuestados'})
        fig_elcsa.update_layout(title='Clasificación de la (in)seguridad alimentaria', xaxis_title='', yaxis_title='Número de encuestados')
        graphJSON_elcsa = json.dumps(fig_elcsa, cls=plotly.utils.PlotlyJSONEncoder)
    else:
        analisis_texto = ["No hay datos suficientes para el análisis ELCSA."]
        graphJSON_elcsa = None

    # Renderizar la plantilla con los nuevos datos
    return render_template('admin.html',
                           promedio_edad=promedio_edad,
                           graficas_preguntas=graficas_preguntas,
                           analisis_texto=analisis_texto,
                           graphJSON_elcsa=graphJSON_elcsa,
                           tablas_contingencia=tablas_contingencia,
                           filter_variables=filter_variables,
                           filter_options=filter_options)



if __name__ == '__main__':
    if not os.path.exists('respuestas.csv'):
        with open('respuestas.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            # Escribe los encabezados según las preguntas
            headers = []
            for seccion_obj in preguntas:
                preguntas_seccion = seccion_obj['preguntas']
                for pregunta in preguntas_seccion:
                    headers.append(f'P{pregunta["id"]}')
                    if pregunta.get('condicional'):
                        for subpregunta in pregunta['condicional']:
                            headers.append(f'P{subpregunta["id"]}')
                            if subpregunta.get('condicional'):
                                for nested_subpregunta in subpregunta['condicional']:
                                    headers.append(f'P{nested_subpregunta["id"]}')
            writer.writerow(headers)

    app.run(debug=True)