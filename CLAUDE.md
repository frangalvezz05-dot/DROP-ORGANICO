# Instrucciones para Claude en este proyecto

Lee `00-LEEME-PRIMERO.md` y `.claude/skills/organico-ebook/SKILL.md` al empezar. Cumple sus reglas siempre.

## Usuario
Fran. Estudiante de Marketing, trabaja sin código. Respuestas en español, directas, sin tecnicismos.
Si una tarea necesita código, lo ejecutas tú; a Fran no le pides que programe.

## Ahorro de tokens
- Antes de releer archivos del `corpus/`, consulta el grafo: `graphify-out/` (skill graphify).
  graphify en Windows: `C:\Users\frangalveez\.graphify-venv\Scripts\graphify.exe`
- Tras añadir transcripciones nuevas, reconstruye el grafo: `/graphify corpus`.
- Delega tareas simples en los agentes de `.claude/agents/` (usan Haiku).
- Usa Sonnet solo si Fran escribe "mucha atención".

## Permisos
Nunca publicar, pagar, crear cuentas ni contactar a nadie sin un "sí" explícito de Fran en el chat.
Todo lo de Shopify se crea en **borrador**.

## Memoria (retroalimentación)
- `memoria/metodo.md`: método extraído de los referentes (fuente de verdad).
- `memoria/lecciones.md`: qué funcionó y qué no en cada ciclo. Léelo antes de cada fase y actualízalo al acabarla.
- `memoria/decisiones.md`: decisiones tomadas y por qué.
