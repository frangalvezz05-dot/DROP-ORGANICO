# Consejo de diseño · Prueba 1 · Propuesta módulo 1 (`diseno/m1-propuesta.md`)

_14-oct-2026 · Opus · Fuentes revisadas: CLAUDE.md, ESTADO.md, GRAPH_REPORT.md, crítica Travis vs Elevate, los dos `01-analisis.md`, `datos/idioma-es-vs-en.md`._

## 1. Fiscal de fuentes
1. **MEDIA · Origen mal atribuido en "Estabilidad/crecimiento".** Se cita a Travis [6JXBC5kaDUw], pero Travis usa Google Trends de las **últimas 48 h** para cazar modas (`travis-nicholson/01-analisis.md` §1.1), lo contrario de "estabilidad a 5 años". El origen real es la crítica §6 (dato, no mentor). **Cambio:** citar crítica §6 + Elevate [sE5B7ApMX8E]; quitar a Travis.
2. **MEDIA · Escala 1-5 sin anclas.** Ningún mentor da umbrales (crítica §4.2). Sin definir qué es un 1, un 3 y un 5 (p. ej. nº de hilos, nº de competidores con reseñas), dos ejecuciones darán notas distintas y la regla "cada puntuación con fuente" se cumple en forma pero no en fondo. **Cambio:** tabla de anclas por criterio, todas marcadas [ESTIMACIÓN] a calibrar en la prueba.
3. **MEDIA · "Pruebas de pago" no medible tal cual.** Gumroad y Hotmart suelen ocultar ventas; Amazon muestra reseñas y ranking. **Cambio:** definir la señal por plataforma (reseñas Amazon, "X ventas" visibles en Gumroad, presencia en Biblioteca de anuncios) y qué hacer si no hay dato: [SIN DATO], no un 3 por defecto.
4. **BAJA ·** "≥10 ganchos" sale de Elevate (10-20, [IZCVZQtV2TI]): correcto, pero indicar que es [OPINIÓN mentor].
5. Resto (F1-F5, pesos, lista inicial): bien marcado como decisión del usuario, crítica o [ESTIMACIÓN].

## 2. Abogado del diablo
1. **ALTA · ES + EN sin regla operativa.** F5 dice "óptimo en uno y viable en otro" sin definir "viable", y no se sabe si se puntúa por idioma. Peor: la voz del cliente en Reddit es casi toda EN; el riesgo es que las "frases reales en ES" sean traducciones de frases EN, lo que rompe la regla de frases reales y la prioridad nº 1 (avatar). **Cambio:** puntuar por idioma (dos columnas); "viable" = nota mínima [ESTIMACIÓN] en Dolor repetido y Pruebas de pago; criterio de prueba (b) = ≥10 frases reales **por idioma**, con fuente en ese idioma (foros ES, comentarios TikTok/YouTube ES, reseñas Amazon.es).
2. **MEDIA · El riesgo nº 1 (ebook IA genérico) no está en los filtros.** La crítica §4.1 pedía descartar nichos que exigen autoridad o experiencia vivida; F3 solo pide "ebook de acción". **Cambio:** ampliar F3: "un ebook de acción hecho con IA + voz del cliente puede ser mejor que lo existente sin autoridad profesional" (finanzas sigue entrando con el filtro del usuario).
3. **MEDIA · No se comprueba el canal sin cara.** Hay nichos donde el orgánico depende de la persona (confianza, antes/después). **Cambio:** subcriterio en "Avatar alcanzable" o nuevo: ¿hay cuentas sin cara/IA con tracción en el nicho? (búsqueda en TikTok, ES y EN). Añadir a F4 la obligación de etiquetar contenido IA realista en TikTok/Meta [verificar en mód. 7].
4. **MEDIA · Falta la prueba de pago real.** La crítica §3 aprobó "pruebas de que ya se paga + más adelante una prueba de pago real"; la propuesta la omite. El módulo puede acabar eligiendo un nicho solo con indicios. **Cambio:** declarar que la puntuación es una hipótesis y dejar escrito en qué módulo se valida con dinero (ver orden pendiente en ESTADO).
5. **MEDIA · RGPD en frases reales.** Guardar enlaces + citas de usuarios es tratamiento de datos personales. **Cambio:** guardar frase + enlace sin alias ni datos del autor; en copys/guiones usar paráfrasis, no la cita literal identificable [verificar en mód. 7].

## 3. Auditor de eficiencia
1. **MEDIA · Coste de `avatar-angulos`.** 3 finalistas × 2 idiomas = 6 avatares completos en Sonnet antes de elegir. **Cambio:** avatar ligero para los 3 (5 frases + 5 ganchos por idioma, suficiente para que mentores y crítico comparen) y completo (≥10 frases, banco entero) solo para el nicho elegido. Ajustar el criterio (b) de la prueba en consecuencia. Ahorro [ESTIMACIÓN] ~50-60 % de esa skill.
2. **MEDIA · Choque de nombres con agentes globales.** Existen fuera del proyecto `investigador-avatar` e `investigador-ebooks` (sistema antiguo), con la misma función que `avatar-angulos` e `investigar-nicho`. Riesgo de que el orquestador o Claude llame al antiguo, con conocimiento no aportado (espíritu de la regla 8). **Cambio:** nombres sin solape y regla explícita "no usar agentes globales del sistema antiguo".
3. **BAJA · Mentores.** Aportan poco nuevo (la crítica ya sintetizó, Travis casi no tiene avatar), pero CLAUDE.md exige dos por módulo. Mantener: 1 llamada Sonnet por mentor para los 3 nichos juntos, nunca una por nicho.
4. **BAJA · Modelos:** Haiku búsquedas, Sonnet puntuación, Opus crítico: correctos y los más baratos capaces. Grafo consultado primero: correcto.

## Veredicto: **CAMBIOS**
Estructura buena y bien fundamentada. Antes de crear: regla operativa ES/EN con frases por idioma (ALTA), anclas de puntuación, F3 ampliado, prueba de pago real ubicada, avatar ligero/completo y nombres sin solape. No hay choque entre papeles caro de revertir: no se escala a Fable.
