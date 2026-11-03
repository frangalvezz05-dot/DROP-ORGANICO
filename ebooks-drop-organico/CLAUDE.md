# Proyecto: negocio de ebooks con drop orgánico

Construcción pieza a pieza de un sistema de agentes y skills con orquestador final. Progreso y decisiones: `ESTADO.md`.

## Usuario
- Estudiante de Marketing e Investigación de Mercados (España). No programa: si hace falta código, Claude lo hace entero y lo explica en una frase.
- Español, respuestas cortas salvo que pida desarrollo.

## Reglas obligatorias
1. **Un módulo cada vez.** Nada de agentes, skills ni archivos de un módulo no abierto juntos. Al terminar cada paso: parar y esperar aprobación.
2. **El conocimiento lo aporta el usuario.** Cada agente-mentor solo sabe lo que el usuario da + lo verificado con fuentes reales. Si falta información, decirlo y pedirla.
3. **Crítico.** Señalar ideas flojas (del usuario, mentores o propias) con datos o lógica, y contradicciones entre mentores. Etiquetar siempre: **[DATO]** comprobado con fuente / **[OPINIÓN mentor]** / **[ESTIMACIÓN]** propia.
4. Cambiar de postura solo ante un argumento o dato mejor, no por insistencia.
5. Todo se prueba con un caso real (resultado en `pruebas/`) antes de darlo por bueno.
6. Si algo es ambiguo, preguntar antes de construir.
7. Actualizar `ESTADO.md` al final de cada sesión.
8. **No usar** las skills globales de dropshipping (`ds-*`), `nicho-ebooks` ni la carpeta antigua `Documents\organico-ebook (para otro chat)` sin permiso explícito del usuario: contienen conocimiento no aportado en este proyecto.
9. Nunca publicar, pagar, crear cuentas ni contactar a nadie sin un "sí" explícito.
11. **Agentes y skills genéricos.** Ningún agente ni skill puede depender de un nicho concreto: el nicho entra como dato de entrada. Lo específico de cada nicho (avatar, ángulos, decisiones, borradores) vive en `nichos/<nicho>/`. El nicho de prueba actual (ruptura / contacto cero) es solo un ejemplo; si falla, todo debe funcionar con otro sin reescribir nada.
10. **Prioridad nº 1: AVATAR y ÁNGULOS.** Avatar lo más específico posible (con frases reales del cliente, nunca inventadas) y ángulos de ataque definidos antes de escribir ebook, web o guiones. Todo entregable declara a qué avatar y ángulo sirve. Contrapeso: comprobar con datos que el avatar específico tiene tamaño suficiente para ser rentable.

## Modelos (frontmatter `model:` en cada agente)
- **haiku**: ordenar, resumir material en bruto, formatear, actualizar ESTADO.md, búsquedas simples.
- **sonnet**: borradores, textos de producto y anuncios, análisis de un solo mentor, guiones, revisiones normales.
- **opus** (esfuerzo medio): análisis crítico entre mentores, diseño de agentes/skills, decisiones de negocio, redacción final del ebook, orquestador.
- **fable**: supervisor. Solo si Opus se atasca, da vueltas, tiene dudas importantes o va a tomar una decisión cara de revertir. Revisa, corrige y devuelve el control.
- Antes de cada tarea, decir en una línea qué modelo toca. Ante la duda, el más barato capaz. Si falla, subir un nivel solo para esa tarea.

## Tokens y grafo
- `token-budget-advisor`: fijar profundidad una vez por sesión.
- `graphify`: el conocimiento del proyecto vive en `graphify-out/` (raíz `conocimiento/`). Desde el 15-oct el grafo solo incluye conocimiento **destilado** (análisis de mentores, críticas, resultados de módulo y datos); las transcripciones en bruto quedan fuera y se leen solo si el grafo no basta. Consultar el grafo antes de leer archivos o buscar en internet; buscar fuera solo si no está, y añadir lo nuevo. Actualizarlo al añadir material a `conocimiento/` o al aprobar un módulo. Agentes y orquestador también consultan el grafo primero.
- No releer lo que ya está en contexto; leer solo la parte necesaria.

## Estructura
- `conocimiento/[modulo]/[mentor]/` material en bruto del usuario
- `.claude/agents/` mentores (`mentor-[area]-[nombre].md`), críticos, orquestador
- `.claude/skills/` skills de tareas concretas
- `nichos/<nicho>/` todo lo específico de cada nicho (entrada para agentes y skills)
- `pruebas/` resultados de pruebas con casos reales
- `graphify-out/` grafo

## Agentes-mentor
Dos por módulo (mentores reales distintos). Cada uno: método resumido, reglas concretas, en qué se equivoca o qué no cubre, fuentes de cada afirmación. Más un rol crítico que los compara y propone qué aplicar en nuestro caso.

## Ciclo de módulo
1. Qué necesitamos saber y qué material falta → 2. Usuario pasa material → 3. Análisis crítico contrastado → 4. Propuesta de diseño (con modelo), sin crear → aprobación → 5. Crear → 6. Probar con caso real → 7. Aprobar, ESTADO.md, grafo.

## Orquestador
Solo al final, con todos los módulos aprobados. Para en: gastar dinero, publicar, lanzar anuncios, y avisa si un dato no cuadra.
