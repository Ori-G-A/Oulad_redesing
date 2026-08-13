# Prompts de imagen — ALG-N1 · El Papiro de las Cuatro Casas (Kemet)

**No existe ni un PNG de Egipto en `frontend/public/`.** Los 16 nodos renderizan el marcador
«Imagen de KatIA aquí» y el hub apunta a un archivo que todavía no está. Este documento
cubre las **17 imágenes obligatorias** (1 header de hub + 16 aperturas de KatIA) y deja
listadas las **16 opcionales** de las trampas.

Destino: `frontend/public/algebra/generated/n1-kemet/`. Los nombres de archivo de este
documento son los definitivos — el hub ya declara `a00-hub-papiro-katia.png`.

---

## Continuidad con Preálgebra

Es el mismo mundo y la misma KatIA, en otro sitio. Preálgebra transcurre en Grecia (ágora,
ciudad, fábrica, puerto); aquí KatIA ha remontado el río hasta **Kemet**. La línea gráfica
NO cambia: cambia la arquitectura, la luz y los materiales.

**Línea gráfica obligatoria (`frontend/public/prealgebra/`):** usar como referencia directa
`step-naturales.png`, `step-enteros.png`, `escalera-conjuntos.png`,
`katia-primer-plano-enteros.png` y `caso-enteros-recta.jpg`. Antes de generar, adjuntarlas
como referencias visuales si la herramienta lo permite; si no, copiar completa la línea
gráfica dentro del prompt final.

**Estilo base (copiar tal cual en cada prompt):**

`pixel-art educativo refinado, estilo 16/32-bit narrativo de alta calidad, con clusters de
píxeles visibles, bordes pixelados limpios, sombreado por bloques y dithering sutil; NO
pintura digital hiperrealista. Mantener el lenguaje visual de los assets existentes: KatIA
legible en primer/medio plano, escena contenida, pocos personajes secundarios, objetos
pedagógicos claros sobre mesa/suelo/banco de trabajo, sombras azul noche, luz cálida de
lámpara de aceite, piedra caliza y adobe, acentos teal pequeños en el ocular de KatIA y en
instrumentos mecánicos. KatIA conserva identidad: gata blanca con mancha naranja/negra en la
cabeza, ojo verde visible, ocular mecánico teal, pata/brazo mecánico, túnica morada y
ornamentos dorados. El espacio debe leerse como el INTERIOR de un recinto del Antiguo Egipto
—muros de adobe encalado, columnas papiriformes, dinteles de piedra, esteras, tinajas— con
la arquitectura de fondo siempre secundaria.`

**KatIA es forastera aquí.** Sigue siendo la gata griega: túnica morada, ornamentos dorados,
ocular teal. No se la viste de egipcia ni se le pone tocado nemes. Es la única figura del
cuadro que no pertenece al sitio, y eso debe notarse un poco.

**Personajes secundarios:** todo rol mencionado (escriba, capataz, tintorero, batihoja,
aguador, aprendiz) es **animal antropomórfico**, preferentemente gatos bípedos con faldellín
de lino, delantal o collar ancho egipcio; pelajes variados (atigrado, negro, gris, calicó,
siamés, naranja, blanco moteado). Los cuatro guías tienen aspecto estable entre sus cuatro
salas:

| Guía | Casa | Aspecto |
|---|---|---|
| **Meritka** | La Casa de la Vida | gata negra esbelta, collar ancho de cuentas azules, cálamo tras la oreja |
| **Bakenra** | La obra de la pirámide | gato atigrado corpulento, faldellín corto de cuero, cuerda al hombro |
| **Tabiry** | Los campos tras la crecida | gata calicó, pies descalzos embarrados, sombrero de junco trenzado |
| **Iuty** | El taller del canon | gato gris de pelo corto, delantal manchado de pigmento, plomada al cinto |

**Escaleras y peldaños:** si aparece una escalera o peldaño, va completamente limpio: sin
símbolos, letras, números, runas, marcas, medallones, flechas ni relieves matemáticos.

**Jeroglíficos:** permitidos como textura ambiental en muros y columnas, **nunca legibles ni
protagonistas**, y nunca sobre la superficie donde ocurre la acción pedagógica (la tablilla,
el papiro de trabajo, la cuadrícula). Nada de cartuchos con el nombre del nodo.

**Negativos de estilo:** no panorámica turística, no pirámides al atardecer como postal, no
Esfinge, no faraón ni realeza, no momias ni tumbas, no dioses antropomórficos egipcios
(Anubis, Thot) — los animales antropomórficos de aquí son vecinos, no deidades —, no
multitudes, no pintura digital lisa, no neón saturado, no sci-fi duro, no anime/chibi, no
humanos realistas, no cambiar a KatIA por una gata totalmente metálica.

**Regla dura:** cada prompt describe la SITUACIÓN, nunca la SOLUCIÓN. Ninguna imagen muestra
el resultado numérico del ejercicio, ni una cantidad de objetos dispuesta de forma que se
pueda resolver el ejercicio contando en la imagen. Cuando el relato trata de un error ya
cometido, se muestra **la consecuencia** (madejas apagadas, era vacía, tinaja seca), nunca
la cuenta correcta.

**Paleta por casa** (dominante + acento; el morado de KatIA se mantiene en las cuatro):

| Casa | Dominante | Acento |
|---|---|---|
| La Casa de la Vida | turquesa y ocre | negro de tinta |
| La obra de la pirámide | arena y terracota | sombra azul fría |
| Los campos tras la crecida | verde fértil y limo | agua turquesa |
| El taller del canon | azul egipcio y cal | oro |

---

## A00 — Hub: El Papiro de las Cuatro Casas

`a00-hub-papiro-katia.png` · **16:9**, header de nivel (`.level-presentation-media`).

> Interior en penumbra de una sala de archivo del Antiguo Egipto al amanecer, vista
> contenida a media distancia. Sobre una mesa larga de madera, una gata negra esbelta con
> collar ancho de cuentas azules (Meritka) extiende un papiro grande y visiblemente dañado:
> le faltan cuatro secciones, cuatro huecos rasgados de bordes irregulares. Al otro lado de
> la mesa, KatIA —gata blanca con mancha naranja y negra, ojo verde, ocular mecánico teal,
> brazo mecánico, túnica morada con ornamentos dorados— acaba de llegar y aún lleva el
> polvo del viaje. Por el vano abierto del fondo se ven, muy secundarias y sin detalle,
> cuatro construcciones distintas contra el cielo: un recinto encalado, una rampa de obra,
> unos campos anegados y un taller con andamio. Luz baja de lámpara de aceite sobre la mesa,
> azul frío en el resto de la sala. Los huecos del papiro están vacíos: nada escrito en
> ellos, ninguna letra ni número legible en toda la imagen.

**Opcionales del hub** (1:1, mismo patrón que `e00-ice*` de N2): `a00-ice1-cestos.png`
(cestos de grano apilados junto a una balanza de suelo) · `a00-ice2-registro.png` (dos
tablillas de barro apoyadas contra un muro encalado) · `a00-ice3-hueco.png` (un papiro con
un espacio deliberadamente en blanco en mitad de una línea de anotaciones ilegibles).

---

## Casa I · La Casa de la Vida — Meritka · turquesa y ocre

### L01 · La sala de los cálamos
`l01-variables-katia.png` · **4:3**

> Interior de un escritorio de escribas: estantes de nichos con rollos, un cuenco de tinta
> negra, cálamos de caña en un vaso de cerámica. Meritka sostiene en alto un papiro
> desenrollado ante KatIA; en el papiro se ve una misma anotación breve repetida muchas
> veces en columnas, deliberadamente ilegible (trazos de tinta, no signos reconocibles).
> Al fondo, un cesto lleno de rollos idénticos esperando ser copiados. Luz turquesa de
> mañana entrando por una ventana alta; ocres cálidos en los estantes.

### L02 · El estante sellado
`l02-constantes-katia.png` · **4:3**

> Meritka descorre un sello de arcilla roto de la puertecilla de un estante bajo. Dentro,
> sobre una tela, tres objetos de medida patrón: una vara de madera, una cuerda con nudos
> regulares y un peso de piedra pulida con una marca grabada. KatIA se inclina para mirar
> sin tocar. El resto de la sala es de trabajo cotidiano y está desordenado; solo ese
> estante está limpio y aparte. Contraste entre el turquesa frío del nicho sellado y el
> ocre cálido de la sala.

### L03 · La mesa de dictado
`l03-traduccion-katia.png` · **4:3**

> Mesa baja de dictado. Un mensajero (gato siamés con sandalias de viaje, aún con el manto
> puesto) habla de pie y con prisa, una mano levantada. Sentados frente a él, dos escribas
> jóvenes escriben a la vez sobre dos tablillas distintas; las tablillas están giradas
> hacia el espectador lo justo para verse ocupadas, con trazos de tinta ilegibles y
> claramente DISTINTOS entre sí. Meritka observa de pie, sin intervenir. KatIA en primer
> plano, mirando de una tablilla a la otra. Nada legible en ninguna de las dos.

### L04 · La cámara del recuento
`l04-valor-numerico-katia.png` · **4:3**

> Cámara semisubterránea de recuento, techo bajo. Fichas de barro apiladas por columnas y
> un cordel de conteo con nudos colgado de la pared. Meritka sostiene una tablilla; a su
> lado, en el suelo, una fila de carros de mano de madera vacíos, muchos más de los
> necesarios, esperando carga que no llegó. KatIA mira los carros vacíos. Luz de lámpara
> de aceite rasante; polvo suspendido. No se ve grano, no se ve cifra alguna.

---

## Casa II · La obra de la pirámide — Bakenra · arena y terracota

### O01 · La rampa
`o01-semejantes-katia.png` · **4:3**

> Al pie de una rampa de obra de adobe, a media mañana. Bakenra, gato atigrado corpulento
> con faldellín de cuero y cuerda al hombro, sostiene dos tablillas de turno, una en cada
> mano, mirándolas alternativamente. Detrás, una cuadrilla de gatos obreros espera de pie
> junto a un trineo de madera cargado, sin avanzar. A un lado, cuerdas enrolladas; al otro,
> mazos y herramienta apilada — dos montones claramente separados. Polvo de arena en el
> aire, sombra azul fría bajo la rampa.

### O02 · El patio de aparejos
`o02-signos-katia.png` · **4:3**

> Patio cerrado de almacén de aparejos: poleas de madera colgadas de una viga, sogas
> enrolladas en el suelo, contrapesos de piedra alineados contra el muro. Bakenra sostiene
> una tablilla de vale de devolución. En el muro del fondo, una hilera de soportes de
> madera para contrapesos con varios huecos vacíos, evidentes. En el vano de salida, una
> cuadrilla se aleja con las manos vacías. KatIA en primer plano junto a las poleas. Luz
> dura de mediodía, sombras azules cortas.

### O03 · El taller de cinceles
`o03-producto-katia.png` · **4:3**

> Interior del taller de talla: banco largo con cinceles alineados por tamaño, piedras de
> afilar, virutas de piedra, plantillas de madera colgadas. Bakenra ha dejado una tablilla
> de pedido sobre el banco y mira por el vano hacia fuera, donde se ve —muy secundaria, sin
> detalle— una explanada de acopio prácticamente vacía con unos pocos sillares. KatIA
> examina un cincel. Ambiente terracota, polvo blanco de piedra, acento teal en el ocular.

### O04 · La caseta del capataz
`o04-cociente-katia.png` · **4:3**

> Caseta de obra pequeña y sombreada, con esteras y una ventana sin postigos. Sobre una
> repisa, el censo de la obra en tablillas. Bakenra señala una línea de una tablilla. Fuera,
> visto por la ventana, un grupo de aguadores de pie con sus cántaros al hombro, todavía
> llenos, sin repartir, mirando hacia la caseta. KatIA sigue el dedo de Bakenra. Calor de
> media tarde, arena y terracota, sombra profunda dentro de la caseta.

---

## Casa III · Los campos tras la crecida — Tabiry · verde fértil y limo

### F01 · La parcela partida
`f01-simplificar-katia.png` · **4:3**

> Campo recién drenado tras la crecida, barro brillante y brotes verdes. Tabiry, gata
> calicó con sombrero de junco y pies embarrados, sostiene una cuerda de agrimensor
> extendida sobre el terreno; los mojones de lindero están caídos o desaparecidos y el
> campo se ve como una sola extensión sin divisiones. Al fondo, un grupo pequeño de
> familias de gatos esperando de pie con sus enseres. KatIA junto a Tabiry, con las patas
> en el barro. Luz de mañana, verdes y ocres de limo, reflejos turquesa en los charcos.

### F02 · El canal madre
`f02-suma-katia.png` · **4:3**

> Junto a un canal principal de riego, con dos acequias que salen de él en direcciones
> distintas y un azud de tablones de madera. Tabiry se ha agachado y ha hundido una mano en
> el agua del canal. En la orilla, apoyada en una piedra, una tablilla de turnos de riego.
> Una de las dos acequias corre visiblemente más seca que la otra. KatIA de pie en el
> borde, mirando el agua. Verde fértil en las orillas, turquesa en el agua, cielo alto.

### F03 · La era de trilla
`f03-producto-katia.png` · **4:3**

> Era de trilla circular de tierra apisonada, con un trillo de madera apoyado en el borde y
> paja suelta arremolinada por el viento. La era está prácticamente vacía: apenas queda
> parva. Tabiry sostiene una tablilla y mira la era barrida. Al fondo, la puerta de una
> troje de adobe, abierta. KatIA junto al trillo. Luz de mediodía muy blanca, dorados de
> paja, sombra corta.

### F04 · El silo de simiente
`f04-division-katia.png` · **4:3**

> Interior de un silo de adobe de planta redonda, con la simiente formando un montón alto
> hasta media pared. Contra el muro, una pila de sacos de tela vacíos y doblados, sin
> llenar. Tabiry sostiene una tablilla de registro y señala el montón lleno con la otra
> mano. KatIA mira los sacos vacíos. Contraste claro entre la abundancia del montón y la
> pila de sacos sin usar. Luz que entra en haz por una tronera alta; verdes apagados y
> tonos tierra.

---

## Casa IV · El taller del canon — Iuty · azul egipcio y cal

### R01 · La cuadrícula del canon
`r01-razones-katia.png` · **4:3**

> Taller de pintores frente a un muro encalado con una cuadrícula de cuerda tensada. En una
> mesa, el boceto pequeño de un motivo; en el muro, la versión ampliada del mismo motivo,
> visiblemente deformada — estirada de un lado y achatada del otro. Iuty, gato gris con
> delantal manchado de pigmento y plomada al cinto, mira el muro con los brazos cruzados.
> KatIA compara el boceto con el muro. Azul egipcio y cal, andamio de madera secundario.

### R02 · El tinte de lino
`r02-regla-de-tres-katia.png` · **4:3**

> Sala del tinte: una tina grande de barro con el líquido oscuro y un banco con madejas de
> lino. Del techo cuelgan madejas puestas a secar; unas tienen color pleno y las últimas de
> la fila están claramente apagadas y desiguales. Iuty sostiene una tablilla con la receta.
> KatIA toca una de las madejas descoloridas. Vapor tenue sobre la tina, suelo húmedo,
> azules profundos y cal.

### R03 · El pan de oro
`r03-porcentajes-katia.png` · **4:3**

> Obrador del batihoja: mesa de piedra pulida, mazo pequeño, pilas de hojas finísimas de
> oro separadas por pergaminos, pinzas. Un batihoja (gato blanco moteado, manos protegidas
> con tela) se ha apartado de la mesa con las manos abiertas y vacías, en gesto de que no
> puede seguir. Iuty sostiene la tablilla del encargo. Sobre la mesa hay un hueco donde
> debería continuar la pila de hojas. KatIA mira el hueco. Dorados intensos y contenidos
> sobre azul egipcio; nada de brillo metálico exagerado.

### R04 · La sala de las lámparas
`r04-variacion-katia.png` · **4:3**

> Sala de trabajo nocturna del taller. Seis lámparas de aceite repartidas por la sala,
> todas apagadas menos una que se está consumiendo, con la mecha casi al final. En el
> centro, una tinaja grande de aceite volcada de lado y vacía. Iuty señala la tinaja. El
> friso del muro se ve a medio terminar, en penumbra. KatIA en el círculo de luz de la
> última llama. Escena predominantemente oscura, azul noche, un único foco cálido pequeño.

---

## Opcionales — las trampas (1:1)

Una por sala, para la tarjeta `trap` de `worked_examples`. Misma línea gráfica, encuadre
cerrado sobre el objeto, sin personajes o con uno solo. Prioridad: las cuatro marcadas con ★
son las que más ganan con imagen.

| Archivo | Qué se ve |
|---|---|
| `l01-trampa-etiqueta.png` | un cálamo apoyado sobre una anotación tachada y reescrita |
| `l02-trampa-pozo.png` ★ | el brocal circular de un pozo visto desde arriba, con una cuerda cruzándolo por el centro |
| `l03-trampa-tablillas.png` | dos tablillas idénticas de tamaño, apoyadas una junto a otra, con trazos distintos |
| `l04-trampa-carros.png` ★ | una fila larga de carros de mano vacíos, en perspectiva, junto a un montón de grano pequeño |
| `o01-trampa-monton.png` | dos montones separados: cuerdas a un lado, mazos al otro, con una raya trazada en la arena entre ellos |
| `o02-trampa-huecos.png` | soportes de contrapeso en un muro, la mitad ocupados y la mitad vacíos |
| `o03-trampa-acopio.png` ★ | una explanada de acopio de sillares vista a media distancia, casi vacía |
| `o04-trampa-cantaros.png` | cántaros llenos alineados y un cuenco de reparto boca abajo junto a ellos |
| `f01-trampa-mojon.png` | un mojón de lindero caído en el barro, medio hundido |
| `f02-trampa-acequias.png` | dos acequias que salen del mismo canal, una con agua y otra casi seca |
| `f03-trampa-era.png` | la era de trilla barrida, con la puerta de la troje abierta al fondo |
| `f04-trampa-sacos.png` ★ | un solo saco de tela vacío colgado de un clavo frente a un montón de simiente |
| `r01-trampa-boceto.png` | el boceto pequeño y su copia deformada, uno al lado del otro sobre la mesa |
| `r02-trampa-madejas.png` | una hilera de madejas colgadas, degradando de color pleno a descolorido |
| `r03-trampa-pila.png` | una pila de hojas de oro con un hueco visible donde debería continuar |
| `r04-trampa-lampara.png` | una sola lámpara de aceite con la mecha consumiéndose, fondo negro |

---

## Cuando lleguen los PNG

Los módulos de nodo todavía **no declaran** las rutas: hay que añadirlas a mano, una línea
por sala, dentro de `CONTENT["katia"]`:

```python
"katia": {
    "eyebrow": "...",
    "image": "/algebra/generated/n1-kemet/l01-variables-katia.png",
    ...
}
```

Y en la tarjeta de trampa de `worked_examples`, `"image_slot": True` más `"image": "..."`
(ver `nodes/e05_potenciacion.py` como referencia ya cableada).

El hub es la excepción: `a00_hub.py` ya declara su `image`, así que en cuanto el archivo
exista se ve solo. Hasta entonces esa ruta **da 404 en el navegador** — es el único asset
roto conocido del módulo.
