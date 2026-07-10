# Prompts de imagen — N4 · El Puerto de la Polis

Fase 7 del plan de guión unificado (`~/.claude/plans/effervescent-scribbling-goblet.md`).
Vocabulario visual del espacio (Fase 0 / skill `prealgebra-narrative-style`): muelles,
barcos, cargamento, rutas, tablillas de cera. Toque retrofuturista permitido: instrumentos
de navegación con detalle mecánico puntual. Nivel de referencia (ya validado, diverso, sin
objetos sobreusados): ánforas de aceite, sacos de trigo, rollos de tela, cerámica, naranjas,
tejas, columnas de mármol, postes con tablillas de ruta.

**Línea gráfica obligatoria (`frontend/public/prealgebra/`):** usar como referencia directa
`step-naturales.png`, `step-enteros.png`, `step-racionales.png`, `step-reales.png`,
`escalera-conjuntos.png`, `katia-primer-plano-enteros.png` y `caso-enteros-recta.jpg`.
Antes de generar, abrir/adjuntar esas imágenes como referencias visuales si la herramienta lo
permite; si no, copiar completa esta línea gráfica dentro del prompt final.

**Método aprobado para KatIA en N4:** no regenerar a KatIA desde prompt libre. Para una escena
con KatIA, generar primero un fondo SIN KatIA, sin gatos/personajes principales y con espacio
libre para componerla; después montar encima `frontend/public/prealgebra/katia-canon-sprite-hard.png`.
El bloque canónico de abajo se usa para validar identidad, no para pedirle al modelo que invente
una nueva versión del personaje.

**Bloque canónico de KatIA (obligatorio para cualquier imagen donde aparezca):** usar
`katia-primer-plano-enteros.png` como referencia de identidad, no solo de estilo. KatIA es una
gata cyborg adulta, serena y socrática, no una mascota infantil. Conservar proporciones del
personaje original: rostro blanco con hocico adulto redondeado, expresión tranquila y
observadora, orejas grandes pero no caricaturescas, ojo verde almendrado visible, mancha
naranja/negra asimétrica en la frente y oreja, ocular mecánico teal sobre el otro ojo con
placas metálicas grises, pata/brazo mecánico segmentado, túnica griega morada con ornamentos
dorados y silueta de tutora/maestra. Si el encuadre es pequeño, simplificar el entorno antes que
simplificar a KatIA. Debe seguir reconociéndose como la misma KatIA del primer plano.

**Estilo base:** `pixel-art educativo refinado, estilo 16/32-bit narrativo de alta calidad,
con clusters de píxeles visibles, bordes pixelados limpios, sombreado por bloques y dithering
sutil, silueta con escalones de píxel visibles y poca mezcla suave; NO pintura digital
hiperrealista ni ilustración lisa. Mantener el lenguaje visual de los assets existentes:
KatIA legible en primer/medio plano, escena contenida, pocos personajes secundarios, objetos
pedagógicos claros sobre muelle/mesa de control, sombras azul noche, luz dorada de faroles,
piedra/madera cálida y acentos teal pequeños en el ocular de KatIA o instrumentos de
navegación. KatIA debe conservar identidad: gata blanca con mancha naranja/negra en la
cabeza, ojo verde visible, ocular mecánico teal, pata/brazo mecánico, túnica morada y
ornamentos dorados. El espacio debe leerse como puerto griego clásico cercano: muelles,
barcos, cargamento, rutas, tablillas de cera e instrumentos de navegación de bronce.`

**Personajes secundarios:** cualquier rol humano mencionado en los prompts (mercader,
escriba, niño, joven, mozo, vendedor, mensajero, etc.) debe representarse como animal
antropomórfico. Preferencia: otros gatos bípedos con túnicas, capas o ropa portuaria griega,
pelajes variados (atigrado, negro, gris, calicó, siamés, naranja, blanco moteado) y texturas
de pelaje diferenciadas. No humanos realistas.

**Escaleras y peldaños:** si aparece una escalera, escalinata o peldaño en cualquier imagen,
debe estar completamente limpio: sin símbolos, letras, números, runas, marcas, medallones,
flechas, etiquetas ni relieves matemáticos.

**Negativos de estilo:** no panorama épico de puerto, no flota enorme, no ciudad costera
turística, no multitudes, no sci-fi duro, no pintura digital lisa, no render suavizado, no
piel/pelaje con aerógrafo, no bordes antialias suaves, no neón saturado, no anime/chibi, no
kawaii, no gatita bebé, no cabeza sobredimensionada, no ojos brillantes infantiles, no mascota
simplificada tipo sticker, no humanos realistas, no cambiar a KatIA por una gata totalmente
metálica.

**Regla dura:** cada prompt describe la SITUACIÓN, nunca la SOLUCIÓN. Ningún prompt muestra
el resultado numérico de un ejercicio ni una cantidad de carga organizada de forma que se
pueda contar y resolver el ejercicio mirando la imagen.

---

## C00 — Hub: El Puerto de la Polis

**Header de nivel** (`.level-presentation-header` + `.level-presentation-media`, ancho
completo, 16:9) — de `welcome_text`/`scene_text`: "aquí llegan y zarpan los barcos... hacia
Atenas, Corinto, Delos, Mileto, Rodas y Esparta... el puerto tiene seis muelles."

> Encuadre de presentación contenido desde un puesto de control del muelle, no panorama
> turístico: KatIA en primer/medio plano con un catalejo en la pata, junto a una mesa de
> madera con pergaminos de ruta, tablillas de cera y un astrolabio de bronce. Detrás se
> sugieren seis muelles de madera y piedra en profundidad, con algunos barcos de vela
> atracados y postes con tablillas de ruta indicando destinos distintos (nombres de ciudades,
> sin números). Faroles de aceite iluminan el muelle al anochecer.
> Estilo base + aspect ratio 16:9.

**Icebreaker ICE1** (multi_select, cuadrado ~1:1) — de `icebreaker.items.ICE1.prompt`: "Un
mercader tiene 12 naranjas y quiere repartirlas en partes iguales."

> Un mercader en el muelle junto a una cesta de naranjas frescas, con varias cestas vacías
> más pequeñas dispuestas en semicírculo frente a él como opciones de reparto, sin que
> ninguna cesta tenga ya naranjas repartidas dentro — solo la cesta original llena y las
> vacías esperando.
> Estilo base + aspect ratio 1:1.

**Icebreaker ICE2** (single_select, cuadrado ~1:1) — de `icebreaker.items.ICE2.story` +
`support_objects`: "5 postes de madera con tablillas numeradas 2, 3, 5, 7, 11" y "una cuerda
de medir intentando marcar tramos iguales en cada poste".

> Cinco postes de madera clavados en el muelle, cada uno con una tablilla de ruta grabada
> con un número distinto (2, 3, 5, 7, 11 — visibles como números, ya que son el dato del
> ejercicio, no la solución), y un escriba portuario con una cuerda de medir intentando
> marcar tramos iguales en uno de los postes, con expresión de dificultad. La cuerda no debe
> mostrarse ya dividida en tramos exitosos en ningún poste.
> Estilo base + aspect ratio 1:1.

**Icebreaker ICE3** (numeric, cuadrado ~1:1) — de `icebreaker.items.ICE3.prompt`: "Cada
carreta nueva que llega al puerto trae 4 rollos de tela más que la anterior."

> Una fila de carretas llegando al puerto por un camino empedrado, cada carreta con una
> cantidad de rollos de tela visiblemente creciente respecto a la anterior (progresión
> visual, no exacta/contable), la última carreta aún entrando por el borde de la imagen sin
> mostrar su carga completa.
> Estilo base + aspect ratio 1:1.

---

## C01 — Divisibilidad: la regla del reparto exacto

**KatiaStorySlot** (columna imagen | copy, ~4:3) — de `katia.body`: "un escriba portuario
reparte la carga de un barco... entre las carretas que esperan en el muelle... si el reparto
no cae exacto, alguna carreta se queda esperando o algo sobra."

> Un escriba portuario junto a un barco recién atracado, repartiendo sacos de carga hacia
> varias carretas alineadas en el muelle, con algunos sacos todavía apilados sobre las
> piedras del muelle sin asignar a ninguna carreta — sugiriendo la posibilidad de un
> sobrante, sin mostrar si el reparto termina exacto o no.
> Estilo base + aspect ratio 4:3.

**Ejemplo 1 · Reparto exacto — "Canicas entre amigos"** (cuadrado ~1:1) — de `statement`:
"36 canicas se reparten en partes iguales entre 4 amigos."

> Cuatro niños sentados en círculo sobre el muelle, cada uno con un pequeño saquito de tela
> vacío frente a él, y un saco más grande de canicas de vidrio de colores en el centro del
> círculo del que aún no se ha repartido nada.
> Estilo base + aspect ratio 1:1.

**Ejemplo 2 · Reparto con residuo — "Entradas de una feria"** (cuadrado ~1:1) — de
`statement`: "23 entradas de feria se reparten en partes iguales entre 5 amigos."

> Cinco jóvenes en fila frente a un puesto de entradas de feria en el muelle, un vendedor
> sosteniendo un mazo de tablillas-entrada de cerámica, con una o dos tablillas sueltas
> ligeramente apartadas del mazo principal (sugiriendo un posible sobrante) sin que se
> puedan contar con precisión.
> Estilo base + aspect ratio 1:1.

---

## C02 — Múltiplos: los números que se forman al repetir

**KatiaStorySlot** (columna imagen | copy, ~4:3) — de `katia.body`: "Un barco zarpa hacia
Rodas cada cierta cantidad de días. Si zarpó hoy, ¿en qué otros días futuros volverá a
zarpar?"

> Un barco de vela zarpando del muelle hacia el horizonte con rumbo a Rodas (tablilla de
> ruta visible en el muelle), y en primer plano un calendario circular de piedra tallado con
> marcas regulares sin números escritos, sugiriendo un ciclo de zarpes repetido.
> Estilo base + aspect ratio 4:3.

**Ejemplo 2 — "El corredor completo"** (cuadrado ~1:1) — de `statement`: "Un corredor avanza
4 km cada hora. ¿Qué distancia lleva recorrida tras 2, 3, 4, 6 y 9 horas?"

> Un mensajero corriendo por un camino costero junto al puerto que se aleja hacia el
> horizonte, con postes miliarios de piedra espaciados regularmente a lo largo del camino
> (sin números grabados) marcando el ritmo de su avance, el corredor a medio camino entre
> dos postes.
> Estilo base + aspect ratio 1:1.

---

## C03 — Números primos: los indivisibles

**KatiaStorySlot** (columna imagen | copy, ~4:3) — de `katia.body`: "Algunas pequeñas polis
solo tienen una ruta directa: hacia el puerto central y ninguna otra."

> Un mapa de navegación de bronce y pergamino desplegado sobre una mesa del muelle, mostrando
> varias islas pequeñas conectadas al puerto central por una sola línea de ruta cada una
> (sin rutas cruzadas entre ellas), mientras otras islas más grandes muestran múltiples
> líneas de ruta entrecruzadas. KatIA señala una de las islas de ruta única con una pata.
> Estilo base + aspect ratio 4:3.

**Ejemplo 1 — "Contar divisores"** (cuadrado ~1:1) — de `statement`: "El 11 tiene divisores 1
y 11 únicamente."

> Un poste de ruta solitario en el muelle con una única tablilla colgando, y una cuerda
> tendida directamente desde ese poste hacia un solo destino en el horizonte, sin
> ramificaciones ni postes intermedios.
> Estilo base + aspect ratio 1:1.

**Ejemplo 2 — "Un compuesto con más vecinos"** (cuadrado ~1:1) — de `statement`: "El 18 tiene
más de dos divisores: no es primo."

> Un poste de ruta en el muelle con múltiples cuerdas tendidas hacia varios destinos
> distintos en el horizonte, ramificándose desde el mismo punto, en clara diferencia visual
> con la escena de ruta única del Ejemplo 1.
> Estilo base + aspect ratio 1:1.

---

## C04 — Factorización prima: los bloques de construcción

**KatiaStorySlot** (columna imagen | copy, ~4:3) — de `katia.body`: "Antes de guardar la
carga en el almacén, conviene desmontar un cargamento grande en sus unidades más pequeñas
indivisibles."

> Un mozo de muelle desmontando un cajón de carga grande, sacando de su interior cajas cada
> vez más pequeñas anidadas unas dentro de otras (como muñecas rusas de embalaje), con las
> más pequeñas ya alineadas a un lado listas para el almacén. KatIA supervisa con una
> tablilla de inventario en la pata.
> Estilo base + aspect ratio 4:3.

**Ejemplo 1 — "División sucesiva"** (cuadrado ~1:1) — de `statement`: "Descompón 84
dividiendo entre primos hasta llegar a 1."

> Una serie de cajones de carga de tamaño decreciente dispuestos en escalera descendente
> sobre el muelle, cada uno abierto mostrando el siguiente cajón más pequeño en su interior,
> el último aún cerrado sin revelar cuántas veces se repitió el proceso.
> Estilo base + aspect ratio 1:1.

**Ejemplo 2 — "Una cadena más larga"** (cuadrado ~1:1) — de `statement`: "Descompón 72
dividiendo entre primos hasta llegar a 1."

> Una cadena similar de cajones anidados, más larga que la del Ejemplo 1, extendiéndose a lo
> largo del muelle en perspectiva hasta perderse hacia el fondo, sin que se puedan contar
> todos los cajones de la fila.
> Estilo base + aspect ratio 1:1.

---

## C05 — Máximo común divisor: el mayor reparto en común

**KatiaStorySlot** (columna imagen | copy, ~4:3) — de `katia.body`: "Dos cargamentos de
tamaños distintos deben repartirse en contenedores del mismo tamaño, sin que sobre nada en
ninguno."

> Dos pilas de cargamento de tamaños claramente distintos sobre el muelle (una de sacos de
> trigo, otra de ánforas de aceite), y junto a ellas una selección de contenedores vacíos de
> varios tamaños posibles dispuestos en fila, como si se estuviera evaluando cuál contenedor
> serviría para ambas pilas sin sobrante. Ningún contenedor debe mostrarse ya lleno.
> Estilo base + aspect ratio 4:3.

**Ejemplo 1 · Factorización prima — "MCD por factores comunes"** (cuadrado ~1:1) — de
`statement`: "Halla el MCD de 225 y 180 descomponiendo ambos a la vez."

> Dos pilas de cajas de carga de distinto tamaño sobre el muelle, cada una con una etiqueta
> de ruta distinta, y entre ambas una balanza de comparación de bronce con el fiel apuntando
> hacia el centro, sin marcar ningún valor de referencia.
> Estilo base + aspect ratio 1:1.

---

## C06 — Mínimo común múltiplo: el primer encuentro común

**KatiaStorySlot** (columna imagen | copy, ~4:3) — de `katia.body`: "Un barco zarpa hacia
Rodas cada 4 días y otro hacia Esparta cada 6 días. Ambos zarparon hoy juntos."

> Dos barcos de vela distintos zarpando juntos del mismo muelle al mismo tiempo, uno con
> rumbo marcado hacia Rodas y otro hacia Esparta (tablillas de ruta visibles), alejándose en
> direcciones ligeramente distintas sobre el mar, con un calendario circular de piedra en
> primer plano marcando el día de partida conjunta sin más fechas señaladas.
> Estilo base + aspect ratio 4:3.

**Ejemplo 1 · Factorización prima — "MCM por factores"** (cuadrado ~1:1) — de `statement`:
"Halla el MCM de 20 y 30."

> Dos calendarios circulares de piedra superpuestos parcialmente en transparencia, cada uno
> con su propio ritmo de marcas de zarpe (diferente espaciado entre marcas), sugiriendo la
> búsqueda de un punto donde ambos ciclos coincidan, sin señalar cuál marca es la coincidencia.
> Estilo base + aspect ratio 1:1.
