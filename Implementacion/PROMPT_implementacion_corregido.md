# Prompt de implementación corregido — Niveles 1 y 2

Usar este prompt al implementar o reimplementar nodos de Preálgebra Nivel 1
`B04–B13` y Nivel 2 `E00–E06`.

---

## Reglas críticas

### Regla 1: No interrumpas la narrativa con definiciones aisladas

Incorrecto:

```markdown
[Narrativa...]
[Bloque de definición aislado]
[Más narrativa...]
[Ejemplos...]
```

Correcto:

```markdown
[Apertura narrativa]
[Descubrimiento guiado]
[Definición integrada en la prosa]
[Ejemplos trabajados inmediatamente después]
[Cierre narrativo]
[Práctica interactiva]
```

La definición puede destacarse visualmente, pero no debe cortar el flujo ni
aparecer como un recuadro desconectado.

### Regla 2: Definición + ejemplos siempre antes de práctica

Orden obligatorio:

1. Apertura narrativa: por qué importa el concepto.
2. Descubrimiento guiado: ejemplos, contraste y contraejemplo.
3. Definición formal en KaTeX integrada en la narración.
4. Dos o tres ejemplos base con pasos.
5. Cierre narrativo con Katia.
6. Práctica interactiva.

No implementar:

- definición como primera pantalla sin contexto,
- ejemplos dispersos después de ejercicios,
- práctica antes de que el estudiante entienda el por qué,
- nodos sin Katia en la narrativa.

### Regla 3: Copiar A2 completo

A2 es la fuente de verdad del texto visible.

- No resumir.
- No comprimir por legibilidad.
- No mover práctica antes de los ejemplos base.
- No eliminar diálogos de Katia.
- Si A2 tiene menos de 350 líneas en Nivel 1, detenerse y pedir corrección.
- Si A2 tiene menos de 450 líneas en Nivel 2, detenerse y pedir corrección.

### Regla 4: Jerarquía visual

- La apertura narrativa debe sentirse como una escena.
- El descubrimiento guiado debe mostrar variación y contraste.
- La definición formal debe renderizar en KaTeX.
- Los ejemplos base deben ser numerados y mostrar pasos.
- La práctica debe iniciar después de una transición clara.
- Katia debe resumir el aprendizaje antes de pasar a la práctica o al cierre.

---

## Plantilla mínima de A2

```markdown
### A2. Guión de pantalla (texto íntegro por pantalla)

#### 2.1 Apertura narrativa

[3–5 párrafos con contexto, Katia y pregunta detonadora.]

---

#### 2.2 Descubrimiento guiado

[3–5 párrafos que muestren un patrón, un segundo ejemplo y un contraejemplo.]

---

#### 2.3 Definición formal integrada + ejemplos base

[Párrafo de entrada.]

$$\text{definición formal en KaTeX}$$

[Párrafo de lectura e interpretación.]

##### Ejemplo 1 (básico)

**Enunciado:**
[Problema simple.]

**Solución paso a paso:**
[Pasos visibles.]

##### Ejemplo 2 (intermedio)

**Enunciado:**
[Problema con una sutileza.]

**Solución paso a paso:**
[Pasos visibles.]

##### Ejemplo 3 (trampa común o caso límite)

[Opcional, pero recomendado si hay misconception frecuente.]

---

#### 2.4 Cierre narrativo

[Katia resume y conecta con lo siguiente.]

---

#### 2.5 Práctica interactiva

[S1, S2, S3... u O1, O2, O3...]
```

---

## Estructura técnica obligatoria en PARTE B

Cada nodo reparado debe exponer en JSON una sección equivalente a:

```json
{
  "type": "narrative_with_integrated_definition",
  "is_integrated": true,
  "sections": [
    {
      "type": "prose",
      "content_summary": "Apertura narrativa con Katia y pregunta detonadora"
    },
    {
      "type": "guided_discovery",
      "content_summary": "Ejemplos, variación y contraejemplo"
    },
    {
      "type": "definition_plus_examples",
      "definition_katex": "...",
      "is_integrated": true,
      "examples": [
        { "name": "Ejemplo 1 (básico)", "steps": [] },
        { "name": "Ejemplo 2 (intermedio)", "steps": [] }
      ]
    }
  ],
  "practice_position": "after_definition_plus_examples"
}
```

Si el JSON todavía tiene `definition_block` con
`position = "interrupts_narrative"`, debe corregirse antes de implementar UI.

---

## Checklist antes de entregar

- [ ] Katia aparece por nombre en la narrativa.
- [ ] Hay pregunta detonadora explícita.
- [ ] Hay descubrimiento guiado con contraste o contraejemplo.
- [ ] La definición formal está integrada y renderiza en KaTeX.
- [ ] Hay al menos 2 ejemplos con pasos antes de la práctica.
- [ ] La práctica aparece después de ejemplos base.
- [ ] A2 cumple longitud mínima.
- [ ] PARTE B refleja `narrative_with_integrated_definition`.
- [ ] No se introducen cambios de ELO en estos nodos formativos.
- [ ] Si se implementa UI, se verifica con screenshots antes/después.

---

## Nodos ya corregidos con este prompt

- `Fase_1/F1_nodo_enteros.md` — B05 Enteros.
- `Fase_2/F2_nodo_suma.md` — E01 Suma.
