---
name: puntuar-nicho
description: Busca, filtra y puntúa nichos para un ebook (escrito con IA, tienda propia, vídeo corto orgánico sin cara) en ESPAÑOL e INGLÉS por separado, con pruebas reales de demanda y de pago sacadas con el navegador. Usar en el módulo 1 cuando el usuario diga "busca nichos", "puntúa este nicho", "qué ebook vendemos", "valida este tema" o al lanzar un ebook nuevo.
model: sonnet
---

# Puntuar nicho (módulo 1) · v2 (14-oct-2026)

Diseño aprobado: `diseno/m1-propuesta.md`. Cambios v2 tras `pruebas/m1-prueba-1/` (13 problemas de la fase 1 + fallo de datos de la fase 2).
Métodos de los mentores (con IDs de vídeo): `conocimiento/01-nichos/travis-nicholson/01-analisis.md` y `elevate-publishers/01-analisis.md`. Consulta el grafo antes: `C:\Users\frangalveez\.graphify-venv\Scripts\graphify.exe query "<pregunta>" --budget 3000`.

## 0. Antes de empezar
1. Lee `CLAUDE.md` y `ESTADO.md`. Prohibido usar agentes/skills antiguos (`investigador-*`, `ds-*`, `nicho-ebooks`).
2. Carpeta de salida: `pruebas/<ejecucion>/`.
3. **Cómo se consiguen los datos (obligatorio):**
   - **En la nube (Linux)**: no hay navegador integrado; usar Chromium con Playwright desde Bash (`require('playwright')`, `page.innerText('body')`), siempre que la red de la sesión permita esos dominios. Si la red los bloquea → parar y pedir al usuario que abra la red; el buscador solo da notas [BUSCADOR] y cobertura insuficiente.
   - **Navegador integrado** (`mcp__Claude_Browser__*`) para Amazon (.es y .com), YouTube, Gumroad, Payhip, Etsy y TikTok si deja entrar. Un solo subagente `model: haiku` que trabaja de forma secuencial (el navegador no se comparte en paralelo). Leer con `get_page_text`, rechazar cookies, no iniciar sesión.
   - **WebSearch** solo para descubrir temas y URLs, nunca como fuente de cifras (los resúmenes del buscador valen como [BUSCADOR], un punto menos).
   - **Reddit**: prohibido en el navegador; no forzar. Solo estadísticas de comunidad vía gummysearch.com.
   - **Google Trends** suele bloquear (429): un intento; si falla, [SIN DATO].

## 1. Candidatos (12-15) → `01-candidatos.md`
Mercados con dolor fuerte (relaciones, salud no médica, dinero personal, crianza, mascotas, estudios/trabajo…) estrechados a subnicho + persona + problema (Elevate [43UQKmwsvO0]). Temas al alza: crecimiento de comunidades (gummysearch) y vídeos recientes con muchas visitas en YouTube (Travis [6JXBC5kaDUw]).

## 2. Filtros → `02-filtros.md` (se aplican una vez; anota si un filtro cambia por idioma)
Un **NO justificado con fuente** elimina. Un **[SIN DATO] nunca elimina**: pasa marcado y debe resolverse antes de la elección final. Objetivo: 5-7 supervivientes.
- **F1 Dolor estable**: hay libros/guías del tema con ≥3 años que siguen vendiendo, o la comunidad crece. Modas solo como ángulo dentro de un nicho estable.
- **F2 Sabemos su miedo**: ≥2 frases reales (con enlace) que expresen un miedo concreto [rO4h5ofNWic].
- **F3 Ebook de acción sin autoridad**: se resuelve con plan, retos, plantillas o guiones, y el contenido no sustituye a un profesional sanitario, legal, financiero regulado o veterinario. Si el núcleo del problema exige diagnóstico o tratamiento → NO.
- **F4 Riesgo de plataforma/legal**: NO si el ebook solo funciona prometiendo: curar/tratar (salud), ingresos o rentabilidad o recomendaciones de inversión (finanzas), resultados garantizados ("recupera a tu ex"), o contenido sexual explícito. Con filtro (sin esas promesas) → SÍ.
- **F6 Sin cara**: en YouTube Shorts o TikTok (navegador) existe ≥1 cuenta sin personaje del tema con ≥10 K seguidores o un vídeo con ≥100 K visitas. Si no se puede comprobar → [SIN DATO].
- **F5 Idioma**: NO va aquí; se decide en el paso 4.

## 3. Puntuación de MERCADO por idioma → `03-puntuacion.md`
ES y EN por separado, datos buscados en cada idioma. Cada nota con fuente (URL + fecha) y tipo: [PÁGINA] verificado en la página / [BUSCADOR] (−1 punto).
**[SIN DATO] no puntúa**: el criterio se excluye y se reparte su peso. Se indica la **cobertura** (% del peso con datos). Cobertura <70 % en un idioma → ese idioma es **"no decidible"** (ni pasa ni suspende) y se lista qué falta.

| Criterio | Peso | 1 | 3 | 5 |
|---|---|---|---|---|
| Dolor repetido | 30 % | top vídeos ESPECÍFICOS de YouTube sobre el problema (5 últimos años) <10 K visitas | 10-100 K | >100 K y comentarios que repiten el dolor |
| Pruebas de pago (DIGITAL) | 30 % | ranking Kindle del ebook específico líder >500 K | 50-500 K | <50 K, o ventas visibles en Gumroad/Payhip/Etsy |
| Hueco | 15 % | reseñas negativas sin patrón | 1 queja repetida | ≥2 quejas repetidas que un ebook de acción resuelve |
| Precio digital | 15 % | mediana digital <5 € y sin packs | 5-12 €, o packs 12-20 € | packs/guías ≥15 € con ventas visibles |

Reglas de medición (añadidas 14-oct tras m1-prueba-1):
- **Mínimo 3 vídeos específicos** por idioma para puntuar Dolor; con menos → [SIN DATO]. Vídeos fuera de tema (humor, música, temas generales) y libros genéricos no cuentan.
- **Pago**: el criterio principal es el **ranking Kindle** del ebook específico líder (abrir siempre su ficha). Las valoraciones solo desempatan dentro de un tramo.
- **Hueco**: las reseñas de Amazon suelen pedir inicio de sesión; usar las visibles en la ficha, Goodreads o comentarios de YouTube que critiquen soluciones existentes. Si no hay → [SIN DATO].
- **Precio**: los 0 € de Kindle Unlimited no entran en la mediana.
| Estabilidad | 10 % | Google Trends cae >50 % en 5 años | estable | crece |

Comunidad en gummysearch (tamaño y crecimiento) entra como apoyo de "Dolor" solo en EN.
**Papel** (tapa blanda) se anota aparte como señal secundaria; no puntúa en pago ni precio.
Pesos y anclas: **[ESTIMACIÓN]**, recalibrar tras cada prueba (con aprobación del usuario, anotando fecha aquí).

## 4. Idioma (F5) y lista corta
- F5 provisional [ESTIMACIÓN]: nota de mercado ≥3,0 en un idioma y ≥2,0 en el otro, ambos con cobertura ≥70 %.
- Top 3 por nota de mercado (media de los dos idiomas que pasen F5). Si menos de 3 pasan F5, se presentan los que haya y por qué.

## 5. Avatar y ángulos → nota FINAL
Para el top 3: ejecutar `avatar-angulos` en modo **ligero**. Puntuar entonces:
| Criterio | 1 | 3 | 5 |
|---|---|---|---|
| Avatar nítido | solo demografía | estilo de vida + 1 miedo con frase real | miedo central con ≥2 frases reales por idioma |
| Ángulos | <5 ganchos | 5-9 | ≥10 para público inconsciente |
**Nota final = 60 % mercado + 20 % avatar + 20 % ángulos** (regla 10: avatar y ángulos pesan). Después: `mentor-nichos-travis-nicholson`, `mentor-nichos-elevate-publishers` y `critico`.
Para que los mentores opinen de forma más independiente, pásales los **datos** (`datos-*.md`, frases y avatar ligero) pero **no** el archivo de notas `03-puntuacion.md`: que juzguen con su método, no con nuestras notas. Sus coincidencias se presentan como señal moderada, no como confirmación.

## 6. Fichas → `fichas/<nicho>.md` y elección
Ficha por finalista: notas con fuentes, cobertura, riesgos, modas aprovechables y qué idioma lidera. **Parar** y presentar al usuario: él elige el nicho.

## Reglas
- Etiquetas: [DATO] / [OPINIÓN mentor] / [ESTIMACIÓN] / [SIN DATO] / [PÁGINA] / [BUSCADOR].
- Frases de clientes: reales, con enlace, sin nombre de usuario (RGPD).
- Fuentes y datos fiables nuevos se anotan para añadirlos al grafo.
