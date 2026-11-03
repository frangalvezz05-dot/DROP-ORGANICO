---
name: redactar-ebook
description: Redacta un ebook de acción (o solo su muestra) a partir de la estructura aprobada, en el idioma líder y adaptado al otro idioma, con reglas estrictas contra el contenido genérico. Usar en el módulo 2 tras estructura-ebook, o cuando el usuario diga "escribe la muestra", "redacta el capítulo", "escribe el ebook".
model: sonnet
---

# Redactar ebook (genérica: el nicho entra como dato)

Entradas: `nichos/<nicho>/estructura.md` (aprobada por el `critico`), avatar completo, ficha del nicho.
Salida: `nichos/<nicho>/ebook/<idioma>/<capitulo>.md` (texto con marcas simples de títulos, listas y espacios para escribir: `[ESPACIO: n líneas]`, `[TRACKER: ...]`).

## Modo y modelo
- **Muestra y borradores**: Sonnet.
- **Ebook completo para el lanzamiento** (decisión del usuario 15-oct-2026: la mejor versión desde el principio, no una versión peor que se mejora si vende): borrador Sonnet → **versión final Opus** (un subagente `model: opus` por bloque de capítulos) → `revisor-calidad`. Requiere aprobación del usuario antes de empezar.

## Proceso por capítulo
1. Relee su fila del índice: problema, frase real, ejercicio, resultado.
2. Escribe en el **idioma líder**.
3. **Adapta** al otro idioma: reescribe ejemplos y referencias para ese público y usa frases reales de ese idioma. Si no hay frase real en ese idioma → [SIN DATO] y usa el ángulo sin cita. **Nunca** presentes una frase traducida como real.
4. Pasa el resultado al agente `revisor-calidad`.

## Reglas anti-genérico (obligatorias)
1. Cada capítulo se apoya en ≥1 frase real del avatar en ese idioma (enlace en `nichos/<nicho>/`) o declara [SIN DATO].
2. Cada sección termina en una acción: ejercicio, plantilla o decisión.
3. Ejemplos concretos (situación, momento, objeto) en vez de generalidades.
4. Frases prohibidas (vacías o cliché). Lista inicial: "en el mundo actual", "es importante destacar", "viaje", "desbloquear tu potencial", "no estás solo/a" sin más, "sin lugar a dudas", "en conclusión". El `revisor-calidad` añade las que detecte; guárdalas aquí con fecha.
   - Añadidas 2026-10-14: "la vida real complica las cosas" / "real life gets in the way"; "la idea es sencilla" / "the idea is simple" como introducción de una explicación.
5. Sin promesas de resultado, testimonios inventados ni urgencias falsas. Avisos de contenido según la ficha del nicho (p. ej. "no sustituye ayuda profesional" + recursos de ayuda).
6. Nada copiado ni parafraseado de cerca de ebooks del mercado ni de mentores.
7. Tono: el del avatar (cómo habla en sus frases reales), segunda persona, frases cortas.

## Nichos con recetas o datos nutricionales (añadido 03-nov-2026)
- Calorías y macros **siempre calculados** con `python3 herramientas/macros.py` (base oficial USDA FoodData Central SR Legacy, dominio público), nunca estimados por la IA. Guardar el `receta.json` de cada receta en `nichos/<nicho>/ebook/recetas/` para poder recalcular.
- Elegir la entrada USDA en el mismo estado que el gramaje (crudo o cocinado). Redondear: kcal a la decena, proteína al gramo.
- Técnicas y tiempos de cocción estándar y seguros (temperaturas internas seguras de la carne, conservación en nevera 3-4 días, congelado). Alérgenos en cada receta.
- Sin promesas de pérdida de peso ni de salud; aviso "no sustituye a un nutricionista o médico".
