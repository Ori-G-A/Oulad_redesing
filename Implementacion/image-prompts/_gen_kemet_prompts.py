"""Genera `alg-n1-kemet-PROMPTS.md`: los 36 prompts de Kemet, cada uno autocontenido.

El bloque de estilo, los personajes y los negativos son idénticos en los 36 y viven
aquí una sola vez. Si hay que corregir la línea gráfica —ya pasó con N2, que empezó
siendo un mercado y acabó siendo edificios— se edita ESTE archivo y se regenera:

    python Implementacion/image-prompts/_gen_kemet_prompts.py

`alg-n1-kemet.md` es la ficha de diseño (por qué cada escena es esa). Este script
produce el pegable.
"""
import io
import os

ESTILO = (
    "ESTILO — pixel-art educativo refinado, estilo 16/32-bit narrativo de alta calidad, con "
    "clusters de píxeles visibles, bordes pixelados limpios, sombreado por bloques y dithering "
    "sutil. NO pintura digital hiperrealista, no render 3D, no vector plano. Escena contenida a "
    "media distancia, pocos personajes, objetos pedagógicos claros y legibles sobre mesa, suelo "
    "o banco de trabajo. Sombras azul noche, luz cálida de lámpara de aceite, piedra caliza y "
    "adobe encalado. El espacio se lee como el INTERIOR de un recinto del Antiguo Egipto: muros "
    "de adobe, columnas papiriformes, dinteles de piedra, esteras, tinajas; la arquitectura de "
    "fondo siempre secundaria."
)

KATIA = (
    "KATIA — gata blanca con mancha naranja y negra en la cabeza, ojo verde visible, ocular "
    "mecánico teal, pata y brazo mecánicos, túnica morada con ornamentos dorados. Es griega y "
    "está de viaje: NO se la viste de egipcia, no lleva tocado nemes ni collar faraónico. Es la "
    "única figura del cuadro que no pertenece al sitio y debe notarse un poco. Legible en primer "
    "o medio plano. No convertirla en una gata totalmente metálica."
)

SECUNDARIOS = (
    "PERSONAJES SECUNDARIOS — todos son animales antropomórficos, preferentemente gatos bípedos "
    "con faldellín de lino, delantal o collar ancho egipcio; pelajes variados (atigrado, negro, "
    "gris, calicó, siamés, naranja, blanco moteado). Nunca humanos realistas."
)

GUIAS = {
    "meritka": (
        "GUÍA — Meritka: gata negra esbelta, collar ancho de cuentas azules, cálamo de caña tras "
        "la oreja. Mismo aspecto en las cuatro salas de su casa."
    ),
    "bakenra": (
        "GUÍA — Bakenra: gato atigrado corpulento, faldellín corto de cuero, cuerda al hombro. "
        "Mismo aspecto en las cuatro salas de su casa."
    ),
    "tabiry": (
        "GUÍA — Tabiry: gata calicó, sombrero de junco trenzado, pies descalzos embarrados. "
        "Mismo aspecto en las cuatro salas de su casa."
    ),
    "iuty": (
        "GUÍA — Iuty: gato gris de pelo corto, delantal manchado de pigmento, plomada al cinto. "
        "Mismo aspecto en las cuatro salas de su casa."
    ),
    None: "",
}

PALETAS = {
    "vida": "PALETA — dominante turquesa y ocre, acento negro de tinta.",
    "obra": "PALETA — dominante arena y terracota, acento sombra azul fría.",
    "campos": "PALETA — dominante verde fértil y limo, acento agua turquesa.",
    "canon": "PALETA — dominante azul egipcio y cal, acento oro contenido.",
}

# Se añade solo cuando KatIA está en la escena: en un bodegón no hay morado que mantener.
PALETA_KATIA = " El morado de la túnica de KatIA se mantiene sobre esa dominante."

# Los bodegones tienen que quedarse vacíos: sin este negativo el generador mete un gato.
SIN_FIGURAS = (
    "SIN FIGURAS — bodegón puro: ni KatIA, ni guías, ni personajes secundarios, ni siluetas ni "
    "manos entrando en el encuadre. Solo objetos y arquitectura."
)

REGLAS = (
    "REGLAS DURAS — la imagen muestra la SITUACIÓN, nunca la solución: ninguna cifra, ningún "
    "resultado, ninguna cantidad de objetos dispuesta de forma que el ejercicio se resuelva "
    "contando en la imagen. Cualquier texto escrito (papiros, tablillas) es ilegible: trazos de "
    "tinta, no signos reconocibles, y nunca letras ni números latinos. Los jeroglíficos solo "
    "valen como textura de muro o columna, nunca legibles, nunca protagonistas y nunca sobre la "
    "superficie donde ocurre la acción. Si aparece una escalera o un peldaño, va completamente "
    "limpio: sin símbolos, letras, números, runas, marcas, medallones, flechas ni relieves."
)

NEGATIVOS = (
    "NEGATIVOS — no panorámica turística, no pirámides al atardecer como postal, no Esfinge, no "
    "faraón ni realeza, no momias ni tumbas, no dioses egipcios antropomórficos (Anubis, Thot: "
    "los animales de aquí son vecinos, no deidades), no multitudes, no plaza pública como foco, "
    "no pintura digital lisa, no neón saturado, no sci-fi duro, no anime ni chibi, no humanos "
    "realistas, no marcas de agua ni firmas."
)

# (archivo, ratio, casa, guía, título, escena)
IMAGENES = [
    # ── Hub ──────────────────────────────────────────────────────────────────
    ("a00-hub-papiro-katia.png", "16:9 (header de nivel, ancho completo)", "vida", "meritka",
     "A00 · Hub — El Papiro de las Cuatro Casas",
     "Interior en penumbra de una sala de archivo del Antiguo Egipto, al amanecer. Sobre una mesa "
     "larga de madera, Meritka extiende un papiro grande y visiblemente dañado: le faltan cuatro "
     "secciones, cuatro huecos rasgados de bordes irregulares y completamente vacíos. Al otro lado "
     "de la mesa, KatIA acaba de llegar y todavía lleva el polvo del viaje. Por el vano abierto del "
     "fondo se ven, muy secundarias y sin detalle, cuatro construcciones distintas recortadas contra "
     "el cielo: un recinto encalado, una rampa de obra, unos campos anegados y un taller con "
     "andamio. Luz baja de lámpara de aceite concentrada sobre la mesa; azul frío en el resto de la "
     "sala."),
    ("a00-ice1-cestos.png", "1:1", "vida", None,
     "A00 · Rompehielos 1 — Los cestos de grano",
     "Bodegón cerrado, sin personajes: varios cestos de mimbre llenos de grano apilados junto a una "
     "balanza de suelo de dos platos, sobre un piso de tierra batida. Un cesto está volcado de lado, "
     "vacío. Muro de adobe encalado detrás. El número de cestos no debe poder contarse con "
     "claridad: unos quedan fuera de encuadre y otros en penumbra."),
    ("a00-ice2-registro.png", "1:1", "vida", None,
     "A00 · Rompehielos 2 — Las dos tablillas",
     "Bodegón cerrado, sin personajes: dos tablillas de barro apoyadas contra un muro de adobe "
     "encalado, una junto a la otra, con anotaciones de trazo ilegible. Una está llena de líneas "
     "cortas repetidas; la otra tiene una sola línea larga. Un cálamo de caña en el suelo entre las "
     "dos."),
    ("a00-ice3-hueco.png", "1:1", "vida", None,
     "A00 · Rompehielos 3 — El dato que falta",
     "Primer plano cenital de un papiro desenrollado sobre una mesa. Sin personajes. Líneas de "
     "anotaciones de trazo ilegible y, en mitad de una de ellas, un espacio deliberadamente en "
     "blanco del tamaño de una palabra. Un cálamo apoyado en el borde del papiro, apuntando a ese "
     "hueco sin tocarlo."),

    # ── Casa I · La Casa de la Vida ───────────────────────────────────────────
    ("l01-variables-katia.png", "4:3", "vida", "meritka",
     "L01 · La sala de los cálamos — Variables",
     "Interior de un escritorio de escribas: estantes de nichos llenos de rollos, un cuenco de tinta "
     "negra, cálamos de caña en un vaso de cerámica. Meritka sostiene en alto un papiro desenrollado "
     "ante KatIA; en el papiro se ve una misma anotación breve repetida muchas veces en columnas, "
     "de trazo ilegible. Al fondo, un cesto lleno de rollos idénticos esperando ser copiados. Luz "
     "turquesa de mañana entrando por una ventana alta."),
    ("l02-constantes-katia.png", "4:3", "vida", "meritka",
     "L02 · El estante sellado — Constantes",
     "Meritka descorre un sello de arcilla roto de la puertecilla de un estante bajo. Dentro, sobre "
     "una tela doblada, tres objetos de medida patrón: una vara de madera, una cuerda con nudos "
     "regulares y un peso de piedra pulida con una marca grabada. KatIA se inclina para mirar sin "
     "tocar. El resto de la sala es de trabajo cotidiano y está desordenado; solo ese estante está "
     "limpio y aparte. Contraste entre el turquesa frío del nicho y el ocre cálido de la sala."),
    ("l03-traduccion-katia.png", "4:3", "vida", "meritka",
     "L03 · La mesa de dictado — Traducción",
     "Mesa baja de dictado. Un mensajero (gato siamés con sandalias de viaje, aún con el manto "
     "puesto) habla de pie y con prisa, una mano levantada. Sentados frente a él, dos escribas "
     "jóvenes escriben a la vez sobre dos tablillas distintas; las tablillas están giradas hacia el "
     "espectador lo justo para verse ocupadas, con trazos de tinta ilegibles y claramente DISTINTOS "
     "entre sí. Meritka observa de pie, sin intervenir. KatIA en primer plano, mirando de una "
     "tablilla a la otra."),
    ("l04-valor-numerico-katia.png", "4:3", "vida", "meritka",
     "L04 · La cámara del recuento — Valor numérico",
     "Cámara semisubterránea de recuento, techo bajo. Fichas de barro apiladas en columnas y un "
     "cordel de conteo con nudos colgado de la pared. Meritka sostiene una tablilla; a su lado, en "
     "el suelo, una fila larga de carros de mano de madera VACÍOS, muchos más de los necesarios, "
     "esperando una carga que no llegó. KatIA mira los carros vacíos. Luz de lámpara de aceite "
     "rasante y polvo suspendido. No se ve grano en ninguna parte."),

    # ── Casa II · La obra de la pirámide ──────────────────────────────────────
    ("o01-semejantes-katia.png", "4:3", "obra", "bakenra",
     "O01 · La rampa — Términos semejantes",
     "Al pie de una rampa de obra de adobe, a media mañana. Bakenra sostiene dos tablillas de turno, "
     "una en cada mano, mirándolas alternativamente. Detrás, una cuadrilla de gatos obreros espera "
     "de pie junto a un trineo de madera cargado, sin avanzar. A un lado del encuadre, cuerdas "
     "enrolladas; al otro, mazos y herramienta apilada — dos montones claramente separados, sin "
     "mezclar. KatIA en primer plano entre los dos montones, mirando las tablillas de Bakenra. "
     "Polvo de arena en el aire y sombra azul fría bajo la rampa."),
    ("o02-signos-katia.png", "4:3", "obra", "bakenra",
     "O02 · El patio de aparejos — Signos y paréntesis",
     "Patio cerrado de almacén de aparejos: poleas de madera colgadas de una viga, sogas enrolladas "
     "en el suelo, contrapesos de piedra alineados contra el muro. Bakenra sostiene una tablilla de "
     "vale de devolución. En el muro del fondo, una hilera de soportes de madera para contrapesos "
     "con varios huecos evidentes. En el vano de salida, una cuadrilla se aleja con las manos "
     "vacías. KatIA en primer plano junto a las poleas. Luz dura de mediodía, sombras cortas."),
    ("o03-producto-katia.png", "4:3", "obra", "bakenra",
     "O03 · El taller de cinceles — Producto de monomios",
     "Interior del taller de talla: banco largo con cinceles alineados por tamaño, piedras de "
     "afilar, virutas de piedra en el suelo, plantillas de madera colgadas del muro. Bakenra ha "
     "dejado una tablilla de pedido sobre el banco y mira por el vano hacia fuera, donde se ve —muy "
     "secundaria y sin detalle— una explanada de acopio prácticamente vacía con unos pocos sillares "
     "sueltos. KatIA examina un cincel. Polvo blanco de piedra en el aire."),
    ("o04-cociente-katia.png", "4:3", "obra", "bakenra",
     "O04 · La caseta del capataz — Cociente de monomios",
     "Caseta de obra pequeña y sombreada, con esteras y una ventana sin postigos. Sobre una repisa, "
     "el censo de la obra en tablillas. Bakenra señala una línea de una de ellas. Fuera, visto por "
     "la ventana, un grupo de aguadores de pie con sus cántaros al hombro TODAVÍA LLENOS, sin "
     "repartir, mirando hacia la caseta. KatIA sigue con la vista el dedo de Bakenra. Calor de media "
     "tarde fuera, sombra profunda dentro."),

    # ── Casa III · Los campos tras la crecida ─────────────────────────────────
    ("f01-simplificar-katia.png", "4:3", "campos", "tabiry",
     "F01 · La parcela partida — Simplificación",
     "Campo recién drenado tras la crecida, barro brillante y primeros brotes verdes. Tabiry "
     "sostiene una cuerda de agrimensor extendida sobre el terreno; los mojones de lindero están "
     "caídos o desaparecidos y el campo se ve como una sola extensión continua, sin divisiones. Al "
     "fondo, un grupo pequeño de familias de gatos esperando de pie con sus enseres. KatIA junto a "
     "Tabiry, con las patas en el barro. Luz de mañana y reflejos turquesa en los charcos."),
    ("f02-suma-katia.png", "4:3", "campos", "tabiry",
     "F02 · El canal madre — Suma de fracciones",
     "Junto a un canal principal de riego, con dos acequias que salen de él en direcciones distintas "
     "y un azud de tablones de madera. Tabiry se ha agachado y ha hundido una mano en el agua del "
     "canal. En la orilla, apoyada en una piedra, una tablilla de turnos de riego. Una de las dos "
     "acequias corre visiblemente más seca que la otra. KatIA de pie en el borde, mirando el agua. "
     "Cielo alto y verdes densos en las orillas."),
    ("f03-producto-katia.png", "4:3", "campos", "tabiry",
     "F03 · La era de trilla — Producto de fracciones",
     "Era de trilla circular de tierra apisonada, con un trillo de madera apoyado en el borde y paja "
     "suelta arremolinada por el viento. La era está prácticamente VACÍA: apenas queda parva. Tabiry "
     "sostiene una tablilla y mira la era barrida. Al fondo, la puerta de una troje de adobe, "
     "abierta y oscura. KatIA junto al trillo. Luz de mediodía muy blanca y sombras cortas."),
    ("f04-division-katia.png", "4:3", "campos", "tabiry",
     "F04 · El silo de simiente — División de fracciones",
     "Interior de un silo de adobe de planta redonda, con la simiente formando un montón alto hasta "
     "media pared. Contra el muro, una pila de sacos de tela VACÍOS y doblados, sin llenar. Tabiry "
     "sostiene una tablilla de registro y señala el montón lleno con la otra mano. KatIA mira los "
     "sacos vacíos. Contraste claro entre la abundancia del montón y la pila de sacos sin usar. Luz "
     "en haz entrando por una tronera alta."),

    # ── Casa IV · El taller del canon ─────────────────────────────────────────
    ("r01-razones-katia.png", "4:3", "canon", "iuty",
     "R01 · La cuadrícula del canon — Razones y proporciones",
     "Taller de pintores frente a un muro encalado con una cuadrícula de cuerda tensada. En una mesa "
     "en primer término, el boceto pequeño de un motivo; en el muro, la versión ampliada del mismo "
     "motivo, visiblemente DEFORMADA: estirada de un lado y achatada del otro. Iuty mira el muro con "
     "los brazos cruzados. KatIA compara el boceto con el muro. Andamio de madera secundario a un "
     "lado."),
    ("r02-regla-de-tres-katia.png", "4:3", "canon", "iuty",
     "R02 · El tinte de lino — Regla de tres",
     "Sala del tinte: una tina grande de barro con el líquido oscuro y un banco con madejas de lino. "
     "Del techo cuelgan madejas puestas a secar; las primeras tienen color pleno y las últimas de la "
     "fila están claramente apagadas y desiguales. Iuty sostiene una tablilla con la receta. KatIA "
     "toca una de las madejas descoloridas. Vapor tenue sobre la tina y suelo húmedo que refleja."),
    ("r03-porcentajes-katia.png", "4:3", "canon", "iuty",
     "R03 · El pan de oro — Porcentajes",
     "Obrador del batihoja: mesa de piedra pulida, mazo pequeño, pilas de hojas finísimas de oro "
     "separadas por pergaminos, pinzas finas. Un batihoja (gato blanco moteado, manos protegidas con "
     "tela) se ha apartado de la mesa con las manos abiertas y vacías, en gesto de que no puede "
     "seguir. Iuty sostiene la tablilla del encargo. Sobre la mesa hay un hueco evidente donde "
     "debería continuar la pila de hojas. KatIA mira el hueco. Dorados intensos pero contenidos, sin "
     "brillo metálico exagerado."),
    ("r04-variacion-katia.png", "4:3", "canon", "iuty",
     "R04 · La sala de las lámparas — Variación directa e inversa",
     "Sala de trabajo nocturna del taller. Seis lámparas de aceite repartidas por la sala, todas "
     "apagadas menos una que se está consumiendo, con la mecha casi al final. En el centro, una "
     "tinaja grande de aceite volcada de lado y vacía. Iuty señala la tinaja. El friso del muro se "
     "ve a medio terminar, en penumbra. KatIA dentro del círculo de luz de la última llama. Escena "
     "predominantemente oscura con un único foco cálido pequeño."),

    # ── Opcionales · las trampas ──────────────────────────────────────────────
    ("l01-trampa-etiqueta.png", "1:1", "vida", None,
     "L01 · Trampa — La anotación reescrita",
     "Primer plano cenital, sin personajes: un cálamo de caña apoyado sobre un papiro donde una "
     "anotación breve aparece tachada con una raya y reescrita justo debajo. Trazos de tinta "
     "ilegibles. Una gota de tinta seca junto al tachón."),
    ("l02-trampa-pozo.png", "1:1", "vida", None,
     "L02 · Trampa — El brocal del pozo",
     "Vista cenital cerrada del brocal circular de un pozo de piedra, con una cuerda cruzándolo de "
     "lado a lado por el centro y el agua oscura al fondo. Sin personajes. El círculo del brocal "
     "ocupa casi todo el encuadre; ninguna marca ni medida grabada en la piedra."),
    ("l03-trampa-tablillas.png", "1:1", "vida", None,
     "L03 · Trampa — Las dos versiones",
     "Dos tablillas de barro del mismo tamaño, apoyadas una junto a otra sobre una estera, con "
     "trazos de tinta ilegibles y claramente distintos entre sí. Sin personajes. Luz lateral que "
     "marca el relieve del barro."),
    ("l04-trampa-carros.png", "1:1", "vida", None,
     "L04 · Trampa — Los carros de más",
     "Fila larga de carros de mano de madera vacíos, vistos en perspectiva y perdiéndose hacia el "
     "fondo, junto a un montón de grano notablemente pequeño en primer término. Sin personajes. "
     "Suelo de tierra batida, luz rasante."),
    ("o01-trampa-monton.png", "1:1", "obra", None,
     "O01 · Trampa — Lo que no se mezcla",
     "Dos montones separados sobre la arena: cuerdas enrolladas a un lado, mazos y herramienta al "
     "otro, con una raya trazada en la arena entre los dos. Sin personajes. Vista a media altura, "
     "sombra azul fría."),
    ("o02-trampa-huecos.png", "1:1", "obra", None,
     "O02 · Trampa — Los soportes vacíos",
     "Detalle de un muro de adobe con una hilera de soportes de madera para contrapesos de piedra: "
     "la mitad ocupados y la mitad vacíos, alternando de forma irregular. Sin personajes. Luz dura "
     "de mediodía que marca los huecos."),
    ("o03-trampa-acopio.png", "1:1", "obra", None,
     "O03 · Trampa — La explanada de acopio",
     "Explanada de acopio de sillares vista a media distancia y casi vacía: unos pocos bloques "
     "sueltos y las marcas en el polvo de donde estuvieron los demás. Sin personajes. Horizonte bajo "
     "y cielo grande."),
    ("o04-trampa-cantaros.png", "1:1", "obra", None,
     "O04 · Trampa — El reparto que no se hizo",
     "Varios cántaros de barro llenos y alineados contra un muro en sombra, con un cuenco de reparto "
     "boca abajo en el suelo junto a ellos. Sin personajes. Detalle cercano, luz de media tarde."),
    ("f01-trampa-mojon.png", "1:1", "campos", None,
     "F01 · Trampa — El mojón caído",
     "Un mojón de lindero de piedra caído en el barro y medio hundido, con la marca de la crecida "
     "todavía húmeda alrededor. Sin personajes. Primer plano bajo, verde y limo."),
    ("f02-trampa-acequias.png", "1:1", "campos", None,
     "F02 · Trampa — Las dos acequias",
     "Dos acequias que salen del mismo canal en ángulo, una con buen caudal y otra casi seca con el "
     "fondo agrietado a la vista. Sin personajes. Vista desde arriba en diagonal."),
    ("f03-trampa-era.png", "1:1", "campos", None,
     "F03 · Trampa — La era barrida",
     "La era de trilla circular vista desde el borde, barrida y prácticamente vacía, con la puerta "
     "de la troje de adobe abierta y oscura al fondo. Sin personajes. Paja suelta movida por el "
     "viento."),
    ("f04-trampa-sacos.png", "1:1", "campos", None,
     "F04 · Trampa — El saco sin llenar",
     "Un solo saco de tela vacío colgado de un clavo de madera, en primer término, con el montón de "
     "simiente lleno detrás y desenfocado por la penumbra. Sin personajes. Haz de luz desde una "
     "tronera alta."),
    ("r01-trampa-boceto.png", "1:1", "canon", None,
     "R01 · Trampa — El boceto y su copia",
     "El boceto pequeño de un motivo y su copia ampliada y deformada, uno al lado del otro sobre una "
     "mesa de taller. Sin personajes. Vista cenital, cuerda de cuadrícula enrollada a un lado."),
    ("r02-trampa-madejas.png", "1:1", "canon", None,
     "R02 · Trampa — Las madejas desiguales",
     "Hilera de madejas de lino colgadas de una vara, degradando de color pleno en un extremo a "
     "claramente descolorido en el otro. Sin personajes. Fondo de muro encalado y goteo en el suelo."),
    ("r03-trampa-pila.png", "1:1", "canon", None,
     "R03 · Trampa — El hueco en la pila",
     "Detalle cerrado de una pila de hojas finísimas de oro separadas por pergaminos, sobre mesa de "
     "piedra pulida, con un hueco evidente donde la pila debería continuar. Sin personajes. Unas "
     "pinzas apoyadas al lado."),
    ("r04-trampa-lampara.png", "1:1", "canon", None,
     "R04 · Trampa — La última mecha",
     "Una sola lámpara de aceite de barro en primer plano con la mecha consumiéndose, la llama "
     "mínima, sobre fondo casi negro. Sin personajes. Único foco de luz de toda la imagen."),
]

CABECERA = """# ALG-N1 · Kemet — los 36 prompts completos

Generado por `_gen_kemet_prompts.py`. **No editar a mano**: si hay que cambiar el estilo, los
personajes o los negativos, se edita el script y se regenera — así los 36 siguen siendo idénticos
en todo lo que debe ser idéntico.

Cada bloque es autocontenido y se pega tal cual en el generador de imágenes. Destino de los
archivos: `frontend/public/algebra/generated/n1-kemet/`.

**Referencias visuales:** si la herramienta lo permite, adjuntar antes de generar
`frontend/public/prealgebra/step-naturales.png`, `step-enteros.png`, `escalera-conjuntos.png`,
`katia-primer-plano-enteros.png` y `caso-enteros-recta.jpg`. Son la línea gráfica que hay que
mantener.

**Orden sugerido:** primero `a00-hub-papiro-katia.png` y una sala de cada casa (L01, O01, F01,
R01). Con esas cinco se valida el estilo y los cuatro guías antes de tirar las 31 restantes.

La ficha de diseño —por qué cada escena es la que es— está en `alg-n1-kemet.md`.

---
"""


def bloque(archivo, ratio, casa, guia, titulo, escena):
    """Monta el prompt. Un bodegón («Sin personajes») no lleva ni KatIA ni secundarios."""
    vacia = "in personajes" in escena
    con_katia = "KatIA" in escena
    partes = [
        f"ESCENA — {escena}",
        ESTILO,
        "" if vacia else (KATIA if con_katia else ""),
        "" if vacia else GUIAS[guia],
        "" if vacia else SECUNDARIOS,
        SIN_FIGURAS if vacia else "",
        PALETAS[casa] + (PALETA_KATIA if con_katia and not vacia else ""),
        f"FORMATO — {ratio}.",
        REGLAS,
        NEGATIVOS,
    ]
    cuerpo = "\n\n".join(p for p in partes if p)
    return f"## {titulo}\n\n`{archivo}` · {ratio}\n\n```text\n{cuerpo}\n```\n"


def revisar():
    """Cada imagen es o un bodegón declarado o una escena con KatIA. No hay tercer caso."""
    for archivo, _ratio, _casa, _guia, _tit, escena in IMAGENES:
        vacia = "in personajes" in escena
        if not vacia and "KatIA" not in escena:
            raise SystemExit(
                f"{archivo}: ni dice «Sin personajes» ni mete a KatIA en la escena. "
                "Una sala sin KatIA es un olvido, no una decisión."
            )


def main():
    revisar()
    destino = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "alg-n1-kemet-PROMPTS.md")
    partes = [CABECERA] + [bloque(*fila) for fila in IMAGENES]
    io.open(destino, "w", encoding="utf-8").write("\n".join(partes))
    print(f"{len(IMAGENES)} prompts escritos en {destino}")


if __name__ == "__main__":
    main()
