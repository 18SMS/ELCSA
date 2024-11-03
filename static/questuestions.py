preguntas = [
    {
        "seccion": "Datos Generales",
        "preguntas": [
            {
                "texto": "Carrera que cursa:",
                "tipo": "seleccion",
                "id": "1",
                "opciones": [
                    "Ingeniería en Gestión Empresarial",
                    "Ingeniería Electromecánica",
                    "Ingeniería Industrial",
                    "Ingeniería en Sistemas Computacionales",
                    "Ingeniería Ambiental",
                    "Ingeniería Química",
                    "Contabilidad",
                    "Maestría en Administración",
                    "Maestría en Ingeniería"
                ]
            },
            {
                "texto": "Modalidad de estudios:",
                "tipo": "seleccion",
                "id": "2",
                "opciones": [
                    "Flexible",
                    "Escolarizado"
                ]
            },
            {
                "texto": "Semestre que cursa:",
                "tipo": "seleccion",
                "id": "3",
                "opciones": [
                    "primero",
                    "segundo",
                    "tercero",
                    "cuarto",
                    "quinto",
                    "sexto",
                    "séptimo",
                    "octavo",
                    "noveno",
                    "décimo",
                    "undécimo",
                    "duodécimo"
                ]
            },
            {
                "texto": "Edad:",
                "tipo": "numero",
                "id": "4"
            },
            {
                "texto": "Género:",
                "tipo": "seleccion",
                "id": "5",
                "opciones": [
                    "Masculino",
                    "Femenino",
                    "Otro"
                ]
            },
            {
                "texto": "Estado civil:",
                "tipo": "seleccion",
                "id": "6",
                "opciones": [
                    "Soltero(a)",
                    "Casado(a)",
                    "Unión libre",
                    "Divorciado(a)",
                    "Viudo(a)"
                ]
            },
            {
                "texto": "Lugar de residencia:",
                "tipo": "seleccion",
                "id": "7",
                "opciones": [
                    "Localidad",
                    "Comunidad",
                    "Ciudad"
                ]
            },
            {
                "texto": "¿Con quién vives?",
                "tipo": "seleccion",
                "id": "8",
                "opciones": [
                    "Solo(a)",
                    "Con padres",
                    "Con madre",
                    "Con padre",
                    "Con pareja",
                    "Con amigos/compañeros",
                    "Otros"
                ]
            }
        ]
    },
    {
        "seccion": "Situación Económica",
        "preguntas": [
            {
                "texto": "¿Dependes económicamente de alguien?",
                "tipo": "radio",
                "id": "9",
                "opciones": [
                    "Sí",
                    "No"
                ],
                "condicional": [
                    {
                        "mostrar_condicional": "Sí",
                        "preguntas": [
                            {
                                "texto": "¿De quién dependes económicamente?",
                                "tipo": "seleccion",
                                "id": "9a",
                                "opciones": [
                                    "Madre",
                                    "Padre",
                                    "Ambos padres",
                                    "Otros familiares",
                                    "Otros"
                                ]
                            },
                            {
                                "texto": "¿Quién más depende del jefe del hogar?",
                                "tipo": "seleccion",
                                "id": "9b",
                                "opciones": [
                                    "Hermanos(as)",
                                    "Abuelos(as)",
                                    "Otros familiares",
                                    "Nadie más"
                                ]
                            },
                            {
                                "texto": "Ingreso promedio mensual del hogar:",
                                "tipo": "seleccion",
                                "id": "9c",
                                "opciones": [
                                    "Menos de $5,000",
                                    "$5,001 - $10,000",
                                    "$10,001 - $15,000",
                                    "Más de $15,000"
                                ]
                            },
                            {
                                "texto": "¿Cuánto recibes tú a la semana?",
                                "tipo": "seleccion",
                                "id": "9d",
                                "opciones": [
                                    "Menos de $500",
                                    "$501 - $1,000",
                                    "$1,001 - $1,500",
                                    "Más de $1,500"
                                ]
                            },
                            {
                                "texto": "¿Tienes beca?",
                                "tipo": "radio",
                                "id": "9e",
                                "opciones": [
                                    "Sí",
                                    "No"
                                ],
                                "condicional": [
                                    {
                                        "mostrar_condicional": "Sí",
                                        "preguntas": [
                                            {
                                                "texto": "¿Qué tipo de beca tienes?",
                                                "tipo": "seleccion",
                                                "id": "9ei",
                                                "opciones": [
                                                    "Beca académica",
                                                    "Beca deportiva",
                                                    "Beca cultural",
                                                    "Beca de manutención",
                                                    "Otra"
                                                ]
                                            },
                                            {
                                                "texto": "Monto mensual de la beca:",
                                                "tipo": "seleccion",
                                                "id": "9eii",
                                                "opciones": [
                                                    "Menos de $1,000",
                                                    "$1,001 - $2,000",
                                                    "$2,001 - $3,000",
                                                    "Más de $3,000"
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "mostrar_condicional": "No",
                        "preguntas": [
                            {
                                "texto": "¿Cuál es tu principal sustento económico?",
                                "tipo": "seleccion",
                                "id": "9f",
                                "opciones": [
                                    "Trabajo",
                                    "Beca",
                                    "Ahorros",
                                    "Otro"
                                ]
                            },
                            {
                                "texto": "¿Tienes beca?",
                                "tipo": "radio",
                                "id": "9g",
                                "opciones": [
                                    "Sí",
                                    "No"
                                ],
                                "condicional": [
                                    {
                                        "mostrar_condicional": "Sí",
                                        "preguntas": [
                                            {
                                                "texto": "¿Qué tipo de beca tienes?",
                                                "tipo": "seleccion",
                                                "id": "9gi",
                                                "opciones": [
                                                    "Beca académica",
                                                    "Beca deportiva",
                                                    "Beca cultural",
                                                    "Beca de manutención",
                                                    "Otra"
                                                ]
                                            },
                                            {
                                                "texto": "Monto mensual de la beca:",
                                                "tipo": "seleccion", "id": "9gii",
                                                "opciones": [
                                                    "Menos de $1,000",
                                                    "$1,001 - $2,000",
                                                    "$2,001 - $3,000",
                                                    "Más de $3,000"
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                "texto": "¿Trabajas actualmente?",
                "tipo": "radio",
                "id": "10",
                "opciones": [
                    "Sí",
                    "No"
                ],
                "condicional": [
                    {
                        "mostrar_condicional": "Sí",
                        "preguntas": [
                            {
                                "texto": "¿En qué trabajas?",
                                "tipo": "texto",
                                "id": "10a"
                            },
                            {
                                "texto": "¿Cuántas horas al día trabajas?",
                                "tipo": "seleccion",
                                "id": "10b",
                                "opciones": [
                                    "Menos de 4 horas",
                                    "4-6 horas",
                                    "7-8 horas",
                                    "Más de 8 horas"
                                ]
                            },
                            {
                                "texto": "¿Cuántos días a la semana trabajas?",
                                "tipo": "seleccion",
                                "id": "10c",
                                "opciones": [
                                    "1-2 días",
                                    "3-4 días",
                                    "5-6 días",
                                    "7 días"
                                ]
                            },
                            {
                                "texto": "Ingreso mensual aproximado:",
                                "tipo": "seleccion",
                                "id": "10d",
                                "opciones": [
                                    "Menos de $5,000",
                                    "$5,001 - $10,000",
                                    "Más de $10,000"
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                "texto": "¿Alguien depende económicamente de ti?",
                "tipo": "radio",
                "id": "11",
                "opciones": [
                    "Sí",
                    "No"
                ],
                "condicional": [
                    {
                        "mostrar_condicional": "Sí",
                        "preguntas": [
                            {
                                "texto": "¿Quién depende de ti?",
                                "tipo": "seleccion",
                                "id": "11a",
                                "opciones": ["Hijo(a)", "Hermano(a)", "Sobrino(a)", "Otro"]
                            }
                        ]
                    }
                ]
            }
        ]
    },
        {
        "seccion": "Situación de Vivienda y Transporte",
        "preguntas": [
            {
                "texto": "¿Eres estudiante foráneo o local?",
                "tipo": "seleccion",
                "id": "12",
                "opciones": [
                    "Foráneo",
                    "Local"
                ],
                "condicional": [
                    {
                        "mostrar_condicional": "Foráneo",
                        "preguntas": [
                            {
                                "texto": "¿Rentas aquí o viajas diariamente?",
                                "tipo": "seleccion",
                                "id": "12a",
                                "opciones": [
                                    "Rentas",
                                    "Viajas diariamente"
                                ],
                                "condicional": [
                                    {
                                        "mostrar_condicional": "Rentas",
                                        "preguntas": [
                                            {
                                                "texto": "¿Qué tipo de vivienda rentas?",
                                                "tipo": "seleccion",
                                                "id": "12ai",
                                                "opciones": [
                                                    "Casa",
                                                    "Cuarto",
                                                    "Departamento"
                                                ]
                                            },
                                            {
                                                "texto": "¿Compartes la renta con otras personas?",
                                                "tipo": "radio",
                                                "id": "12aii",
                                                "opciones": [
                                                    "Sí",
                                                    "No"
                                                ],
                                                "condicional": [
                                                    {
                                                        "mostrar_condicional": "Sí",
                                                        "preguntas": [
                                                            {
                                                                "texto": "¿Con cuántas personas compartes?",
                                                                "tipo": "seleccion",
                                                                "id": "12aiia",
                                                                "opciones": [
                                                                    "1 persona",
                                                                    "2 personas",
                                                                    "3 o más personas"
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "texto": "¿Cuánto pagas de renta mensualmente?",
                                                "tipo": "seleccion",
                                                "id": "12aiii",
                                                "opciones": [
                                                    "Menos de $1,000",
                                                    "$1,001 - $2,000",
                                                    "$2,001 - $3,000",
                                                    "Más de $3,000"
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "mostrar_condicional": "Viajas diariamente",
                                        "preguntas": [
                                            {
                                                "texto": "¿Cuánto gastas en transporte semanalmente (ida y vuelta, incluyendo taxis)?",
                                                "tipo": "seleccion",
                                                "id": "12aiv",
                                                "opciones": [
                                                    "Menos de $200",
                                                    "$201 - $400",
                                                    "$401 - $600",
                                                    "Más de $600"
                                                ]
                                            },
                                            {
                                                "texto": "¿Cuánto tiempo tardas desde tu casa hasta Huatusco?",
                                                "tipo": "seleccion",
                                                "id": "12av",
                                                "opciones": [
                                                    "Menos de 30 minutos",
                                                    "31-60 minutos",
                                                    "1-2 horas",
                                                    "Más de 2 horas"
                                                ]
                                            },
                                            {
                                                "texto": "¿En qué medio de transporte te desplazas?",
                                                "tipo": "seleccion",
                                                "id": "12avi",
                                                "opciones": [
                                                    "Autobús",
                                                    "Carro particular",
                                                    "Taxi",
                                                    "Otro"
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "mostrar_condicional": "Local",
                        "preguntas": [
                            {
                                "texto": "¿Con quién vives?",
                                "tipo": "seleccion",
                                "id": "12b",
                                "opciones": [
                                    "Madre",
                                    "Padre",
                                    "Ambos padres",
                                    "Hermanos(as)",
                                    "Otros familiares",
                                    "Solo(a)",
                                    "Otro"
                                ]
                            },
                            {
                                "texto": "Número de personas en tu hogar (incluyéndote a ti):",
                                "tipo": "seleccion",
                                "id": "12c",
                                "opciones": [
                                    "1-2 personas",
                                    "3-4 personas",
                                    "5-6 personas",
                                    "Más de 6 personas"
                                ]
                            },
                            {
                                "texto": "¿Cómo te desplazas hasta la escuela?",
                                "tipo": "seleccion",
                                "id": "12d",
                                "opciones": [
                                    "Caminando",
                                    "Taxi",
                                    "Carro particular",
                                    "Motocicleta",
                                    "Autobús",
                                    "Otro"
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    },
    {
        "seccion": "Alimentación",
        "preguntas": [
            {
                "texto": "¿Sueles cocinar en casa o comprar comida preparada?",
                "tipo": "radio",
                "id": "13",
                "opciones": [
                    "Cocinar en casa",
                    "Comprar comida preparada"
                ],
                "condicional": [
                    {
                        "mostrar_condicional": "Cocinar en casa",
                        "preguntas": [
                            {
                                "texto": "¿Cuánto gastas en promedio a la semana en alimentos?",
                                "tipo": "seleccion",
                                "id": "13a",
                                "opciones": [
                                    "Menos de $300",
                                    "$301 - $500",
                                    "$501 - $700",
                                    "Más de $700"
                                ]
                            }
                        ]
                    },
                    {
                        "mostrar_condicional": "Comprar comida preparada",
                        "preguntas": [
                            {
                                "texto": "¿Cuánto gastas en promedio semanal en comida?",
                                "tipo": "seleccion",
                                "id": "13b",
                                "opciones": [
                                    "Menos de $300",
                                    "$301 - $500",
                                    "$501 - $700",
                                    "Más de $700"
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                "texto": "¿Tienes algún tipo de respaldo económico en caso de perder ingresos?",
                "tipo": "radio",
                "id": "14",
                "opciones": [
                    "Sí",
                    "No"
                ]
            },
            {
                "texto": "Si perdieras tu principal sustento económico, ¿continuarías estudiando?",
                "tipo": "seleccion",
                "id": "15",
                "opciones": [
                    "Sí",
                    "No",
                    "No estoy seguro(a)"
                ]
            }
        ]
    },
    {
        "seccion": "Hábitos Alimenticios",
        "preguntas": [
            {
                "texto": "¿Cuántas veces al día sueles comer (incluyendo snacks o bocadillos)?",
                "tipo": "seleccion",
                "id": "16",
                "opciones": [
                    "Menos de 2 veces al día",
                    "2 veces al día",
                    "3 veces al día",
                    "4 veces al día",
                    "5 veces o más al día"
                ]
            },
            {
                "texto": "¿Tienes horarios regulares para tus comidas principales (desayuno, almuerzo, cena)?",
                "tipo": "seleccion",
                "id": "17",
                "opciones": [
                    "Nunca",
                    "Rara vez",
                    "A veces",
                    "Frecuentemente",
                    "Siempre"
                ]
            },
            {
                "texto": "¿Con qué frecuencia te saltas una comida principal debido a falta de tiempo o recursos?",
                "tipo": "seleccion",
                "id": "18",
                "opciones": [
                    "Nunca",
                    "Rara vez",
                    "A veces",
                    "Frecuentemente",
                    "Siempre"
                ]
            },
            {
                "texto": "¿Incluyes snacks o bocadillos entre tus comidas principales?",
                "tipo": "seleccion",
                "id": "19",
                "opciones": [
                    "No",
                    "Sí, 1 vez al día",
                    "Sí, 2 veces al día",
                    "Sí, más de 2 veces al día"
                ]
            },
            {
                "texto": "¿Cuántas veces al día consumes comida preparada en casa?",
                "tipo": "seleccion",
                "id": "20",
                "opciones": [
                    "Ninguna",
                    "1 vez al día",
                    "2 veces al día",
                    "3 veces al día",
                    "4 veces o más al día"
                ]
            },
            {
                "texto": "¿Cuántas veces a la semana compras comida preparada o comes fuera de casa?",
                "tipo": "seleccion",
                "id": "21",
                "opciones": [
                    "Nunca",
                    "1-2 veces a la semana",
                    "3-4 veces a la semana",
                    "5-6 veces a la semana",
                    "Todos los días"
                ]
            },
            {
                "texto": "¿Consideras que la cantidad de alimentos que consumes es suficiente para tus necesidades?",
                "tipo": "seleccion",
                "id": "22",
                "opciones": [
                    "Nunca",
                    "Rara vez",
                    "A veces",
                    "Frecuentemente",
                    "Siempre"
                ]
            },
            {
                "texto": "¿Crees que la calidad de tus comidas es adecuada para mantener una dieta balanceada?",
                "tipo": "seleccion",
                "id": "23",
                "opciones": [
                    "Nunca",
                    "Rara vez",
                    "A veces",
                    "Frecuentemente",
                    "Siempre"
                ]
            },
            {
                "texto": "¿Hay alguna razón específica por la cual no consumes una cantidad adecuada de comidas al día? (Por ejemplo: falta de tiempo, recursos económicos, falta de apetito, etc.)",
                "tipo": "texto",
                "id": "24"
            }
        ]
    },
    {
        "seccion": "Situación de Vivienda",
        "preguntas": [
            {
                "texto": "¿Cómo describirías tu situación de vivienda en términos de comodidad, estabilidad y seguridad?",
                "tipo": "seleccion",
                "id": "25",
                "opciones": [
                    "Muy insatisfecho(a)",
                    "Insatisfecho(a)",
                    "Neutral",
                    "Satisfecho(a)",
                    "Muy satisfecho(a)"
                ]
            }
        ]
    },
    {
        "seccion": "Escala Latinoamericana y Caribeña de Seguridad Alimentaria (ELCSA)",
        "preguntas": [
            {
                "texto": "¿Te preocupaste porque los alimentos se acabaran en tu hogar por falta de dinero u otros recursos?",
                "tipo": "radio",
                "id": "26",
                "opciones": [
                    "Sí",
                    "No",
                    "No sé"
                ]
            },
            {
                "texto": "¿En tu hogar se quedaron sin alimentos por falta de dinero u otros recursos?",
                "tipo": "radio",
                "id": "27",
                "opciones": [
                    "Sí",
                    "No",
                    "No sé"
                ]
            },
            {
                "texto": "¿Dejaste de tener una alimentación saludable por falta de dinero u otros recursos?",
                "tipo": "radio",
                "id": "28",
                "opciones": [
                    "Sí",
                    "No",
                    "No sé"
                ]
            },
            {
                "texto": "¿Consumiste pocos tipos de alimentos por falta de dinero u otros recursos?",
                "tipo": "radio",
                "id": "29",
                "opciones": [
                    "Sí",
                    "No",
                    "No sé"
                ]
            },
            {
                "texto": "¿Tú o algún adulto en tu hogar dejó de desayunar, almorzar o cenar por falta de dinero u otros recursos?",
                "tipo": "radio",
                "id": "30",
                "opciones": [
                    "Sí",
                    "No",
                    "No sé"
                ]
            },
            {
                "texto": "¿Comiste menos de lo que debías por falta de dinero u otros recursos?",
                "tipo": "radio",
                "id": "31",
                "opciones": [
                    "Sí",
                    "No",
                    "No sé"
                ]
            },
            {
                "texto": "¿Sentiste hambre pero no comiste por falta de dinero u otros recursos?",
                "tipo": "radio",
                "id": "32",
                "opciones": [
                    "Sí",
                    "No",
                    "No sé"
                ]
            },
            {
                "texto": "¿Comiste solo una vez al día o dejaste de comer durante todo un día por falta de dinero u otros recursos?",
                "tipo": "radio",
                "id": "33",
                "opciones": [
                    "Sí",
                    "No",
                    "No sé"
                ]
            },
            {
                "texto": "¿Hay menores de 18 en tu casa?",
                "tipo": "radio",
                "id": "33b",
                "opciones": [
                    "Sí",
                    "No"
                ]
            },
            
            {
                "texto": "¿Algún menor de 18 años en tu hogar dejó de tener una alimentación saludable por falta de dinero u otros recursos?",
                "tipo": "radio",
                "id": "34",
                "opciones": [
                    "Sí",
                    "No",
                    "No sé"
                ]
            },
            {
                "texto": "¿Algún menor de 18 años en tu hogar consumió pocos tipos de alimentos por falta de dinero u otros recursos?",
                "tipo": "radio",
                "id": "35",
                "opciones": [
                    "Sí",
                    "No",
                    "No sé"
                ]
            },
            {
                "texto": "¿Algún menor de 18 años en tu hogar comió menos de lo que debía por falta de dinero u otros recursos?",
                "tipo": "radio",
                "id": "36",
                "opciones": [
                    "Sí",
                    "No",
                    "No sé"
                ]
            },
            {
                "texto": "¿Algún menor de 18 años en tu hogar dejó de desayunar, almorzar o cenar por falta de dinero u otros recursos?",
                "tipo": "radio",
                "id": "37",
                "opciones": [
                    "Sí",
                    "No",
                    "No sé"
                ]
            },
            {
                "texto": "¿Reduciste la cantidad de comida servida a algún menor de 18 años en tu hogar por falta de dinero u otros recursos?",
                "tipo": "radio",
                "id": "38",
                "opciones": [
                    "Sí",
                    "No",
                    "No sé"
                ]
            },
            {
                "texto": "¿Algún menor de 18 años en tu hogar sintió hambre pero no comió por falta de dinero u otros recursos?",
                "tipo": "radio",
                "id": "39",
                "opciones": [
                    "Sí",
                    "No",
                    "No sé"
                ]
            },
            {
                "texto": "¿Algún menor de 18 años en tu hogar comió solo una vez al día o dejó de comer durante todo un día por falta de dinero u otros recursos?",
                "tipo": "radio",
                "id": "40",
                "opciones": [
                    "Sí",
                    "No",
                    "No sé"
                ]
            }
        ]
    },
    {
        "seccion": "Rendimiento Académico",
        "preguntas": [
            {
                "texto": "¿Cuál fue tu promedio general del semestre anterior?",
                "tipo": "seleccion",
                "id": "41",
                "opciones": [
                    "Menos de 70",
                    "70 - 79",
                    "80 - 89",
                    "90 - 100"
                ]
            },
            {
                "texto": "¿Llevas materias de repite?",
                "tipo": "radio",
                "id": "42",
                "opciones": [
                    "Sí",
                    "No"
                ]
            },
            {
                "texto": "¿Has experimentado dificultades académicas relacionadas con tu situación alimentaria o económica?",
                "tipo": "radio",
                "id": "43",
                "opciones": [
                    "Sí",
                    "No"
                ],
                "condicional": [
                    {
                        "mostrar_condicional": "Sí",
                        "preguntas": [
                            {
                                "texto": "Describe brevemente cómo ha afectado tu situación a tu rendimiento académico:",
                                "tipo": "texto",
                                "id": "43a"
                            }
                        ]
                    }
                ]
            }
        ]
    }
]