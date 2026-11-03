# Prompt para pegar en la sesión local (DROP ORGANICO LOCAL)

Copia desde la línea de abajo hasta el final y pégalo en el chat de la sesión local.

---

Hola. Vengo de la sesión en la nube ("DROP NUBE"), que avanzó mucho mientras aquí no había créditos. **Antes de nada, trae el trabajo de GitHub**: el repositorio `frangalvezz05-dot/DROP-ORGANICO`, rama `claude/eager-dirac-x9n7c8`, carpeta `ebooks-drop-organico/`. Contiene la versión más reciente de TODO este proyecto (la tuya más lo nuevo). Cópiala sobre mi carpeta `C:\Users\frangalveez\OneDrive\Documents\ebooks-drop-organico` sin borrar nada que solo exista aquí (si hay conflicto, gana la versión de GitHub, salvo `graphify-out/cache`). Luego lee `CLAUDE.md` (hay reglas nuevas: modo continuo y regla 12 "no reinventar la rueda"), `ESTADO.md` (sección 03-nov · Sesión NUBE) y `LANZAMIENTO-LO-QUE-FALTA.md`. Consulta el grafo (`graphify-out/`, ya actualizado con los módulos 5, 7, 8, 9 y el nicho).

## Dónde estamos
- **Nicho elegido (con reservas): meal prep alto en proteína, en inglés primero, 24,99 $.** Producto: **"The Sunday Sheet"** (`nichos/meal-prep/`). Ganó entre 7 nichos verificados en páginas reales (nota 4,6/5 en EN): una tienda Shopify (Stealth Health) vende un pack de 2 ebooks de meal prep a 49,99 $ con 1.046 reseñas; en Gumroad hay packs de 17-30 $ con 49-63 valoraciones. Boda: lo que vende son plantillas Notion. Cachorro: precio de referencia 4 $. ES: ningún pack ≥15 € con ventas. Detalle: `conocimiento/01-nichos/04-resultado-busqueda-amplia.md` y `pruebas/m1-busqueda-amplia/`.
- **Hecho**: avatar y ángulos (EN aprobado con reservas, ES sin aprobar), análisis de ebooks y páginas del mercado, ebook completo (60 recetas con macros USDA, 48 platos, plan de 4 semanas, coste por ración), maquetado en PDF (336 págs. A5 + imprimible 34 págs. Letter + muestra "The Mini Sunday" 31 págs.), portada, 10 imágenes de tienda, página de producto, textos legales EN/ES, 7 emails, 14 guiones de vídeo, plan de publicación, guía de montaje de Shopify, agente `orquestador`. Módulos 5, 7, 8 y 9 construidos y probados. Skills nuevas: `textos-legales`, `guiones-organicos`, `plan-publicacion`, `emails-ebook`, `numeros-negocio`; agentes `revisor-legal`, `mentor-contenido-marc-verdu`, `orquestador`. Herramientas: `herramientas/macros.py` (USDA), `herramientas/costes.py` (USDA ERS), `herramientas/leer.js`.

## Lo que la nube NO pudo hacer y tú SÍ (tienes el navegador de mi ordenador)
Hazlo en este orden, apuntando cada resultado con fuente y fecha, y actualiza `ESTADO.md` y sube a GitHub tras cada paso:

1. **Biblioteca de anuncios de Meta (lo más importante, método de Dani [Nd2W781CvC8] y Marc [8OqvpohPMvo]).** facebook.com/ads/library · país **Estados Unidos** · "Todos los anuncios" · solo activos. Busca: `meal prep ebook`, `meal prep cookbook`, `high protein meal prep`, `meal prep plan pdf`, y para descubrir otros nichos: `ebook`, `PDF guide`, `digital download`, `workbook`. Para cada anunciante de producto digital: fecha "En circulación desde" (≥30 días = probablemente rentable), nº de anuncios activos, tienda de destino, precio y qué incluye. Repite con país **España**: `batch cooking`, `meal prep recetas`, `ebook`, `guía pdf`. Guarda en `pruebas/m1-busqueda-amplia/08-biblioteca-anuncios.md`.
   - **Si aparece un infoproducto que se anuncia más y mejor que meal prep** (más anunciantes, más tiempo activo, precio ≥15 €, sin promesas prohibidas), compáralo con la tabla de `.claude/skills/puntuar-nicho/SKILL.md` (criterio Pago corregido) y dime si conviene cambiar de nicho. Las skills son genéricas: solo habría que rehacer `nichos/<nuevo>/`.
2. **Etsy** (la nube estaba bloqueada): ventas de las tiendas de meal prep y boda citadas en `pruebas/m1-busqueda-amplia/03-pendiente-navegador.md`.
3. **Google Trends** (5 años, EE. UU. y España): "meal prep", "batch cooking", "high protein meal prep". Completa el criterio Estabilidad.
4. **Reseñas negativas (1-3 estrellas) en Amazon.com y Amazon.es** de 3 libros de meal prep líderes (`nichos/meal-prep/ebooks-mercado.md`). Completa el criterio Hueco y añade frases a `nichos/meal-prep/frases.md`.
5. **Comentarios de YouTube**: 3-4 Shorts/vídeos top de meal prep en inglés y 2-3 de "batch cooking" en español (los de `nichos/meal-prep/contenido/referentes-virales.md`). Saca 15-20 frases reales de problemas (sin nombres de usuario) → `frases.md`. Con eso: re-pasa `avatar.md` por el agente `critico` y aprueba (o no) el avatar ES. Mira también 4-5 de esos Shorts y confirma el formato (texto en pantalla, voz en off, manos, timelapse) en `referentes-virales.md`.
6. **Registro de marcas EE. UU.** (tmsearch.uspto.gov): "The Sunday Sheet". Si existe en libros/comida, propón 3 nombres alternativos.
7. **Recalcula la nota del nicho** con todo lo anterior (cobertura objetivo ≥90 %) en `pruebas/m1-busqueda-amplia/09-puntuacion-final.md` y escribe la conclusión: **meal prep confirmado o cambio de nicho**, con datos.

## Mejoras pendientes del producto (hazlas si el nicho se confirma)
- Ajustar platos (hoy 510-850 kcal y sodio alto) y reescalar recetas para que cada semana cuadre sin "pesa y divide" (`nichos/meal-prep/ebook/recetas-json/`, luego `python ebook/construir.py`, `python herramientas/costes.py`, `python ebook/maquetar.py`).
- Valorar una versión más compacta (336 págs. frente a 86-132 de la competencia).
- Frases reales para los capítulos 13, 14 y 19; método sin olla lenta para P2; 3 platos que rompen la regla de sabor (D-8, C5, C8).
- Reintentar precios oficiales BLS para subir del 36 % de coste con dato oficial.
- Poner `[LINK_TIENDA]` en la muestra cuando exista la tienda.

## Lo que solo hago yo (Fran) — no lo hagas tú
Conectar Shopify (o seguir `nichos/meal-prep/tienda/montaje.md`), darte mis datos legales, cocinar y cronometrar la Semana 1, la consulta al gestor (`conocimiento/07-legal/consulta-gestor.md`), decidir la revisión nativa del inglés, y dar el "sí" a pagos, cuentas y publicar.

Reglas de siempre: nada de publicar, pagar, crear cuentas ni contactar sin mi "sí"; etiquetas [DATO]/[OPINIÓN mentor]/[ESTIMACIÓN]; replicar lo que ya funciona; tras cada paso, `ESTADO.md` + subir a GitHub en la rama `claude/eager-dirac-x9n7c8`.
