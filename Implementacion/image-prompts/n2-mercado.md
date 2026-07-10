# Prompts de imagen — N2 · El Mercado

Fase 7 del plan de guión unificado (`~/.claude/plans/effervescent-scribbling-goblet.md`).
Vocabulario visual del espacio (Fase 0 / skill `prealgebra-narrative-style`): puestos,
mercaderes, telas, cerámica, especias, cestas, balanzas de mano. Toque retrofuturista
permitido: ábaco o balanza con detalle mecánico puntual. Cero vocabulario de ágora
(columnas/plaza pública como espacio propio de N1 — las columnas de fondo del mercado son
arquitectura circundante, no el foco de la escena).

**Línea gráfica obligatoria (`frontend/public/prealgebra/`):** usar como referencia directa
`step-naturales.png`, `step-enteros.png`, `step-racionales.png`, `step-reales.png`,
`escalera-conjuntos.png`, `katia-primer-plano-enteros.png` y `caso-enteros-recta.jpg`.
Antes de generar, abrir/adjuntar esas imágenes como referencias visuales si la herramienta lo
permite; si no, copiar completa esta línea gráfica dentro del prompt final.

**Estilo base:** `pixel-art educativo refinado, estilo 16/32-bit narrativo de alta calidad,
con clusters de píxeles visibles, bordes pixelados limpios, sombreado por bloques y dithering
sutil; NO pintura digital hiperrealista. Mantener el lenguaje visual de los assets existentes:
KatIA legible en primer/medio plano, escena contenida, pocos personajes secundarios, objetos
pedagógicos claros sobre mostrador/mesa/suelo, sombras azul noche, luz dorada de lámpara,
mármol o piedra cálida, acentos teal pequeños en el ocular de KatIA y en instrumentos
mecánicos. KatIA debe conservar identidad: gata blanca con mancha naranja/negra en la cabeza,
ojo verde visible, ocular mecánico teal, pata/brazo mecánico, túnica morada y ornamentos
dorados. El espacio debe leerse como mercado griego compacto: puestos, telas, cerámica,
especias, cestas y balanzas de mano; si aparece arquitectura de fondo, es secundaria.`

**Personajes secundarios:** cualquier rol humano mencionado en los prompts (mercader,
albañil, ayudante, cliente, aprendiz, vendedor, etc.) debe representarse como animal
antropomórfico. Preferencia: otros gatos bípedos con túnicas o delantales griegos, pelajes
variados (atigrado, negro, gris, calicó, siamés, naranja, blanco moteado) y texturas de
pelaje diferenciadas. No humanos realistas.

**Escaleras y peldaños:** si aparece una escalera, escalinata o peldaño en cualquier imagen,
debe estar completamente limpio: sin símbolos, letras, números, runas, marcas, medallones,
flechas, etiquetas ni relieves matemáticos.

**Negativos de estilo:** no panorámica turística, no plaza pública de ágora como foco, no
multitudes, no mercado medieval genérico, no pintura digital lisa, no neón saturado, no
sci-fi duro, no anime/chibi, no humanos realistas, no cambiar a KatIA por una gata totalmente
metálica.

**Regla dura:** cada prompt describe la SITUACIÓN, nunca la SOLUCIÓN. Ningún prompt muestra
el resultado numérico de un ejercicio, ni una cantidad de objetos organizada de forma que se
pueda contar y resolver el ejercicio mirando la imagen.

---

## E00 — Hub: La Ciudad de las Operaciones Básicas

**Header de nivel** (`.level-presentation-header` + `.level-presentation-media`, ancho
completo, 16:9) — de `welcome_text`/`scene_text`: "La ciudad tiene seis edificios... desde
los naturales hasta los números reales".

> Encuadre de presentación contenido de un mercado griego compacto al atardecer, no una
> plaza panorámica: KatIA en primer/medio plano junto a un mostrador de piedra con pergaminos
> y una balanza de mano; detrás se ven seis puestos de madera y tela sugeridos en profundidad,
> cada uno con un símbolo de operación tallado en un cartel pequeño (+, −, ×, ÷, un exponente
> genérico "aⁿ", una raíz "√" — sin ecuaciones completas). Mercaderes montando puestos con
> cestas, telas enrolladas y cerámica, pocos y desenfocados. KatIA señala hacia los puestos
> como invitando a recorrerlos.
> Estilo base + aspect ratio 16:9.

**Icebreaker ICE1** (numeric, cuadrado ~1:1) — de `icebreaker.items.ICE1.prompt`: "Un
albañil apila 3 filas de ladrillos: la primera con 4 ladrillos, la segunda con 4 más, la
tercera con 4 más."

> Un albañil en el borde de la plaza del mercado apilando ladrillos de barro en filas
> horizontales, con la primera fila ya asentada y la segunda a medio colocar, mortero fresco
> visible entre algunos ladrillos. Ángulo lateral que muestre las filas sin que se puedan
> contar con precisión los ladrillos de cada una (foco en el gesto de apilar, filas
> parcialmente ocultas por sombra o por el propio cuerpo del albañil).
> Estilo base + aspect ratio 1:1.

**Icebreaker ICE2** (single_select, cuadrado ~1:1) — de `icebreaker.items.ICE2.story` +
`support_objects`: "3 pilas de 5 tejas cada una" y "1 montón suelto de 15 tejas".

> En la obra junto al mercado, un albañil junto a tres pilas ordenadas de tejas de barro, y
> a un lado un ayudante junto a un montón grande de tejas sueltas y desordenadas. Ambos
> grupos de tejas deben lucir de tamaño visualmente similar en total, sin que ninguna
> disposición sugiera con claridad cuál cantidad es mayor — la comparación es conceptual
> (agrupado vs. suelto), no de volumen aparente.
> Estilo base + aspect ratio 1:1.

**Icebreaker ICE3** (numeric, cuadrado ~1:1) — de `icebreaker.items.ICE3.prompt`: "Al abrir
la plaza hay 20 puestos vacíos. Durante la mañana llegan comerciantes y ocupan 14."

> Vista aérea esquemática de una hilera de puestos de mercado vacíos con toldos plegados, y
> mercaderes llegando por un lado con sus carretas para ocupar algunos de ellos, montando
> toldos de colores. La escena debe capturar el momento de "llegando", no el resultado
> final: algunos puestos ya con toldo, muchos aún vacíos, sin que se puedan contar con
> precisión cuántos de cada tipo.
> Estilo base + aspect ratio 1:1.

---

## E01 — Suma: la máquina de juntar

**KatiaStorySlot** (columna imagen | copy, ~4:3) — de `katia.body`: "KatIA ordena rollos de
tela y monedas de plata sobre el mostrador de su puesto."

> KatIA detrás del mostrador de su puesto de mercado, con rollos de tela apilados a un lado
> y un pequeño montón de monedas de plata al otro, acomodando ambos grupos con las patas
> como preparándose para juntarlos. Toldo de tela violeta sobre el puesto, otros puestos
> desenfocados al fondo.
> Estilo base + aspect ratio 4:3.

**Ejemplo 1 · Naturales — "Higos reunidos"** (cuadrado ~1:1) — de `statement`: "3 higos de
una cesta y 5 de otra."

> Dos cestas de mimbre distintas sobre el mostrador de un puesto de mercado, cada una con
> higos frescos adentro, una mano (de un mercader fuera de cuadro) acercando las dos cestas
> entre sí como a punto de juntarlas. No mostrar los higos ya combinados en una sola cesta
> ni un total visible.
> Estilo base + aspect ratio 1:1.

**Ejemplo 2 · Enteros — "Deuda y pago"** (cuadrado ~1:1) — de `statement`: "KatIA registra
una deuda de 3 monedas y luego entran 5 monedas."

> KatIA junto a una pequeña balanza de mano de bronce sobre el mostrador, con una tablilla
> de cuentas al lado marcada con una única muesca en el lado "debe" (sin número visible), y
> una bolsa de monedas de plata entrando en escena desde un lado sostenida por un cliente.
> El fiel de la balanza debe estar inclinado, sin marcar el resultado final del ajuste.
> Estilo base + aspect ratio 1:1.

---

## E02 — Resta: la máquina de quitar o comparar

**KatiaStorySlot** (columna imagen | copy, ~4:3) — de `katia.body`: "KatIA cuenta dracmas
sobre el mostrador de su puesto."

> KatIA detrás de su mostrador contando dracmas de un pequeño montón, con la pata retirando
> algunas monedas hacia un lado como apartándolas, expresión concentrada. Balanza de mano
> colgada de un gancho del puesto al fondo.
> Estilo base + aspect ratio 4:3.

**Ejemplo 1 · Naturales — "Quitar sin cruzar cero"** (cuadrado ~1:1) — de `statement`: "8
piezas de cerámica en el puesto; KatIA vende 3."

> Un estante de puesto de mercado con piezas de cerámica pintada (vasijas pequeñas y tazones)
> ordenadas, y KatIA entregando algunas de ellas envueltas en tela a un cliente que se aleja
> con ellas en brazos. El estante debe verse parcialmente ocupado, sin que la cantidad
> restante sea fácil de contar con precisión.
> Estilo base + aspect ratio 1:1.

**Ejemplo 2 · Enteros — "Restar más de lo que hay"** (cuadrado ~1:1) — de `statement`:
"KatIA tiene 3 dracmas y debe pagar 5."

> KatIA con un pequeño montón de dracmas frente a ella sobre el mostrador y, junto a una
> tablilla de cuentas, la silueta de una obligación de pago mayor sugerida por una segunda
> pila de fichas de arcilla (representando lo que debe) más alta que el montón de monedas
> reales que tiene. Sin marcar el saldo final.
> Estilo base + aspect ratio 1:1.

---

## E03 — Multiplicación: la máquina de agrupar

**KatiaStorySlot** (columna imagen | copy, ~4:3) — de `katia.body`: "KatIA organiza filas de
tinajas de cerámica junto a su puesto."

> KatIA junto a su puesto de mercado organizando tinajas de cerámica en filas ordenadas
> sobre el suelo de tierra compactada, colocando una tinaja más mientras mira la disposición
> de las filas ya existentes con aire evaluador.
> Estilo base + aspect ratio 4:3.

**Ejemplo 1 · Naturales — "Filas de tinajas"** (cuadrado ~1:1) — de `statement`: "3 filas con
4 tinajas cada una."

> Varias filas idénticas de tinajas de cerámica alineadas frente a un puesto de mercado,
> vistas en perspectiva ligeramente elevada, con las filas parcialmente ocultas entre sí por
> la perspectiva para que no se puedan contar con precisión todas las tinajas de un vistazo.
> Estilo base + aspect ratio 1:1.

**Ejemplo 2 · Enteros — "Deuda repetida"** (cuadrado ~1:1) — de `statement`: "Una deuda de 3
dracmas se repite 4 veces."

> Una fila de fichas de arcilla idénticas sobre una tablilla de cuentas, cada ficha marcando
> una obligación de pago pendiente idéntica a las demás (sin número inscrito), con KatIA
> señalando la fila con una pata como contando "otra vez, y otra vez".
> Estilo base + aspect ratio 1:1.

---

## E04 — División: la máquina de repartir

**KatiaStorySlot** (columna imagen | copy, ~4:3) — de `katia.body`: "En su puesto del
mercado, KatIA reparte una cesta de aceitunas en partes iguales entre sus aprendices."

> KatIA de pie junto a una cesta grande de aceitunas, repartiendo puñados en cestas más
> pequeñas frente a un grupo de aprendices jóvenes (con delantales simples, no togas de
> ágora) que esperan en fila con las manos extendidas. Gesto de reparto en proceso, no
> terminado.
> Estilo base + aspect ratio 4:3.

**Ejemplo 1 · Naturales — "Reparto exacto"** (cuadrado ~1:1) — de `statement`: "12 aceitunas
entre 4 aprendices."

> Cuatro cestitas pequeñas idénticas dispuestas en semicírculo frente a KatIA, quien tiene
> en las patas una cesta más grande de aceitunas de la que está a punto de repartir un
> puñado hacia la primera cestita. Ninguna cestita debe mostrarse ya con su contenido final.
> Estilo base + aspect ratio 1:1.

**Ejemplo 2 · Naturales — "Reparto con residuo"** (cuadrado ~1:1) — de `statement`: "27
higos entre 6 aprendices."

> Seis cestitas idénticas en fila y una cesta grande de higos frescos junto a KatIA, con
> algunos higos sueltos visibles fuera de las cestitas sobre la mesa (sugiriendo que el
> reparto no será perfectamente parejo) sin mostrar cuántos quedan sueltos con precisión
> contable.
> Estilo base + aspect ratio 1:1.

---

## E05 — Potenciación: la máquina de crecer

**KatiaStorySlot** (columna imagen | copy, ~4:3) — de `katia.body`: "KatIA apila sacos de
grano junto a su puesto: cada nivel duplica lo que había en el nivel anterior."

> KatIA junto a una pila de sacos de grano de arpillera que crece en altura de forma
> visiblemente irregular hacia arriba (los niveles superiores considerablemente más anchos
> que los inferiores, sugiriendo crecimiento acelerado sin mostrar el conteo exacto de sacos
> por nivel), mirando hacia arriba de la pila con asombro.
> Estilo base + aspect ratio 4:3.

**Ejemplo 1 · Exponente natural — "Crecimiento por niveles"** (cuadrado ~1:1) — de
`statement`: "Una pila de sacos de grano duplica su tamaño durante 3 niveles."

> Vista lateral de una pila de sacos de grano organizada en niveles horizontales
> superpuestos, cada nivel visiblemente más ancho que el anterior, con difuminado o
> perspectiva que impida contar con exactitud cuántos sacos hay en cada nivel.
> Estilo base + aspect ratio 1:1.

**Ejemplo 2 · Exponente entero negativo — "Bajar niveles invierte"** (cuadrado ~1:1) — de
`statement`: "KatIA eleva 2 a −2."

> KatIA junto a la misma pila de sacos de grano, pero esta vez señalando hacia abajo, hacia
> una sección de la pila que se estrecha progresivamente en niveles por debajo del suelo
> (un pozo o depósito subterráneo visible en corte), sugiriendo un "invertir" el crecimiento
> sin mostrar cifras.
> Estilo base + aspect ratio 1:1.

---

## E06 — Radicación: la máquina de encontrar raíces

**KatiaStorySlot** (columna imagen | copy, ~4:3) — de `katia.body`: "KatIA embaldosa el
suelo de su puesto con losas cuadradas."

> KatIA arrodillada colocando losas de piedra cuadradas en el suelo de su puesto de
> mercado, con una losa a medio encajar en las manos, algunas losas ya puestas formando un
> patrón parcial y otras aún apiladas a un lado sin colocar.
> Estilo base + aspect ratio 4:3.

**Ejemplo 1 · Naturales — "Cuadrado perfecto"** (cuadrado ~1:1) — de `statement`: "Un puesto
cuadrado del mercado tiene área 16."

> El suelo cuadrado de un puesto de mercado visto desde arriba, parcialmente embaldosado
> con losas cuadradas idénticas dispuestas en cuadrícula regular, con el patrón cortado por
> el encuadre de la imagen de forma que no se puedan contar todas las losas del lado.
> Estilo base + aspect ratio 1:1.

**Ejemplo 2 · Enteros — "No toda raíz es entera"** (cuadrado ~1:1) — de `statement`: "KatIA
calcula la raíz cuadrada de 2."

> KatIA con una cuerda de medir tensada en diagonal sobre una sola losa cuadrada del suelo
> de su puesto, mirando la cuerda con expresión de sorpresa porque la medida no coincide con
> ninguna marca entera de la cuerda.
> Estilo base + aspect ratio 1:1.
