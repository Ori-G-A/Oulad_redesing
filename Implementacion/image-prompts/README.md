# Prompts de imagen — índice

Todos los prompts de generación de imágenes de la plataforma, **numerados por orden de
aparición en la ruta del estudiante**. El número del prompt coincide con el número de la
carpeta de arte en `frontend/public/leccion/`.

| # | Nivel | Prompt | Arte servido | Hechas | Faltan |
|---|---|---|---|---:|---:|
| 00 | — (estilo global) | [00-estilo-base.md](00-estilo-base.md) | `leccion/00-comunes/` | 6 | 0 |
| 01 | PREALG-N1 · El ágora | [01-prealg-n1-agora.md](01-prealg-n1-agora.md) | `leccion/01-prealg-n1-agora/` | 13 | 0 |
| 02 | PREALG-N2 · La ciudad de las operaciones | [02-prealg-n2-ciudad.md](02-prealg-n2-ciudad.md) | `leccion/02-prealg-n2-mercado/` | 15 | **15 a regenerar** |
| 03 | PREALG-N3 · La fábrica de propiedades | [03-prealg-n3-fabrica.md](03-prealg-n3-fabrica.md) | `leccion/03-prealg-n3-fabrica/` | 11 | 0 |
| 04 | PREALG-N4 · El puerto de la polis | [04-prealg-n4-puerto.md](04-prealg-n4-puerto.md) | `leccion/04-prealg-n4-puerto/` | 10 | 0 |
| 05 | ALG-N1 · El papiro de las cuatro casas (Kemet) | [05-alg-n1-kemet.md](05-alg-n1-kemet.md) · [pegable](05-alg-n1-kemet-PEGABLE.md) | `leccion/05-alg-n1-kemet/` | 0 | **17** (+16 opcionales) |
| 06 | ALG-N2 · La sala de los troqueles (Bagdad) | [06-alg-n2-n3-bagdad.md](06-alg-n2-n3-bagdad.md) | `leccion/06-alg-n2-troqueles/` | 0 | **5** (hub + 4 salas, +4 opcionales) |
| 06 | ALG-N3 · El almacén de la caravana (Bagdad) | [06-alg-n2-n3-bagdad.md](06-alg-n2-n3-bagdad.md) | `leccion/07-alg-n3-caravana/` | 0 | **5** (+5 opcionales) |

**Total pendiente: 27 imágenes obligatorias** (+25 opcionales de trampa).

Los dos niveles de Bagdad **comparten hub** (`ALG-S00-CASA-DE-LA-SABIDURIA`): su header
vive con los troqueles, en `leccion/06-alg-n2-troqueles/s00-hub-patio-katia.png`.

## Deudas conocidas

- **N2 arrastra el arte equivocado.** Las 15 imágenes de `02-prealg-n2-mercado/` son puestos
  de mercado; V2-R12 cambió el nivel a **seis edificios con nombre propio** (El Granero
  Público, La Casa de Cuentas, El Taller de Mosaicos, El Comedor Comunal, El Invernadero, La
  Cantera). El prompt ya está reescrito; el arte no. La carpeta conserva el nombre `mercado`
  a propósito, para que la deuda se vea.
- **El hub de Kemet 404ea.** `05-alg-n1-kemet/a00-hub-papiro-katia.png` está referenciado en
  `a00_hub.py` y no existe todavía. Es la única referencia rota que queda en el código.
- El hub de N4 apuntaba a `c00-hub-puerto-katia-canon-v10.png`, una composición que nunca se
  guardó; ahora apunta a `c00-hub-puerto-v4.png`, que sí existe. Si aparece la v10, se
  cambia la referencia en `prealgebra.py` y en `LevelFourLesson.tsx`.

## Qué hay en cada carpeta

- **`referencias/`** — las imágenes que los prompts citan como referencia de identidad y de
  estilo (`katia-primer-plano-enteros.png`, los sprites canónicos, `caso-enteros-recta.jpg`).
  La app no las sirve: son material de generación. Adjuntarlas a la herramienta antes de
  generar.
- **`correcciones/`** — las hojas de corrección por imagen. Estaban dentro de
  `frontend/public/`, o sea publicadas en la web; ahora no se sirven.
- **`_gen_kemet_prompts.py`** — genera `05-alg-n1-kemet-PEGABLE.md` a partir de
  `05-alg-n1-kemet.md`, inlineando el bloque de estilo en cada prompt. Solo Kemet lo necesita
  (33 imágenes); los demás niveles llevan el estilo declarado una vez.

## Dónde está lo demás

- **Arte que sirve la plataforma:** `frontend/public/leccion/NN-<nivel>/`, misma numeración.
- **Descartes:** `arte/descartes/` — versiones superadas, fondos sin KatIA del método de
  composición de N4, y el juego `amarillas/` de N1. Fuera de `public/`, así que ya no se
  suben en el build.
