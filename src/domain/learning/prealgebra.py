"""Catálogo curricular puro para Preálgebra, Nivel 1: conjuntos numéricos.

El contenido visible vive en i18n. Este módulo conserva la identidad, el orden,
las reglas de presentación y los invariantes que no dependen de la interfaz.
"""

import re
from copy import deepcopy

PREALGEBRA_COURSE_ID = "algebra_basica"
WELCOME_NODE_ID = "PREALG-N1-B01-BIENVENIDA"
TRIGGER_NODE_ID = "PREALG-N1-B02-PREGUNTA-DETONADORA"
STAIRCASE_NODE_ID = "PREALG-N1-B03-ESCALERA-NECESIDAD"
NATURALS_NODE_ID = "PREALG-N1-B04-NATURALES-CONTAR"
INTEGERS_NODE_ID = "PREALG-N1-B05-ENTEROS-DEUDA"
RATIONALS_NODE_ID = "PREALG-N1-B06-RACIONALES-FRACCION-DIVISION"
IRRATIONALS_NODE_ID = "PREALG-N1-B07-IRRACIONALES-DECIMALES"
REALS_NODE_ID = "PREALG-N1-B08-REALES-RECTA"
COMPLEX_NODE_ID = "PREALG-N1-B09-COMPLEJOS-PLANO"
CLASSIFIER_BASIC_NODE_ID = "PREALG-N1-B10-CLASIFICADOR-BASICO"
CLASSIFIER_RIGOROUS_NODE_ID = "PREALG-N1-B11-CLASIFICADOR-RIGUROSO"
DETECTIVE_NODE_ID = "PREALG-N1-B12-DETECTIVE-FALSEDADES"
CLOSING_NODE_ID = "PREALG-N1-B13-CIERRE-DIAGNOSTICO"

N2_HUB_NODE_ID = "PREALG-N2-E00-CIUDAD"
N2_SUM_NODE_ID = "PREALG-N2-E01-SUMA-JUNTAR"
N2_SUBTRACTION_NODE_ID = "PREALG-N2-E02-RESTA-QUITAR"
N2_MULTIPLICATION_NODE_ID = "PREALG-N2-E03-MULTIPLICACION-AGRUPAR"
N2_DIVISION_NODE_ID = "PREALG-N2-E04-DIVISION-REPARTIR"
N2_EXPONENTIATION_NODE_ID = "PREALG-N2-E05-POTENCIACION-CRECER"
N2_RADICATION_NODE_ID = "PREALG-N2-E06-RADICACION-RAIZ"

N3_HUB_NODE_ID = "PREALG-N3-M00-LABORATORIO"
N3_COMMUTATIVE_NODE_ID = "PREALG-N3-M01-CONMUTATIVA"
N3_ASSOCIATIVE_NODE_ID = "PREALG-N3-M02-ASOCIATIVA"
N3_DISTRIBUTIVE_NODE_ID = "PREALG-N3-M03-DISTRIBUTIVA"
N3_IDENTITY_NODE_ID = "PREALG-N3-M04-ELEMENTO-NEUTRO"
N3_INVERSES_NODE_ID = "PREALG-N3-M05-INVERSOS"

N2_OPERATION_NODE_IDS = [
    N2_SUM_NODE_ID,
    N2_SUBTRACTION_NODE_ID,
    N2_MULTIPLICATION_NODE_ID,
    N2_DIVISION_NODE_ID,
    N2_EXPONENTIATION_NODE_ID,
    N2_RADICATION_NODE_ID,
]
N2_NODE_IDS = [N2_HUB_NODE_ID, *N2_OPERATION_NODE_IDS]

N3_MACHINE_NODE_IDS = [
    N3_COMMUTATIVE_NODE_ID,
    N3_ASSOCIATIVE_NODE_ID,
    N3_DISTRIBUTIVE_NODE_ID,
    N3_IDENTITY_NODE_ID,
    N3_INVERSES_NODE_ID,
]
N3_NODE_IDS = [N3_HUB_NODE_ID, *N3_MACHINE_NODE_IDS]

N4_HUB_NODE_ID = "PREALG-N4-C00-PUERTO-DE-LA-POLIS"
N4_DIVISIBILITY_NODE_ID = "PREALG-N4-C01-DIVISIBILIDAD"
N4_MULTIPLES_NODE_ID = "PREALG-N4-C02-MULTIPLOS"
N4_PRIMES_NODE_ID = "PREALG-N4-C03-PRIMOS"
N4_FACTORIZATION_NODE_ID = "PREALG-N4-C04-FACTORIZACION-PRIMA"
N4_GCD_NODE_ID = "PREALG-N4-C05-MCD"
N4_LCM_NODE_ID = "PREALG-N4-C06-MCM"

N4_CONCEPT_NODE_IDS = [
    N4_DIVISIBILITY_NODE_ID,
    N4_MULTIPLES_NODE_ID,
    N4_PRIMES_NODE_ID,
    N4_FACTORIZATION_NODE_ID,
    N4_GCD_NODE_ID,
    N4_LCM_NODE_ID,
]
N4_NODE_IDS = [N4_HUB_NODE_ID, *N4_CONCEPT_NODE_IDS]

_LESSONS = {
    WELCOME_NODE_ID: {
        "node_id": WELCOME_NODE_ID,
        "node_type": "content_intro",
        "topic": "orientacion_intro",
        "i18n_prefix": "prealgebra.n1.b01",
        "next_node_id": "PREALG-N1-B02-PREGUNTA-DETONADORA",
        "affects_elo": False,
        "is_safe_zone": True,
        "optional_branch": False,
        "objectives": [
            "recognize_sets",
            "explain_uses",
            "classify_numbers",
            "identify_membership",
        ],
        "optional_objectives": ["explore_complex"],
        "interactions": [],
    },
    TRIGGER_NODE_ID: {
        "node_id": TRIGGER_NODE_ID,
        "node_type": "safe_interaction",
        "topic": "conflicto_cognitivo_intro",
        "i18n_prefix": "prealgebra.n1.b02",
        "next_node_id": "PREALG-N1-B03-ESCALERA-NECESIDAD",
        "unlock_after": WELCOME_NODE_ID,
        "affects_elo": False,
        "is_safe_zone": True,
        "optional_branch": False,
        "objectives": ["identify_limits_of_counting"],
        "optional_objectives": [],
        # Solo se exponen claves estructuradas; nunca texto libre ni respuestas esperadas.
        "interactions": [
            {
                "interaction_id": "PREALG-N1-B02-Q01",
                "type": "single_select",
                "prompt_key": "prealgebra.n1.b02.q01.prompt",
                "option_keys": ["yes", "no"],
            },
            {
                "interaction_id": "PREALG-N1-B02-Q02",
                "type": "single_select",
                "prompt_key": "prealgebra.n1.b02.q02.prompt",
                "option_keys": ["temperature", "pizza", "debt"],
            },
        ],
    },
    STAIRCASE_NODE_ID: {
        "node_id": STAIRCASE_NODE_ID,
        "node_type": "concept_organizer",
        "topic": "organizador_previo",
        "i18n_prefix": "prealgebra.n1.b03",
        "next_node_id": "PREALG-N1-B04-NATURALES-CONTAR",
        "unlock_after": TRIGGER_NODE_ID,
        "affects_elo": False,
        "is_safe_zone": True,
        "optional_branch": False,
        "objectives": ["recognize_progressive_expansion"],
        "optional_objectives": ["preview_complex_plane"],
        "staircase": {
            "core_steps": ["naturals", "integers", "rationals", "irrationals", "reals"],
            "optional_detour": "complex",
        },
        "interactions": [
            {
                "interaction_id": "PREALG-N1-B03-Q01",
                "type": "single_select",
                "prompt_key": "prealgebra.n1.b03.q01.prompt",
                "option_keys": ["expand", "replace", "bigger"],
                "can_retry": True,
            }
        ],
    },
    NATURALS_NODE_ID: {
        "node_id": NATURALS_NODE_ID,
        "node_type": "guided_practice",
        "topic": "naturales",
        "i18n_prefix": "prealgebra.n1.b04",
        "next_node_id": "PREALG-N1-B05-ENTEROS-DEUDA",
        "unlock_after": STAIRCASE_NODE_ID,
        "affects_elo": False,
        "is_safe_zone": True,
        "optional_branch": False,
        "objectives": ["count_whole_quantities", "recognize_naturals"],
        "optional_objectives": ["explain_zero_convention"],
        "content": {
            "kind": "number_set_story_node",
            "type": "narrative_with_integrated_definition",
            "practice_position": "after_definition_plus_examples",
            "is_integrated": True,
            "definition_katex": "\\mathbb{N}=\\{0,1,2,3,\\ldots\\}",
            "sections": [
                {
                    "type": "prose",
                    "i18n_key": "prealgebra.n1.b04.story.opening",
                    "content_summary": (
                        "Katia presenta los naturales como el primer lenguaje para "
                        "contar cantidades completas y pregunta que cuenta como una "
                        "cantidad completa."
                    ),
                },
                {
                    "type": "guided_discovery",
                    "i18n_key": "prealgebra.n1.b04.story.discovery",
                    "content_summary": (
                        "Contrasta contar objetos completos, representar ausencia "
                        "con cero y excluir negativos, fracciones y decimales."
                    ),
                },
                {
                    "type": "definition_plus_examples",
                    "i18n_key": "prealgebra.n1.b04.story.definition",
                    "definition_katex": "\\mathbb{N}=\\{0,1,2,3,\\ldots\\}",
                    "is_integrated": True,
                    "examples": [
                        {
                            "i18n_key": "prealgebra.n1.b04.story.examples.count",
                            "name": "Contar objetos completos",
                            "steps": [
                                "Identificar objetos completos.",
                                "Contarlos uno a uno.",
                                "Expresar el total con un natural.",
                            ],
                        },
                        {
                            "i18n_key": "prealgebra.n1.b04.story.examples.zero",
                            "name": "El cero como ausencia",
                            "steps": [
                                "Observar que no hay objetos.",
                                "Representar la ausencia con 0.",
                                "Aplicar la convencion 0 pertenece a N.",
                            ],
                        },
                    ],
                },
            ],
        },
        "interactions": [
            {
                "interaction_id": "PREALG-N1-B04-Q01",
                "type": "numeric_input",
                "prompt_key": "prealgebra.n1.b04.q01.prompt",
                "option_keys": [],
                "can_retry": True,
            },
            {
                "interaction_id": "PREALG-N1-B04-Q02",
                "type": "single_select",
                "prompt_key": "prealgebra.n1.b04.q02.prompt",
                "option_keys": ["yes", "no"],
                "can_retry": True,
            },
            {
                "interaction_id": "PREALG-N1-B04-Q03",
                "type": "numeric_input",
                "prompt_key": "prealgebra.n1.b04.q03.prompt",
                "option_keys": [],
                "can_retry": True,
            },
            {
                "interaction_id": "PREALG-N1-B04-Q04",
                "type": "multi_select",
                "prompt_key": "prealgebra.n1.b04.q04.prompt",
                "option_keys": ["zero", "four", "negative_two", "sqrt_two", "fifteen", "decimal_25"],
                "can_retry": True,
            },
        ],
    },
    INTEGERS_NODE_ID: {
        "node_id": INTEGERS_NODE_ID,
        "node_type": "guided_practice",
        "topic": "enteros",
        "i18n_prefix": "prealgebra.n1.b05",
        "next_node_id": "PREALG-N1-B06-RACIONALES-FRACCION-DIVISION",
        "unlock_after": NATURALS_NODE_ID,
        "affects_elo": False,
        "is_safe_zone": True,
        "optional_branch": False,
        "objectives": ["represent_negative_quantities", "order_integers"],
        "optional_objectives": [],
        "content": {
            "kind": "number_set_story_node",
            "type": "narrative_with_integrated_definition",
            "practice_position": "after_definition_plus_examples",
            "is_integrated": True,
            "definition_katex": "\\mathbb{Z}=\\{\\ldots,-3,-2,-1,0,1,2,3,\\ldots\\}",
            "sections": [
                {
                    "type": "prose",
                    "i18n_key": "prealgebra.n1.b05.story.opening",
                    "content_summary": (
                        "Katia plantea que los naturales no bastan para representar "
                        "faltantes, deudas y cantidades por debajo del cero."
                    ),
                },
                {
                    "type": "guided_discovery",
                    "i18n_key": "prealgebra.n1.b05.story.discovery",
                    "content_summary": (
                        "Contrasta dinero disponible, deuda, temperaturas positivas "
                        "y negativas, y no ejemplos con decimales o fracciones."
                    ),
                },
                {
                    "type": "definition_plus_examples",
                    "i18n_key": "prealgebra.n1.b05.story.definition",
                    "definition_katex": "\\mathbb{Z}=\\{\\ldots,-3,-2,-1,0,1,2,3,\\ldots\\}",
                    "is_integrated": True,
                    "examples": [
                        {
                            "i18n_key": "prealgebra.n1.b05.story.examples.debt",
                            "name": "Deuda simple",
                            "steps": [
                                "Identificar 0 como equilibrio.",
                                "Reconocer que una deuda esta por debajo de 0.",
                                "Conservar la cantidad completa.",
                                "Usar signo negativo.",
                            ],
                        },
                        {
                            "i18n_key": "prealgebra.n1.b05.story.examples.payment",
                            "name": "Abono hacia el equilibrio",
                            "steps": [
                                "Partir de una deuda negativa.",
                                "Interpretar el abono como movimiento hacia la derecha.",
                                "Calcular la deuda restante.",
                                "Mantener signo negativo si todavia queda deuda.",
                            ],
                        },
                    ],
                },
            ],
        },
        "interactions": [
            {
                "interaction_id": "PREALG-N1-B05-Q01",
                "type": "numeric_input",
                "prompt_key": "prealgebra.n1.b05.q01.prompt",
                "option_keys": [],
                "can_retry": True,
            },
            {
                "interaction_id": "PREALG-N1-B05-Q02",
                "type": "numeric_input",
                "prompt_key": "prealgebra.n1.b05.q02.prompt",
                "option_keys": [],
                "can_retry": True,
            },
            {
                "interaction_id": "PREALG-N1-B05-Q03",
                "type": "single_select",
                "prompt_key": "prealgebra.n1.b05.q03.prompt",
                "option_keys": ["positive", "negative", "zero"],
                "can_retry": True,
            },
            {
                "interaction_id": "PREALG-N1-B05-Q04",
                "type": "number_line",
                "prompt_key": "prealgebra.n1.b05.q04.prompt",
                "option_keys": ["negative_35000", "negative_5000", "zero", "positive_5000"],
                "can_retry": True,
            },
            {
                "interaction_id": "PREALG-N1-B05-Q05",
                "type": "multi_select",
                "prompt_key": "prealgebra.n1.b05.q05.prompt",
                "option_keys": ["neg8", "neg_3_5", "zero", "half", "six", "neg_2_1"],
                "can_retry": True,
            },
        ],
    },
    RATIONALS_NODE_ID: {
        "node_id": RATIONALS_NODE_ID,
        "node_type": "guided_practice",
        "topic": "racionales",
        "i18n_prefix": "prealgebra.n1.b06",
        "next_node_id": "PREALG-N1-B07-IRRACIONALES-DECIMALES",
        "unlock_after": INTEGERS_NODE_ID,
        "affects_elo": False,
        "is_safe_zone": True,
        "optional_branch": False,
        "objectives": ["interpret_fraction_as_sharing", "connect_fraction_division_decimal"],
        "optional_objectives": ["recognize_repeating_decimal"],
        "content": {
            "kind": "number_set_story_node",
            "type": "narrative_with_integrated_definition",
            "practice_position": "after_definition_plus_examples",
            "is_integrated": True,
            "definition_katex": "\\mathbb{Q}=\\left\\{\\frac{a}{b}:a,b\\in\\mathbb{Z},\\ b\\ne0\\right\\}",
            "sections": [
                {
                    "type": "prose",
                    "i18n_key": "prealgebra.n1.b06.story.opening",
                    "content_summary": (
                        "Katia recuerda que los enteros representan deudas, saldos y "
                        "posiciones bajo cero, pero no alcanzan cuando una unidad debe "
                        "repartirse en partes iguales."
                    ),
                },
                {
                    "type": "guided_discovery",
                    "i18n_key": "prealgebra.n1.b06.story.discovery",
                    "content_summary": (
                        "El caso de tres panes para cuatro personas muestra que cada "
                        "persona recibe tres cuartos: una fraccion que tambien se lee "
                        "como division 3 entre 4."
                    ),
                },
                {
                    "type": "definition_plus_examples",
                    "i18n_key": "prealgebra.n1.b06.story.definition",
                    "definition_katex": (
                        "\\mathbb{Q}=\\left\\{\\frac{a}{b}:a,b\\in\\mathbb{Z},\\ b\\ne0\\right\\}"
                    ),
                    "is_integrated": True,
                    "examples": [
                        {
                            "i18n_key": "prealgebra.n1.b06.story.examples.sharing",
                            "name": "Reparto en partes iguales",
                            "steps": [
                                "Identificar la cantidad total que se reparte.",
                                "Identificar entre cuantas partes iguales se divide.",
                                "Escribir la fraccion total sobre partes.",
                                "Leer la fraccion como una division.",
                            ],
                        },
                        {
                            "i18n_key": "prealgebra.n1.b06.story.examples.decimal",
                            "name": "Fraccion, division y decimal",
                            "steps": [
                                "Empezar con una fraccion.",
                                "Dividir numerador entre denominador.",
                                "Reconocer el decimal equivalente si termina o se repite.",
                            ],
                        },
                    ],
                },
            ],
        },
        "interactions": [
            {
                "interaction_id": "PREALG-N1-B06-Q01",
                "type": "single_select",
                "prompt_key": "prealgebra.n1.b06.q01.prompt",
                "option_keys": ["three_fourths", "four_thirds", "add", "subtract"],
                "can_retry": True,
            },
            {
                "interaction_id": "PREALG-N1-B06-Q02",
                "type": "single_select",
                "prompt_key": "prealgebra.n1.b06.q02.prompt",
                "option_keys": ["three_div_four", "four_div_three", "add", "subtract"],
                "can_retry": True,
            },
            {
                "interaction_id": "PREALG-N1-B06-Q03",
                "type": "single_select",
                "prompt_key": "prealgebra.n1.b06.q03.prompt",
                "option_keys": ["decimal_075", "repeating_0333", "decimal_34", "decimal_43"],
                "can_retry": False,
            },
            {
                "interaction_id": "PREALG-N1-B06-Q04",
                "type": "multi_select",
                "prompt_key": "prealgebra.n1.b06.q04.prompt",
                "option_keys": ["frac_34", "dec_025", "neg3", "periodic_0333", "sqrt2", "pi"],
                "can_retry": True,
            },
        ],
    },
    IRRATIONALS_NODE_ID: {
        "node_id": IRRATIONALS_NODE_ID,
        "node_type": "guided_practice",
        "topic": "irracionales",
        "i18n_prefix": "prealgebra.n1.b07",
        "next_node_id": "PREALG-N1-B08-REALES-RECTA",
        "unlock_after": RATIONALS_NODE_ID,
        "affects_elo": False,
        "is_safe_zone": True,
        "optional_branch": False,
        "objectives": ["define_irrational_as_non_fraction", "distinguish_approximation_from_exact"],
        "optional_objectives": ["locate_sqrt2_on_line"],
        "content": {
            "kind": "number_set_story_node",
            "type": "narrative_with_integrated_definition",
            "practice_position": "after_definition_plus_examples",
            "is_integrated": True,
            "definition_katex": "\\mathbb{I}=\\mathbb{R}\\setminus\\mathbb{Q}",
            "sections": [
                {
                    "type": "prose",
                    "i18n_key": "prealgebra.n1.b07.story.opening",
                    "content_summary": (
                        "Katia compara decimales exactos, periodicos e infinitos no "
                        "periodicos para abrir la pregunta de si todos vienen de una "
                        "fraccion."
                    ),
                },
                {
                    "type": "guided_discovery",
                    "i18n_key": "prealgebra.n1.b07.story.discovery",
                    "content_summary": (
                        "El criterio central no es que el decimal sea largo, sino que "
                        "el numero no pueda escribirse como fraccion de enteros."
                    ),
                },
                {
                    "type": "definition_plus_examples",
                    "i18n_key": "prealgebra.n1.b07.story.definition",
                    "definition_katex": "\\mathbb{I}=\\mathbb{R}\\setminus\\mathbb{Q}",
                    "is_integrated": True,
                    "examples": [
                        {
                            "i18n_key": "prealgebra.n1.b07.story.examples.pi",
                            "name": "Aproximacion frente a valor exacto",
                            "steps": [
                                "Usar 3,14 como aproximacion de pi.",
                                "Reconocer que pi no termina ni se repite.",
                                "Distinguir el valor exacto de sus aproximaciones.",
                            ],
                        },
                        {
                            "i18n_key": "prealgebra.n1.b07.story.examples.sqrt",
                            "name": "Raiz cuadrada no racional",
                            "steps": [
                                "Ubicar la raiz entre dos enteros.",
                                "Aproximar su posicion en la recta.",
                                "Reconocer que no se expresa como fraccion de enteros.",
                            ],
                        },
                    ],
                },
            ],
        },
        "interactions": [
            {
                "interaction_id": "PREALG-N1-B07-Q01",
                "type": "single_select",
                "prompt_key": "prealgebra.n1.b07.q01.prompt",
                "option_keys": ["exact_025", "periodic_0333", "nonperiodic_pi"],
                "can_retry": True,
            },
            {
                "interaction_id": "PREALG-N1-B07-Q02",
                "type": "single_select",
                "prompt_key": "prealgebra.n1.b07.q02.prompt",
                "option_keys": ["pi_exact", "pi_approx", "pi_ends"],
                "can_retry": True,
            },
            {
                # Camino interno opcional (banda avanzado): ubicar √2 en la recta.
                "interaction_id": "PREALG-N1-B07-Q03",
                "type": "number_line",
                "prompt_key": "prealgebra.n1.b07.q03.prompt",
                "option_keys": ["between_1_2", "at_2", "between_2_3"],
                "can_retry": True,
            },
        ],
    },
    REALS_NODE_ID: {
        "node_id": REALS_NODE_ID,
        "node_type": "guided_practice",
        "topic": "reales",
        "i18n_prefix": "prealgebra.n1.b08",
        # Cierre de la ruta núcleo; de aquí parte la rama opcional de complejos.
        "next_node_id": "PREALG-N1-B09-COMPLEJOS-PLANO",
        "unlock_after": IRRATIONALS_NODE_ID,
        "affects_elo": False,
        "is_safe_zone": True,
        "optional_branch": False,
        "nucleus_closing_node": True,
        "objectives": ["recognize_reals_as_number_line", "classify_membership_in_reals"],
        "optional_objectives": ["reals_are_not_all_numbers"],
        "content": {
            "kind": "number_set_story_node",
            "type": "narrative_with_integrated_definition",
            "practice_position": "after_definition_plus_examples",
            "is_integrated": True,
            "definition_katex": "\\mathbb{R}=\\mathbb{Q}\\cup(\\mathbb{R}\\setminus\\mathbb{Q})",
            "sections": [
                {
                    "type": "prose",
                    "i18n_key": "prealgebra.n1.b08.story.opening",
                    "content_summary": (
                        "Katia reune los pasos anteriores: contar, deber, repartir y "
                        "medir con decimales no periodicos en una misma recta."
                    ),
                },
                {
                    "type": "guided_discovery",
                    "i18n_key": "prealgebra.n1.b08.story.discovery",
                    "content_summary": (
                        "La recta real contiene racionales e irracionales; los enteros "
                        "funcionan como marcas de referencia, no como limite del sistema."
                    ),
                },
                {
                    "type": "definition_plus_examples",
                    "i18n_key": "prealgebra.n1.b08.story.definition",
                    "definition_katex": "\\mathbb{R}=\\mathbb{Q}\\cup(\\mathbb{R}\\setminus\\mathbb{Q})",
                    "is_integrated": True,
                    "examples": [
                        {
                            "i18n_key": "prealgebra.n1.b08.story.examples.membership",
                            "name": "Pertenencia acumulada",
                            "steps": [
                                "Un natural tambien es entero.",
                                "Un entero tambien es racional.",
                                "Todo racional o irracional pertenece a los reales.",
                            ],
                        },
                        {
                            "i18n_key": "prealgebra.n1.b08.story.examples.line",
                            "name": "Ubicar numeros en la recta",
                            "steps": [
                                "Tomar los enteros como etiquetas de referencia.",
                                "Poner fracciones entre enteros.",
                                "Ubicar aproximaciones de irracionales sin convertirlos en racionales.",
                            ],
                        },
                    ],
                },
            ],
        },
        "interactions": [
            {
                "interaction_id": "PREALG-N1-B08-Q01",
                "type": "single_select",
                "prompt_key": "prealgebra.n1.b08.q01.prompt",
                "option_keys": ["union_yes", "irr_not_on_line", "integers_left_out"],
                "can_retry": True,
            },
            {
                "interaction_id": "PREALG-N1-B08-Q02",
                "type": "multi_select",
                "prompt_key": "prealgebra.n1.b08.q02.prompt",
                "option_keys": ["neg4", "dec075", "sqrt2", "pi", "two_i", "three_plus_two_i"],
                "can_retry": True,
            },
        ],
    },
    COMPLEX_NODE_ID: {
        "node_id": COMPLEX_NODE_ID,
        "node_type": "optional_extension",
        "topic": "complejos",
        "i18n_prefix": "prealgebra.n1.b09",
        # Hoja: rama lateral; no continúa la línea principal.
        "next_node_id": None,
        "unlock_after": REALS_NODE_ID,
        # Visible/explorable solo para banda media/alta (gating en el mapa).
        "unlock_rule": "elo_band in ['intermedio','avanzado']",
        "affects_elo": False,
        "is_safe_zone": True,
        "optional_branch": True,
        "skip_penalty": False,
        "objectives": ["identify_real_and_imaginary_parts", "locate_complex_in_plane"],
        "optional_objectives": ["recognize_reals_as_complex_with_zero_imaginary"],
        "interactions": [
            {
                "interaction_id": "PREALG-N1-B09-Q03",
                "type": "single_select",
                "prompt_key": "prealgebra.n1.b09.q03.prompt",
                "option_keys": ["imaginary_unit", "irrationals", "natural", "zero"],
                "can_retry": True,
            },
            {
                "interaction_id": "PREALG-N1-B09-Q01",
                "type": "single_select",
                "prompt_key": "prealgebra.n1.b09.q01.prompt",
                "option_keys": ["re3_im2", "re2_im3", "re0_im5", "no_real"],
                "can_retry": True,
            },
            {
                "interaction_id": "PREALG-N1-B09-Q02",
                "type": "single_select",
                "prompt_key": "prealgebra.n1.b09.q02.prompt",
                "option_keys": ["plane_off_line", "on_real_line", "cannot_place", "real_axis_5"],
                "can_retry": True,
            },
        ],
    },
}

_INTERACTION_RULES = {
    "PREALG-N1-B02-Q01": {
        "node_id": TRIGGER_NODE_ID,
        "valid_options": {"yes", "no"},
        "expected": "no",
        "misconception_by_option": {"yes": "cree_que_todo_numero_sirve_para_contar"},
        "feedback_by_option": {"yes": "counting_is_not_enough", "no": "need_new_numbers"},
    },
    "PREALG-N1-B02-Q02": {
        "node_id": TRIGGER_NODE_ID,
        "valid_options": {"temperature", "pizza", "debt"},
        "expected": None,
        "misconception_by_option": {},
        "feedback_by_option": {
            "temperature": "temperature_needs_integers",
            "pizza": "sharing_needs_fractions",
            "debt": "debt_needs_integers",
        },
    },
    "PREALG-N1-B03-Q01": {
        "node_id": STAIRCASE_NODE_ID,
        "valid_options": {"expand", "replace", "bigger"},
        "expected": "expand",
        "misconception_by_option": {
            "replace": "no_reconoce_ampliacion_progresiva",
            "bigger": "interpreta_conjuntos_como_categorias_aisladas",
        },
        "feedback_by_option": {
            "expand": "sets_expand",
            "replace": "numbers_remain",
            "bigger": "size_is_not_the_point",
        },
    },
    "PREALG-N1-B04-Q01": {
        "node_id": NATURALS_NODE_ID,
        "input_kind": "numeric",
        "expected": "8",
        "misconception_by_option": {},
        "feedback_by_result": {True: "total_correct", False: "sum_again"},
        "default_misconception": "error_de_suma",
    },
    "PREALG-N1-B04-Q02": {
        "node_id": NATURALS_NODE_ID,
        "valid_options": {"yes", "no"},
        "expected": "no",
        "misconception_by_option": {"yes": "calcula_sin_interpretar_suficiencia"},
        "feedback_by_option": {"yes": "eight_is_not_enough", "no": "comparison_correct"},
    },
    "PREALG-N1-B04-Q03": {
        "node_id": NATURALS_NODE_ID,
        "input_kind": "numeric",
        "expected": "2",
        "misconception_by_option": {},
        "feedback_by_result": {True: "missing_correct", False: "subtract_again"},
        "default_misconception": "error_de_resta",
    },
    "PREALG-N1-B04-Q04": {
        "node_id": NATURALS_NODE_ID,
        "input_kind": "multi_select",
        "valid_options": {"zero", "four", "negative_two", "sqrt_two", "fifteen", "decimal_25"},
        "expected": {"zero", "four", "fifteen"},
        "misconception_by_option": {},
    },
    "PREALG-N1-B05-Q01": {
        "node_id": INTEGERS_NODE_ID,
        "input_kind": "numeric",
        "expected": "35000",
        "misconception_by_option": {},
        "feedback_by_result": {True: "debt_total_correct", False: "add_debts_again"},
        "default_misconception": "error_de_suma",
    },
    "PREALG-N1-B05-Q02": {
        "node_id": INTEGERS_NODE_ID,
        "input_kind": "numeric",
        "expected": "5000",
        "misconception_by_option": {},
        "feedback_by_result": {True: "balance_correct", False: "payment_moves_to_zero"},
        "default_misconception": "confunde_abono_con_aumento_de_deuda",
    },
    "PREALG-N1-B05-Q03": {
        "node_id": INTEGERS_NODE_ID,
        "valid_options": {"positive", "negative", "zero"},
        "expected": "negative",
        "misconception_by_option": {
            "positive": "confunde_deuda_con_cantidad_positiva",
            "zero": "no_reconoce_cero_como_equilibrio",
        },
        "feedback_by_option": {
            "positive": "debt_is_below_zero",
            "negative": "negative_representation_correct",
            "zero": "zero_is_equilibrium",
        },
    },
    "PREALG-N1-B05-Q04": {
        "node_id": INTEGERS_NODE_ID,
        "valid_options": {"negative_35000", "negative_5000", "zero", "positive_5000"},
        "expected": "negative_5000",
        "misconception_by_option": {
            "negative_35000": "confunde_abono_con_aumento_de_deuda",
            "zero": "no_reconoce_cero_como_equilibrio",
            "positive_5000": "confunde_deuda_con_cantidad_positiva",
        },
        "feedback_by_option": {
            "negative_35000": "payment_changes_position",
            "negative_5000": "number_line_correct",
            "zero": "five_thousand_still_owed",
            "positive_5000": "debt_stays_negative",
        },
    },
    "PREALG-N1-B05-Q05": {
        "node_id": INTEGERS_NODE_ID,
        "input_kind": "multi_select",
        "valid_options": {"neg8", "neg_3_5", "zero", "half", "six", "neg_2_1"},
        "expected": {"neg8", "zero", "six"},
        "feedback_correct": "integers_correct",
        "default_feedback": "integers_review",
        "error_rules": [
            {"when_missing": "zero", "feedback": "zero_is_integer",
             "misconception": "no_reconoce_cero_como_equilibrio"},
            {"when_selected": "neg_3_5", "feedback": "decimal_not_integer",
             "misconception": "incluye_no_enteros_en_enteros"},
            {"when_selected": "neg_2_1", "feedback": "decimal_not_integer",
             "misconception": "incluye_no_enteros_en_enteros"},
            {"when_selected": "half", "feedback": "fraction_not_integer",
             "misconception": "incluye_no_enteros_en_enteros"},
        ],
    },
    "PREALG-N1-B06-Q01": {
        "node_id": RATIONALS_NODE_ID,
        "valid_options": {"three_fourths", "four_thirds", "add", "subtract"},
        "expected": "three_fourths",
        "misconception_by_option": {
            "four_thirds": "confunde_numerador_denominador",
            "add": "no_interpreta_fraccion_como_reparto",
            "subtract": "no_interpreta_fraccion_como_reparto",
        },
        "feedback_by_option": {
            "three_fourths": "sharing_fraction_correct",
            "four_thirds": "numerator_denominator_order",
            "add": "sharing_not_total",
            "subtract": "sharing_not_difference",
        },
    },
    "PREALG-N1-B06-Q02": {
        "node_id": RATIONALS_NODE_ID,
        "valid_options": {"three_div_four", "four_div_three", "add", "subtract"},
        "expected": "three_div_four",
        "misconception_by_option": {
            "four_div_three": "no_interpreta_fraccion_como_division",
            "add": "no_interpreta_fraccion_como_division",
            "subtract": "no_interpreta_fraccion_como_division",
        },
        "feedback_by_option": {
            "three_div_four": "division_order_correct",
            "four_div_three": "divide_numerator_by_denominator",
            "add": "fraction_means_division",
            "subtract": "fraction_means_division",
        },
    },
    "PREALG-N1-B06-Q03": {
        "node_id": RATIONALS_NODE_ID,
        "valid_options": {"decimal_075", "repeating_0333", "decimal_34", "decimal_43"},
        "expected": "decimal_075",
        "misconception_by_option": {
            "repeating_0333": "confunde_decimal_exacto_periodico",
            "decimal_34": "confunde_decimal_desde_division",
            "decimal_43": "confunde_decimal_desde_division",
        },
        "feedback_by_option": {
            "decimal_075": "decimal_correct",
            "repeating_0333": "one_third_repeats",
            "decimal_34": "perform_division",
            "decimal_43": "perform_division",
        },
    },
    "PREALG-N1-B06-Q04": {
        "node_id": RATIONALS_NODE_ID,
        "input_kind": "multi_select",
        "valid_options": {"frac_34", "dec_025", "neg3", "periodic_0333", "sqrt2", "pi"},
        "expected": {"frac_34", "dec_025", "neg3", "periodic_0333"},
        "feedback_correct": "rationals_all_correct",
        "default_feedback": "rationals_review",
        "error_rules": [
            {"when_missing": "neg3", "feedback": "omitted_integer",
             "misconception": "cree_que_enteros_no_son_racionales"},
            {"when_missing": "periodic_0333", "feedback": "omitted_periodic",
             "misconception": "cree_que_todo_decimal_infinito_es_irracional"},
            {"when_selected": "sqrt2", "feedback": "included_irrational",
             "misconception": "confunde_decimal_exacto_periodico"},
            {"when_selected": "pi", "feedback": "included_irrational",
             "misconception": "confunde_decimal_exacto_periodico"},
        ],
    },
    "PREALG-N1-B07-Q01": {
        "node_id": IRRATIONALS_NODE_ID,
        "valid_options": {"exact_025", "periodic_0333", "nonperiodic_pi"},
        "expected": "periodic_0333",
        "misconception_by_option": {
            "exact_025": "confunde_decimal_exacto_con_periodico",
            "nonperiodic_pi": "cree_que_todo_decimal_infinito_es_irracional",
        },
        "feedback_by_option": {
            "periodic_0333": "periodic_correct",
            "exact_025": "exact_not_periodic",
            "nonperiodic_pi": "pi_not_periodic",
        },
    },
    "PREALG-N1-B07-Q02": {
        "node_id": IRRATIONALS_NODE_ID,
        "valid_options": {"pi_exact", "pi_approx", "pi_ends"},
        "expected": "pi_approx",
        "misconception_by_option": {
            "pi_exact": "confunde_aproximacion_con_valor_exacto",
            "pi_ends": "cree_que_pi_termina",
        },
        "feedback_by_option": {
            "pi_approx": "approx_correct",
            "pi_exact": "approx_vs_exact",
            "pi_ends": "pi_does_not_end",
        },
    },
    "PREALG-N1-B07-Q03": {
        "node_id": IRRATIONALS_NODE_ID,
        "valid_options": {"between_1_2", "at_2", "between_2_3"},
        "expected": "between_1_2",
        "misconception_by_option": {
            "at_2": "confunde_sqrt2_con_aproximacion_decimal",
            "between_2_3": "confunde_sqrt2_con_aproximacion_decimal",
        },
        "feedback_by_option": {
            "between_1_2": "sqrt2_between_correct",
            "at_2": "sqrt2_not_2",
            "between_2_3": "sqrt2_too_high",
        },
    },
    "PREALG-N1-B08-Q01": {
        "node_id": REALS_NODE_ID,
        "valid_options": {"union_yes", "irr_not_on_line", "integers_left_out"},
        "expected": "union_yes",
        "misconception_by_option": {
            "irr_not_on_line": "no_reconoce_irracionales_como_reales",
            "integers_left_out": "no_reconoce_inclusion_de_conjuntos",
        },
        "feedback_by_option": {
            "union_yes": "union_correct",
            "irr_not_on_line": "irr_are_on_line",
            "integers_left_out": "integers_included",
        },
    },
    "PREALG-N1-B08-Q02": {
        "node_id": REALS_NODE_ID,
        "input_kind": "multi_select",
        "valid_options": {"neg4", "dec075", "sqrt2", "pi", "two_i", "three_plus_two_i"},
        "expected": {"neg4", "dec075", "sqrt2", "pi"},
        # camino genérico con trampas: incluir un complejo vs excluir un irracional.
        "trap_options": {"two_i", "three_plus_two_i"},
        "feedback_correct": "reales_correct",
        "feedback_trap": "complex_not_real",
        "feedback_missing": "irrationals_are_real",
        "feedback_incorrect": "reales_review",
        "misconception_trap": "ubica_complejos_en_recta_real",
        "misconception_missing": "no_reconoce_irracionales_como_reales",
        "misconception_incorrect": "confunde_reales_con_racionales",
    },
    "PREALG-N1-B09-Q03": {
        "node_id": COMPLEX_NODE_ID,
        "valid_options": {"imaginary_unit", "irrationals", "natural", "zero"},
        "expected": "imaginary_unit",
        "misconception_by_option": {
            "irrationals": "confunde_i_imaginaria_con_I_irracionales",
            "natural": "no_reconoce_unidad_imaginaria",
            "zero": "no_reconoce_unidad_imaginaria",
        },
        "feedback_by_option": {
            "imaginary_unit": "recognize_correct",
            "irrationals": "notation_warning",
            "natural": "not_those_sets",
            "zero": "not_those_sets",
        },
    },
    "PREALG-N1-B09-Q01": {
        "node_id": COMPLEX_NODE_ID,
        "valid_options": {"re3_im2", "re2_im3", "re0_im5", "no_real"},
        "expected": "re3_im2",
        "misconception_by_option": {
            "re2_im3": "confunde_parte_real_con_imaginaria",
            "re0_im5": "no_identifica_parte_real",
            "no_real": "cree_que_todo_complejo_es_imaginario",
        },
        "feedback_by_option": {
            "re3_im2": "parts_correct",
            "re2_im3": "parts_swapped",
            "re0_im5": "not_zero_five",
            "no_real": "has_real_part",
        },
    },
    "PREALG-N1-B09-Q02": {
        "node_id": COMPLEX_NODE_ID,
        "valid_options": {"plane_off_line", "on_real_line", "cannot_place", "real_axis_5"},
        "expected": "plane_off_line",
        "misconception_by_option": {
            "on_real_line": "ubica_complejos_no_reales_en_recta_real",
            "real_axis_5": "ubica_complejos_no_reales_en_recta_real",
            "cannot_place": "cree_que_complejos_no_se_ubican",
        },
        "feedback_by_option": {
            "plane_off_line": "plane_correct",
            "on_real_line": "not_on_line",
            "cannot_place": "can_place_in_plane",
            "real_axis_5": "not_at_5",
        },
    },
}


# ── B10 — El Clasificador I: conjunto más específico ──────────────────────────
# Cada tarjeta es una interacción single_select cuya "opción" es la zona elegida.
# Las tarjetas/zonas complejas (2i, 3+2i) solo se muestran con rama compleja
# (gating por banda en el frontend). Aquí se definen igual; el backend solo evalúa.
_B10_ZONES = ["naturals", "integers", "rationals", "irrationals", "pure_imaginary", "complex_general"]
_B10_REAL_ZONES = ["naturals", "integers", "rationals", "irrationals"]

# value → (expected_zone, {wrong_zone: (feedback_key, misconception_or_None)}, requires_complex)
_B10_CARDS = {
    "minus3": ("integers", {"naturals": ("minus_three_as_natural", None)}, False),
    "zero": ("naturals", {z: ("zero_not_natural", "excluye_cero_de_naturales_pese_a_convencion")
                          for z in _B10_ZONES if z != "naturals"}, False),
    "half": ("rationals", {
        "naturals": ("fraction_as_integer", "clasifica_fraccion_como_entero"),
        "integers": ("fraction_as_integer", "clasifica_fraccion_como_entero"),
        "irrationals": ("fraction_as_irrational", None),
    }, False),
    "sqrt2": ("irrationals", {"rationals": ("sqrt2_as_rational", "clasifica_irracional_como_racional")}, False),
    "pi": ("irrationals", {"rationals": ("pi_as_rational", "clasifica_irracional_como_racional")}, False),
    "five": ("naturals", {"integers": ("five_as_integer", "clasifica_entero_positivo_como_Z_en_vez_de_N")}, False),
    "two_i": ("pure_imaginary", {
        "irrationals": ("2i_as_irrational", "confunde_i_imaginaria_con_I_irracionales"),
        "complex_general": ("2i_as_complex_general", None),
    }, True),
    "three_plus_two_i": ("complex_general", {
        "pure_imaginary": ("3plus2i_as_pure", "clasifica_complejo_general_como_imaginario_puro"),
        **{z: ("3plus2i_as_real", "ubica_complejos_no_reales_en_recta_real") for z in _B10_REAL_ZONES},
    }, True),
    # Cartas extra de banda Avanzado (gating por banda en el frontend; el backend
    # solo evalúa). No requieren rama compleja.
    "decimal_0333": ("rationals", {
        "irrationals": ("decimal_0333_is_rational", "cree_que_todo_decimal_infinito_es_irracional"),
    }, False),
    "neg7": ("integers", {
        "naturals": ("neg7_is_integer", None),
    }, False),
    "four_fourths": ("naturals", {
        "rationals": ("four_fourths_is_one", "confunde_fraccion_aparente_con_racional"),
        "integers": ("four_fourths_is_one", "confunde_fraccion_aparente_con_racional"),
    }, False),
}

_LESSONS[CLASSIFIER_BASIC_NODE_ID] = {
    "node_id": CLASSIFIER_BASIC_NODE_ID,
    "node_type": "guided_practice",
    "topic": "clasificacion_especifica",
    "i18n_prefix": "prealgebra.n1.b10",
    "next_node_id": "PREALG-N1-B11-CLASIFICADOR-RIGUROSO",
    "unlock_after": REALS_NODE_ID,
    "affects_elo": False,
    "is_safe_zone": True,
    "optional_branch": False,
    "objectives": ["classify_in_most_specific_set"],
    "optional_objectives": ["distinguish_specific_from_multiple_membership"],
    "interactions": [
        {
            "interaction_id": f"PREALG-N1-B10-CARD-{value}",
            "type": "single_select",
            "prompt_key": f"prealgebra.n1.b10.cards.{value}",
            "option_keys": list(_B10_ZONES),
            "can_retry": True,
        }
        for value in _B10_CARDS
    ],
}

for _value, (_expected, _wrongs, _requires_complex) in _B10_CARDS.items():
    _INTERACTION_RULES[f"PREALG-N1-B10-CARD-{_value}"] = {
        "node_id": CLASSIFIER_BASIC_NODE_ID,
        "input_kind": "single_select",
        "valid_options": set(_B10_ZONES),
        "expected": _expected,
        "misconception_by_option": {z: m for z, (_f, m) in _wrongs.items() if m},
        "feedback_by_option": {_expected: "card_correct", **{z: f for z, (f, _m) in _wrongs.items()}},
        "default_feedback": "classify_generic",
    }


# ── B07 — mini-reto: rejilla de clasificación racional/irracional ─────────────
# Cada número es una interacción single_select con opciones {rational, irrational}.
# value → (expected, (feedback_wrong, misconception_wrong) | None)
_B07_GRID = {
    "dec05": ("rational", None),
    "periodic03": ("rational", ("periodic_as_irrational", "cree_que_todo_decimal_infinito_es_irracional")),
    "pi": ("irrational", ("irrational_as_rational", "no_reconoce_irracional_como_real")),
    "sqrt2": ("irrational", ("irrational_as_rational", "no_reconoce_irracional_como_real")),
    "seven": ("rational", ("integer_as_irrational", "cree_que_enteros_no_son_racionales")),
}

_LESSONS[IRRATIONALS_NODE_ID]["interactions"].extend(
    {
        "interaction_id": f"PREALG-N1-B07-G-{value}",
        "type": "single_select",
        "prompt_key": f"prealgebra.n1.b07.grid.items.{value}",
        "option_keys": ["rational", "irrational"],
        "can_retry": True,
    }
    for value in _B07_GRID
)

for _value, (_expected, _wrong) in _B07_GRID.items():
    _other = "irrational" if _expected == "rational" else "rational"
    _fb = {_expected: "grid_correct"}
    _mis = {}
    if _wrong:
        _fb[_other], _mis[_other] = _wrong[0], _wrong[1]
    _INTERACTION_RULES[f"PREALG-N1-B07-G-{_value}"] = {
        "node_id": IRRATIONALS_NODE_ID,
        "input_kind": "single_select",
        "valid_options": {"rational", "irrational"},
        "expected": _expected,
        "misconception_by_option": _mis,
        "feedback_by_option": _fb,
        "default_feedback": "grid_review",
    }


# ── B08 — mini-reto: rejilla verdadero/falso ──────────────────────────────────
# value → (expected, (feedback_wrong, misconception_wrong) | None). Cada afirmación
# es single_select {true, false}. (El drag_to_region del spec se omite: duplica la
# clasificación de B10.)
_B08_TF = {
    "s1": ("true", None),
    "s2": ("true", None),
    "s3": ("true", ("irrational_is_real_false", "no_reconoce_irracionales_como_reales")),
    "s4": ("false", ("real_is_rational_true", "cree_que_todo_real_es_racional")),
    "s5": ("false", ("complex_in_real_line", "ubica_complejos_en_recta_real")),
}

_LESSONS[REALS_NODE_ID]["interactions"].extend(
    {
        "interaction_id": f"PREALG-N1-B08-{key.upper()}",
        "type": "single_select",
        "prompt_key": f"prealgebra.n1.b08.tf.items.{key}",
        "option_keys": ["true", "false"],
        "can_retry": True,
    }
    for key in _B08_TF
)

for _key, (_expected, _wrong) in _B08_TF.items():
    _other = "false" if _expected == "true" else "true"
    _fb = {_expected: "tf_correct"}
    _mis = {}
    if _wrong:
        _fb[_other], _mis[_other] = _wrong[0], _wrong[1]
    _INTERACTION_RULES[f"PREALG-N1-B08-{_key.upper()}"] = {
        "node_id": REALS_NODE_ID,
        "input_kind": "single_select",
        "valid_options": {"true", "false"},
        "expected": _expected,
        "misconception_by_option": _mis,
        "feedback_by_option": _fb,
        "default_feedback": "tf_review",
    }


# ── B11 — El Clasificador II: pertenencia múltiple (matriz) ───────────────────
# Cada fila (número) es un multi_select sobre las columnas/conjuntos a los que
# pertenece. Columna ℂ y filas complejas (2i, 3+2i) requieren rama compleja
# (gating por flag en el frontend). El "descriptor" (imaginario puro / complejo
# no real) se difiere: el núcleo es la matriz de pertenencia.
# value → (expected_sets, complex_row, [error_rules])
_B11_COLS = ["n", "z", "q", "i", "r", "c"]
_B11_ROWS = {
    "minus3": ({"z", "q", "r", "c"}, False, [
        {"when_missing": "q", "feedback": "integer_not_rational", "misconception": "no_reconoce_Z_dentro_de_Q_R_C"},
        {"when_missing": "c", "feedback": "real_not_complex", "misconception": "no_reconoce_reales_como_complejos"},
        {"when_missing": "r", "feedback": "rational_not_real", "misconception": "no_reconoce_Q_dentro_de_R_C"},
    ]),
    "zero": ({"n", "z", "q", "r", "c"}, False, [
        {"when_missing": "n", "feedback": "zero_not_natural", "misconception": "excluye_cero_de_naturales_pese_a_convencion"},
        {"when_missing": "c", "feedback": "real_not_complex", "misconception": "no_reconoce_reales_como_complejos"},
    ]),
    "half": ({"q", "r", "c"}, False, [
        {"when_missing": "r", "feedback": "rational_not_real", "misconception": "no_reconoce_Q_dentro_de_R_C"},
        {"when_missing": "c", "feedback": "real_not_complex", "misconception": "no_reconoce_reales_como_complejos"},
    ]),
    "sqrt2": ({"i", "r", "c"}, False, [
        {"when_selected": "q", "feedback": "irrational_as_rational", "misconception": "clasifica_irracional_como_racional"},
        {"when_missing": "r", "feedback": "irrational_not_real", "misconception": "no_reconoce_irracionales_como_reales"},
        {"when_missing": "c", "feedback": "real_not_complex", "misconception": "no_reconoce_reales_como_complejos"},
    ]),
    "pi": ({"i", "r", "c"}, False, [
        {"when_selected": "q", "feedback": "irrational_as_rational", "misconception": "clasifica_irracional_como_racional"},
        {"when_missing": "r", "feedback": "irrational_not_real", "misconception": "no_reconoce_irracionales_como_reales"},
        {"when_missing": "c", "feedback": "real_not_complex", "misconception": "no_reconoce_reales_como_complejos"},
    ]),
    "five": ({"n", "z", "q", "r", "c"}, False, [
        {"when_missing": "z", "feedback": "only_most_specific", "misconception": "marca_solo_conjunto_mas_especifico"},
        {"when_missing": "c", "feedback": "real_not_complex", "misconception": "no_reconoce_reales_como_complejos"},
    ]),
    "two_i": ({"c"}, True, [
        {"when_selected": "r", "feedback": "two_i_as_real", "misconception": "ubica_complejos_no_reales_en_recta_real"},
        {"when_selected": "i", "feedback": "two_i_as_irrational", "misconception": "confunde_imaginario_puro_con_irracional"},
    ]),
    "three_plus_two_i": ({"c"}, True, [
        {"when_selected": "r", "feedback": "three_plus_two_i_as_real", "misconception": "ubica_complejos_no_reales_en_recta_real"},
        {"when_selected": "i", "feedback": "three_plus_two_i_as_real", "misconception": "ubica_complejos_no_reales_en_recta_real"},
    ]),
}

_LESSONS[CLASSIFIER_RIGOROUS_NODE_ID] = {
    "node_id": CLASSIFIER_RIGOROUS_NODE_ID,
    "node_type": "guided_practice",
    "topic": "clasificacion_multiple",
    "i18n_prefix": "prealgebra.n1.b11",
    "next_node_id": "PREALG-N1-B12-DETECTIVE-FALSEDADES",
    "unlock_after": CLASSIFIER_BASIC_NODE_ID,
    "affects_elo": False,
    "is_safe_zone": True,
    "optional_branch": False,
    "objectives": ["recognize_multiple_membership"],
    "optional_objectives": [],
    "interactions": [
        {
            "interaction_id": f"PREALG-N1-B11-ROW-{value}",
            "type": "multi_select",
            "prompt_key": f"prealgebra.n1.b11.rows.{value}",
            "option_keys": list(_B11_COLS),
            "can_retry": True,
        }
        for value in _B11_ROWS
    ],
}

for _value, (_expected, _complex, _rules) in _B11_ROWS.items():
    _INTERACTION_RULES[f"PREALG-N1-B11-ROW-{_value}"] = {
        "node_id": CLASSIFIER_RIGOROUS_NODE_ID,
        "input_kind": "multi_select",
        "valid_options": set(_B11_COLS),
        "expected": _expected,
        "feedback_correct": "row_correct",
        "default_feedback": "row_review",
        "error_rules": _rules,
    }

# Descriptor (solo filas complejas, requiere rama compleja): imaginario puro /
# complejo no real. Descriptor formal dentro de ℂ, no un conjunto de la cadena.
_B11_DESCRIPTORS = {"two_i": "pure_imaginary", "three_plus_two_i": "complex_non_real"}
_LESSONS[CLASSIFIER_RIGOROUS_NODE_ID]["interactions"].extend(
    {
        "interaction_id": f"PREALG-N1-B11-DESC-{value}",
        "type": "single_select",
        "prompt_key": f"prealgebra.n1.b11.descriptorPrompt.{value}",
        "option_keys": ["pure_imaginary", "complex_non_real", "none"],
        "can_retry": True,
    }
    for value in _B11_DESCRIPTORS
)
for _value, _expected in _B11_DESCRIPTORS.items():
    _wrong_fb = "desc_3plus2i_as_pure" if _value == "three_plus_two_i" else "desc_review"
    _INTERACTION_RULES[f"PREALG-N1-B11-DESC-{_value}"] = {
        "node_id": CLASSIFIER_RIGOROUS_NODE_ID,
        "input_kind": "single_select",
        "valid_options": {"pure_imaginary", "complex_non_real", "none"},
        "expected": _expected,
        "misconception_by_option": {
            ("pure_imaginary" if _expected == "complex_non_real" else "complex_non_real"):
                "confunde_conjunto_formal_con_descriptor",
        },
        "feedback_by_option": {_expected: "desc_correct"},
        "default_feedback": _wrong_fb,
    }


# ── B12 — El Detective de Falsedades: 14 afirmaciones V/F ──────────────────────
# A1–A9 siempre; A10–A14 requieren rama compleja (gating por flag en el frontend).
# key → (expected, misconception_on_error | None, requires_complex)
_B12_STATEMENTS = {
    "a1": ("true", None, False),
    "a2": ("false", "confunde_implicacion_con_reciproca", False),
    "a3": ("true", None, False),
    "a4": ("true", None, False),
    "a5": ("false", "cree_que_todo_real_es_racional", False),
    "a6": ("false", "cree_que_todo_decimal_infinito_es_irracional", False),
    "a7": ("true", "cree_que_todo_decimal_infinito_es_irracional", False),
    "a8": ("false", "cree_que_todo_real_es_racional", False),
    "a9": ("true", "no_reconoce_irracionales_como_reales", False),
    "a10": ("true", "no_reconoce_reales_como_complejos", True),
    "a11": ("false", "cree_que_todo_complejo_es_real", True),
    "a12": ("false", "cree_que_todo_complejo_es_real", True),
    "a13": ("true", None, True),
    "a14": ("true", "confunde_imaginario_puro_con_irracional", True),
}

_LESSONS[DETECTIVE_NODE_ID] = {
    "node_id": DETECTIVE_NODE_ID,
    "node_type": "guided_practice",
    "topic": "evaluacion_conceptual",
    "i18n_prefix": "prealgebra.n1.b12",
    "next_node_id": CLOSING_NODE_ID,
    "unlock_after": CLASSIFIER_RIGOROUS_NODE_ID,
    "affects_elo": False,
    "is_safe_zone": True,
    "optional_branch": False,
    "objectives": ["evaluate_membership_statements"],
    "optional_objectives": [],
    "interactions": [
        {
            "interaction_id": f"PREALG-N1-B12-{key.upper()}",
            "type": "single_select",
            "prompt_key": f"prealgebra.n1.b12.statements.{key}",
            "option_keys": ["true", "false"],
            "can_retry": True,
        }
        for key in _B12_STATEMENTS
    ],
}

for _key, (_expected, _mis, _complex) in _B12_STATEMENTS.items():
    _other = "false" if _expected == "true" else "true"
    _INTERACTION_RULES[f"PREALG-N1-B12-{_key.upper()}"] = {
        "node_id": DETECTIVE_NODE_ID,
        "input_kind": "single_select",
        "valid_options": {"true", "false"},
        "expected": _expected,
        "misconception_by_option": ({_other: _mis} if _mis else {}),
        "feedback_by_option": {_expected: f"{_key}_correct", _other: f"{_key}_incorrect"},
    }


# ── B13 — Cierre diagnóstico (nodo de resumen, sin interacciones) ─────────────
_LESSONS[CLOSING_NODE_ID] = {
    "node_id": CLOSING_NODE_ID,
    "node_type": "diagnostic_summary",
    "topic": "cierre_diagnostico",
    "i18n_prefix": "prealgebra.n1.b13",
    "next_node_id": None,
    "unlock_after": DETECTIVE_NODE_ID,
    "affects_elo": False,
    "is_safe_zone": True,
    "optional_branch": False,
    "objectives": ["consolidate_level_progress"],
    "optional_objectives": [],
    "interactions": [],
}

# Nodos formativos que consolida el diagnóstico (orden de ruta). B09 solo cuenta
# si el estudiante exploró la rama compleja.
# Nivel 2 - Operaciones basicas. El contenido marcado como NEW queda con
# validation_status para revision pedagogica antes de publicacion formal.
_N2_BUILDINGS = [
    {"id": "E01", "operation": "suma", "symbol": "+", "node_id": N2_SUM_NODE_ID,
     "card": "Tienes 3 manzanas y tu amigo te da 2 mas. Cuantas tienes ahora?"},
    {"id": "E02", "operation": "resta", "symbol": "-", "node_id": N2_SUBTRACTION_NODE_ID,
     "card": "Tienes 5 galletas y te comes 2. Cuantas te quedan?"},
    {"id": "E03", "operation": "multiplicacion", "symbol": "x",
     "node_id": N2_MULTIPLICATION_NODE_ID,
     "card": "Tienes 4 bolsas con 3 caramelos cada una. Cuantos caramelos tienes en total?"},
    {"id": "E04", "operation": "division", "symbol": "÷", "node_id": N2_DIVISION_NODE_ID,
     "card": "Tienes 12 chocolates y quieres repartirlos entre 4 amigos. Cuantos le tocan a cada uno?"},
    {"id": "E05", "operation": "potenciacion", "symbol": "a^n",
     "node_id": N2_EXPONENTIATION_NODE_ID,
     "card": "Un cultivo de bacterias se duplica cada hora. Si empiezas con 1 bacteria, cuantas tendras despues de 3 horas?"},
    {"id": "E06", "operation": "radicacion", "symbol": "√", "node_id": N2_RADICATION_NODE_ID,
     "card": "Tienes un jardin cuadrado de 16 m². Cuanto mide cada lado?"},
]

_N2_HUB_CONTENT = {
    "kind": "operation_city_hub",
    "level": "Nivel 2 - Operaciones basicas",
    "title": "La Ciudad de las Operaciones Basicas",
    "welcome_text": (
        "Hola, bienvenido a la ciudad de las operaciones basicas. Aqui podras conocer "
        "cada una de las operaciones primordiales de las matematicas, que en ambitos "
        "de la vida cobran mucha importancia. Espero que te diviertas y te deseo el "
        "mayor de los exitos."
    ),
    "scene_text": (
        "La ciudad tiene seis edificios. En cada uno descubrirás cómo esa operación se "
        "extiende desde los naturales hasta los números reales."
    ),
    "icebreaker": {
        "title": "Antes de entrar: calentando motores",
        "intro": "Tres escenas de la obra en construcción para entrar en calor antes de visitar los edificios.",
        "items": [
            {
                "id": "ICE1",
                "kind": "numeric",
                "prompt": (
                    "Un albañil apila 3 filas de ladrillos: la primera con 4 ladrillos, la "
                    "segunda con 4 más, la tercera con 4 más. ¿Cuántos ladrillos apiló en total?"
                ),
                "image_slot": True,
                "expr": "3\\times 4",
                "answer": "12",
            },
            {
                "id": "ICE2",
                "kind": "single_select",
                "story": (
                    "En la obra, un albañil junta 3 pilas de 5 tejas cada una, mientras que otro "
                    "ayudante ya tiene amontonadas 15 tejas sueltas en un solo montón."
                ),
                "image_slot": True,
                "support_objects": [
                    "3 pilas de 5 tejas cada una",
                    "1 montón suelto de 15 tejas",
                ],
                "prompt": "¿En qué se parecen las dos cantidades de tejas?",
                "options": [
                    {"id": "a", "text": "Ambas son 15 tejas, aunque estén agrupadas distinto."},
                    {"id": "b", "text": "El montón suelto pesa menos."},
                    {"id": "c", "text": "Las pilas se ven más ordenadas."},
                ],
                "expected": "a",
                "feedback_by_option": {
                    "a": "correct",
                    "b": "fb_n2_ice2_b",
                    "c": "fb_n2_ice2_c",
                },
                "misconception_by_option": {
                    "b": "confunde_agrupacion_con_cantidad",
                    "c": "confunde_orden_con_cantidad",
                },
            },
            {
                "id": "ICE3",
                "kind": "numeric",
                "prompt": (
                    "Al abrir la plaza hay 20 puestos vacíos. Durante la mañana llegan "
                    "comerciantes y ocupan 14. ¿Cuántos puestos quedan vacíos?"
                ),
                "image_slot": True,
                "expr": "20-14",
                "answer": "6",
            },
        ],
    },
    "advance_text": (
        "Ya conociste las seis operaciones de la ciudad. Ahora entra a cada edificio "
        "cuando quieras y descubrelas a fondo. Te recomiendo empezar por la suma."
    ),
    "gating": {"rule": "all_cards_opened", "cards_required": 6},
    "buildings": _N2_BUILDINGS,
    "feedback": {
        "correct": "¡Correcto!",
        "default": "Revisa la respuesta con calma antes de continuar.",
        "fb_n2_ice2_b": "El peso no cambia la cantidad: cuenta cuántas tejas hay en cada agrupación, no cómo se ven.",
        "fb_n2_ice2_c": "El orden o la prolijidad no cambian el total — cuenta las tejas de cada grupo.",
    },
    "validation_status": "NEW_content_pending_pedagogical_validation",
}

_N2_OPERATION_CONTENT = {
    N2_SUM_NODE_ID: {
        "kind": "operation_building", "operation": "addition",
        "title": "Suma: la máquina de juntar", "character": "KatIA",
        "intro": "En el ágora, KatIA reúne cantidades y observa cuándo el resultado permanece en el mismo conjunto.",
        "story_contract": {
            "type": "unified_set_extension",
            "practice_position": "after_definition_plus_examples",
            "is_integrated": True,
        },
        "katia": {
            "eyebrow": "KatIA abre el edificio de la suma",
            "title": "Juntar ofrendas en el ágora",
            "body": (
                "KatIA ordena ánforas, aceitunas y dracmas en una mesa de piedra. "
                "Al reunir cantidades, algunas familias numéricas conservan su tipo, "
                "pero otras pueden cambiar de familia aunque los dos números iniciales "
                "parezcan venir del mismo lugar."
            ),
            "question": "¿Juntar dos cantidades siempre da una cantidad del mismo tipo?",
        },
        "discovery": {
            "eyebrow": "Descubrimiento guiado",
            "title": "Juntar puede conservar o cambiar el conjunto",
            "body": (
                "3 aceitunas más 5 aceitunas siguen siendo 8 aceitunas: natural. "
                "Una deuda de 3 dracmas más 5 dracmas a favor da 2: entero. "
                "Las fracciones también se suman dentro de los racionales. Pero "
                "√2 + (−√2) usa dos irracionales y termina en 0, que es racional. "
                "Por eso no basta mirar los sumandos: hay que mirar el resultado."
            ),
        },
        "definition": (
            "Sumar combina dos o más cantidades llamadas sumandos para obtener un "
            "total. La suma conserva naturales, enteros, racionales, reales y "
            "complejos; no conserva siempre los irracionales."
        ),
        "definition_title": "Suma: combinar sumandos",
        "definition_katex": r"a+b=c",
        "worked_examples": [
            {
                "eyebrow": "Ejemplo 1 · Naturales",
                "title": "Aceitunas reunidas",
                "statement": "3 aceitunas de una cesta y 5 de otra.",
                "latex": r"3+5=8",
                "image_slot": True,
                "steps": [
                    "Primer sumando: 3 aceitunas.",
                    "Segundo sumando: 5 aceitunas.",
                    "Se juntan todas sin quitar ninguna: 3 + 5.",
                    "El total es 8, que sigue siendo natural.",
                ],
            },
            {
                "eyebrow": "Ejemplo 2 · Enteros",
                "title": "Deuda y pago",
                "statement": "KatIA registra una deuda de 3 dracmas y luego entran 5 dracmas.",
                "latex": r"-3+5=2",
                "image_slot": True,
                "steps": [
                    "La deuda se representa como −3.",
                    "El ingreso se representa como +5.",
                    "Sumamos los movimientos: −3 + 5.",
                    "El saldo queda en 2, un entero positivo.",
                ],
            },
            {
                "eyebrow": "Ejemplo 3 · Racionales",
                "title": "Dos medidas de aceite",
                "statement": "Media ánfora y un tercio de ánfora se vierten juntas.",
                "latex": r"\dfrac{1}{2}+\dfrac{1}{3}=\dfrac{3}{6}+\dfrac{2}{6}=\dfrac{5}{6}",
                "steps": [
                    "Ambos sumandos son fracciones de enteros.",
                    "Buscamos denominador común: 6.",
                    "1/2 = 3/6 y 1/3 = 2/6.",
                    "Sumamos numeradores: 3/6 + 2/6 = 5/6, que sigue en ℚ.",
                ],
            },
            {
                "eyebrow": "Ejemplo 4 · Reales",
                "title": "Un irracional más otro real",
                "statement": "KatIA suma una longitud √2 con una longitud π.",
                "latex": r"\sqrt{2}+\pi\in\mathbb{R}",
                "steps": [
                    "√2 es irracional y π también es real.",
                    "Los reales contienen racionales e irracionales.",
                    "La suma de dos reales sigue ubicada en la recta real.",
                    "Por eso √2 + π pertenece a ℝ.",
                ],
            },
            {
                "eyebrow": "Ejemplo 5 · Complejos",
                "title": "Suma en el plano",
                "statement": "Dos marcas del plano complejo se suman coordenada a coordenada.",
                "latex": r"(2+i)+(3+2i)=5+3i",
                "steps": [
                    "Sumamos las partes reales: 2 + 3 = 5.",
                    "Sumamos los coeficientes imaginarios: 1i + 2i = 3i.",
                    "El resultado es 5 + 3i.",
                    "Los complejos son cerrados bajo suma.",
                ],
            },
            {
                "eyebrow": "Trampa común · Irracionales",
                "title": "Dos irracionales pueden terminar en racional",
                "statement": "KatIA junta dos longitudes opuestas: √2 y −√2.",
                "latex": r"\sqrt{2}+(-\sqrt{2})=0",
                "trap": True,
                "steps": [
                    "√2 es irracional.",
                    "−√2 también es irracional.",
                    "Al sumarlas se cancelan exactamente: √2 + (−√2) = 0.",
                    "0 es racional; por eso los irracionales no son cerrados bajo suma.",
                ],
            },
        ],
        "closure": {
            "title": "¿Hasta dónde llega la suma?",
            "intro": "La suma conserva casi todos los conjuntos principales, pero los irracionales pueden caer a los racionales.",
            "rows": [
                {"symbol": r"\mathbb{N}", "name": "Naturales", "closed": "yes",
                 "latex": r"3+5=8",
                 "note": "Juntar dos cantidades completas no negativas sigue dando una cantidad natural."},
                {"symbol": r"\mathbb{Z}", "name": "Enteros", "closed": "yes",
                 "latex": r"-3+5=2",
                 "note": "Los enteros permiten sumar deudas y ganancias sin salir de ℤ."},
                {"symbol": r"\mathbb{Q}", "name": "Racionales", "closed": "yes",
                 "latex": r"\dfrac{1}{2}+\dfrac{1}{3}=\dfrac{5}{6}",
                 "note": "La suma de fracciones de enteros vuelve a ser una fracción de enteros."},
                {"symbol": r"\mathbb{I}", "name": "Irracionales", "closed": "no",
                 "latex": r"\sqrt{2}+(-\sqrt{2})=0\in\mathbb{Q}",
                 "note": "Dos irracionales pueden cancelarse y dar un racional: 𝕀 no cierra bajo suma."},
                {"symbol": r"\mathbb{R}", "name": "Reales", "closed": "yes",
                 "latex": r"\sqrt{2}+\pi\in\mathbb{R}",
                 "note": "La recta real es estable bajo suma."},
                {"symbol": r"\mathbb{C}", "name": "Complejos", "closed": "yes",
                 "latex": r"(2+i)+(3+2i)=5+3i",
                 "note": "También cierra; este es el desvío opcional avanzado."},
            ],
        },
        "situations": [
            {"id": "S1", "set_label": "Naturales", "prompt": "7 higos y 6 higos. ¿Cuántos hay en total?", "expr": r"7+6", "answer": "13"},
            {"id": "S2", "set_label": "Enteros", "prompt": "Una deuda de 8 dracmas y un pago de 5 dracmas. ¿Cuál es el saldo?", "expr": r"-8+5", "answer": "-3"},
            {"id": "S3", "set_label": "Racionales", "prompt": "Suma 1/4 de ánfora y 1/4 de ánfora. Responde en decimal.", "expr": r"\dfrac{1}{4}+\dfrac{1}{4}", "answer": "0,5"},
            {"id": "S4", "set_label": "Irracionales → racional", "prompt": "Suma √3 y −√3. ¿Qué número resulta?", "expr": r"\sqrt{3}+(-\sqrt{3})", "answer": "0"},
        ],
        "feedback": {"correct": "Correcto. Sumar es juntar cantidades y contar el total.",
                     "default": "Revisa que estes juntando todas las cantidades una sola vez."},
        "formalization": ["La suma es conmutativa: a + b = b + a.",
                          "La suma es asociativa: (a + b) + c = a + (b + c).",
                          "El elemento neutro es 0: a + 0 = a."],
        "closing": (
            "Katia resume: sumar es juntar partes para formar un total. En el "
            "siguiente edificio veremos que pasa cuando quitamos o comparamos."
        ),
        "validation_status": "F2_E01_unified_set_extension",
    },
    N2_SUBTRACTION_NODE_ID: {
        "kind": "operation_building", "operation": "subtraction",
        "title": "Resta: la máquina de quitar o comparar", "character": "KatIA",
        "intro": "En el mercado griego, KatIA muestra cómo quitar, comparar y bajar de cero obliga a ampliar conjuntos.",
        "story_contract": {
            "type": "unified_set_extension",
            "practice_position": "after_definition_plus_examples",
            "is_integrated": True,
        },
        "katia": {
            "eyebrow": "KatIA abre el edificio de la resta",
            "title": "Cuando quitar puede cruzar el cero",
            "body": (
                "KatIA cuenta dracmas en una mesa del ágora. Quitar pocas monedas "
                "parece natural; quitar más de las que hay revela otra zona de la "
                "escalera: los enteros. La resta enseña que comparar y quitar no "
                "siempre dejan el resultado en la familia inicial."
            ),
            "question": "¿Restar dos naturales siempre da un natural?",
        },
        "discovery": {
            "eyebrow": "Descubrimiento guiado",
            "title": "Restar muestra lo que falta",
            "body": (
                "Si hay 8 aceitunas y se entregan 3, quedan 5. Pero si KatIA tiene "
                "3 dracmas y debe pagar 5, la cuenta no se detiene: 3 − 5 = −2. "
                "La resta puede representar faltantes, deudas o posiciones bajo "
                "cero. En racionales sigue funcionando con fracciones, mientras "
                "que dos irracionales pueden restarse y terminar en un racional."
            ),
        },
        "definition": (
            "Restar parte de una cantidad inicial y quita o compara otra cantidad "
            "para obtener una diferencia. Cuando se quita más de lo disponible, "
            "el resultado puede quedar por debajo de cero."
        ),
        "definition_title": "Resta: diferencia entre cantidades",
        "definition_katex": r"a-b=c",
        "worked_examples": [
            {
                "eyebrow": "Ejemplo 1 · Naturales",
                "title": "Quitar sin cruzar cero",
                "statement": "8 aceitunas en una mesa; KatIA entrega 3.",
                "latex": r"8-3=5",
                "image_slot": True,
                "steps": [
                    "Cantidad inicial: 8 aceitunas.",
                    "Cantidad que se quita: 3 aceitunas.",
                    "Calculamos 8 − 3.",
                    "Quedan 5 aceitunas, un número natural.",
                ],
            },
            {
                "eyebrow": "Ejemplo 2 · Enteros",
                "title": "Restar más de lo que hay",
                "statement": "KatIA tiene 3 dracmas y debe pagar 5.",
                "latex": r"3-5=-2",
                "image_slot": True,
                "steps": [
                    "Partimos de 3 dracmas disponibles.",
                    "La obligación es pagar 5 dracmas.",
                    "Como faltan 2, el resultado cruza el cero.",
                    "3 − 5 = −2, que no es natural pero sí entero.",
                ],
            },
            {
                "eyebrow": "Ejemplo 3 · Racionales",
                "title": "Diferencia entre fracciones",
                "statement": "De media ánfora se usa un tercio.",
                "latex": r"\dfrac{1}{2}-\dfrac{1}{3}=\dfrac{3}{6}-\dfrac{2}{6}=\dfrac{1}{6}",
                "steps": [
                    "Ambas cantidades son racionales.",
                    "Buscamos denominador común: 6.",
                    "1/2 = 3/6 y 1/3 = 2/6.",
                    "La diferencia es 1/6, que sigue siendo racional.",
                ],
            },
            {
                "eyebrow": "Ejemplo 4 · Reales",
                "title": "Restar longitudes reales",
                "statement": "KatIA compara una longitud π con una longitud √2.",
                "latex": r"\pi-\sqrt{2}\in\mathbb{R}",
                "steps": [
                    "π y √2 se ubican en la recta real.",
                    "Restar dos reales produce otra posición en la recta.",
                    "El resultado puede no ser racional, pero sigue siendo real.",
                    "Por eso ℝ es cerrado bajo resta.",
                ],
            },
            {
                "eyebrow": "Ejemplo 5 · Complejos",
                "title": "Resta en el plano",
                "statement": "KatIA resta dos puntos complejos.",
                "latex": r"(3+2i)-(1+i)=2+i",
                "steps": [
                    "Restamos partes reales: 3 − 1 = 2.",
                    "Restamos coeficientes imaginarios: 2i − i = i.",
                    "El resultado es 2 + i.",
                    "Los complejos son cerrados bajo resta.",
                ],
            },
            {
                "eyebrow": "Trampa común · Irracionales",
                "title": "Restar irracionales puede dar racional",
                "statement": "KatIA compara una misma diagonal consigo misma.",
                "latex": r"\sqrt{2}-\sqrt{2}=0",
                "trap": True,
                "steps": [
                    "√2 es irracional.",
                    "Restamos el mismo irracional.",
                    "Toda cantidad menos sí misma da 0.",
                    "0 es racional; por eso 𝕀 no cierra bajo resta.",
                ],
            },
        ],
        "closure": {
            "title": "¿Hasta dónde llega la resta?",
            "intro": "La resta rompe primero en los naturales y vuelve a romper en los irracionales.",
            "rows": [
                {"symbol": r"\mathbb{N}", "name": "Naturales", "closed": "no",
                 "latex": r"3-5=-2\notin\mathbb{N}",
                 "note": "Restar más de lo disponible exige enteros negativos."},
                {"symbol": r"\mathbb{Z}", "name": "Enteros", "closed": "yes",
                 "latex": r"3-5=-2",
                 "note": "Los enteros sí contienen el resultado bajo cero."},
                {"symbol": r"\mathbb{Q}", "name": "Racionales", "closed": "yes",
                 "latex": r"\dfrac{1}{2}-\dfrac{1}{3}=\dfrac{1}{6}",
                 "note": "La diferencia de dos fracciones vuelve a ser fracción."},
                {"symbol": r"\mathbb{I}", "name": "Irracionales", "closed": "no",
                 "latex": r"\sqrt{2}-\sqrt{2}=0\in\mathbb{Q}",
                 "note": "Dos irracionales pueden dar un racional: 𝕀 no cierra bajo resta."},
                {"symbol": r"\mathbb{R}", "name": "Reales", "closed": "yes",
                 "latex": r"\pi-\sqrt{2}\in\mathbb{R}",
                 "note": "La recta real conserva la resta."},
                {"symbol": r"\mathbb{C}", "name": "Complejos", "closed": "yes",
                 "latex": r"(3+2i)-(1+i)=2+i",
                 "note": "También cierra; este es el desvío opcional avanzado."},
            ],
        },
        "situations": [
            {"id": "S1", "set_label": "Naturales", "prompt": "9 aceitunas menos 4 aceitunas. ¿Cuántas quedan?", "expr": r"9-4", "answer": "5"},
            {"id": "S2", "set_label": "Enteros", "prompt": "4 dracmas menos una deuda de 7 dracmas. ¿Qué saldo queda?", "expr": r"4-7", "answer": "-3"},
            {"id": "S3", "set_label": "Racionales", "prompt": "Resta 1/2 menos 1/4. Responde en decimal.", "expr": r"\dfrac{1}{2}-\dfrac{1}{4}", "answer": "0,25"},
            {"id": "S4", "set_label": "Irracionales → racional", "prompt": "Resta √5 menos √5. ¿Qué número resulta?", "expr": r"\sqrt{5}-\sqrt{5}", "answer": "0"},
        ],
        "feedback": {"correct": "Correcto. Restar es quitar o comparar.",
                     "default": "Cuidado con el orden: primero la cantidad inicial y luego la que quitas."},
        "formalization": ["La resta no es conmutativa.", "La resta es inversa de la suma.",
                          "Cuando falta mas de lo que hay, el resultado puede ser negativo."],
        "closing": (
            "Katia resume: restar puede significar quitar, comparar o medir lo "
            "que falta. En el siguiente edificio veremos una forma rapida de "
            "sumar grupos iguales."
        ),
        "validation_status": "F2_E02_unified_set_extension",
    },
    N2_MULTIPLICATION_NODE_ID: {
        "kind": "operation_building", "operation": "multiplication",
        "title": "Multiplicación: la máquina de agrupar", "character": "KatIA",
        "intro": "En el ágora, KatIA agrupa cantidades iguales y prueba qué conjuntos resisten la multiplicación.",
        "story_contract": {
            "type": "unified_set_extension",
            "practice_position": "after_definition_plus_examples",
            "is_integrated": True,
        },
        "katia": {
            "eyebrow": "KatIA abre el edificio de la multiplicación",
            "title": "Grupos iguales bajo las columnas",
            "body": (
                "KatIA organiza filas de ánforas junto a las columnas del ágora. "
                "Multiplicar puede verse como repetir grupos iguales, pero también "
                "como escalar una cantidad. Al subir por la escalera numérica, la "
                "pregunta cambia: ¿el resultado permanece en el mismo conjunto?"
            ),
            "question": "¿Multiplicar dos irracionales da siempre un irracional?",
        },
        "discovery": {
            "eyebrow": "Descubrimiento guiado",
            "title": "Agrupar conserva casi todo, menos 𝕀",
            "body": (
                "3 grupos de 4 ánforas dan 12 ánforas: natural. Una deuda repetida "
                "4 veces da un entero negativo. Las fracciones se multiplican entre "
                "sí y siguen siendo racionales. Pero √2 · √2 = 2: dos irracionales "
                "pueden producir un racional. Esa caída muestra que 𝕀 no es cerrado."
            ),
        },
        "definition": (
            "Multiplicar combina factores para obtener un producto. Puede representar "
            "suma repetida, grupos iguales o escalamiento. Conserva ℕ, ℤ, ℚ, ℝ y ℂ; "
            "no conserva siempre 𝕀."
        ),
        "definition_title": "Multiplicación: producto de factores",
        "definition_katex": r"a\cdot b=c",
        "worked_examples": [
            {
                "eyebrow": "Ejemplo 1 · Naturales",
                "title": "Filas de ánforas",
                "statement": "3 filas con 4 ánforas cada una.",
                "latex": r"3\times4=12",
                "image_slot": True,
                "steps": [
                    "Hay 3 grupos iguales.",
                    "Cada grupo tiene 4 ánforas.",
                    "Multiplicar resume la suma 4 + 4 + 4.",
                    "El producto es 12, que sigue siendo natural.",
                ],
            },
            {
                "eyebrow": "Ejemplo 2 · Enteros",
                "title": "Deuda repetida",
                "statement": "Una deuda de 3 dracmas se repite 4 veces.",
                "latex": r"(-3)\times4=-12",
                "image_slot": True,
                "steps": [
                    "Cada deuda se representa como −3.",
                    "La deuda ocurre 4 veces.",
                    "Sumar −3 cuatro veces equivale a (−3) × 4.",
                    "El resultado es −12, un entero.",
                ],
            },
            {
                "eyebrow": "Ejemplo 3 · Racionales",
                "title": "Parte de una parte",
                "statement": "KatIA toma 2/3 de una medida y luego 3/4 de esa parte.",
                "latex": r"\dfrac{2}{3}\times\dfrac{3}{4}=\dfrac{6}{12}=\dfrac{1}{2}",
                "steps": [
                    "Ambos factores son fracciones de enteros.",
                    "Multiplicamos numeradores: 2 × 3 = 6.",
                    "Multiplicamos denominadores: 3 × 4 = 12.",
                    "Simplificamos 6/12 = 1/2: sigue siendo racional.",
                ],
            },
            {
                "eyebrow": "Ejemplo 4 · Reales",
                "title": "Escalar una longitud",
                "statement": "Una longitud √2 se escala por π.",
                "latex": r"\sqrt{2}\cdot\pi\in\mathbb{R}",
                "steps": [
                    "√2 y π son reales.",
                    "Multiplicar reales produce otro número de la recta real.",
                    "El resultado puede ser irracional, pero no sale de ℝ.",
                    "Por eso los reales son cerrados bajo multiplicación.",
                ],
            },
            {
                "eyebrow": "Ejemplo 5 · Complejos",
                "title": "Factores conjugados",
                "statement": "KatIA multiplica dos complejos conjugados.",
                "latex": r"(1+i)(1-i)=1-i+i-i^{2}=2",
                "steps": [
                    "Distribuimos cada término.",
                    "Las partes imaginarias −i e +i se cancelan.",
                    "Como i² = −1, entonces −i² = 1.",
                    "El resultado es 2, que sigue perteneciendo a ℂ.",
                ],
            },
            {
                "eyebrow": "Trampa común · Irracionales",
                "title": "Dos irracionales pueden dar racional",
                "statement": "Multiplicar una diagonal √2 por sí misma.",
                "latex": r"\sqrt{2}\times\sqrt{2}=2",
                "trap": True,
                "steps": [
                    "√2 es irracional.",
                    "Multiplicamos el irracional por sí mismo.",
                    "√2 × √2 = (√2)² = 2.",
                    "2 es racional; por eso 𝕀 no cierra bajo multiplicación.",
                ],
            },
        ],
        "closure": {
            "title": "¿Hasta dónde llega la multiplicación?",
            "intro": "La multiplicación cierra en casi todos los conjuntos habituales, salvo en los irracionales.",
            "rows": [
                {"symbol": r"\mathbb{N}", "name": "Naturales", "closed": "yes",
                 "latex": r"3\times4=12",
                 "note": "Grupos completos de objetos completos siguen dando naturales."},
                {"symbol": r"\mathbb{Z}", "name": "Enteros", "closed": "yes",
                 "latex": r"(-3)\times4=-12",
                 "note": "El producto de enteros sigue siendo entero, con signo según los factores."},
                {"symbol": r"\mathbb{Q}", "name": "Racionales", "closed": "yes",
                 "latex": r"\dfrac{2}{3}\times\dfrac{3}{4}=\dfrac{1}{2}",
                 "note": "El producto de fracciones de enteros vuelve a ser fracción de enteros."},
                {"symbol": r"\mathbb{I}", "name": "Irracionales", "closed": "no",
                 "latex": r"\sqrt{2}\times\sqrt{2}=2\in\mathbb{Q}",
                 "note": "Dos irracionales pueden producir un racional: 𝕀 no cierra bajo multiplicación."},
                {"symbol": r"\mathbb{R}", "name": "Reales", "closed": "yes",
                 "latex": r"\sqrt{2}\cdot\pi\in\mathbb{R}",
                 "note": "El producto de reales sigue en la recta real."},
                {"symbol": r"\mathbb{C}", "name": "Complejos", "closed": "yes",
                 "latex": r"(1+i)(1-i)=2",
                 "note": "También cierra; este es el desvío opcional avanzado."},
            ],
        },
        "situations": [
            {"id": "S1", "set_label": "Naturales", "prompt": "6 filas con 7 ánforas cada una. ¿Cuántas ánforas hay?", "expr": r"6\times7", "answer": "42"},
            {"id": "S2", "set_label": "Enteros", "prompt": "Una deuda de 5 dracmas se repite 4 veces. ¿Cuál es el total?", "expr": r"(-5)\times4", "answer": "-20"},
            {"id": "S3", "set_label": "Racionales", "prompt": "Multiplica 1/2 por 1/2. Responde en decimal.", "expr": r"\dfrac{1}{2}\times\dfrac{1}{2}", "answer": "0,25"},
            {"id": "S4", "set_label": "Irracionales → racional", "prompt": "Multiplica √3 por √3. ¿Qué número resulta?", "expr": r"\sqrt{3}\times\sqrt{3}", "answer": "3"},
        ],
        "feedback": {"correct": "Correcto. Multiplicar es sumar grupos iguales de forma mas rapida.",
                     "default": "No sumes los factores entre si: identifica grupos y elementos por grupo."},
        "formalization": ["La multiplicacion es conmutativa.", "La multiplicacion es asociativa.",
                          "Se relaciona con la division como operacion inversa."],
        "validation_status": "F2_E03_unified_set_extension",
    },
    N2_DIVISION_NODE_ID: {
        "kind": "operation_building", "operation": "division",
        "title": "División: la máquina de repartir", "character": "KatIA",
        "intro": "En el ágora, KatIA reparte provisiones en partes iguales entre sus discípulos.",
        "story_contract": {
            "type": "unified_set_extension",
            "practice_position": "after_definition_plus_examples",
            "is_integrated": True,
        },
        "katia": {
            "eyebrow": "KatIA abre el edificio de la división",
            "title": "Repartir en partes iguales en el ágora",
            "body": (
                "En el ágora, KatIA reparte una cesta de aceitunas en partes iguales "
                "entre sus discípulos. Dividir es eso: repartir —o agrupar— una "
                "cantidad en grupos del mismo tamaño."
            ),
            "question": "¿Toda división entre dos naturales da otro número natural?",
        },
        "discovery": {
            "eyebrow": "Descubrimiento guiado",
            "title": "A veces el reparto no es exacto",
            "body": (
                "12 aceitunas entre 4 discípulos dan 3 a cada uno: el reparto es "
                "exacto. 27 higos entre 6 dan 4 y sobran 3: aparece un residuo. "
                "Pero 5 medidas de aceite entre 2 ánforas no caben en un entero, y "
                "aun así cada ánfora recibe la mitad de la que sobra: 5 ÷ 2 = 2,5. "
                "El reparto pide un número nuevo, una fracción."
            ),
        },
        "definition": (
            "Dividir reparte el dividendo en partes iguales según el divisor y "
            "obtiene un cociente. Si el reparto no es exacto, queda un residuo. "
            "El divisor nunca puede ser cero."
        ),
        "definition_title": "División: reparto en partes iguales",
        "definition_katex": r"a \div b = c, \quad b \neq 0",
        "worked_examples": [
            {
                "eyebrow": "Ejemplo 1 · Naturales",
                "title": "Reparto exacto",
                "statement": "12 aceitunas entre 4 discípulos.",
                "latex": r"12 \div 4 = 3",
                "image_slot": True,
                "steps": [
                    "Dividendo: 12 aceitunas. Divisor: 4 discípulos.",
                    "Buscamos cuántas recibe cada uno en partes iguales.",
                    "12 ÷ 4 = 3: cada discípulo recibe 3 aceitunas y no sobra nada.",
                ],
            },
            {
                "eyebrow": "Ejemplo 2 · Naturales",
                "title": "Reparto con residuo",
                "statement": "27 higos entre 6 discípulos.",
                "latex": r"27 = 6 \cdot 4 + 3",
                "image_slot": True,
                "steps": [
                    "Dividendo: 27 higos. Divisor: 6 discípulos.",
                    "El múltiplo de 6 más cercano sin pasarse es 6 × 4 = 24.",
                    "Sobran 27 − 24 = 3 higos: ese es el residuo.",
                    "Cociente 4 y residuo 3, es decir 27 = 6 × 4 + 3.",
                ],
            },
            {
                "eyebrow": "Ejemplo 3 · Enteros",
                "title": "Repartir una deuda",
                "statement": "Una deuda de 12 dracmas se reparte en 4 pagos iguales.",
                "latex": r"-12 \div 4 = -3",
                "steps": [
                    "La deuda total es −12 dracmas: una cantidad negativa.",
                    "Se reparte en 4 pagos iguales: −12 ÷ 4.",
                    "Cada pago es −3 dracmas: la división conserva el signo.",
                ],
            },
            {
                "eyebrow": "Ejemplo 4 · Racionales",
                "title": "Cuando no cabe en los enteros",
                "statement": "5 medidas de aceite entre 2 ánforas.",
                "latex": r"5 \div 2 = \dfrac{5}{2} = 2{,}5",
                "steps": [
                    "No es «2 y sobra 1 para siempre»: el reparto sí se completa.",
                    "La medida que sobra también se reparte: la mitad para cada ánfora.",
                    "Cada ánfora recibe 5 ÷ 2 = 5/2 = 2,5: un número racional, no entero.",
                ],
            },
            {
                "eyebrow": "Ejemplo 5 · Racionales",
                "title": "Dividir una fracción entre otra fracción",
                "statement": "¿Cuántas porciones de 1/2 ánfora hay en 3/4 de ánfora?",
                "latex": r"\dfrac{3}{4} \div \dfrac{1}{2} = \dfrac{3}{4} \cdot \dfrac{2}{1} = \dfrac{6}{4} = \dfrac{3}{2} = 1{,}5",
                "steps": [
                    "Dividir entre una fracción es multiplicar por su inverso: se da vuelta la segunda fracción.",
                    "3/4 ÷ 1/2 = 3/4 × 2/1.",
                    "Multiplicamos en línea: (3 × 2) / (4 × 1) = 6/4.",
                    "Simplificamos: 6/4 = 3/2 = 1,5. El resultado sigue siendo racional, así que ℚ es cerrado.",
                ],
            },
            {
                "eyebrow": "Trampa común · Irracionales",
                "title": "Dividir irracionales puede salir del conjunto",
                "statement": "Dividir dos cantidades irracionales: √8 entre √2.",
                "latex": r"\sqrt{8} \div \sqrt{2} = \sqrt{\tfrac{8}{2}} = \sqrt{4} = 2",
                "trap": True,
                "steps": [
                    "√8 y √2 son irracionales: su decimal es infinito y no periódico.",
                    "Al dividir raíces de la misma clase: √8 ÷ √2 = √(8 ÷ 2) = √4.",
                    "Pero √4 = 2, que es racional: el resultado SE SALE de los irracionales.",
                    "Por eso los irracionales no son cerrados bajo división; los reales sí lo son.",
                ],
            },
        ],
        "closure": {
            "title": "¿Hasta dónde llega la división?",
            "intro": (
                "La división se cierra en los racionales, pero al subir a los "
                "irracionales se rompe otra vez. Por eso necesitamos los reales."
            ),
            "rows": [
                {"symbol": r"\mathbb{N}", "name": "Naturales", "closed": "no",
                 "latex": r"5 \div 2 \notin \mathbb{N}",
                 "note": "El reparto no exacto no da un número natural."},
                {"symbol": r"\mathbb{Z}", "name": "Enteros", "closed": "no",
                 "latex": r"5 \div 2 \notin \mathbb{Z}",
                 "note": "Los signos no bastan: 5 entre 2 sigue sin ser entero."},
                {"symbol": r"\mathbb{Q}", "name": "Racionales", "closed": "yes",
                 "latex": r"\dfrac{a}{b} \div \dfrac{c}{d} = \dfrac{a\,d}{b\,c} \in \mathbb{Q}",
                 "note": "Toda división con divisor distinto de 0 tiene resultado. Por esto existen los racionales (B06)."},
                {"symbol": r"\mathbb{I}", "name": "Irracionales", "closed": "no",
                 "latex": r"\sqrt{2} \div \sqrt{2} = 1 \in \mathbb{Q}",
                 "note": "Dividir dos irracionales puede dar un racional: el resultado se sale del conjunto. Los irracionales NO son cerrados bajo división."},
                {"symbol": r"\mathbb{R}", "name": "Reales", "closed": "yes",
                 "latex": r"\pi \div 2 = \dfrac{\pi}{2} \in \mathbb{R}",
                 "note": "Un real entre un real distinto de 0 sigue siendo real. Por esto la unión de racionales e irracionales, los reales (B08), sí cierra."},
                {"symbol": r"\mathbb{C}", "name": "Complejos", "closed": "yes",
                 "latex": r"\dfrac{1}{i} = -i",
                 "note": "También cierra; lo retoma el desvío opcional de complejos (B09)."},
            ],
        },
        "situations": [
            {"id": "S1", "set_label": "Naturales", "prompt": "18 aceitunas entre 3 discípulos. ¿Cuántas recibe cada uno?", "expr": r"18 \div 3", "answer": "6"},
            {"id": "S2", "set_label": "Naturales", "prompt": "20 higos entre 5 discípulos. ¿Cuántos recibe cada uno?", "expr": r"20 \div 5", "answer": "4"},
            {"id": "S3", "set_label": "Naturales · residuo", "prompt": "22 higos entre 6 discípulos. ¿Cuál es el cociente (lo que recibe cada uno)?", "expr": r"22 \div 6", "answer": "3"},
            {"id": "S4", "set_label": "Enteros", "prompt": "Una deuda de 20 dracmas se reparte en 5 pagos iguales. ¿Cuánto es cada pago? (en negativo)", "expr": r"-20 \div 5", "answer": "-4"},
            {"id": "S5", "set_label": "Racionales", "prompt": "9 medidas de aceite entre 2 ánforas. ¿Cuánto recibe cada una? (decimal)", "expr": r"9 \div 2", "answer": "4,5"},
            {"id": "S6", "set_label": "Racionales", "prompt": "7 panes entre 4 discípulos. ¿Cuánto recibe cada uno? (decimal)", "expr": r"7 \div 4", "answer": "1,75"},
            {"id": "S7", "set_label": "Racionales · fracciones", "prompt": "¿Cuántas porciones de 1/4 caben en 1/2 ánfora? (entero)", "expr": r"\dfrac{1}{2} \div \dfrac{1}{4}", "answer": "2"},
            {"id": "S8", "set_label": "Irracionales → racional", "prompt": "Divide √18 entre √2. ¿Qué número entero resulta?", "expr": r"\sqrt{18} \div \sqrt{2}", "answer": "3"},
        ],
        "feedback": {"correct": "Correcto. Dividir reparte en partes iguales.",
                     "default": "Revisa que todos reciban la misma cantidad antes de contar lo que sobra."},
        "formalization": ["División exacta: a = b × c.", "Con residuo: a = b × c + r, con 0 ≤ r < b.",
                          "La división no es conmutativa ni asociativa.",
                          "Es cerrada en ℚ\\{0} y en ℝ; nunca se divide por 0."],
        "validation_status": "F2_E04_unified_set_extension_pilot",
    },
    N2_EXPONENTIATION_NODE_ID: {
        "kind": "operation_building", "operation": "exponentiation",
        "title": "Potenciación: la máquina de crecer", "character": "KatIA",
        "intro": "En el ágora, KatIA eleva bases y cambia exponentes para ver cuándo el resultado abandona el conjunto inicial.",
        "story_contract": {
            "type": "unified_set_extension",
            "practice_position": "after_definition_plus_examples",
            "is_integrated": True,
        },
        "katia": {
            "eyebrow": "KatIA abre el edificio de la potenciación",
            "title": "La torre de exponentes",
            "body": (
                "KatIA apila tablillas junto a una columna griega: cada nivel "
                "multiplica la base otra vez. Pero cuando el exponente baja de "
                "cero o se vuelve fraccionario, la torre deja de comportarse como "
                "un simple conteo natural."
            ),
            "question": "Si subimos el exponente por debajo de cero o entre enteros, ¿el resultado sigue siendo natural?",
        },
        "discovery": {
            "eyebrow": "Descubrimiento guiado",
            "title": "El exponente decide el salto",
            "body": (
                "2³ multiplica 2 tres veces y da 8, natural. Pero 2⁻² ya no es "
                "un natural: equivale a 1/4. Y 2^(1/2) significa una raíz, por eso "
                "aparece √2, un irracional. La potenciación no solo depende de la "
                "base: el tipo de exponente puede empujar el resultado a otro conjunto."
            ),
        },
        "definition": (
            "Potenciar consiste en elevar una base a un exponente. Con exponente "
            "natural, la base se multiplica por sí misma. Exponentes negativos "
            "producen recíprocos y exponentes fraccionarios se relacionan con raíces."
        ),
        "definition_title": "Potenciación: base y exponente",
        "definition_katex": r"a^{n}=a\cdot a\cdots a",
        "worked_examples": [
            {
                "eyebrow": "Ejemplo 1 · Exponente natural",
                "title": "Crecimiento por niveles",
                "statement": "Una pila duplica su tamaño durante 3 niveles.",
                "latex": r"2^{3}=2\cdot2\cdot2=8",
                "image_slot": True,
                "steps": [
                    "La base es 2.",
                    "El exponente 3 indica tres factores iguales.",
                    "No calculamos 2 × 3; calculamos 2 × 2 × 2.",
                    "El resultado es 8, un natural.",
                ],
            },
            {
                "eyebrow": "Ejemplo 2 · Exponente entero negativo",
                "title": "Bajar niveles invierte",
                "statement": "KatIA eleva 2 a −2.",
                "latex": r"2^{-2}=\dfrac{1}{2^{2}}=\dfrac{1}{4}=0{,}25",
                "image_slot": True,
                "steps": [
                    "Un exponente negativo no vuelve negativa la base.",
                    "Indica recíproco: 2^(-2) = 1/2².",
                    "Calculamos 2² = 4.",
                    "El resultado es 1/4 = 0,25, racional y no natural.",
                ],
            },
            {
                "eyebrow": "Ejemplo 3 · Exponente racional",
                "title": "El exponente fraccionario es raíz",
                "statement": "KatIA eleva 2 a la mitad.",
                "latex": r"2^{1/2}=\sqrt{2}",
                "steps": [
                    "El exponente 1/2 se interpreta como raíz cuadrada.",
                    "2^(1/2) pregunta por el número cuyo cuadrado es 2.",
                    "Ese número es √2.",
                    "√2 es irracional, así que el resultado sale de ℚ.",
                ],
            },
            {
                "eyebrow": "Ejemplo 4 · Irracionales",
                "title": "Un irracional puede volver a racional",
                "statement": "La diagonal √2 se eleva al cuadrado.",
                "latex": r"(\sqrt{2})^{2}=2",
                "steps": [
                    "√2 es irracional.",
                    "Elevar al cuadrado deshace la raíz cuadrada.",
                    "(√2)² = 2.",
                    "2 es racional; 𝕀 no cierra bajo potenciación.",
                ],
            },
            {
                "eyebrow": "Ejemplo 5 · Reales",
                "title": "Base positiva con exponente real",
                "statement": "KatIA observa 2 elevado a π.",
                "latex": r"2^{\pi}\in\mathbb{R}",
                "steps": [
                    "La base 2 es positiva.",
                    "π es un exponente real.",
                    "La potencia se define dentro de los reales positivos.",
                    "El resultado pertenece a ℝ.",
                ],
            },
            {
                "eyebrow": "Trampa común · Complejos",
                "title": "Una base negativa con exponente fraccionario",
                "statement": "KatIA pregunta por la raíz cuadrada de −1.",
                "latex": r"(-1)^{1/2}=\sqrt{-1}=i",
                "trap": True,
                "steps": [
                    "El exponente 1/2 pide una raíz cuadrada.",
                    "En los reales no existe un número cuyo cuadrado sea −1.",
                    "El desvío complejo define i con i² = −1.",
                    "Por eso (−1)^(1/2) motiva ℂ.",
                ],
            },
        ],
        "closure": {
            "title": "¿Hasta dónde llega la potenciación?",
            "intro": "Aquí la pregunta es si el resultado se queda en el conjunto de la base cuando cambia el exponente.",
            "rows": [
                {"symbol": r"\mathbb{N}", "name": "Naturales", "closed": "yes",
                 "latex": r"2^{3}=8",
                 "note": "Base natural y exponente natural conservan un resultado natural."},
                {"symbol": r"\mathbb{Z}", "name": "Enteros", "closed": "no",
                 "latex": r"2^{-2}=\dfrac{1}{4}",
                 "note": "El exponente negativo lleva a racionales: no se queda en naturales ni enteros."},
                {"symbol": r"\mathbb{Q}", "name": "Racionales", "closed": "no",
                 "latex": r"2^{1/2}=\sqrt{2}",
                 "note": "Un exponente racional puede producir un irracional."},
                {"symbol": r"\mathbb{I}", "name": "Irracionales", "closed": "no",
                 "latex": r"(\sqrt{2})^{2}=2\in\mathbb{Q}",
                 "note": "Un irracional elevado a una potencia puede caer a ℚ."},
                {"symbol": r"\mathbb{R}", "name": "Reales", "closed": "yes",
                 "latex": r"2^{\pi}\in\mathbb{R}",
                 "note": "Con base positiva, exponentes reales permanecen en ℝ."},
                {"symbol": r"\mathbb{C}", "name": "Complejos", "closed": "yes",
                 "latex": r"(-1)^{1/2}=i",
                 "note": "El caso complejo explica raíces de bases negativas; es el desvío opcional avanzado."},
            ],
        },
        "situations": [
            {"id": "S1", "set_label": "Naturales", "prompt": "Calcula 3 elevado a 3.", "expr": r"3^{3}", "answer": "27"},
            {"id": "S2", "set_label": "Enteros negativos → racional", "prompt": "Calcula 5 elevado a −2. Responde en decimal.", "expr": r"5^{-2}", "answer": "0,04"},
            {"id": "S3", "set_label": "Racionales", "prompt": "Calcula (1/2) elevado a 2. Responde en decimal.", "expr": r"\left(\dfrac{1}{2}\right)^{2}", "answer": "0,25"},
            {"id": "S4", "set_label": "Irracionales → racional", "prompt": "Calcula (√3) elevado a 2.", "expr": r"(\sqrt{3})^{2}", "answer": "3"},
            {"id": "S5", "set_label": "Exponente fraccionario", "prompt": "Calcula 9 elevado a 1/2.", "expr": r"9^{1/2}", "answer": "3"},
        ],
        "feedback": {"correct": "Correcto. Eso es crecimiento exponencial.",
                     "default": "Aqui no se suma siempre lo mismo: cada paso multiplica por el factor."},
        "formalization": ["a^n x a^m = a^(n+m).", "a^0 = 1 si a no es 0.",
                          "La radicacion deshace una potencia."],
        "validation_status": "F2_E05_unified_set_extension",
    },
    N2_RADICATION_NODE_ID: {
        "kind": "operation_building", "operation": "radication",
        "title": "Radicación: la máquina de encontrar raíces", "character": "KatIA",
        "intro": "En el último edificio, KatIA busca raíces y muestra cómo nacen irracionales y complejos.",
        "story_contract": {
            "type": "unified_set_extension",
            "practice_position": "after_definition_plus_examples",
            "is_integrated": True,
        },
        "katia": {
            "eyebrow": "KatIA abre el edificio de la radicación",
            "title": "Buscar el lado oculto",
            "body": (
                "KatIA dibuja cuadrados en el suelo del ágora. Si conoce el área, "
                "busca el lado; si conoce el volumen, busca la arista. Algunas raíces "
                "vuelven a números conocidos, pero otras obligan a aceptar nuevos "
                "puntos de la recta y, con negativos, el plano complejo."
            ),
            "question": "¿Toda raíz de un número entero es otro entero?",
        },
        "discovery": {
            "eyebrow": "Descubrimiento guiado",
            "title": "La raíz puede crear nuevos números",
            "body": (
                "√16 = 4 porque 4² = 16: aquí todo queda en naturales. Pero √2 no "
                "es entero ni racional; aparece un irracional. Al tomar raíces, los "
                "cuadrados perfectos son casos especiales. Si el radicando es negativo, "
                "la recta real ya no alcanza y aparece i."
            ),
        },
        "definition": (
            "La radicación es la operación inversa de la potenciación: busca el número "
            "que, elevado al índice indicado, produce el radicando. En raíces pares "
            "reales, el radicando debe ser no negativo."
        ),
        "definition_title": "Radicación: operación inversa",
        "definition_katex": r"\sqrt[n]{a}=b \quad \Longleftrightarrow \quad b^{n}=a",
        "worked_examples": [
            {
                "eyebrow": "Ejemplo 1 · Naturales",
                "title": "Cuadrado perfecto",
                "statement": "Un patio cuadrado tiene área 16.",
                "latex": r"\sqrt{16}=4",
                "image_slot": True,
                "steps": [
                    "Buscamos el lado del cuadrado.",
                    "Preguntamos qué número al cuadrado da 16.",
                    "4² = 16.",
                    "Por eso √16 = 4, que es natural.",
                ],
            },
            {
                "eyebrow": "Ejemplo 2 · Enteros",
                "title": "No toda raíz es entera",
                "statement": "KatIA calcula la raíz cuadrada de 2.",
                "latex": r"\sqrt{2}\notin\mathbb{Z}",
                "image_slot": True,
                "steps": [
                    "2 no es un cuadrado perfecto.",
                    "No existe entero cuyo cuadrado sea 2.",
                    "Por eso √2 no pertenece a ℤ.",
                    "Necesitamos ampliar hacia los irracionales.",
                ],
            },
            {
                "eyebrow": "Ejemplo 3 · Racionales",
                "title": "Raíz que sale de ℚ",
                "statement": "KatIA pregunta si √2 puede escribirse como fracción.",
                "latex": r"\sqrt{2}\notin\mathbb{Q}",
                "steps": [
                    "Los racionales son fracciones de enteros.",
                    "√2 tiene decimal infinito no periódico.",
                    "No puede escribirse como fracción de enteros.",
                    "La radicación puede producir irracionales.",
                ],
            },
            {
                "eyebrow": "Ejemplo 4 · Irracionales",
                "title": "La raíz crea un irracional",
                "statement": "La diagonal de un cuadrado de lado 1.",
                "latex": r"\sqrt{2}\in\mathbb{R}\setminus\mathbb{Q}",
                "steps": [
                    "El lado del cuadrado mide 1.",
                    "La diagonal cumple d² = 1² + 1² = 2.",
                    "Entonces d = √2.",
                    "√2 es real, pero no racional.",
                ],
            },
            {
                "eyebrow": "Ejemplo 5 · Reales",
                "title": "Raíz real aproximada",
                "statement": "Un patio cuadrado tiene área 20.",
                "latex": r"\sqrt{20}\approx4{,}4721",
                "steps": [
                    "20 no es cuadrado perfecto.",
                    "La raíz existe porque 20 es positivo.",
                    "El resultado es real, aunque no sea racional.",
                    "Aproximamos √20 ≈ 4,4721.",
                ],
            },
            {
                "eyebrow": "Trampa común · Complejos",
                "title": "Raíz de un negativo",
                "statement": "KatIA busca un número cuyo cuadrado sea −1.",
                "latex": r"\sqrt{-1}=i",
                "trap": True,
                "steps": [
                    "Ningún número real al cuadrado da −1.",
                    "La recta real no basta para esta raíz.",
                    "En el plano complejo aparece i, definido por i² = −1.",
                    "Por eso la radicación motiva el desvío a ℂ.",
                ],
            },
        ],
        "closure": {
            "title": "¿Hasta dónde llega la radicación?",
            "intro": "La radicación no conserva los conjuntos pequeños: puede crear irracionales y motivar complejos.",
            "rows": [
                {"symbol": r"\mathbb{N}", "name": "Naturales", "closed": "no",
                 "latex": r"\sqrt{16}=4,\quad \sqrt{2}\notin\mathbb{N}",
                 "note": "Solo los cuadrados perfectos vuelven a naturales."},
                {"symbol": r"\mathbb{Z}", "name": "Enteros", "closed": "no",
                 "latex": r"\sqrt{2}\notin\mathbb{Z}",
                 "note": "La raíz de un entero no siempre es otro entero."},
                {"symbol": r"\mathbb{Q}", "name": "Racionales", "closed": "no",
                 "latex": r"\sqrt{2}\notin\mathbb{Q}",
                 "note": "La raíz de un no-cuadrado puede ser irracional."},
                {"symbol": r"\mathbb{I}", "name": "Irracionales", "closed": "partial",
                 "latex": r"\sqrt{2}\in\mathbb{R}\setminus\mathbb{Q}",
                 "note": "La radicación produce irracionales y motiva el peldaño 𝕀."},
                {"symbol": r"\mathbb{R}", "name": "Reales", "closed": "yes",
                 "latex": r"\sqrt{20}\approx4{,}4721",
                 "note": "Para radicandos no negativos, la raíz queda en ℝ."},
                {"symbol": r"\mathbb{C}", "name": "Complejos", "closed": "yes",
                 "latex": r"\sqrt{-1}=i",
                 "note": "Los radicandos negativos de índice par motivan el desvío opcional avanzado."},
            ],
        },
        "situations": [
            {"id": "S1", "set_label": "Naturales", "prompt": "Un patio cuadrado tiene área 25. ¿Cuánto mide cada lado?", "expr": r"\sqrt{25}", "answer": "5"},
            {"id": "S2", "set_label": "Naturales", "prompt": "Si 3² = 9, ¿cuánto es √9?", "expr": r"\sqrt{9}", "answer": "3"},
            {"id": "S3", "set_label": "Enteros", "prompt": "La raíz cúbica de −27 es un entero. ¿Cuál?", "expr": r"\sqrt[3]{-27}", "answer": "-3"},
            {"id": "S4", "set_label": "Racionales", "prompt": "Calcula √0,25. Responde en decimal.", "expr": r"\sqrt{0{,}25}", "answer": "0,5"},
            {"id": "S5", "set_label": "Reales", "prompt": "Aproxima √50 a cuatro decimales.", "expr": r"\sqrt{50}", "answer": "7,0711"},
        ],
        "feedback": {"correct": "Correcto. La raiz es la operacion inversa de la potencia.",
                     "default": "La raiz busca el numero que elevado al indice da el radicando."},
        "formalization": ["n√a = b equivale a b^n = a.", "√20 se aproxima a 4,4721.",
                          "En reales, una raiz de indice par requiere radicando no negativo."],
        "validation_status": "F2_E06_unified_set_extension",
    },
}

_N2_SEQUENCE = [
    (N2_HUB_NODE_ID, "level_hub_3d", "ciudad_operaciones", "prealgebra.n2.e00", CLOSING_NODE_ID),
    (N2_SUM_NODE_ID, "operation_building_manipulative", "suma", "prealgebra.n2.e01", N2_HUB_NODE_ID),
    (N2_SUBTRACTION_NODE_ID, "operation_building_situations", "resta", "prealgebra.n2.e02", N2_HUB_NODE_ID),
    (N2_MULTIPLICATION_NODE_ID, "operation_building_progressive", "multiplicacion", "prealgebra.n2.e03", N2_HUB_NODE_ID),
    (N2_DIVISION_NODE_ID, "operation_building_manipulative", "division", "prealgebra.n2.e04", N2_HUB_NODE_ID),
    (N2_EXPONENTIATION_NODE_ID, "operation_building_growth_table", "potenciacion", "prealgebra.n2.e05", N2_HUB_NODE_ID),
    (N2_RADICATION_NODE_ID, "operation_building_geometric_last", "radicacion", "prealgebra.n2.e06", N2_HUB_NODE_ID),
]

for _index, (_node_id, _node_type, _topic, _prefix, _unlock_after) in enumerate(_N2_SEQUENCE):
    _content = _N2_HUB_CONTENT if _node_id == N2_HUB_NODE_ID else _N2_OPERATION_CONTENT[_node_id]
    _next = _N2_SEQUENCE[_index + 1][0] if _index + 1 < len(_N2_SEQUENCE) else None
    _LESSONS[_node_id] = {
        "node_id": _node_id,
        "node_type": _node_type,
        "topic": _topic,
        "i18n_prefix": _prefix,
        "next_node_id": _next,
        "unlock_after": _unlock_after,
        "affects_elo": False,
        "is_safe_zone": True,
        "optional_branch": False,
        "skip_penalty": False,
        "objectives": ["understand_basic_operations", "solve_contextual_situations"],
        "optional_objectives": [],
        "content": _content,
        "interactions": [],
    }

for _building in _N2_BUILDINGS:
    _interaction_id = f"{N2_HUB_NODE_ID}-CARD-{_building['id']}"
    _LESSONS[N2_HUB_NODE_ID]["interactions"].append({
        "interaction_id": _interaction_id,
        "type": "single_select",
        "prompt_key": _building["operation"],
        "option_keys": ["opened"],
        "can_retry": False,
    })
    _INTERACTION_RULES[_interaction_id] = {
        "node_id": N2_HUB_NODE_ID,
        "valid_options": {"opened"},
        "expected": "opened",
        "misconception_by_option": {},
        "feedback_by_option": {"opened": "card_opened"},
    }

for _node_id in N2_OPERATION_NODE_IDS:
    for _situation in _N2_OPERATION_CONTENT[_node_id]["situations"]:
        _interaction_id = f"{_node_id}-{_situation['id']}"
        _LESSONS[_node_id]["interactions"].append({
            "interaction_id": _interaction_id,
            "type": "numeric_input",
            "prompt_key": _situation["id"],
            "option_keys": [],
            "can_retry": True,
        })
        _INTERACTION_RULES[_interaction_id] = {
            "node_id": _node_id,
            "input_kind": "numeric",
            "expected": _situation["answer"],
            "misconception_by_option": {},
            "feedback_by_result": {True: "correct", False: "default"},
            "default_misconception": f"error_{_N2_OPERATION_CONTENT[_node_id]['operation']}",
        }

# Nivel 3 - Laboratorio de propiedades misteriosas. Guion Fase 3:
# aprendizaje por descubrimiento, hub de laboratorio y cinco máquinas secuenciales.
_N3_MACHINES = [
    {
        "id": "M01",
        "property": "conmutativa",
        "station": "La Prensa de Intercambio · el orden no importa",
        "symbol": "a↔b",
        "node_id": N3_COMMUTATIVE_NODE_ID,
        "demo": "3 + 5 = 8; 5 + 3 = 8",
        "katia_message": "¡Qué curioso! El orden no importa.",
    },
    {
        "id": "M02",
        "property": "asociativa",
        "station": "El Horno de Fundición · agrupar sin reordenar",
        "symbol": "( )",
        "node_id": N3_ASSOCIATIVE_NODE_ID,
        "demo": "(2 + 3) + 4 = 9; 2 + (3 + 4) = 9",
        "katia_message": "¡Extraño! La forma de agrupar no cambia el resultado.",
    },
    {
        "id": "M03",
        "property": "distributiva",
        "station": "La Cinta Repartidora · un factor, muchas piezas",
        "symbol": "×→",
        "node_id": N3_DISTRIBUTIVE_NODE_ID,
        "demo": "3 × (4 + 2) = 18; 3 × 4 + 3 × 2 = 18",
        "katia_message": "¡Increíble! La multiplicación se distribuye sobre la suma.",
    },
    {
        "id": "M04",
        "property": "elemento neutro",
        "station": "El Calibre Cero · el número que no cambia nada",
        "symbol": "0·1",
        "node_id": N3_IDENTITY_NODE_ID,
        "demo": "5 + 0 = 5; 5 × 1 = 5",
        "katia_message": "Hay números que no cambian el resultado.",
    },
    {
        "id": "M05",
        "property": "inversos",
        "station": "La Prensa de Contrapesos · la pieza que cancela",
        "symbol": "±",
        "node_id": N3_INVERSES_NODE_ID,
        "demo": "5 − 5 = 0; 5 × 1/5 = 1",
        "katia_message": "Hay números que se cancelan entre sí.",
    },
]

_N3_HUB_CONTENT = {
    "kind": "property_laboratory_hub",
    "level": "Nivel 3 - Propiedades",
    "title": "El Laboratorio de las Propiedades Misteriosas",
    "welcome_text": (
        "Hola, bienvenido al laboratorio de las propiedades misteriosas. Aquí podrás "
        "conocer algunas de las propiedades más importantes de los números al realizar "
        "operaciones matemáticas. Espero que te diviertas y te deseo el mayor de los éxitos."
    ),
    "scene_text": (
        "El laboratorio tiene cinco máquinas industriales. En cada una descubrirás una "
        "regla secreta de las operaciones mediante una demostración, una serie guiada "
        "y una formalización."
    ),
    "drag_rule": (
        "Al seleccionar un número, la casilla destino se ilumina de verde y las demás "
        "de rojo; solo se permite soltar el número en la casilla correspondiente."
    ),
    "icebreaker": {
        "title": "Antes de calibrar: primeras pesadas",
        "intro": "Tres pesadas de prueba en la balanza del laboratorio para entrar en calor antes de las máquinas.",
        "items": [
            {
                "id": "ICE1",
                "kind": "numeric",
                "prompt": (
                    "Una máquina del laboratorio pesa 3 bloques de 4 kg cada uno en el platillo "
                    "izquierdo. ¿Cuántos kg marca la balanza en total?"
                ),
                "image_slot": True,
                "expr": "3\\times 4",
                "answer": "12",
            },
            {
                "id": "ICE2",
                "kind": "single_select",
                "story": (
                    "Un ayudante coloca primero un engranaje de 5 kg y luego uno de 3 kg en el "
                    "platillo de una balanza. En una balanza idéntica, otro ayudante coloca "
                    "primero el de 3 kg y luego el de 5 kg."
                ),
                "image_slot": True,
                "support_objects": [
                    "2 balanzas de laboratorio idénticas",
                    "un engranaje de 5 kg y uno de 3 kg por balanza",
                ],
                "prompt": "¿Qué marcarán las dos balanzas al final?",
                "options": [
                    {"id": "a", "text": "Lo mismo: 8 kg en ambas, el orden no cambió el peso total."},
                    {"id": "b", "text": "La segunda balanza marcará menos."},
                    {"id": "c", "text": "No se puede saber sin pesarlos de nuevo."},
                ],
                "expected": "a",
                "feedback_by_option": {
                    "a": "correct",
                    "b": "fb_n3_ice2_b",
                    "c": "fb_n3_ice2_c",
                },
                "misconception_by_option": {
                    "b": "cree_que_el_orden_cambia_el_total",
                    "c": "duda_de_propiedad_verificable",
                },
            },
            {
                "id": "ICE3",
                "kind": "numeric",
                "prompt": (
                    "La balanza marca 9 kg con una pieza de prueba puesta. Al retirar esa "
                    "pieza, que pesa exactamente 9 kg, ¿cuánto marca la balanza?"
                ),
                "image_slot": True,
                "expr": "9-9",
                "answer": "0",
            },
        ],
    },
    "advance_text": (
        "¡Descubriste las cinco propiedades del laboratorio! Ahora entiendes algunas "
        "de las reglas secretas que siguen los números cuando operamos con ellos."
    ),
    "gating": {"rule": "all_machines_introduced", "machines_required": 5},
    "machines": _N3_MACHINES,
    "feedback": {
        "correct": "¡Correcto!",
        "default": "Revisa la respuesta con calma antes de continuar.",
        "fb_n3_ice2_b": "El peso total no depende del orden en que se coloquen las piezas — suma ambas, en cualquier orden.",
        "fb_n3_ice2_c": "Sí se puede saber sin volver a pesar: el orden de las piezas no cambia cuánto pesan juntas.",
    },
    "validation_status": "F3_storytelling_implemented",
}

_N3_MACHINE_CONTENT = {
    N3_COMMUTATIVE_NODE_ID: {
        "kind": "property_machine",
        "machine_id": "M01",
        "property": "commutative",
        "title": "Máquina Conmutativa - La Propiedad del Intercambio",
        "intro": (
            "Hola de nuevo, bienvenido a la máquina conmutativa. Aquí aprenderás cómo "
            "funciona y cómo aplica para algunas operaciones matemáticas, como la suma "
            "y la multiplicación, pero no para la resta y la división."
        ),
        "opening_hook": {
            "demo": "3 + 5 = 8; luego 5 + 3 = 8",
            "katia_message": "¡Qué curioso! El orden no importa.",
        },
        "definition": (
            "Conmutar es intercambiar el orden de los números. Una operación es "
            "conmutativa si, al intercambiar el orden, el resultado no cambia."
        ),
        "formal_expression": "a ⊕ b = b ⊕ a",
        "story_contract": {
            "type": "unified_set_extension",
            "practice_position": "after_definition_plus_examples",
            "is_integrated": True,
        },
        "katia": {
            "eyebrow": "KatIA · La Prensa de Intercambio",
            "title": "¿Importa el orden?",
            "body": (
                "En el banco de ensamblaje da igual colocar primero 3 engranajes y luego 6 tornillos, o "
                "al revés: la pieza montada es la misma, 3 + 6 = 6 + 3. Pero si la prensa primero perfora "
                "y luego suelda, invertir el orden arruina la pieza. No todos los procesos de la fábrica "
                "son tan indiferentes al orden."
            ),
            "question": "¿El orden en que operas dos cantidades cambia el resultado en todas las operaciones?",
        },
        "discovery": {
            "eyebrow": "Descubrimiento guiado",
            "title": "Conmutar es intercambiar el orden",
            "body": (
                "Una operación es CONMUTATIVA si al intercambiar el orden de los números el resultado no "
                "cambia. Lo comprobaremos operación por operación: suma, multiplicación, resta y división."
            ),
        },
        "definition_title": "Propiedad conmutativa",
        "definition_katex": "a+b=b+a \\qquad a\\times b=b\\times a",
        "worked_examples": [
            {
                "eyebrow": "Ejemplo 1 · Enteros",
                "title": "La suma conmuta con negativos",
                "statement": "En el banco de ensamblaje, aun con una pieza de peso negativo en la báscula, el orden de la suma no cambia el total.",
                "latex": "-3+8=5=8+(-3)",
                "image_slot": True,
                "steps": ["−3 + 8 = 5.", "8 + (−3) = 5.", "Mismo resultado con enteros: la suma conmuta."],
                "solution": "−3 + 8 = 5 y 8 + (−3) = 5",
            },
            {
                "eyebrow": "Ejemplo 2 · Racionales",
                "title": "También conmuta con fracciones",
                "statement": "Al calibrar dos fracciones de una plancha, sumarlas da lo mismo en cualquier orden.",
                "latex": "\\dfrac{1}{2}+\\dfrac{1}{4}=\\dfrac{3}{4}=\\dfrac{1}{4}+\\dfrac{1}{2}",
                "steps": ["½ + ¼ = ¾.", "¼ + ½ = ¾.", "El orden tampoco importa con racionales."],
                "solution": "½ + ¼ = ¾ y ¼ + ½ = ¾",
            },
            {
                "eyebrow": "Ejemplo 3 · Irracionales",
                "title": "Y conmuta con irracionales",
                "statement": "En la prensa, el producto de dos medidas irracionales no depende del orden en que se introducen.",
                "latex": "\\sqrt{2}\\cdot\\sqrt{3}=\\sqrt{6}=\\sqrt{3}\\cdot\\sqrt{2}",
                "steps": ["√2 · √3 = √6.", "√3 · √2 = √6.", "La conmutatividad vale en todos los conjuntos."],
                "solution": "√2 · √3 = √6 y √3 · √2 = √6",
            },
            {
                "eyebrow": "Trampa común",
                "title": "La división tampoco conmuta",
                "statement": "En la línea de corte, invertir el orden de una división cambia por completo el resultado; no es libre como en el banco de ensamblaje.",
                "latex": "6\\div 3=2\\quad\\text{pero}\\quad 3\\div 6=0{,}5",
                "trap": True,
                "steps": ["6 ÷ 3 = 2.", "3 ÷ 6 = 0,5.", "Resta y división dependen del orden: NO son conmutativas."],
                "solution": "6 ÷ 3 = 2 pero 3 ÷ 6 = 0,5",
            },
        ],
        "closure": {
            "eyebrow": "Validez a lo largo de las operaciones",
            "title": "¿En qué operaciones el orden es libre?",
            "intro": "Recorremos las cuatro operaciones básicas preguntando si intercambiar el orden conserva el resultado.",
            "rows": [
                {"symbol": "+", "name": "Suma", "closed": "yes", "latex": "7+5=5+7",
                 "note": "El orden es libre: a + b = b + a."},
                {"symbol": "\\times", "name": "Multiplicación", "closed": "yes", "latex": "8\\times 3=3\\times 8",
                 "note": "También libre: a × b = b × a."},
                {"symbol": "-", "name": "Resta", "closed": "no", "latex": "9-2\\neq 2-9",
                 "note": "Cambiar el orden cambia el signo del resultado."},
                {"symbol": "\\div", "name": "División", "closed": "no", "latex": "6\\div 3\\neq 3\\div 6",
                 "note": "El orden altera por completo el cociente."},
            ],
        },
        "instruction": "Escribe el valor correspondiente a las siguientes operaciones matemáticas.",
        "operation_groups": [
            {"id": "G1", "ops": [{"id": "O1", "expr": "5 + 3", "answer": "8"},
                                  {"id": "O2", "expr": "3 + 5", "answer": "8"}],
             "katia_after": "Ohhh, vaya, ¿será que el orden de los números al sumar no afecta el resultado final? Comprobémoslo."},
            {"id": "G2", "ops": [{"id": "O3", "expr": "10 + 8", "answer": "18"},
                                  {"id": "O4", "expr": "8 + 10", "answer": "18"}],
             "katia_after": "Efectivamente, dentro de la suma el orden no altera el resultado final. Veamos si aplica a las otras operaciones."},
            {"id": "G3", "ops": [{"id": "O5", "expr": "4 × 6", "answer": "24"},
                                  {"id": "O6", "expr": "6 × 4", "answer": "24"}],
             "katia_after": "Por lo visto, con la multiplicación también el orden de los números no afecta el resultado."},
            {"id": "G4", "ops": [{"id": "O7", "expr": "9 × 4", "answer": "36"},
                                  {"id": "O8", "expr": "4 × 9", "answer": "36"}],
             "katia_after": "Efectivamente, en la multiplicación el orden no afecta el resultado final. Ahora veamos qué tal con la resta."},
            {"id": "G5", "ops": [{"id": "O9", "expr": "8 − 3", "answer": "5"},
                                  {"id": "O10", "expr": "3 − 8", "answer": "-5"}],
             "katia_after": "¿Qué pasó aquí? ¿Será acaso que en la resta el orden sí cambia el resultado?"},
            {"id": "G6", "ops": [{"id": "O11", "expr": "17 − 6", "answer": "11"},
                                  {"id": "O12", "expr": "6 − 17", "answer": "-11"}],
             "katia_after": "En la resta sí cambia el resultado según el orden. Ahora veamos qué tal nos va en la división."},
            {"id": "G7", "ops": [{"id": "O13", "expr": "8 ÷ 2", "answer": "4"},
                                  {"id": "O14", "expr": "2 ÷ 8", "answer": "0,25"}],
             "katia_after": "Wow, ese sí fue un cambio enorme. En la división el orden de los números sí importa muchísimo."},
            {"id": "G8", "ops": [{"id": "O15", "expr": "10 ÷ 4", "answer": "2,5"},
                                  {"id": "O16", "expr": "4 ÷ 10", "answer": "0,4"}],
             "katia_after": "Efectivamente, dentro de la división es fundamental el orden en que se expresan los números."},
            {"id": "G9", "ops": [{"id": "O17", "expr": "-8 + 3", "answer": "-5"},
                                  {"id": "O18", "expr": "3 + (-8)", "answer": "-5"}],
             "katia_after": "Con enteros negativos la suma tampoco depende del orden."},
            {"id": "G10", "ops": [{"id": "O19", "expr": "3/4 + 1/4", "answer": "1"},
                                   {"id": "O20", "expr": "1/4 + 3/4", "answer": "1"}],
             "katia_after": "Y con fracciones igual: el orden no cambia la suma."},
        ],
        "feedback": {
            "correct": "✓ Correcto. Si el resultado es el mismo al invertir el orden, esa operación es conmutativa.",
            "default": "Revisa la operación y compárala con su pareja: suma y multiplicación conservan el resultado; resta y división no.",
        },
        "formalization": [
            "Una operación ⊕ es conmutativa si para todos los números a y b se cumple que a ⊕ b = b ⊕ a.",
            "Operaciones conmutativas: suma (+) y multiplicación (×).",
            "Operaciones NO conmutativas: resta (−) y división (÷).",
        ],
        "closing": "Ya descubriste la primera propiedad. En la siguiente máquina veremos qué pasa cuando agrupamos los números de distinta forma.",
    },
    N3_ASSOCIATIVE_NODE_ID: {
        "kind": "property_machine",
        "machine_id": "M02",
        "property": "associative",
        "title": "Máquina Asociativa - La Propiedad de la Agrupación",
        "intro": (
            "Bienvenido a la máquina asociativa. Aquí aprenderás en cuáles operaciones "
            "básicas, al operar tres o más números, el resultado no cambia sin importar "
            "cómo se agrupen o asocien los términos."
        ),
        "opening_hook": {
            "demo": "(2 + 3) + 4 = 9; luego 2 + (3 + 4) = 9",
            "katia_message": "¡Extraño! La forma de agrupar no cambia el resultado.",
        },
        "definition": (
            "Asociar es agrupar los números con paréntesis para decidir qué operación "
            "se hace primero, sin cambiar el orden de los números."
        ),
        "formal_expression": "(a ⊕ b) ⊕ c = a ⊕ (b ⊕ c)",
        "story_contract": {
            "type": "unified_set_extension",
            "practice_position": "after_definition_plus_examples",
            "is_integrated": True,
        },
        "katia": {
            "eyebrow": "KatIA · El Horno de Fundición",
            "title": "¿Importa a quién agrupo primero?",
            "body": (
                "Tres lingotes distintos entran al horno de fundición. Da igual fundir primero el par de "
                "la izquierda y sumar el tercero después, o agrupar al revés: la aleación final pesa lo "
                "mismo. Pero si la prensa primero perfora una plancha y luego corta, cambiar el orden de "
                "las etapas sí altera la pieza."
            ),
            "question": "Cuando operamos tres cantidades, ¿importa cuáles agrupamos primero?",
        },
        "discovery": {
            "eyebrow": "Descubrimiento guiado",
            "title": "Asociar es agrupar sin reordenar",
            "body": (
                "Una operación es ASOCIATIVA si al cambiar SOLO el agrupamiento (los paréntesis), sin "
                "reordenar los números, el resultado no cambia. Es distinta de la conmutativa: aquí los "
                "números se quedan en su lugar, solo cambia qué etapa se resuelve primero. Lo "
                "comprobaremos con las cuatro operaciones básicas."
            ),
        },
        "definition_title": "Propiedad asociativa",
        "definition_katex": "(a+b)+c=a+(b+c)\\qquad(a\\times b)\\times c=a\\times(b\\times c)",
        "worked_examples": [
            {
                "eyebrow": "Ejemplo 1 · Enteros",
                "title": "La suma asocia con negativos",
                "statement": "En el horno, con un lingote de peso negativo en el trío, reagrupar la fundición no cambia el total.",
                "latex": "(-2+5)+3=6=-2+(5+3)",
                "image_slot": True,
                "steps": ["(−2 + 5) + 3 = 3 + 3 = 6.", "−2 + (5 + 3) = −2 + 8 = 6.", "Mismo total con enteros: la suma asocia."],
                "solution": "(−2 + 5) + 3 = 6 y −2 + (5 + 3) = 6",
            },
            {
                "eyebrow": "Ejemplo 2 · Racionales",
                "title": "La multiplicación asocia con fracciones",
                "statement": "Al fundir una fracción de metal con dos lingotes enteros, el producto no depende de cómo se agrupen en el horno.",
                "latex": "\\left(\\dfrac{1}{2}\\cdot 4\\right)\\cdot 3=6=\\dfrac{1}{2}\\cdot(4\\cdot 3)",
                "steps": ["(½ · 4) · 3 = 2 · 3 = 6.", "½ · (4 · 3) = ½ · 12 = 6.", "También asocia con racionales."],
                "solution": "(½ · 4) · 3 = 6 y ½ · (4 · 3) = 6",
            },
            {
                "eyebrow": "Ejemplo 3 · Irracionales",
                "title": "Y asocia con irracionales",
                "statement": "Fundir tres cargas de √2 kg da el mismo total sin importar cómo se agrupen en el horno.",
                "latex": "(\\sqrt{2}+\\sqrt{2})+\\sqrt{2}=3\\sqrt{2}=\\sqrt{2}+(\\sqrt{2}+\\sqrt{2})",
                "steps": ["(√2 + √2) + √2 = 2√2 + √2 = 3√2.", "√2 + (√2 + √2) = √2 + 2√2 = 3√2.", "La asociatividad vale en todos los conjuntos."],
                "solution": "(√2 + √2) + √2 = 3√2 y √2 + (√2 + √2) = 3√2",
            },
            {
                "eyebrow": "Trampa común",
                "title": "La división tampoco asocia",
                "statement": "En la prensa de corte, el agrupamiento cambia el cociente; no se puede mover el paréntesis a la ligera.",
                "latex": "(16\\div 4)\\div 2=2\\quad\\text{pero}\\quad 16\\div(4\\div 2)=8",
                "trap": True,
                "steps": ["(16 ÷ 4) ÷ 2 = 4 ÷ 2 = 2.", "16 ÷ (4 ÷ 2) = 16 ÷ 2 = 8.", "Resta y división NO son asociativas."],
                "solution": "(16 ÷ 4) ÷ 2 = 2 pero 16 ÷ (4 ÷ 2) = 8",
            },
        ],
        "closure": {
            "eyebrow": "Validez a lo largo de las operaciones",
            "title": "¿En qué operaciones el agrupamiento es libre?",
            "intro": "Recorremos las cuatro operaciones preguntando si reagrupar (sin reordenar) conserva el resultado.",
            "rows": [
                {"symbol": "+", "name": "Suma", "closed": "yes", "latex": "(a+b)+c=a+(b+c)",
                 "note": "El agrupamiento es libre."},
                {"symbol": "\\times", "name": "Multiplicación", "closed": "yes", "latex": "(a\\times b)\\times c=a\\times(b\\times c)",
                 "note": "También libre."},
                {"symbol": "-", "name": "Resta", "closed": "no", "latex": "(10-4)-3\\neq 10-(4-3)",
                 "note": "Reagrupar cambia el resultado."},
                {"symbol": "\\div", "name": "División", "closed": "no", "latex": "(16\\div 4)\\div 2\\neq 16\\div(4\\div 2)",
                 "note": "El cociente depende del agrupamiento."},
            ],
        },
        "instruction": "Escribe el valor correspondiente a las siguientes operaciones matemáticas.",
        "operation_groups": [
            {"id": "G1", "ops": [{"id": "O1", "expr": "(2 + 3) + 4", "answer": "9"},
                                  {"id": "O2", "expr": "2 + (3 + 4)", "answer": "9"}],
             "katia_after": "Ok, con 3 números diferentes vemos que la suma se conserva igual, pero verifiquémoslo con otros valores."},
            {"id": "G2", "ops": [{"id": "O3", "expr": "(12 + 5) + 24", "answer": "41"},
                                  {"id": "O4", "expr": "12 + (5 + 24)", "answer": "41"}],
             "katia_after": "Sin importar cómo agrupemos, la suma da el mismo resultado. Ahora pasemos a la multiplicación."},
            {"id": "G3", "ops": [{"id": "O5", "expr": "(2 × 3) × 4", "answer": "24"},
                                  {"id": "O6", "expr": "2 × (3 × 4)", "answer": "24"}],
             "katia_after": "La multiplicación, al igual que la suma, no cambia su resultado según el agrupamiento. Ahora la resta."},
            {"id": "G4", "ops": [{"id": "O7", "expr": "(8 − 3) − 2", "answer": "3"},
                                  {"id": "O8", "expr": "8 − (3 − 2)", "answer": "7"}],
             "katia_after": "Con la resta, al operar varios números y cambiar el agrupamiento, el resultado se altera. Ahora la división."},
            {"id": "G5", "ops": [{"id": "O9", "expr": "(12 ÷ 4) ÷ 2", "answer": "1,5"},
                                  {"id": "O10", "expr": "12 ÷ (4 ÷ 2)", "answer": "6"}],
             "katia_after": "La resta y la división son rebeldes: cambias el agrupamiento y dan algo distinto."},
            {"id": "G6", "ops": [{"id": "O11", "expr": "(-4 + 6) + 2", "answer": "4"},
                                  {"id": "O12", "expr": "-4 + (6 + 2)", "answer": "4"}],
             "katia_after": "Con un negativo, reagrupar la suma sigue dando lo mismo."},
            {"id": "G7", "ops": [{"id": "O13", "expr": "(1/2 × 4) × 3", "answer": "6"},
                                  {"id": "O14", "expr": "1/2 × (4 × 3)", "answer": "6"}],
             "katia_after": "Y con una fracción, la multiplicación tampoco depende del agrupamiento."},
        ],
        "feedback": {
            "correct": "✓ Correcto. Resolviste primero lo que está dentro del paréntesis.",
            "default": "Aquí no cambiamos el orden de los números, solo el agrupamiento. Primero resuelve los paréntesis.",
        },
        "formalization": [
            "Una operación ⊕ es asociativa si (a ⊕ b) ⊕ c = a ⊕ (b ⊕ c).",
            "Operaciones asociativas: suma (+) y multiplicación (×).",
            "Operaciones NO asociativas: resta (−) y división (÷).",
        ],
        "closing": "Ya tienes dos propiedades: conmutar cambia el orden y asociar cambia el agrupamiento.",
    },
    N3_DISTRIBUTIVE_NODE_ID: {
        "kind": "property_machine",
        "machine_id": "M03",
        "property": "distributive",
        "title": "Máquina Distributiva - La Propiedad del Reparto",
        "intro": (
            "Bienvenido a la máquina distributiva. Aquí aprenderás cómo, al multiplicar "
            "un número por una suma o resta, será igual a multiplicarlo por cada término."
        ),
        "opening_hook": {
            "demo": "3 × (4 + 2) = 18; luego 3 × 4 + 3 × 2 = 18",
            "katia_message": "¡Increíble! La multiplicación se distribuye sobre la suma.",
        },
        "definition": "Distribuir es repartir un factor que multiplica a una suma o resta entre cada uno de sus términos.",
        "formal_expression": "a × (b + c) = a × b + a × c",
        "story_contract": {
            "type": "unified_set_extension",
            "practice_position": "after_definition_plus_examples",
            "is_integrated": True,
        },
        "katia": {
            "eyebrow": "KatIA · La Cinta Repartidora",
            "title": "Repartir el factor",
            "body": (
                "La cinta repartidora envía 3 cajas a cada bahía. Si llegan 6 bahías con piezas pequeñas "
                "y 4 con piezas grandes, puede repartir todo junto, 3 × (6 + 4), o repartir cada tipo por "
                "separado y sumar, 3 × 6 + 3 × 4. Reparte la misma cantidad: el factor se distribuye "
                "entre cada bahía."
            ),
            "question": "¿Multiplicar por una suma es lo mismo que multiplicar término a término?",
        },
        "discovery": {
            "eyebrow": "Descubrimiento guiado",
            "title": "Distribuir es repartir el factor",
            "body": (
                "La propiedad DISTRIBUTIVA reparte un factor que multiplica a una suma (o resta) entre "
                "cada término, en vez de resolver primero lo que está dentro del paréntesis. Funciona "
                "igual si el factor va antes o después del paréntesis. Es la base para factorizar y "
                "resolver ecuaciones más adelante."
            ),
        },
        "definition_title": "Propiedad distributiva",
        "definition_katex": "a\\times(b+c)=a\\times b+a\\times c",
        "worked_examples": [
            {
                "eyebrow": "Ejemplo 1 · Enteros",
                "title": "Distribuye con un factor negativo",
                "statement": "En la cinta repartidora, un factor negativo se reparte a cada bahía conservando los signos.",
                "latex": "-2\\times(3+5)=-16=-2\\times 3+(-2)\\times 5",
                "image_slot": True,
                "steps": ["−2 × (3 + 5) = −2 × 8 = −16.", "−2 × 3 + (−2) × 5 = −6 + (−10) = −16.", "Igual con enteros negativos."],
                "solution": "−2 × (3 + 5) = −16 y −2 × 3 + (−2) × 5 = −16",
            },
            {
                "eyebrow": "Ejemplo 2 · Racionales",
                "title": "Distribuye una fracción sobre la suma",
                "statement": "Una fracción de carga como factor se reparte igual entre las bahías de la cinta.",
                "latex": "\\dfrac{1}{2}\\times(4+6)=5=\\dfrac{1}{2}\\times 4+\\dfrac{1}{2}\\times 6",
                "steps": ["½ × (4 + 6) = ½ × 10 = 5.", "½ × 4 + ½ × 6 = 2 + 3 = 5.", "El reparto funciona con racionales."],
                "solution": "½ × (4 + 6) = 5 y ½ × 4 + ½ × 6 = 5",
            },
            {
                "eyebrow": "Ejemplo 3 · Irracionales",
                "title": "Distribuye con un factor irracional",
                "statement": "Al repartir una carga de √2 kg entre las bahías, aparece √2·√2 = 2: la distributiva vale también con medidas irracionales.",
                "latex": "\\sqrt{2}\\times(\\sqrt{2}+3)=2+3\\sqrt{2}=\\sqrt{2}\\cdot\\sqrt{2}+\\sqrt{2}\\cdot 3",
                "steps": ["√2 × (√2 + 3) se reparte término a término.", "√2 · √2 = 2 y √2 · 3 = 3√2.", "Total: 2 + 3√2."],
                "solution": "√2 × (√2 + 3) = 2 + 3√2",
            },
            {
                "eyebrow": "Trampa común",
                "title": "La potencia NO se distribuye sobre la suma",
                "statement": "En la prensa de compactado, elevar una suma de cargas al cuadrado NO es elevar cada carga por separado — es el error más frecuente en la cinta.",
                "latex": "(3+4)^2=49\\quad\\text{pero}\\quad 3^2+4^2=25",
                "trap": True,
                "steps": ["(3 + 4)² = 7² = 49.", "3² + 4² = 9 + 16 = 25.", "49 ≠ 25: la potenciación NO distribuye sobre la suma."],
                "solution": "(3 + 4)² = 49 pero 3² + 4² = 25",
            },
        ],
        "closure": {
            "eyebrow": "Validez del reparto",
            "title": "¿Qué se reparte sobre una suma y qué no?",
            "intro": "Revisamos sobre cuáles operaciones la multiplicación (y la división) se reparte y dónde está la trampa.",
            "rows": [
                {"symbol": "\\times", "name": "Por la suma", "closed": "yes", "latex": "a(b+c)=ab+ac",
                 "note": "La multiplicación se reparte sobre la suma."},
                {"symbol": "\\times", "name": "Por la resta", "closed": "yes", "latex": "a(b-c)=ab-ac",
                 "note": "También sobre la resta."},
                {"symbol": "\\div", "name": "División (derecha)", "closed": "partial", "latex": "(a+b)\\div c=a\\div c+b\\div c",
                 "note": "Solo cuando la suma está a la izquierda del divisor."},
                {"symbol": "x^2", "name": "Potenciación", "closed": "no", "latex": "(a+b)^2\\neq a^2+b^2",
                 "note": "La potencia NO se distribuye sobre la suma (trampa clásica)."},
            ],
        },
        "instruction": "Escribe el valor correspondiente a las siguientes operaciones matemáticas.",
        "operation_groups": [
            {"id": "G1", "ops": [{"id": "O1", "expr": "3 × (4 + 2)", "answer": "18"},
                                  {"id": "O2", "expr": "(3 × 4) + (3 × 2)", "answer": "18"}],
             "katia_after": "Ya veo por qué le dicen distributiva: el 3 se repartió entre 4 y 2 y dio el mismo resultado."},
            {"id": "G2", "ops": [{"id": "O3", "expr": "5 × (8 − 3)", "answer": "25"},
                                  {"id": "O4", "expr": "5 × 8 − 5 × 3", "answer": "25"}],
             "katia_after": "Para la resta también funciona; esto será muy importante más adelante para factorizar."},
            {"id": "G3", "ops": [{"id": "O5", "expr": "-3 × (2 + 4)", "answer": "-18"},
                                  {"id": "O6", "expr": "(-3 × 2) + (-3 × 4)", "answer": "-18"}],
             "katia_after": "Con un factor negativo, el reparto conserva los signos y el total."},
            {"id": "G4", "ops": [{"id": "O7", "expr": "1/2 × (6 + 8)", "answer": "7"},
                                  {"id": "O8", "expr": "(1/2 × 6) + (1/2 × 8)", "answer": "7"}],
             "katia_after": "Y una fracción también se reparte por igual entre los términos."},
        ],
        "feedback": {
            "correct": "✓ Correcto. El factor se reparte entre cada término del paréntesis.",
            "default": "El factor multiplica a todos los términos del paréntesis; si hay resta, el segundo producto se resta.",
        },
        "formalization": [
            "a × (b + c) = a × b + a × c",
            "a × (b − c) = a × b − a × c",
            "(b + c) × a = b × a + c × a",
            "(b − c) × a = b × a − c × a",
        ],
        "closing": "La multiplicación se reparte sobre la suma y la resta. Esta propiedad será clave para factorizar.",
    },
    N3_IDENTITY_NODE_ID: {
        "kind": "property_machine",
        "machine_id": "M04",
        "property": "identity_element",
        "title": "Máquina del Elemento Neutro - La Propiedad del Que No Cambia",
        "intro": (
            "Bienvenido a la máquina del elemento neutro. Aquí aprenderás cómo, en ciertas "
            "operaciones, existe un valor que no altera el número original por ningún lado."
        ),
        "opening_hook": {
            "demo": "5 + 0 = 5; luego 5 × 1 = 5",
            "katia_message": "Hay números que no cambian el resultado.",
        },
        "definition": "Un elemento neutro no cambia el número sin importar de qué lado se ponga: debe funcionar a la izquierda y a la derecha.",
        "formal_expression": "a ⊕ e = e ⊕ a = a",
        "story_contract": {
            "type": "unified_set_extension",
            "practice_position": "after_definition_plus_examples",
            "is_integrated": True,
        },
        "katia": {
            "eyebrow": "KatIA · El Calibre Cero",
            "title": "El número que deja todo igual",
            "body": (
                "En el calibre de la fábrica, sumar 0 gramos de ajuste no cambia el peso de la pieza, y "
                "multiplicar por 1 vuelta no altera cuántas unidades produce la máquina. El 0 es el "
                "neutro de la suma y el 1 el de la multiplicación. Pero restar o dividir por partes no "
                "tienen un ajuste neutro que sirva en ambos sentidos."
            ),
            "question": "¿Toda operación tiene un número que, puesto a cualquier lado, deja al otro intacto?",
        },
        "discovery": {
            "eyebrow": "Descubrimiento guiado",
            "title": "Un neutro debe servir por los dos lados",
            "body": (
                "El ELEMENTO NEUTRO no cambia el número sin importar de qué lado se ponga: debe funcionar "
                "a la izquierda y a la derecha. Si solo sirve por un lado, no es neutro de verdad."
            ),
        },
        "definition_title": "Elemento neutro",
        "definition_katex": "a+0=0+a=a\\qquad a\\times 1=1\\times a=a",
        "worked_examples": [
            {
                "eyebrow": "Ejemplo 1 · Enteros",
                "title": "El 0 deja igual a un negativo",
                "statement": "En el calibre, sumar 0 gramos de ajuste a una pieza con peso negativo no la cambia, por ningún lado.",
                "latex": "-7+0=-7=0+(-7)",
                "image_slot": True,
                "steps": ["−7 + 0 = −7.", "0 + (−7) = −7.", "El 0 es neutro de la suma también con enteros."],
                "solution": "−7 + 0 = −7 y 0 + (−7) = −7",
            },
            {
                "eyebrow": "Ejemplo 2 · Racionales",
                "title": "El 1 deja igual a una fracción",
                "statement": "Multiplicar una fracción de producción por 1 vuelta de la máquina no la cambia, en cualquier orden.",
                "latex": "\\dfrac{3}{5}\\times 1=\\dfrac{3}{5}=1\\times\\dfrac{3}{5}",
                "steps": ["(3/5) × 1 = 3/5.", "1 × (3/5) = 3/5.", "El 1 es neutro del producto también con racionales."],
                "solution": "(3/5) × 1 = 3/5 y 1 × (3/5) = 3/5",
            },
            {
                "eyebrow": "Ejemplo 3 · Irracionales",
                "title": "Los neutros sirven con irracionales",
                "statement": "El ajuste 0 y la vuelta 1 dejan igual incluso a una medida irracional como √2.",
                "latex": "\\sqrt{2}+0=\\sqrt{2}\\qquad\\sqrt{2}\\times 1=\\sqrt{2}",
                "steps": ["√2 + 0 = √2 (neutro de la suma).", "√2 × 1 = √2 (neutro del producto).", "Los neutros son los mismos en todos los conjuntos."],
                "solution": "√2 + 0 = √2 y √2 × 1 = √2",
            },
            {
                "eyebrow": "Trampa común",
                "title": "La división tampoco tiene neutro",
                "statement": "En el calibre de división, el 1 deja igual solo por la derecha; por la izquierda da el recíproco — no es un ajuste neutro verdadero.",
                "latex": "5\\div 1=5\\quad\\text{pero}\\quad 1\\div 5=0{,}2",
                "trap": True,
                "steps": ["5 ÷ 1 = 5 (sirve por la derecha).", "1 ÷ 5 = 0,2 (falla por la izquierda).", "Resta y división NO tienen elemento neutro."],
                "solution": "5 ÷ 1 = 5 pero 1 ÷ 5 = 0,2",
            },
        ],
        "closure": {
            "eyebrow": "Validez a lo largo de las operaciones",
            "title": "¿Qué operaciones tienen un neutro de verdad?",
            "intro": "Recorremos las operaciones preguntando si existe un número que deje al otro intacto por ambos lados.",
            "rows": [
                {"symbol": "+", "name": "Suma", "closed": "yes", "latex": "a+0=0+a=a",
                 "note": "Neutro 0, sirve por ambos lados."},
                {"symbol": "\\times", "name": "Multiplicación", "closed": "yes", "latex": "a\\times 1=1\\times a=a",
                 "note": "Neutro 1, sirve por ambos lados."},
                {"symbol": "-", "name": "Resta", "closed": "no", "latex": "a-0=a\\ \\text{pero}\\ 0-a=-a",
                 "note": "El 0 solo sirve por la derecha: no hay neutro."},
                {"symbol": "\\div", "name": "División", "closed": "no", "latex": "a\\div 1=a\\ \\text{pero}\\ 1\\div a\\neq a",
                 "note": "El 1 solo sirve por la derecha: no hay neutro."},
            ],
        },
        "instruction": "Escribe el valor correspondiente a las siguientes operaciones matemáticas.",
        "operation_groups": [
            {"id": "G1", "ops": [{"id": "O1", "expr": "5 + 0", "answer": "5"},
                                  {"id": "O2", "expr": "0 + 5", "answer": "5"},
                                  {"id": "O3", "expr": "100 + 0", "answer": "100"},
                                  {"id": "O4", "expr": "0 + 100", "answer": "100"}],
             "katia_after": "Ya pescamos nuestro primer elemento neutro: en la suma, el elemento neutro es el 0."},
            {"id": "G2", "ops": [{"id": "O5", "expr": "8 × 1", "answer": "8"},
                                  {"id": "O6", "expr": "1 × 8", "answer": "8"},
                                  {"id": "O7", "expr": "150 × 1", "answer": "150"},
                                  {"id": "O8", "expr": "1 × 150", "answer": "150"}],
             "katia_after": "Para la multiplicación el elemento neutro es el 1, que no altera el resultado en cualquier orden."},
            {"id": "G3", "ops": [{"id": "O9", "expr": "6 − 0", "answer": "6"},
                                  {"id": "O10", "expr": "0 − 6", "answer": "-6"},
                                  {"id": "O11", "expr": "17 − 0", "answer": "17"},
                                  {"id": "O12", "expr": "0 − 17", "answer": "-17"}],
             "katia_after": "El 0 funciona solo a la derecha en la resta. Como un neutro debe funcionar por los dos lados, la resta NO tiene elemento neutro."},
            {"id": "G4", "ops": [{"id": "O13", "expr": "4 ÷ 1", "answer": "4"},
                                  {"id": "O14", "expr": "1 ÷ 4", "answer": "0,25"},
                                  {"id": "O15", "expr": "8 ÷ 1", "answer": "8"},
                                  {"id": "O16", "expr": "1 ÷ 8", "answer": "0,125"}],
             "katia_after": "Con la división pasa lo mismo: el 1 funciona solo cuando está a la derecha. La división TAMPOCO tiene elemento neutro."},
            {"id": "G5", "ops": [{"id": "O17", "expr": "-9 + 0", "answer": "-9"},
                                  {"id": "O18", "expr": "0 + (-9)", "answer": "-9"}],
             "katia_after": "El 0 deja igual a un negativo por ambos lados: sigue siendo el neutro de la suma."},
            {"id": "G6", "ops": [{"id": "O19", "expr": "1{,}5 × 1", "answer": "1,5"},
                                  {"id": "O20", "expr": "1 × 1{,}5", "answer": "1,5"}],
             "katia_after": "Y el 1 deja igual a un decimal: el neutro del producto es el mismo en todo conjunto."},
        ],
        "feedback": {
            "correct": "✓ Correcto. Un elemento neutro de verdad no cambia el número por ningún lado.",
            "default": "Recuerda la clave: el neutro debe funcionar por los dos lados. Resta y división no tienen neutro verdadero.",
        },
        "formalization": [
            "Elemento neutro de la suma: a + 0 = 0 + a = a.",
            "Elemento neutro de la multiplicación: a × 1 = 1 × a = a.",
            "Resta: no tiene elemento neutro; 0 funciona solo a la derecha.",
            "División: no tiene elemento neutro; 1 funciona solo a la derecha.",
        ],
        "closing": "Ahora conoces a los neutros. En la última máquina veremos números que se cancelan para llegar a ellos.",
    },
    N3_INVERSES_NODE_ID: {
        "kind": "property_machine",
        "machine_id": "M05",
        "property": "inverses",
        "title": "Máquina de Inversos - La Propiedad de la Cancelación",
        "intro": (
            "Bienvenido a la máquina de inversos aditivo y multiplicativo, donde aprenderás "
            "a encontrar números que anulan o cancelan a otros para llegar a un neutro."
        ),
        "story_contract": {
            "type": "unified_set_extension",
            "practice_position": "after_definition_plus_examples",
            "is_integrated": True,
        },
        "katia": {
            "eyebrow": "KatIA · La Prensa de Contrapesos",
            "title": "La máquina de deshacer",
            "body": (
                "En la fábrica, cada ajuste tiene su contrapeso. Si la prensa añade 8 kg de presión, la "
                "báscula vuelve a cero cuando retiras exactamente esos 8 kg: 8 + (−8) = 0. Y si divides "
                "una plancha en 3 raciones iguales, volver a juntarlas reconstruye la plancha entera: "
                "3 · ⅓ = 1. Cada ajuste guarda la pieza que lo deshace."
            ),
            "question": "¿Todo número guarda, dentro de su propio conjunto, la pieza que lo devuelve al neutro?",
        },
        "discovery": {
            "eyebrow": "Descubrimiento guiado",
            "title": "Dos formas de volver al neutro",
            "body": (
                "Hay dos neutros: el 0 para la suma y el 1 para la multiplicación. El OPUESTO de a "
                "es −a y lo lleva al 0 (inverso aditivo). El RECÍPROCO de a es 1/a y lo lleva al 1 "
                "(inverso multiplicativo, con a ≠ 0). Opuesto y recíproco son piezas distintas."
            ),
        },
        "definition_title": "Inverso aditivo e inverso multiplicativo",
        "definition_katex": "a+(-a)=0 \\qquad a\\cdot\\dfrac{1}{a}=1\\ (a\\neq 0)",
        "definition": "Un inverso es el número que cancela a otro llevándolo al elemento neutro: 0 para la suma y 1 para la multiplicación.",
        "formal_expression": "a + (−a) = 0; a × (1/a) = 1",
        "worked_examples": [
            {
                "eyebrow": "Ejemplo 1 · Enteros",
                "title": "Opuesto: descargar la prensa",
                "statement": "En la prensa, el opuesto de 6 kg de presión es −6 kg porque juntos devuelven la báscula al neutro 0.",
                "latex": "6+(-6)=0",
                "image_slot": True,
                "steps": [
                    "Neutro de la suma: 0.",
                    "Busco el número que sumado a 6 da 0.",
                    "Es su opuesto, −6: 6 + (−6) = 0.",
                ],
                "solution": "6 + (−6) = 0",
            },
            {
                "eyebrow": "Ejemplo 2 · Racionales",
                "title": "Recíproco: recomponer la plancha",
                "statement": "El recíproco de 4 vueltas de la máquina es 1/4 porque su producto es el neutro 1.",
                "latex": "4\\cdot\\dfrac{1}{4}=1",
                "image_slot": True,
                "steps": [
                    "Neutro de la multiplicación: 1.",
                    "Busco el número que multiplicado por 4 da 1.",
                    "Es su recíproco, 1/4: 4 · (1/4) = 4/4 = 1.",
                ],
                "solution": "4 × (1/4) = 1",
            },
            {
                "eyebrow": "Ejemplo 3 · Racionales",
                "title": "Una fracción guarda sus dos inversos",
                "statement": "Para una carga de 3/5 de plancha: su opuesto es −3/5 y su recíproco se obtiene invirtiendo la fracción, 5/3.",
                "latex": "\\dfrac{3}{5}+\\left(-\\dfrac{3}{5}\\right)=0\\quad\\dfrac{3}{5}\\cdot\\dfrac{5}{3}=1",
                "steps": [
                    "Opuesto: cambio el signo → −3/5, y 3/5 + (−3/5) = 0.",
                    "Recíproco: invierto numerador y denominador → 5/3.",
                    "Compruebo: (3/5) · (5/3) = 15/15 = 1.",
                ],
                "solution": "3/5 + (−3/5) = 0 y (3/5) × (5/3) = 1",
            },
            {
                "eyebrow": "Ejemplo 4 · Irracionales",
                "title": "El recíproco de √2 (esto es racionalizar)",
                "statement": "√2 también tiene recíproco: 1/√2. Reescribirlo sin raíz en el denominador es racionalizar, y da √2/2 (también irracional).",
                "latex": "\\sqrt{2}\\cdot\\dfrac{1}{\\sqrt{2}}=1\\quad\\dfrac{1}{\\sqrt{2}}=\\dfrac{\\sqrt{2}}{2}",
                "steps": [
                    "El recíproco de √2 es 1/√2, y √2 · (1/√2) = 1.",
                    "Multiplico arriba y abajo por √2: (1·√2)/(√2·√2) = √2/2.",
                    "Esto es RACIONALIZAR; el recíproco existe y sigue siendo irracional.",
                ],
                "solution": "√2 × (1/√2) = 1 y 1/√2 = √2/2",
            },
            {
                "eyebrow": "Trampa común",
                "title": "Opuesto ≠ recíproco, y el 0 es la excepción",
                "statement": (
                    "El opuesto y el recíproco son piezas distintas: para 2 el opuesto es −2 y el "
                    "recíproco es 1/2, no son iguales. Y el 0 tiene opuesto (−0 = 0) pero NO tiene "
                    "recíproco, porque 1/0 no está definido."
                ),
                "latex": "-2\\neq\\dfrac{1}{2}\\qquad\\dfrac{1}{0}\\ \\text{no existe}",
                "trap": True,
                "steps": [
                    "Opuesto de 2 → −2 (lleva al 0). Recíproco de 2 → 1/2 (lleva al 1). Distintos.",
                    "El 0 no tiene recíproco: ningún número multiplicado por 0 da 1.",
                ],
                "solution": "Opuesto de 2 = −2; recíproco de 2 = 1/2; el 0 no tiene recíproco.",
            },
        ],
        "closure": {
            "eyebrow": "Inversos a lo largo de los conjuntos numéricos",
            "title": "¿Cada conjunto guarda los inversos de sus números?",
            "intro": (
                "Recorremos los conjuntos preguntando si el opuesto y el recíproco de cada número "
                "viven dentro del mismo conjunto."
            ),
            "rows": [
                {"symbol": "\\mathbb{N}", "name": "Naturales", "closed": "no",
                 "latex": "3\\to -3\\notin\\mathbb{N}",
                 "note": "Sin opuestos (−3 no es natural) ni recíprocos (1/3 no es natural). Solo viven los neutros 0 y 1."},
                {"symbol": "\\mathbb{Z}", "name": "Enteros", "closed": "partial",
                 "latex": "5+(-5)=0",
                 "note": "Aparece el OPUESTO: todo entero tiene su −a. Pero el recíproco aún se escapa (1/5 ∉ ℤ) → motiva los racionales."},
                {"symbol": "\\mathbb{Q}", "name": "Racionales", "closed": "yes",
                 "latex": "\\dfrac{2}{3}\\cdot\\dfrac{3}{2}=1",
                 "note": "Aparece el RECÍPROCO: todo racional ≠ 0 tiene su 1/a (basta invertir la fracción). Opuesto y recíproco viven aquí."},
                {"symbol": "\\mathbb{I}", "name": "Irracionales", "closed": "partial",
                 "latex": "\\dfrac{1}{\\sqrt{2}}=\\dfrac{\\sqrt{2}}{2}",
                 "note": "Cada irracional tiene opuesto y recíproco, y son irracionales: el recíproco de √2 es 1/√2 = √2/2 (esto es racionalizar). Pero el neutro 1 ∉ 𝕀, así que su hogar completo son los reales."},
                {"symbol": "\\mathbb{R}", "name": "Reales", "closed": "yes",
                 "latex": "a+(-a)=0\\quad a\\cdot\\tfrac{1}{a}=1",
                 "note": "Todo real ≠ 0 tiene opuesto y recíproco aquí mismo. Es el hogar completo de los inversos."},
                {"symbol": "\\mathbb{C}", "name": "Complejos", "closed": "yes",
                 "latex": "i\\cdot(-i)=1",
                 "note": "También: cada complejo ≠ 0 tiene su inverso. Desvío opcional avanzado."},
            ],
        },
        "instruction": "Escribe el número que cancela al primero para llegar al resultado neutro.",
        "operation_groups": [
            {"id": "G1", "ops": [{"id": "O1", "expr": "5 + (___) = 0", "answer": "-5"},
                                  {"id": "O2", "expr": "7 + (___) = 0", "answer": "-7"}],
             "katia_after": "Para llegar al neutro de la suma, sumamos al número su contraparte negativa."},
            {"id": "G2", "ops": [{"id": "O3", "expr": "−15 + (___) = 0", "answer": "15"},
                                  {"id": "O4", "expr": "−9 + (___) = 0", "answer": "9"}],
             "katia_after": "Si el número original es negativo, le sumamos su contraparte positiva."},
            {"id": "G3", "ops": [{"id": "O5", "expr": "5 × (___) = 1", "answer": "1/5"},
                                  {"id": "O6", "expr": "10 × (___) = 1", "answer": "1/10"}],
             "katia_after": "Para el inverso multiplicativo, multiplicamos por el recíproco: 1 dividido por el número."},
            {"id": "G4", "ops": [{"id": "O7", "expr": "3/4 × (___) = 1", "answer": "4/3"},
                                  {"id": "O8", "expr": "√5 + (___) = 0", "answer": "-sqrt5",
                                   "accepted_answers": ["-√5", "-\\sqrt{5}"]}],
             "katia_after": (
                 "Los inversos también funcionan fuera de los enteros: una fracción no entera "
                 "tiene recíproco y un irracional tiene opuesto."
             )},
        ],
        "feedback": {
            "correct": "✓ Correcto. El inverso cancela al número y lo lleva al neutro.",
            "default": "Para llegar a 0 usa el opuesto; para llegar a 1 usa el recíproco.",
        },
        "formalization": [
            "Inverso aditivo u opuesto: para todo número a existe −a tal que a + (−a) = 0.",
            "Inverso multiplicativo o recíproco: para todo número a ≠ 0 existe 1/a tal que a × (1/a) = 1.",
            "El 0 no tiene inverso multiplicativo porque 1/0 no está definido.",
        ],
        "closing": "¡Felicidades! Completaste el laboratorio de las propiedades. Estos inversos serán la llave para despejar incógnitas más adelante.",
    },
}

_N3_SEQUENCE = [
    (N3_HUB_NODE_ID, "level_hub_laboratory", "laboratorio_propiedades", "prealgebra.n3.m00", N2_RADICATION_NODE_ID),
    (N3_COMMUTATIVE_NODE_ID, "property_machine_guided_discovery", "conmutativa", "prealgebra.n3.m01", N3_HUB_NODE_ID),
    (N3_ASSOCIATIVE_NODE_ID, "property_machine_guided_discovery", "asociativa", "prealgebra.n3.m02", N3_COMMUTATIVE_NODE_ID),
    (N3_DISTRIBUTIVE_NODE_ID, "property_machine_guided_discovery", "distributiva", "prealgebra.n3.m03", N3_ASSOCIATIVE_NODE_ID),
    (N3_IDENTITY_NODE_ID, "property_machine_guided_discovery", "elemento_neutro", "prealgebra.n3.m04", N3_DISTRIBUTIVE_NODE_ID),
    (N3_INVERSES_NODE_ID, "property_machine_cancellation_last", "inversos", "prealgebra.n3.m05", N3_IDENTITY_NODE_ID),
]

for _index, (_node_id, _node_type, _topic, _prefix, _unlock_after) in enumerate(_N3_SEQUENCE):
    _content = _N3_HUB_CONTENT if _node_id == N3_HUB_NODE_ID else _N3_MACHINE_CONTENT[_node_id]
    _next = _N3_SEQUENCE[_index + 1][0] if _index + 1 < len(_N3_SEQUENCE) else None
    _LESSONS[_node_id] = {
        "node_id": _node_id,
        "node_type": _node_type,
        "topic": _topic,
        "i18n_prefix": _prefix,
        "next_node_id": _next,
        "unlock_after": _unlock_after,
        "affects_elo": False,
        "is_safe_zone": True,
        "optional_branch": False,
        "skip_penalty": False,
        "objectives": ["recognize_operation_properties", "compare_property_examples"],
        "optional_objectives": ["connect_properties_to_equations"],
        "content": _content,
        "interactions": [],
    }

for _machine in _N3_MACHINES:
    _interaction_id = f"{N3_HUB_NODE_ID}-MACHINE-{_machine['id']}"
    _LESSONS[N3_HUB_NODE_ID]["interactions"].append({
        "interaction_id": _interaction_id,
        "type": "single_select",
        "prompt_key": _machine["property"],
        "option_keys": ["introduced"],
        "can_retry": False,
    })
    _INTERACTION_RULES[_interaction_id] = {
        "node_id": N3_HUB_NODE_ID,
        "valid_options": {"introduced"},
        "expected": "introduced",
        "misconception_by_option": {},
        "feedback_by_option": {"introduced": "machine_introduced"},
    }

for _node_id in N3_MACHINE_NODE_IDS:
    _input_kind = "text_exact" if _node_id == N3_INVERSES_NODE_ID else "numeric"
    for _group in _N3_MACHINE_CONTENT[_node_id]["operation_groups"]:
        for _operation in _group["ops"]:
            _interaction_id = f"{_node_id}-{_operation['id']}"
            _LESSONS[_node_id]["interactions"].append({
                "interaction_id": _interaction_id,
                "type": "numeric_input",
                "prompt_key": _operation["id"],
                "option_keys": [],
                "can_retry": True,
            })
            _INTERACTION_RULES[_interaction_id] = {
                "node_id": _node_id,
                "input_kind": _input_kind,
                "expected": _operation["answer"],
                "accepted": set(_operation.get("accepted_answers", [])),
                "misconception_by_option": {},
                "feedback_by_result": {True: "correct", False: "default"},
                "default_misconception": f"error_{_N3_MACHINE_CONTENT[_node_id]['property']}",
            }


def _register_mixed_interactions(
    node_id: str, concept_slug: str, items: list[dict], required: bool = True,
) -> None:
    """Registra interacciones de tipo mixto (numeric/single_select/multi_select).

    Nivel 4 mezcla los tres tipos dentro de un mismo nodo (a diferencia de N2/N3,
    que solo generaban `numeric`/`text_exact`), así que un único registrador
    data-driven reemplaza los tres bucles distintos que tendría cada tipo.

    `required=False` (rompe-hielo de un hub): la interacción es evaluable vía
    `/interactions` pero NO se agrega a `_LESSONS[node_id]["interactions"]`, así
    que no cuenta para el gating de `node_completed` — es calentamiento opcional,
    no bloquea "Completar ciudad/Activar laboratorio/Entrar al puerto".
    """
    for item in items:
        interaction_id = f"{node_id}-{item['id']}"
        kind = item["kind"]
        if kind == "numeric":
            if required:
                _LESSONS[node_id]["interactions"].append({
                    "interaction_id": interaction_id,
                    "type": "numeric_input",
                    "prompt_key": item["id"],
                    "option_keys": [],
                    "can_retry": True,
                })
            _INTERACTION_RULES[interaction_id] = {
                "node_id": node_id,
                "input_kind": "numeric",
                "expected": item["answer"],
                "misconception_by_option": {},
                "feedback_by_result": {True: "correct", False: "default"},
                "default_misconception": f"error_{concept_slug}",
            }
        elif kind == "single_select":
            option_ids = {opt["id"] for opt in item["options"]}
            if required:
                _LESSONS[node_id]["interactions"].append({
                    "interaction_id": interaction_id,
                    "type": "single_select",
                    "prompt_key": item["id"],
                    "option_keys": [opt["id"] for opt in item["options"]],
                    "can_retry": True,
                })
            _INTERACTION_RULES[interaction_id] = {
                "node_id": node_id,
                "valid_options": option_ids,
                "expected": item["expected"],
                "misconception_by_option": item.get("misconception_by_option", {}),
                "feedback_by_option": item.get("feedback_by_option", {}),
                "default_feedback": item.get("default_feedback", "default"),
            }
        elif kind == "multi_select":
            if required:
                _LESSONS[node_id]["interactions"].append({
                    "interaction_id": interaction_id,
                    "type": "multi_select",
                    "prompt_key": item["id"],
                    "option_keys": sorted(item["valid_options"]),
                    "can_retry": True,
                })
            _INTERACTION_RULES[interaction_id] = {
                "node_id": node_id,
                "input_kind": "multi_select",
                "valid_options": set(item["valid_options"]),
                "expected": set(item["expected"]),
                "trap_options": set(item.get("trap_options", set())),
                "feedback_correct": item.get("feedback_correct", "correct"),
                "feedback_trap": item.get("feedback_trap", "default"),
                "misconception_trap": item.get("misconception_trap"),
                "feedback_missing": item.get("feedback_missing", "default"),
                "misconception_missing": item.get("misconception_missing"),
                "feedback_incorrect": item.get("feedback_incorrect", "default"),
                "misconception_incorrect": item.get("misconception_incorrect"),
            }
        else:
            raise ValueError(f"unsupported N4 interaction kind: {kind}")


_N4_CARDS = [
    {"id": "C01", "concept": "divisibilidad", "symbol": "b \\mid a", "node_id": N4_DIVISIBILITY_NODE_ID,
     "destination": "Corinto · el reparto exacto", "teaser": "Reparte la carga de un barco sin que sobre nada."},
    {"id": "C02", "concept": "multiplos", "symbol": "M(b)", "node_id": N4_MULTIPLES_NODE_ID,
     "destination": "Rodas · lo que se repite", "teaser": "Descubre los barcos que zarpan cada cierto número de días."},
    {"id": "C03", "concept": "primos", "symbol": "p", "node_id": N4_PRIMES_NODE_ID,
     "destination": "Delos · la isla indivisible", "teaser": "Encuentra las polis con una sola ruta directa al puerto."},
    {"id": "C04", "concept": "factorizacion_prima", "symbol": "2\\times3\\times5", "node_id": N4_FACTORIZATION_NODE_ID,
     "destination": "Mileto · piezas fundamentales", "teaser": "Desmonta la carga de un barco en sus piezas más pequeñas."},
    {"id": "C05", "concept": "mcd", "symbol": "\\text{MCD}", "node_id": N4_GCD_NODE_ID,
     "destination": "Atenas · lo más grande en común", "teaser": "Halla el contenedor más grande que reparte exacto dos cargamentos."},
    {"id": "C06", "concept": "mcm", "symbol": "\\text{MCM}", "node_id": N4_LCM_NODE_ID,
     "destination": "Esparta · donde coinciden las rutas", "teaser": "Calcula cada cuánto coinciden dos barcos en el mismo muelle."},
]

_N4_HUB_CONTENT = {
    "kind": "level_hub_port",
    "level": "Nivel 4 - Divisibilidad",
    "title": "El Puerto de la Polis",
    "welcome_text": (
        "Bienvenido al Puerto de la Polis. Aquí llegan y zarpan los barcos que cargan "
        "ánforas de aceite, sacos de trigo, rollos de tela y cerámica hacia Atenas, Corinto, "
        "Delos, Mileto, Rodas y Esparta. El escriba portuario necesita entender cómo se "
        "reparte, se repite y se combina la carga antes de que cada barco zarpe."
    ),
    "scene_text": (
        "El puerto tiene seis muelles. En cada uno descubrirás una idea distinta sobre cómo "
        "se comportan los números al repartirse, repetirse y combinarse."
    ),
    "icebreaker": {
        "title": "Antes de zarpar: rompiendo el hielo",
        "intro": "Tres escenas del puerto para entrar en calor antes de visitar los muelles.",
        "items": [
            {
                "id": "ICE1",
                "kind": "multi_select",
                "prompt": (
                    "Un mercader tiene 12 naranjas y quiere repartirlas en partes iguales. "
                    "Selecciona con cuántas personas puede repartirlas sin que sobre ninguna: "
                    "1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12."
                ),
                "image_slot": True,
                "valid_options": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
                "expected": ["1", "2", "3", "4", "6", "12"],
                "trap_options": [],
                "feedback_correct": "correct",
                "feedback_trap": "default",
                "feedback_missing": "fb_hub_ice1_missing",
                "misconception_missing": "olvida_verificar_residuo_cero",
                "feedback_incorrect": "default",
                "misconception_incorrect": "error_puerto",
            },
            {
                "id": "ICE2",
                "kind": "single_select",
                "story": (
                    "En el muelle hay cinco postes clavados con tablillas de ruta: 2, 3, 5, 7 y 11 "
                    "escalas. El escriba intenta repartir cada poste en tramos iguales con una cuerda "
                    "y, salvo cortar en 1 tramo o en tantos tramos como escalas tiene, ninguno se deja "
                    "partir parejo."
                ),
                "image_slot": True,
                "support_objects": [
                    "5 postes de madera con tablillas numeradas 2, 3, 5, 7, 11",
                    "una cuerda de medir intentando marcar tramos iguales en cada poste",
                ],
                "prompt": "¿Qué tienen en común los números 2, 3, 5, 7 y 11?",
                "options": [
                    {"id": "a", "text": "Solo tienen dos divisores: 1 y ellos mismos."},
                    {"id": "b", "text": "Son todos impares."},
                    {"id": "c", "text": "La suma de todos es múltiplo de 5."},
                ],
                "expected": "a",
                "feedback_by_option": {
                    "a": "correct",
                    "b": "fb_hub_ice2_b",
                    "c": "fb_hub_ice2_c",
                },
                "misconception_by_option": {
                    "b": "confunde_paridad_con_ser_primo",
                    "c": "inventa_criterio_por_suma_total",
                },
            },
            {
                "id": "ICE3",
                "kind": "numeric",
                "prompt": (
                    "Cada carreta nueva que llega al puerto trae 4 rollos de tela más que la anterior: "
                    "4, 8, 12, 16, 20... Siguiendo el patrón, ¿cuántos rollos de tela trae la 6ª carreta?"
                ),
                "image_slot": True,
                "expr": "4\\times 6",
                "answer": "24",
            },
        ],
    },
    "advance_text": (
        "Ya viste que reparto exacto, repetición y coincidencia están en todas partes del "
        "puerto. Ahora visita los seis muelles para dominarlas una por una."
    ),
    "gating": {"rule": "all_cards_opened", "cards_required": 6},
    "cards": _N4_CARDS,
    "feedback": {
        "correct": "¡Correcto!",
        "default": "Revisa la respuesta con calma antes de continuar.",
        "fb_hub_ice1_missing": "Te falta al menos una cantidad: verifica que 12 se reparta exacto entre ese número de personas.",
        "fb_hub_ice2_b": "2 es primo y es par; 'impar' no es el criterio correcto — cuenta los divisores.",
        "fb_hub_ice2_c": "La suma total no tiene relación; cuenta los divisores de cada número por separado.",
    },
    "validation_status": "F4_C01_pilot",
}

_N4_CONCEPT_CONTENT = {
    N4_DIVISIBILITY_NODE_ID: {
        "kind": "divisibility_concept",
        "concept_id": "C01",
        "concept_slug": "divisibilidad",
        "title": "Divisibilidad: la regla del reparto exacto",
        "story_contract": {
            "type": "guided_discovery_formalization",
            "practice_position": "after_definition_plus_examples",
            "is_integrated": True,
        },
        "katia": {
            "eyebrow": "KatIA abre el muelle de la divisibilidad",
            "title": "Repartir la carga sin que sobre nada",
            "body": (
                "En el puerto, un escriba portuario reparte la carga de un barco recién "
                "atracado entre las carretas que esperan en el muelle. Si el reparto no cae "
                "exacto, alguna carreta se queda esperando o algo sobra sobre las piedras del "
                "muelle. KatIA quiere saber cuándo un número puede repartirse sin que sobre nada."
            ),
            "question": "¿Todo número puede repartirse en partes iguales entre cualquier cantidad de carretas, sin que sobre nada?",
        },
        "discovery": {
            "eyebrow": "Descubrimiento guiado",
            "title": "Reparto exacto vs. reparto con residuo",
            "body": (
                "En el rompe-hielo repartiste 12 naranjas entre distintas cantidades de "
                "personas: con 1, 2, 3, 4, 6 y 12 personas el reparto caía exacto; con otras "
                "cantidades sobraban naranjas. Cuando el reparto es exacto —el residuo es 0— "
                "decimos que el número de naranjas ES DIVISIBLE por el número de personas."
            ),
        },
        "definition": (
            "Un número a es divisible por otro número b (b ≠ 0) si la división a ÷ b es "
            "exacta: el residuo es 0. También decimos que b es divisor de a, o que a es "
            "múltiplo de b."
        ),
        "definition_title": "Divisibilidad: reparto en partes iguales",
        "definition_katex": r"b \mid a \iff \exists\, k \in \mathbb{N} : a = b \times k \ \ (\text{residuo } 0)",
        "worked_examples": [
            {
                "eyebrow": "Ejemplo 1 · Reparto exacto",
                "title": "Canicas entre amigos",
                "statement": "36 canicas se reparten en partes iguales entre 4 amigos.",
                "latex": r"36 \div 4 = 9",
                "image_slot": True,
                "steps": [
                    "36 ÷ 4 = 9.",
                    "No sobra ninguna canica.",
                    "36 es divisible por 4 porque el residuo es 0.",
                ],
                "solution": "36 ÷ 4 = 9, residuo 0",
            },
            {
                "eyebrow": "Ejemplo 2 · Reparto con residuo",
                "title": "Entradas de una feria",
                "statement": "23 entradas de feria se reparten en partes iguales entre 5 amigos.",
                "latex": r"23 \div 5 = 4 \ \text{residuo } 3",
                "image_slot": True,
                "steps": [
                    "23 ÷ 5 = 4 con residuo 3.",
                    "Cada amigo recibe 4 entradas y sobran 3.",
                    "23 NO es divisible por 5 porque el residuo no es 0.",
                ],
                "solution": "23 ÷ 5 = 4, residuo 3",
            },
            {
                "eyebrow": "Trampa común",
                "title": "Par no es lo mismo que divisible por 4",
                "statement": (
                    "18 termina en 8 (es par, divisible por 2), pero eso no basta para "
                    "asegurar que también sea divisible por 4."
                ),
                "latex": r"18 \div 2 = 9 \quad\text{pero}\quad 18 \div 4 = 4{,}5",
                "trap": True,
                "steps": [
                    "18 ÷ 2 = 9: sí es divisible por 2.",
                    "18 ÷ 4 = 4,5: NO es divisible por 4.",
                    "Cada criterio de divisibilidad es independiente: cumplir uno no garantiza cumplir otro.",
                ],
                "solution": "18 es divisible por 2 pero no por 4",
            },
        ],
        "formalization": {
            "title": "Criterios de divisibilidad",
            "intro": "Estos atajos permiten saber si un número es divisible por otro sin hacer la división completa.",
            "items": [
                {"label": "Por 2", "rule": "El número termina en 0, 2, 4, 6 u 8.", "latex": r"140 \to \text{termina en 0}"},
                {"label": "Por 3", "rule": "La suma de sus dígitos es múltiplo de 3.", "latex": r"108 \to 1+0+8=9"},
                {"label": "Por 4", "rule": "Los dos últimos dígitos forman un múltiplo de 4.", "latex": r"316 \to 16"},
                {"label": "Por 5", "rule": "El número termina en 0 o 5.", "latex": r"320 \to \text{termina en 0}"},
                {"label": "Por 6", "rule": "Es divisible por 2 y por 3 a la vez.", "latex": r"108 \to 2\mid108 \text{ y } 3\mid108"},
                {"label": "Por 9", "rule": "La suma de sus dígitos es múltiplo de 9.", "latex": r"108 \to 1+0+8=9"},
                {"label": "Por 10", "rule": "El número termina en 0.", "latex": r"1330 \to \text{termina en 0}"},
            ],
        },
        "practice": [
            {"id": "Q1", "kind": "numeric",
             "prompt": "24 caramelos se reparten entre 6 niños en partes iguales. ¿Cuántos caramelos recibe cada niño?",
             "expr": r"24 \div 6", "answer": "4"},
            {"id": "Q2", "kind": "numeric",
             "prompt": "Esos mismos 24 caramelos ahora se reparten entre 5 niños en partes iguales. ¿Cuántos caramelos sobran?",
             "expr": r"24 \div 5", "answer": "4"},
            {"id": "Q3", "kind": "single_select",
             "prompt": "24, 66, 8 y 140 son divisibles por 2. ¿Qué tienen en común?",
             "options": [
                 {"id": "a", "text": "Todos son números de dos dígitos."},
                 {"id": "b", "text": "Todos son números cuya suma de dígitos da un número par."},
                 {"id": "c", "text": "Todos terminan en 0, 2, 4, 6 u 8."},
             ],
             "expected": "c",
             "feedback_by_option": {"a": "fb_c01_q3_a", "b": "fb_c01_q3_b", "c": "correct"},
             "misconception_by_option": {
                 "a": "criterio_por_cantidad_de_digitos",
                 "b": "confunde_suma_de_digitos_con_ultimo_digito",
             }},
            {"id": "Q4", "kind": "single_select",
             "prompt": "81, 36, 9 y 108 son divisibles por 3. ¿Qué tienen en común?",
             "options": [
                 {"id": "a", "text": "La suma de sus dígitos es un múltiplo de 3."},
                 {"id": "b", "text": "Todos son números impares."},
                 {"id": "c", "text": "Al restar sus dígitos da un número impar."},
             ],
             "expected": "a",
             "feedback_by_option": {"a": "correct", "b": "fb_c01_q4_b", "c": "fb_c01_q4_c"},
             "misconception_by_option": {
                 "b": "confunde_paridad_con_criterio_de_3",
                 "c": "inventa_criterio_por_resta_de_digitos",
             }},
            {"id": "Q5", "kind": "single_select",
             "prompt": "35, 170, 95 y 320 son divisibles por 5. ¿Qué tienen en común?",
             "options": [
                 {"id": "a", "text": "Todos tienen más de dos cifras."},
                 {"id": "b", "text": "Todos terminan en 0 o 5."},
                 {"id": "c", "text": "El primer dígito es impar."},
             ],
             "expected": "b",
             "feedback_by_option": {"a": "fb_c01_q5_a", "b": "correct", "c": "fb_c01_q5_c"},
             "misconception_by_option": {
                 "a": "confunde_cantidad_de_digitos_con_criterio",
                 "c": "inventa_criterio_por_primer_digito",
             }},
            {"id": "Q6", "kind": "single_select",
             "prompt": "70, 3040, 520 y 1330 son divisibles por 10. ¿Qué tienen en común?",
             "options": [
                 {"id": "a", "text": "La suma de sus dígitos da 7."},
                 {"id": "b", "text": "Todos terminan en 0."},
                 {"id": "c", "text": "Todos empiezan con un número primo."},
             ],
             "expected": "b",
             "feedback_by_option": {"a": "fb_c01_q6_a", "b": "correct", "c": "fb_c01_q6_c"},
             "misconception_by_option": {
                 "a": "inventa_criterio_por_suma_de_digitos",
                 "c": "inventa_criterio_por_primer_digito",
             }},
            {"id": "Q7", "kind": "multi_select",
             "prompt": "De esta lista de sacos de trigo, selecciona los que se pueden repartir exacto por 3: 14, 21, 40, 45, 52, 63.",
             "valid_options": ["14", "21", "40", "45", "52", "63"],
             "expected": ["21", "45", "63"],
             "trap_options": ["40", "52"],
             "feedback_correct": "correct",
             "feedback_trap": "fb_c01_q7_trap",
             "misconception_trap": "confunde_criterio_de_3_con_otros_criterios",
             "feedback_missing": "fb_c01_q7_missing",
             "misconception_missing": "olvida_verificar_suma_de_digitos",
             "feedback_incorrect": "default",
             "misconception_incorrect": "error_divisibilidad"},
            {"id": "Q8", "kind": "multi_select",
             "prompt": "De esta lista de remos por embarcación, selecciona los que son divisibles por 10: 40, 65, 90, 150, 205, 300.",
             "valid_options": ["40", "65", "90", "150", "205", "300"],
             "expected": ["40", "90", "150", "300"],
             "trap_options": ["65", "205"],
             "feedback_correct": "correct",
             "feedback_trap": "fb_c01_q8_trap",
             "misconception_trap": "confunde_terminar_en_5_con_terminar_en_0",
             "feedback_missing": "fb_c01_q8_missing",
             "misconception_missing": "olvida_revisar_ultimo_digito",
             "feedback_incorrect": "default",
             "misconception_incorrect": "error_divisibilidad"},
            {"id": "Q9", "kind": "numeric",
             "prompt": "En una bodega reparten 50 ánforas de aceite entre 8 estantes en partes iguales. ¿Cuántas ánforas sobran?",
             "expr": r"50 \div 8", "answer": "2"},
        ],
        "feedback": {
            "correct": "¡Correcto! El reparto cae exacto.",
            "default": "Revisa el residuo de la división: si no es 0, el número no es divisible.",
            "fb_c01_q3_a": "La cantidad de dígitos no determina la divisibilidad por 2; fíjate en el último dígito.",
            "fb_c01_q3_b": "La suma de dígitos es el criterio para el 3 y el 9, no para el 2.",
            "fb_c01_q4_b": "Ser impar no tiene relación con el criterio de 3; suma los dígitos.",
            "fb_c01_q4_c": "No existe un criterio de divisibilidad basado en restar dígitos.",
            "fb_c01_q5_a": "La cantidad de cifras no es un criterio de divisibilidad.",
            "fb_c01_q5_c": "El primer dígito no determina la divisibilidad por 5; mira el último.",
            "fb_c01_q6_a": "La suma de dígitos no es el criterio para el 10; mira el último dígito.",
            "fb_c01_q6_c": "El primer dígito no determina la divisibilidad por 10.",
            "fb_c01_q7_trap": "Revisa de nuevo: algunos de los que marcaste cumplen otro criterio (por 2 o por 5), no el de 3.",
            "fb_c01_q7_missing": "Te falta al menos un número: suma sus dígitos y verifica si el resultado es múltiplo de 3.",
            "fb_c01_q8_trap": "Terminar en 5 no es lo mismo que terminar en 0: revisa el criterio del 10 de nuevo.",
            "fb_c01_q8_missing": "Te falta al menos un número divisible por 10: debe terminar exactamente en 0.",
        },
        "closing": (
            "Ya conoces la regla del reparto exacto y los atajos para reconocerla sin dividir. "
            "En el siguiente muelle veremos los números que se van formando al repetir una "
            "cantidad: los múltiplos."
        ),
        "validation_status": "F4_C01_pilot",
    },
    N4_MULTIPLES_NODE_ID: {
        "kind": "divisibility_concept",
        "concept_id": "C02",
        "concept_slug": "multiplos",
        "title": "Múltiplos: los números que se forman al repetir",
        "story_contract": {
            "type": "guided_discovery_formalization",
            "practice_position": "after_definition_plus_examples",
            "is_integrated": True,
        },
        "katia": {
            "eyebrow": "KatIA en la ruta hacia Rodas",
            "title": "Los números que se repiten",
            "body": (
                "Un barco zarpa hacia Rodas cada cierta cantidad de días. Si zarpó hoy, "
                "¿en qué otros días futuros volverá a zarpar exactamente el mismo barco?"
            ),
            "question": "¿Qué números se obtienen al repetir una cantidad una y otra vez?",
        },
        "discovery": {
            "eyebrow": "Descubrimiento guiado",
            "title": "Múltiplos: resultados de repetir una cantidad",
            "body": (
                "Si un corredor avanza 4 km cada hora, después de 2, 3, 4, 6 y 9 horas habrá "
                "recorrido 8, 12, 16, 24 y 36 km. Esos resultados son los múltiplos de 4."
            ),
        },
        "definition": "Un número a es múltiplo de b si existe un número natural n tal que a = b × n.",
        "definition_title": "Múltiplos",
        "definition_katex": r"M(b) = \{0, b, 2b, 3b, 4b, \dots\}",
        "worked_examples": [
            {"eyebrow": "Ejemplo 1", "title": "Torre de bloques",
             "statement": "Cada bloque mide 7 cm. ¿Qué altura tiene una torre de 5 bloques?",
             "latex": r"7\times 5=35", "steps": ["7×5=35.", "35 es múltiplo de 7."], "solution": "35 cm"},
            {"eyebrow": "Ejemplo 2", "title": "El corredor completo",
             "statement": "Un corredor avanza 4 km cada hora. ¿Qué distancia lleva recorrida tras 2, 3, 4, 6 y 9 horas?",
             "latex": r"4\times2,\ 4\times3,\ 4\times4,\ 4\times6,\ 4\times9",
             "image_slot": True,
             "steps": [
                 "Tras 2 horas: 4×2 = 8 km.",
                 "Tras 3 horas: 4×3 = 12 km.",
                 "Tras 4 horas: 4×4 = 16 km.",
                 "Tras 6 horas: 4×6 = 24 km.",
                 "Tras 9 horas: 4×9 = 36 km.",
                 "8, 12, 16, 24 y 36 son todos múltiplos de 4.",
             ],
             "solution": "8, 12, 16, 24, 36 km"},
            {"eyebrow": "Trampa común", "title": "No todo número cercano es múltiplo",
             "statement": "26 está cerca de un múltiplo de 4 (24), pero eso no lo hace múltiplo.",
             "latex": r"24=4\times 6 \quad\text{pero}\quad 26\neq 4\times n", "trap": True,
             "steps": ["24 ÷ 4 = 6 exacto.", "26 ÷ 4 = 6,5 no exacto.", "26 no es múltiplo de 4 aunque esté cerca de uno."],
             "solution": "26 no es múltiplo de 4"},
        ],
        "formalization": {
            "title": "Propiedades de los múltiplos",
            "intro": "Reglas que cumplen todos los múltiplos, sin excepción.",
            "items": [
                {"label": "Múltiplo de sí mismo", "rule": "Todo número es múltiplo de sí mismo: a = a × 1."},
                {"label": "El cero", "rule": "El 0 es múltiplo de todos los números: 0 = a × 0."},
                {"label": "Conjunto infinito", "rule": "Los múltiplos de un número nunca se acaban."},
                {"label": "Suma de múltiplos", "rule": "Si a es múltiplo de b, entonces a + b también es múltiplo de b."},
            ],
        },
        "practice": [
            {"id": "Q1", "kind": "numeric", "prompt": "Un corredor avanza 4 km cada hora. ¿Cuántos km recorre en 9 horas?",
             "expr": r"4\times 9", "answer": "36"},
            {"id": "Q2", "kind": "numeric", "prompt": "Una torre de bloques de 7 cm cada uno tiene 12 bloques. ¿Qué altura alcanza?",
             "expr": r"7\times 12", "answer": "84"},
            {"id": "Q3", "kind": "numeric",
             "prompt": "En un huerto siembran árboles en filas de 8. ¿Cuántos árboles hay en 7 filas completas?",
             "expr": r"8\times 7", "answer": "56"},
            {"id": "Q4", "kind": "numeric",
             "prompt": "Cada paquete de cuadernos trae 6 unidades. ¿Cuántos cuadernos hay en 11 paquetes completos?",
             "expr": r"6\times 11", "answer": "66"},
            {"id": "Q5", "kind": "single_select",
             "prompt": "¿Cuál de estas afirmaciones sobre los múltiplos de 9 es correcta?",
             "options": [
                 {"id": "a", "text": "Todo múltiplo de 9 es también múltiplo de 3."},
                 {"id": "b", "text": "Los múltiplos de 9 son siempre números de dos dígitos."},
                 {"id": "c", "text": "Solo hay 9 múltiplos de 9 en total."},
             ],
             "expected": "a",
             "feedback_by_option": {"a": "correct", "b": "fb_c02_q5_b", "c": "fb_c02_q5_c"},
             "misconception_by_option": {
                 "b": "confunde_ejemplos_vistos_con_regla_general",
                 "c": "cree_que_los_multiplos_son_finitos",
             }},
            {"id": "Q6", "kind": "multi_select",
             "prompt": "De esta lista de distancias en km, selecciona las que son múltiplos de 6: 12, 18, 20, 27, 30, 44.",
             "valid_options": ["12", "18", "20", "27", "30", "44"],
             "expected": ["12", "18", "30"],
             "trap_options": ["20", "27"],
             "feedback_correct": "correct", "feedback_trap": "fb_c02_q6_trap",
             "misconception_trap": "confunde_multiplos_de_6_con_otros",
             "feedback_missing": "fb_c02_q6_missing", "misconception_missing": "olvida_verificar_multiplo",
             "feedback_incorrect": "default", "misconception_incorrect": "error_multiplos"},
            {"id": "Q7", "kind": "multi_select",
             "prompt": "De esta lista de valores de moneda, selecciona los que son múltiplos de 15: 30, 40, 45, 50, 60, 70.",
             "valid_options": ["30", "40", "45", "50", "60", "70"],
             "expected": ["30", "45", "60"],
             "trap_options": ["40", "50", "70"],
             "feedback_correct": "correct", "feedback_trap": "fb_c02_q7_trap",
             "misconception_trap": "confunde_multiplos_de_5_con_multiplos_de_15",
             "feedback_missing": "fb_c02_q7_missing", "misconception_missing": "olvida_verificar_multiplo",
             "feedback_incorrect": "default", "misconception_incorrect": "error_multiplos"},
            {"id": "Q8", "kind": "numeric",
             "prompt": "Un tambor da un golpe cada 5 segundos, empezando en el segundo 5. ¿En qué segundo se escucha el noveno golpe?",
             "expr": r"5\times 9", "answer": "45"},
        ],
        "feedback": {
            "correct": "¡Correcto! Es el resultado de repetir la cantidad esa cantidad de veces.",
            "default": "Revisa la multiplicación: un múltiplo de b siempre es b × n para algún natural n.",
            "fb_c02_q5_b": "Esa regularidad no es general: hay múltiplos de 9 de una, dos, tres o más cifras (9, 90, 900...).",
            "fb_c02_q5_c": "Los múltiplos de un número nunca se acaban: son infinitos.",
            "fb_c02_q6_trap": "Revisa de nuevo: alguno de los que marcaste no resulta de multiplicar 6 por un natural exacto.",
            "fb_c02_q6_missing": "Te falta al menos un múltiplo de 6: divide entre 6 y verifica que el residuo sea 0.",
            "fb_c02_q7_trap": "Revisa de nuevo: alguno de los que marcaste es múltiplo de 5 o de 10, pero no de 15.",
            "fb_c02_q7_missing": "Te falta al menos un múltiplo de 15: divide entre 15 y verifica que el residuo sea 0.",
        },
        "closing": (
            "Ya sabes reconocer los múltiplos de un número y verificar cuáles lo son de verdad. "
            "En el siguiente muelle veremos un tipo especial de número: los que no se pueden "
            "repartir más que entre 1 y sí mismos, los números primos."
        ),
        "validation_status": "F4_C02_pilot",
    },
    N4_PRIMES_NODE_ID: {
        "kind": "divisibility_concept",
        "concept_id": "C03",
        "concept_slug": "primos",
        "title": "Números primos: los indivisibles",
        "story_contract": {
            "type": "guided_discovery_formalization",
            "practice_position": "after_definition_plus_examples",
            "is_integrated": True,
        },
        "katia": {
            "eyebrow": "KatIA en la ruta hacia Delos",
            "title": "Polis con una sola ruta",
            "body": (
                "Algunas pequeñas polis solo tienen una ruta directa: hacia el puerto central "
                "y ninguna otra. No comparten camino con nadie más."
            ),
            "question": "¿Qué números solo pueden repartirse entre sí mismos y el 1?",
        },
        "discovery": {
            "eyebrow": "Descubrimiento guiado",
            "title": "Contar divisores",
            "body": (
                "El 7 solo tiene 2 divisores: 1 y 7. El 12, en cambio, tiene 6 divisores. Los "
                "números con exactamente 2 divisores se llaman NÚMEROS PRIMOS."
            ),
        },
        "definition": (
            "Un número natural mayor que 1 es primo si tiene exactamente dos divisores: 1 y "
            "sí mismo. Si tiene más de dos divisores, es compuesto."
        ),
        "definition_title": "Primos y compuestos",
        "definition_katex": r"p \text{ es primo} \iff \text{divisores}(p) = \{1, p\}",
        "worked_examples": [
            {"eyebrow": "Ejemplo 1", "title": "Contar divisores",
             "statement": "El 11 tiene divisores 1 y 11 únicamente.",
             "latex": r"\text{divisores}(11)=\{1,11\}",
             "steps": ["11 solo se divide exacto entre 1 y 11.", "Tiene 2 divisores: es primo."], "solution": "11 es primo"},
            {"eyebrow": "Ejemplo 2", "title": "Un compuesto con más vecinos",
             "statement": "El 18 tiene más de dos divisores: no es primo.",
             "latex": r"\text{divisores}(18)=\{1,2,3,6,9,18\}",
             "steps": ["1, 2, 3, 6, 9 y 18 dividen exacto a 18.", "Son 6 divisores, no 2.", "18 es compuesto."],
             "solution": "18 es compuesto"},
            {"eyebrow": "Trampa común", "title": "El 1 no es primo",
             "statement": "El 1 tiene un único divisor (él mismo), no dos, así que no es primo ni compuesto.",
             "latex": r"\text{divisores}(1)=\{1\}", "trap": True,
             "steps": ["El 1 solo tiene un divisor.", "No cumple 'exactamente dos divisores'.",
                       "El 1 no es primo ni compuesto: es un caso especial."],
             "solution": "El 1 no es primo"},
        ],
        "formalization": {
            "title": "Primos y compuestos",
            "intro": "Cómo distinguir unos de otros.",
            "items": [
                {"label": "Primos", "rule": "2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31..."},
                {"label": "Compuestos", "rule": "4, 6, 8, 9, 10, 12, 14, 15, 16, 18..."},
                {"label": "El 2", "rule": "Es el único número primo par."},
                {"label": "Teorema fundamental", "rule": "Todo número compuesto se descompone de forma única como producto de primos."},
            ],
        },
        "practice": [
            {"id": "Q1", "kind": "numeric", "prompt": "¿Cuántos divisores tiene el número 12?",
             "expr": r"\text{divisores}(12)", "answer": "6"},
            {"id": "Q2", "kind": "numeric", "prompt": "¿Cuántos divisores tiene el número 7?",
             "expr": r"\text{divisores}(7)", "answer": "2"},
            {"id": "Q3", "kind": "numeric", "prompt": "¿Cuántos divisores tiene el número 1?",
             "expr": r"\text{divisores}(1)", "answer": "1"},
            {"id": "Q4", "kind": "numeric", "prompt": "¿Cuántos divisores tiene el número 11?",
             "expr": r"\text{divisores}(11)", "answer": "2"},
            {"id": "Q5", "kind": "single_select",
             "prompt": "¿Cuál de estas afirmaciones sobre los números primos es correcta?",
             "options": [
                 {"id": "a", "text": "El 2 es el único número primo que es par."},
                 {"id": "b", "text": "Todos los números primos son impares."},
                 {"id": "c", "text": "Todo número impar es primo."},
             ],
             "expected": "a",
             "feedback_by_option": {"a": "correct", "b": "fb_c03_q5_b", "c": "fb_c03_q5_c"},
             "misconception_by_option": {
                 "b": "olvida_que_2_es_primo_y_par",
                 "c": "confunde_impar_con_primo",
             }},
            {"id": "Q6", "kind": "multi_select",
             "prompt": "De esta lista de polis numeradas, selecciona las que tienen ruta solo consigo mismas y con el puerto (números primos): 14, 29, 33, 37, 42, 61.",
             "valid_options": ["14", "29", "33", "37", "42", "61"],
             "expected": ["29", "37", "61"],
             "trap_options": ["33"],
             "feedback_correct": "correct", "feedback_trap": "fb_c03_q6_trap",
             "misconception_trap": "confunde_multiplos_de_11_con_primos",
             "feedback_missing": "fb_c03_q6_missing", "misconception_missing": "olvida_verificar_divisores",
             "feedback_incorrect": "default", "misconception_incorrect": "error_primos"},
            {"id": "Q7", "kind": "multi_select",
             "prompt": "En un anfiteatro, cada fila tiene un número distinto de asientos. Selecciona las filas cuyo número de asientos es primo: 21, 23, 33, 41, 49, 53.",
             "valid_options": ["21", "23", "33", "41", "49", "53"],
             "expected": ["23", "41", "53"],
             "trap_options": ["49"],
             "feedback_correct": "correct", "feedback_trap": "fb_c03_q7_trap",
             "misconception_trap": "no_reconoce_cuadrados_de_primos_como_compuestos",
             "feedback_missing": "fb_c03_q7_missing", "misconception_missing": "olvida_verificar_divisores",
             "feedback_incorrect": "default", "misconception_incorrect": "error_primos"},
        ],
        "feedback": {
            "correct": "¡Correcto!",
            "default": "Cuenta con cuidado todos los divisores del número, no solo algunos.",
            "fb_c03_q5_b": "El 2 es primo y es par: no todos los primos son impares.",
            "fb_c03_q5_c": "Hay impares compuestos, como el 9 o el 21 (9=3×3, 21=3×7).",
            "fb_c03_q6_trap": "Revisa de nuevo: alguno de los que marcaste tiene más de 2 divisores (por ejemplo, 33 = 3×11).",
            "fb_c03_q6_missing": "Te falta al menos un número primo: verifica que solo se divida entre 1 y él mismo.",
            "fb_c03_q7_trap": "49 = 7×7 tiene 3 divisores (1, 7, 49): es compuesto, aunque no sea obvio a simple vista.",
            "fb_c03_q7_missing": "Te falta al menos una fila prima: verifica que el número solo se divida entre 1 y él mismo.",
        },
        "closing": (
            "Ya sabes distinguir un número primo de uno compuesto contando sus divisores. En el "
            "siguiente muelle usarás los primos como piezas para desarmar cualquier número "
            "compuesto: la factorización prima."
        ),
        "validation_status": "F4_C03_pilot",
    },
    N4_FACTORIZATION_NODE_ID: {
        "kind": "divisibility_concept",
        "concept_id": "C04",
        "concept_slug": "factorizacion_prima",
        "title": "Factorización prima: los bloques de construcción",
        "story_contract": {
            "type": "guided_discovery_formalization",
            "practice_position": "after_definition_plus_examples",
            "is_integrated": True,
        },
        "katia": {
            "eyebrow": "KatIA en la ruta hacia Mileto",
            "title": "Desmontar la carga del barco",
            "body": (
                "Antes de guardar la carga en el almacén, conviene desmontar un cargamento "
                "grande en sus unidades más pequeñas indivisibles."
            ),
            "question": "¿De qué 'piezas' está hecho un número compuesto?",
        },
        "discovery": {
            "eyebrow": "Descubrimiento guiado",
            "title": "División sucesiva",
            "body": "Dividir 72 sucesivamente entre primos —2, 2, 2, 3, 3— hasta llegar a 1 revela sus piezas más pequeñas.",
        },
        "definition": "Factorizar un número compuesto es expresarlo como producto de sus factores primos.",
        "definition_title": "Factorización prima",
        "definition_katex": r"n = p_1^{a_1}\times p_2^{a_2}\times\cdots\times p_k^{a_k}",
        "worked_examples": [
            {"eyebrow": "Ejemplo 1", "title": "División sucesiva",
             "statement": "Descompón 84 dividiendo entre primos hasta llegar a 1.",
             "latex": r"84=2\times2\times3\times7",
             "steps": ["84÷2=42.", "42÷2=21.", "21÷3=7.", "7÷7=1.", "84 = 2² × 3 × 7."], "solution": "84 = 2² × 3 × 7"},
            {"eyebrow": "Ejemplo 2", "title": "Una cadena más larga",
             "statement": "Descompón 72 dividiendo entre primos hasta llegar a 1.",
             "latex": r"72=2\times2\times2\times3\times3",
             "steps": ["72÷2=36.", "36÷2=18.", "18÷2=9.", "9÷3=3.", "3÷3=1.", "72 = 2³ × 3²."], "solution": "72 = 2³ × 3²"},
            {"eyebrow": "Trampa común", "title": "No cualquier producto sirve",
             "statement": "36 = 6 × 6 es una descomposición, pero 6 no es primo: hay que seguir factorizando.",
             "latex": r"36=6\times6=2\times3\times2\times3", "trap": True,
             "steps": ["6 no es primo (6=2×3).", "Hay que descomponer cada factor hasta que todos sean primos.", "36 = 2² × 3²."],
             "solution": "36 = 2² × 3²"},
        ],
        "formalization": {
            "title": "Factorización prima",
            "intro": "Todo número compuesto tiene una única descomposición en primos.",
            "items": [
                {"label": "Teorema fundamental de la aritmética", "rule": "Todo número mayor que 1 se descompone de forma única (salvo el orden) como producto de primos."},
                {"label": "División sucesiva", "rule": "Dividir por el menor primo posible hasta que el cociente sea 1."},
            ],
        },
        "practice": [
            {"id": "Q1", "kind": "numeric",
             "prompt": "Al descomponer 64 dividiendo sucesivamente entre 2, ¿cuántas veces se divide entre 2 hasta llegar a 1?",
             "expr": r"64=2^n", "answer": "6"},
            {"id": "Q2", "kind": "numeric", "prompt": "Descompón 630 en factores primos. ¿Cuál es el mayor factor primo?",
             "expr": r"630=2\times3\times3\times5\times7", "answer": "7"},
            {"id": "Q3", "kind": "numeric",
             "prompt": "Al descomponer 81 dividiendo sucesivamente entre 3, ¿cuántas veces se divide entre 3 hasta llegar a 1?",
             "expr": r"81=3^n", "answer": "4"},
            {"id": "Q4", "kind": "numeric",
             "prompt": "125 se descompone dividiendo sucesivamente entre un único primo. ¿A qué exponente queda elevado ese primo?",
             "expr": r"125=5^n", "answer": "3"},
            {"id": "Q5", "kind": "numeric",
             "prompt": "Al descomponer 1200 en factores primos, el primer paso es 1200÷2=600. ¿Cuál es el resultado del siguiente paso, 600÷2?",
             "expr": r"600\div 2", "answer": "300"},
            {"id": "Q6", "kind": "multi_select",
             "prompt": "De estas expresiones para el número 36, selecciona las que son su descomposición completa en factores primos: 2²×3², 2×2×3×3, 6×6, 4×9, 2×18.",
             "valid_options": ["2²×3²", "2×2×3×3", "6×6", "4×9", "2×18"],
             "expected": ["2²×3²", "2×2×3×3"],
             "trap_options": ["6×6", "4×9", "2×18"],
             "feedback_correct": "correct", "feedback_trap": "fb_c04_q6_trap",
             "misconception_trap": "detiene_la_descomposicion_antes_de_llegar_a_primos",
             "feedback_missing": "fb_c04_q6_missing", "misconception_missing": "no_reconoce_formas_equivalentes",
             "feedback_incorrect": "default", "misconception_incorrect": "error_factorizacion_prima"},
            {"id": "Q7", "kind": "multi_select",
             "prompt": "De estas expresiones para el número 90, selecciona las que son su descomposición completa en factores primos: 2×3²×5, 9×10, 2×45, 3×3×2×5, 6×15.",
             "valid_options": ["2×3²×5", "9×10", "2×45", "3×3×2×5", "6×15"],
             "expected": ["2×3²×5", "3×3×2×5"],
             "trap_options": ["9×10", "2×45", "6×15"],
             "feedback_correct": "correct", "feedback_trap": "fb_c04_q7_trap",
             "misconception_trap": "detiene_la_descomposicion_antes_de_llegar_a_primos",
             "feedback_missing": "fb_c04_q7_missing", "misconception_missing": "no_reconoce_formas_equivalentes",
             "feedback_incorrect": "default", "misconception_incorrect": "error_factorizacion_prima"},
        ],
        "feedback": {
            "correct": "¡Correcto!",
            "default": "Sigue dividiendo entre primos hasta que el cociente sea 1.",
            "fb_c04_q6_trap": "Revisa de nuevo: alguna opción que marcaste tiene un factor que no es primo (6, 4, 9 o 18 no lo son).",
            "fb_c04_q6_missing": "Te falta al menos una forma correcta: 2²×3² y 2×2×3×3 son la misma descomposición escrita distinto.",
            "fb_c04_q7_trap": "Revisa de nuevo: alguna opción que marcaste tiene un factor que no es primo (9, 10, 45, 6 o 15 no lo son).",
            "fb_c04_q7_missing": "Te falta al menos una forma correcta: 2×3²×5 y 3×3×2×5 son la misma descomposición escrita distinto.",
        },
        "closing": (
            "Ya sabes desarmar cualquier número compuesto en sus factores primos. En el "
            "siguiente muelle usarás esa descomposición para hallar el mayor divisor que "
            "comparten dos cargamentos: el máximo común divisor."
        ),
        "validation_status": "F4_C04_pilot",
    },
    N4_GCD_NODE_ID: {
        "kind": "divisibility_concept",
        "concept_id": "C05",
        "concept_slug": "mcd",
        "title": "Máximo común divisor: el mayor reparto en común",
        "story_contract": {
            "type": "guided_discovery_formalization",
            "practice_position": "after_definition_plus_examples",
            "is_integrated": True,
        },
        "katia": {
            "eyebrow": "KatIA en la ruta hacia Atenas",
            "title": "El contenedor más grande posible",
            "body": (
                "Dos cargamentos de tamaños distintos deben repartirse en contenedores del "
                "mismo tamaño, sin que sobre nada en ninguno. ¿Cuál es el contenedor más "
                "grande que sirve para ambos?"
            ),
            "question": "¿Cuál es el número más grande que divide exacto a dos cantidades a la vez?",
        },
        "discovery": {
            "eyebrow": "Descubrimiento guiado",
            "title": "El mayor divisor común",
            "body": (
                "24 ánforas y 36 rollos de tela deben repartirse en cajas iguales, la caja más "
                "grande posible. El mayor divisor que comparten 24 y 36 es 12."
            ),
        },
        "definition": "El máximo común divisor (MCD) de dos o más números es el mayor divisor que tienen en común.",
        "definition_title": "Máximo común divisor",
        "definition_katex": r"\text{MCD}(a,b) = \max\{d : d\mid a \text{ y } d\mid b\}",
        "worked_examples": [
            {"eyebrow": "Ejemplo 1 · Factorización prima", "title": "MCD por factores comunes",
             "statement": "Halla el MCD de 225 y 180 descomponiendo ambos a la vez.",
             "latex": r"225=3^2\times5^2 \quad 180=2^2\times3^2\times5",
             "steps": ["Factores comunes: 3² y 5.", "MCD = 3×3×5 = 45."], "solution": "MCD(225,180)=45"},
            {"eyebrow": "Trampa común", "title": "MCD no es el producto de los números",
             "statement": "El MCD de 24 y 36 no es 24×36; hay que buscar el mayor divisor COMÚN, no multiplicar.",
             "latex": r"\text{MCD}(24,36)=12 \quad\neq\quad 24\times36", "trap": True,
             "steps": ["Divisores comunes de 24 y 36: 1,2,3,4,6,12.", "El mayor es 12.", "MCD(24,36)=12."],
             "solution": "MCD(24,36)=12"},
        ],
        "formalization": {
            "title": "Máximo común divisor",
            "intro": "Tres formas de calcularlo.",
            "items": [
                {"label": "Listado de divisores", "rule": "Encontrar todos los divisores de cada número y tomar el mayor común."},
                {"label": "Factorización prima", "rule": "Multiplicar los factores primos comunes con el menor exponente."},
                {"label": "Algoritmo de Euclides", "rule": "Dividir el mayor entre el menor, luego el divisor entre el residuo, hasta residuo 0."},
            ],
        },
        "practice": [
            {"id": "Q1", "kind": "numeric", "prompt": "Halla el MCD de 24, 18 y 12 descomponiendo a la vez.",
             "expr": r"\text{MCD}(24,18,12)", "answer": "6"},
            {"id": "Q2", "kind": "numeric", "prompt": "Halla el MCD de 108 y 72.",
             "expr": r"\text{MCD}(108,72)", "answer": "36"},
            {"id": "Q3", "kind": "single_select",
             "prompt": "¿Cuál es el MCD de 24 y 36?",
             "options": [
                 {"id": "a", "text": "6"},
                 {"id": "b", "text": "12"},
                 {"id": "c", "text": "72"},
             ],
             "expected": "b",
             "feedback_by_option": {"a": "fb_c05_q3_a", "b": "correct", "c": "fb_c05_q3_c"},
             "misconception_by_option": {
                 "a": "encuentra_un_divisor_comun_pero_no_el_mayor",
                 "c": "confunde_mcd_con_producto_o_mcm",
             }},
            {"id": "Q4", "kind": "single_select",
             "prompt": "¿Cuál es el MCD de 45 y 60?",
             "options": [
                 {"id": "a", "text": "5"},
                 {"id": "b", "text": "15"},
                 {"id": "c", "text": "180"},
             ],
             "expected": "b",
             "feedback_by_option": {"a": "fb_c05_q4_a", "b": "correct", "c": "fb_c05_q4_c"},
             "misconception_by_option": {
                 "a": "encuentra_un_divisor_comun_pero_no_el_mayor",
                 "c": "confunde_mcd_con_producto_o_mcm",
             }},
            {"id": "Q5", "kind": "numeric", "prompt": "Halla el MCD de 28 y 42.",
             "expr": r"\text{MCD}(28,42)", "answer": "14"},
            {"id": "Q6", "kind": "numeric", "prompt": "Halla el MCD de 54 y 72.",
             "expr": r"\text{MCD}(54,72)", "answer": "18"},
            {"id": "Q7", "kind": "single_select",
             "prompt": "¿Cuál es el MCD de 120 y 180?",
             "options": [
                 {"id": "a", "text": "30"},
                 {"id": "b", "text": "60"},
                 {"id": "c", "text": "360"},
             ],
             "expected": "b",
             "feedback_by_option": {"a": "fb_c05_q7_a", "b": "correct", "c": "fb_c05_q7_c"},
             "misconception_by_option": {
                 "a": "encuentra_un_divisor_comun_pero_no_el_mayor",
                 "c": "confunde_mcd_con_producto_o_mcm",
             }},
            {"id": "Q8", "kind": "numeric", "prompt": "Halla el MCD de 144 y 216.",
             "expr": r"\text{MCD}(144,216)", "answer": "72"},
            {"id": "Q9", "kind": "multi_select",
             "prompt": "De estas parejas de números, selecciona las que tienen MCD igual a 12: (24,36), (18,30), (16,44), (60,84), (20,50).",
             "valid_options": ["(24,36)", "(18,30)", "(16,44)", "(60,84)", "(20,50)"],
             "expected": ["(24,36)", "(60,84)"],
             "trap_options": ["(18,30)"],
             "feedback_correct": "correct", "feedback_trap": "fb_c05_q9_trap",
             "misconception_trap": "confunde_un_divisor_comun_con_el_maximo",
             "feedback_missing": "fb_c05_q9_missing", "misconception_missing": "olvida_verificar_ambas_parejas",
             "feedback_incorrect": "default", "misconception_incorrect": "error_mcd"},
        ],
        "feedback": {
            "correct": "¡Correcto!",
            "default": "Busca el mayor divisor que compartan todos los números, no un múltiplo.",
            "fb_c05_q3_a": "6 sí es un divisor común, pero no el mayor: 12 también divide a ambos.",
            "fb_c05_q3_c": "72 no es divisor de 24 ni de 36: el MCD nunca es mayor que el menor de los números.",
            "fb_c05_q4_a": "5 sí es un divisor común, pero no el mayor: 15 también divide a ambos.",
            "fb_c05_q4_c": "180 no es divisor de 45 ni de 60: revisa la definición de MCD.",
            "fb_c05_q7_a": "30 sí es un divisor común, pero no el mayor: 60 también divide a ambos.",
            "fb_c05_q7_c": "360 no es divisor de 120 ni de 180: el MCD nunca es mayor que el menor de los números.",
            "fb_c05_q9_trap": "(18,30) tiene MCD 6, no 12: 6 es común pero no el mayor divisor común de esa pareja.",
            "fb_c05_q9_missing": "Te falta al menos una pareja con MCD 12: verifica descomponiendo ambos números.",
        },
        "closing": (
            "Ya sabes hallar el mayor divisor que comparten dos o más números. En el siguiente "
            "muelle, el último de este nivel, verás lo opuesto: el menor múltiplo que comparten, "
            "el mínimo común múltiplo."
        ),
        "validation_status": "F4_C05_pilot",
    },
    N4_LCM_NODE_ID: {
        "kind": "divisibility_concept",
        "concept_id": "C06",
        "concept_slug": "mcm",
        "title": "Mínimo común múltiplo: el primer encuentro común",
        "story_contract": {
            "type": "guided_discovery_formalization",
            "practice_position": "after_definition_plus_examples",
            "is_integrated": True,
        },
        "katia": {
            "eyebrow": "KatIA en la ruta hacia Esparta",
            "title": "Cuándo vuelven a coincidir dos barcos",
            "body": (
                "Un barco zarpa hacia Rodas cada 4 días y otro hacia Esparta cada 6 días. "
                "Ambos zarparon hoy juntos. ¿Cuándo volverán a coincidir en el mismo muelle?"
            ),
            "question": "¿Cuál es el número más pequeño que es múltiplo de dos cantidades a la vez?",
        },
        "discovery": {
            "eyebrow": "Descubrimiento guiado",
            "title": "El primer múltiplo común",
            "body": (
                "Múltiplos de 4: 4,8,12,16,20,24... Múltiplos de 6: 6,12,18,24... El primer "
                "múltiplo común es 12: cada 12 días vuelven a coincidir."
            ),
        },
        "definition": "El mínimo común múltiplo (MCM) de dos o más números es el menor múltiplo que tienen en común.",
        "definition_title": "Mínimo común múltiplo",
        "definition_katex": r"\text{MCM}(a,b) = \min\{m>0 : a\mid m \text{ y } b\mid m\}",
        "worked_examples": [
            {"eyebrow": "Ejemplo 1 · Factorización prima", "title": "MCM por factores",
             "statement": "Halla el MCM de 20 y 30.",
             "latex": r"20=2^2\times5 \quad 30=2\times3\times5",
             "steps": ["Factores con mayor exponente: 2², 3, 5.", "MCM = 4×3×5 = 60."], "solution": "MCM(20,30)=60"},
            {"eyebrow": "Trampa común", "title": "MCM no es siempre el producto",
             "statement": "El MCM de 4 y 6 no es 24 (su producto); es 12, porque comparten el factor 2.",
             "latex": r"\text{MCM}(4,6)=12 \quad\neq\quad 4\times6=24", "trap": True,
             "steps": ["4=2², 6=2×3.", "El factor común 2 se toma una sola vez con el mayor exponente: 2².", "MCM=2²×3=12."],
             "solution": "MCM(4,6)=12"},
        ],
        "formalization": {
            "title": "Mínimo común múltiplo",
            "intro": "Tres formas de calcularlo.",
            "items": [
                {"label": "Listado de múltiplos", "rule": "Encontrar los primeros múltiplos de cada número y tomar el menor común."},
                {"label": "Factorización prima", "rule": "Multiplicar los factores primos comunes y no comunes con el mayor exponente."},
                {"label": "Relación con el MCD", "rule": "MCD(a,b) × MCM(a,b) = a × b."},
            ],
        },
        "practice": [
            {"id": "Q1", "kind": "numeric",
             "prompt": "Dos barcos zarpan cada 4 y cada 10 días respectivamente, coincidiendo hoy. ¿En cuántos días volverán a coincidir?",
             "expr": r"\text{MCM}(4,10)", "answer": "20"},
            {"id": "Q2", "kind": "numeric", "prompt": "Halla el MCM de 6, 8 y 12.",
             "expr": r"\text{MCM}(6,8,12)", "answer": "24"},
            {"id": "Q3", "kind": "single_select",
             "prompt": "¿Cuál es el MCM de 16 y 24?",
             "options": [
                 {"id": "a", "text": "8"},
                 {"id": "b", "text": "48"},
                 {"id": "c", "text": "384"},
             ],
             "expected": "b",
             "feedback_by_option": {"a": "fb_c06_q3_a", "b": "correct", "c": "fb_c06_q3_c"},
             "misconception_by_option": {
                 "a": "confunde_mcm_con_mcd",
                 "c": "cree_que_el_mcm_es_siempre_el_producto",
             }},
            {"id": "Q4", "kind": "numeric", "prompt": "Halla el MCM de 21 y 35.",
             "expr": r"\text{MCM}(21,35)", "answer": "105"},
            {"id": "Q5", "kind": "numeric", "prompt": "Halla el MCM de 28 y 40.",
             "expr": r"\text{MCM}(28,40)", "answer": "280"},
            {"id": "Q6", "kind": "single_select",
             "prompt": "¿Cuál es el MCM de 36 y 54?",
             "options": [
                 {"id": "a", "text": "18"},
                 {"id": "b", "text": "108"},
                 {"id": "c", "text": "1944"},
             ],
             "expected": "b",
             "feedback_by_option": {"a": "fb_c06_q6_a", "b": "correct", "c": "fb_c06_q6_c"},
             "misconception_by_option": {
                 "a": "confunde_mcm_con_mcd",
                 "c": "cree_que_el_mcm_es_siempre_el_producto",
             }},
            {"id": "Q7", "kind": "numeric",
             "prompt": "Si MCD(132,180)=12, y sabes que MCD(a,b)×MCM(a,b)=a×b, ¿cuál es el MCM(132,180)?",
             "expr": r"\text{MCM}(132,180) = \dfrac{132\times180}{12}", "answer": "1980"},
            {"id": "Q8", "kind": "multi_select",
             "prompt": "De estas parejas de barcos, selecciona las que vuelven a coincidir cada 24 días (MCM=24): (6,8), (4,12), (9,16), (3,24), (18,8).",
             "valid_options": ["(6,8)", "(4,12)", "(9,16)", "(3,24)", "(18,8)"],
             "expected": ["(6,8)", "(3,24)"],
             "trap_options": ["(4,12)"],
             "feedback_correct": "correct", "feedback_trap": "fb_c06_q8_trap",
             "misconception_trap": "confunde_un_multiplo_comun_con_el_minimo",
             "feedback_missing": "fb_c06_q8_missing", "misconception_missing": "olvida_verificar_ambas_parejas",
             "feedback_incorrect": "default", "misconception_incorrect": "error_mcm"},
        ],
        "feedback": {
            "correct": "¡Correcto!",
            "default": "Busca el menor número que sea múltiplo de todos a la vez, no cualquier múltiplo.",
            "fb_c06_q3_a": "8 es el MCD de 16 y 24, no el MCM: el MCM siempre es mayor o igual que ambos números.",
            "fb_c06_q3_c": "384 es el producto 16×24, pero comparten el factor 8: el MCM real es menor.",
            "fb_c06_q6_a": "18 es el MCD de 36 y 54, no el MCM: el MCM siempre es mayor o igual que ambos números.",
            "fb_c06_q6_c": "1944 es el producto 36×54, pero comparten el factor 18: el MCM real es menor.",
            "fb_c06_q8_trap": "(4,12) tiene MCM 12, no 24: 12 ya es múltiplo común, pero no hace falta llegar a 24.",
            "fb_c06_q8_missing": "Te falta al menos una pareja con MCM 24: verifica descomponiendo ambos números.",
        },
        "closing": (
            "Has recorrido todo el Puerto de la Polis: divisibilidad, múltiplos, primos, "
            "factorización prima, MCD y MCM. Con estas herramientas puedes repartir, combinar y "
            "sincronizar cualquier cargamento que llegue al puerto."
        ),
        "validation_status": "F4_C06_pilot",
    },
}

_N4_SEQUENCE = [
    (N4_HUB_NODE_ID, "level_hub_port", "puerto_de_la_polis", "prealgebra.n4.c00", N3_INVERSES_NODE_ID),
    (N4_DIVISIBILITY_NODE_ID, "divisibility_concept_guided_discovery", "divisibilidad", "prealgebra.n4.c01", N4_HUB_NODE_ID),
    (N4_MULTIPLES_NODE_ID, "divisibility_concept_guided_discovery", "multiplos", "prealgebra.n4.c02", N4_DIVISIBILITY_NODE_ID),
    (N4_PRIMES_NODE_ID, "divisibility_concept_guided_discovery", "primos", "prealgebra.n4.c03", N4_MULTIPLES_NODE_ID),
    (N4_FACTORIZATION_NODE_ID, "divisibility_concept_guided_discovery", "factorizacion_prima", "prealgebra.n4.c04", N4_PRIMES_NODE_ID),
    (N4_GCD_NODE_ID, "divisibility_concept_guided_discovery", "mcd", "prealgebra.n4.c05", N4_FACTORIZATION_NODE_ID),
    (N4_LCM_NODE_ID, "divisibility_concept_guided_discovery", "mcm", "prealgebra.n4.c06", N4_GCD_NODE_ID),
]

for _index, (_node_id, _node_type, _topic, _prefix, _unlock_after) in enumerate(_N4_SEQUENCE):
    _content = _N4_HUB_CONTENT if _node_id == N4_HUB_NODE_ID else _N4_CONCEPT_CONTENT[_node_id]
    _next = _N4_SEQUENCE[_index + 1][0] if _index + 1 < len(_N4_SEQUENCE) else None
    _LESSONS[_node_id] = {
        "node_id": _node_id,
        "node_type": _node_type,
        "topic": _topic,
        "i18n_prefix": _prefix,
        "next_node_id": _next,
        "unlock_after": _unlock_after,
        "affects_elo": False,
        "is_safe_zone": True,
        "optional_branch": False,
        "skip_penalty": False,
        "objectives": ["understand_divisibility_and_multiples", "apply_prime_factorization"],
        "optional_objectives": [],
        "content": _content,
        "interactions": [],
    }

_LESSONS[N3_INVERSES_NODE_ID]["next_node_id"] = N4_HUB_NODE_ID

for _card in _N4_CARDS:
    _interaction_id = f"{N4_HUB_NODE_ID}-CARD-{_card['id']}"
    _LESSONS[N4_HUB_NODE_ID]["interactions"].append({
        "interaction_id": _interaction_id,
        "type": "single_select",
        "prompt_key": _card["concept"],
        "option_keys": ["opened"],
        "can_retry": False,
    })
    _INTERACTION_RULES[_interaction_id] = {
        "node_id": N4_HUB_NODE_ID,
        "valid_options": {"opened"},
        "expected": "opened",
        "misconception_by_option": {},
        "feedback_by_option": {"opened": "card_opened"},
    }

_register_mixed_interactions(N4_HUB_NODE_ID, "puerto", _N4_HUB_CONTENT["icebreaker"]["items"], required=False)
_register_mixed_interactions(N2_HUB_NODE_ID, "ciudad", _N2_HUB_CONTENT["icebreaker"]["items"], required=False)
_register_mixed_interactions(N3_HUB_NODE_ID, "laboratorio", _N3_HUB_CONTENT["icebreaker"]["items"], required=False)

for _node_id in N4_CONCEPT_NODE_IDS:
    _concept_content = _N4_CONCEPT_CONTENT[_node_id]
    _register_mixed_interactions(_node_id, _concept_content["concept_slug"], _concept_content["practice"])

DIAGNOSTIC_NODE_IDS = [
    NATURALS_NODE_ID, INTEGERS_NODE_ID, RATIONALS_NODE_ID, IRRATIONALS_NODE_ID,
    REALS_NODE_ID, COMPLEX_NODE_ID, CLASSIFIER_BASIC_NODE_ID,
    CLASSIFIER_RIGOROUS_NODE_ID, DETECTIVE_NODE_ID,
]


def recommended_node_for_misconception(tag: str) -> str | None:
    """Ruta de repaso: mapea un misconception a la pantalla donde se trabaja.

    Lazy: enrutado por palabras clave del tag (no un diccionario exhaustivo);
    el orden importa — las reglas más específicas van primero.
    """
    t = tag.lower()
    if "natural" in t and any(k in t for k in ("cero", "negativ", "fraccion", "no_enteros")):
        return NATURALS_NODE_ID
    if any(k in t for k in ("equilibrio", "deuda", "abono")) or "no_enteros_en_enteros" in t:
        return INTEGERS_NODE_ID
    if any(k in t for k in ("numerador", "reparto", "fraccion_como_division", "decimal_desde_division",
                            "enteros_no_son_racionales", "decimal_exacto_periodico")):
        return RATIONALS_NODE_ID
    if any(k in t for k in ("decimal_infinito", "periodico", "aproximacion", "pi_termina",
                            "sqrt2", "irracional_como_real")):
        return IRRATIONALS_NODE_ID
    if any(k in t for k in ("irracionales_como_reales", "reales_con_racionales",
                            "todo_real_es_racional", "inclusion_de_conjuntos", "complejos_en_recta_real")):
        return REALS_NODE_ID
    if any(k in t for k in ("imaginaria", "unidad_imaginaria", "parte_real", "complejos_no_reales")):
        return COMPLEX_NODE_ID
    if any(k in t for k in ("conjunto_mas_especifico", "_dentro_de_", "reales_como_complejos",
                            "imaginario_puro_con_irracional")):
        return CLASSIFIER_RIGOROUS_NODE_ID
    if t.startswith("clasifica_"):
        return CLASSIFIER_BASIC_NODE_ID
    if "implicacion" in t or "todo_complejo_es_real" in t:
        return DETECTIVE_NODE_ID
    return None


def get_lesson(node_id: str) -> dict | None:
    """Devuelve una copia del nodo para evitar mutar el catálogo global."""
    lesson = _LESSONS.get(node_id)
    return deepcopy(lesson) if lesson else None


def evaluate_interaction(node_id: str, interaction_id: str, selected_option: str) -> dict | None:
    """Evalúa una selección cerrada sin aceptar ni conservar texto libre."""
    rule = _INTERACTION_RULES.get(interaction_id)
    if not rule or rule["node_id"] != node_id:
        return None

    input_kind = rule.get("input_kind", "single_select")
    if input_kind == "numeric":
        raw_option = selected_option.strip().replace(" ", "").replace(".", ",").replace("−", "-")
        if not re.fullmatch(r"-?\d{1,6}(,\d{1,4})?", raw_option):
            return None
        selected_option = str(int(raw_option)) if "," not in raw_option else raw_option
        expected = str(rule["expected"]).replace(".", ",").replace("−", "-")
        is_expected = selected_option == expected
        return {
            "interaction_id": interaction_id,
            "selected_option": selected_option,
            "is_expected": is_expected,
            "misconception_tag": None if is_expected else rule["default_misconception"],
            "feedback_key": rule["feedback_by_result"][is_expected],
        }

    if input_kind == "text_exact":
        def _normalize_text_answer(value: str) -> str:
            normalized = value.strip().lower().replace(" ", "").replace("−", "-")
            normalized = re.sub(r"\\frac\{(-?\d{1,4})\}\{(\d{1,4})\}", r"\1/\2", normalized)
            normalized = normalized.replace("\\sqrt", "sqrt").replace("√", "sqrt")
            normalized = normalized.replace("{", "").replace("}", "")
            normalized = normalized.replace("(", "").replace(")", "")
            return normalized[1:] if normalized.startswith("+") else normalized

        raw_option = _normalize_text_answer(selected_option)
        if not re.fullmatch(
            r"-?(?:\d{1,4}(?:/\d{1,4})?|sqrt\d{1,4}(?:/\d{1,4})?|1/sqrt\d{1,4})",
            raw_option,
        ):
            return None
        accepted = {rule["expected"], *rule.get("accepted", set())}
        expected_options = {_normalize_text_answer(str(option)) for option in accepted}
        selected_option = raw_option
        is_expected = selected_option in expected_options
        return {
            "interaction_id": interaction_id,
            "selected_option": selected_option,
            "is_expected": is_expected,
            "misconception_tag": None if is_expected else rule["default_misconception"],
            "feedback_key": rule["feedback_by_result"][is_expected],
        }

    if input_kind == "multi_select":
        selected = {part for part in selected_option.split(",") if part}
        if not selected or not selected.issubset(rule["valid_options"]):
            return None
        selected_option = ",".join(sorted(selected))
        is_expected = selected == rule["expected"]
        if "error_rules" in rule:
            # Multi-select genérico, dirigido por datos: primera regla que casa gana
            # (when_missing = falta marcar X; when_selected = marcó X de más).
            if is_expected:
                misconception, feedback = None, rule["feedback_correct"]
            else:
                misconception, feedback = None, rule["default_feedback"]
                for er in rule["error_rules"]:
                    miss, sel = er.get("when_missing"), er.get("when_selected")
                    if (miss and miss not in selected) or (sel and sel in selected):
                        misconception, feedback = er.get("misconception"), er["feedback"]
                        break
            return {
                "interaction_id": interaction_id,
                "selected_option": selected_option,
                "is_expected": is_expected,
                "misconception_tag": misconception,
                "feedback_key": feedback,
            }
        if "feedback_correct" in rule:
            # camino genérico con trampas: prioriza incluir un distractor "trampa"
            # sobre excluir un esperado (B08-Q02 y futuros nodos).
            if is_expected:
                misconception, feedback = None, rule["feedback_correct"]
            elif selected & rule.get("trap_options", set()):
                misconception = rule.get("misconception_trap")
                feedback = rule["feedback_trap"]
            elif rule["expected"] - selected:
                misconception = rule.get("misconception_missing")
                feedback = rule["feedback_missing"]
            else:
                misconception = rule.get("misconception_incorrect")
                feedback = rule["feedback_incorrect"]
            return {
                "interaction_id": interaction_id,
                "selected_option": selected_option,
                "is_expected": is_expected,
                "misconception_tag": misconception,
                "feedback_key": feedback,
            }
        if is_expected:
            misconception = None
            feedback = "naturals_correct"
        elif "zero" not in selected:
            misconception = "excluye_cero_de_naturales_pese_a_convencion"
            feedback = "zero_is_natural"
        elif "negative_two" in selected:
            misconception = "incluye_negativos_en_naturales"
            feedback = "negatives_are_not_natural"
        elif "sqrt_two" in selected:
            misconception = "incluye_no_enteros_en_naturales"
            feedback = "irrationals_not_natural"
        elif "decimal_25" in selected:
            misconception = "incluye_fracciones_en_naturales"
            feedback = "decimals_not_natural"
        else:
            misconception = None
            feedback = "naturals_review"
        return {
            "interaction_id": interaction_id,
            "selected_option": selected_option,
            "is_expected": is_expected,
            "misconception_tag": misconception,
            "feedback_key": feedback,
        }

    if selected_option not in rule["valid_options"]:
        return None
    expected = rule["expected"]
    # default_feedback cubre combinaciones no documentadas (p. ej. clasificador:
    # cualquier zona equivocada sin retro específica cae al mensaje genérico).
    feedback_key = rule["feedback_by_option"].get(selected_option) or rule.get("default_feedback")
    return {
        "interaction_id": interaction_id,
        "selected_option": selected_option,
        "is_expected": None if expected is None else selected_option == expected,
        "misconception_tag": rule["misconception_by_option"].get(selected_option),
        "feedback_key": feedback_key,
    }


def presentation_band(score_pct: float | None) -> str:
    """Traduce los cortes provisionales del diagnóstico a presentación.

    Los cortes son deliberadamente centralizados y deberán recalibrarse con el
    piloto. No afectan el ELO ni la ubicación del estudiante.
    """
    score = float(score_pct or 0.0)
    if score >= 80.0:
        return "avanzado"
    if score >= 50.0:
        return "intermedio"
    return "basico"
