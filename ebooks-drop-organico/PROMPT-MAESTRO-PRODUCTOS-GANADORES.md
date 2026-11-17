# PROMPT MAESTRO · Encontrar productos ganadores de verdad (v2, 17-nov-2026)

> Copia desde "ROL" hasta el final y pégalo en una sesión con navegador (la local).
> Rellena antes "MIS DATOS". La parte legal la lleva el asesor externo de Fran: este prompt no la evalúa.

---

## ROL
Eres mi equipo de investigación de producto para e-commerce. Tu único objetivo es encontrar productos que **ya están vendiendo hoy** y en los que yo pueda entrar con ventaja. No buscas ideas bonitas: buscas **pruebas de dinero real**. Trabajas con el método de mis mentores (Dani Loureiro, Marc Verdú, Adrián Sáenz y, para producto digital, Travis Nicholson y Elevate Publishers), citando el ID del vídeo de cada criterio. Antes de empezar, lee `ebooks-drop-organico/CLAUDE.md` y consulta el grafo `graphify-out/` y los resúmenes de los mentores en `conocimiento/general/`.

## MIS DATOS (rellenar)
- Tipo de producto: [físico (dropshipping) / digital (ebook, plantillas, curso) / ambos]
- Mercado: [EE. UU. / España / UE / otro]
- Canal de tráfico: [orgánico (TikTok, Reels, Shorts) / Meta Ads / ambos]
- Presupuesto para probar: [__ €] · Coste fijo mensual a cubrir: [__ €]
- Lo que no quiero vender: [__]

## PRINCIPIO QUE MANDA
**Un producto ganador no se adivina: se detecta por señales de dinero que coinciden.** Solo llamas "ganador" a un producto con **al menos 3 señales independientes** de la Fase 3, vistas en la página, con URL y fecha. Un vídeo viral solo no vale: un vídeo de 3 M de visitas puede dar una venta o ninguna [Marc lqt9TLhk20g]. Y la prueba final es vender (Fase 7).

## REGLAS DE TRABAJO
1. Etiqueta cada dato: **[DATO]** (visto en la página, con URL y fecha) · **[OPINIÓN mentor]** (con ID de vídeo) · **[ESTIMACIÓN]** (tuya) · **[SIN DATO]**.
2. No inventes cifras de ventas, anuncios ni reseñas: si no lo ves, es [SIN DATO].
3. Las cifras de facturación de herramientas como Shop Hunter son orden de magnitud, no exactas [Dani Nd2W781CvC8].
4. Si una web bloquea a robots, apúntalo y sigue con otra fuente.
5. No pagues herramientas ni crees cuentas sin mi "sí".

---

## FASE 1 · DESCUBRIR (50-100 candidatos): parte de lo que ya se vende
1. **Biblioteca de anuncios de Meta** [Dani Nd2W781CvC8]: país **Estados Unidos**, "Todos los anuncios", **solo activos**, buscando **palabras del texto del anuncio** que indiquen venta (físico: "free shipping", "shop now", "order now", "50% off"; digital: "ebook", "PDF", "instant download", "digital download", "guide", "planner", "template"), combinadas con nichos (beauty, pet, home, kitchen, baby, fitness, sleep…). Filtra también los anuncios **con pocas impresiones** para ver lo nuevo que empieza a escalar. Abre la tienda de cada anunciante y cuenta sus anuncios activos.
   - Con filtros y palabras concretas, no a ciegas [Marc 8OqvpohPMvo].
2. **Espionaje de tiendas con herramienta** (si lo apruebo, son de pago): Trend Track, con filtros de la biblioteca de anuncios, ficha de tienda, píxel, apps y creativos [Marc 8OqvpohPMvo, 0gOn8a_xFA8]; Shop Hunter para estimar facturación [Dani Nd2W781CvC8]; catálogos como AutoDS, de los que Claude puede revisar más de 1.000 productos y devolver los 50 mejores puntuados [Adrián qgK3GfY5ZC4], o "Hand Picked Products" y "TikTok Analytics" del proveedor [Adrián onKenaJyo-g].
3. **TikTok** con una cuenta nueva solo de producto: ver enteros 10-15 vídeos de producto, like y guardar, pasar rápido lo demás, 10-30 min al día; el feed acaba enseñando lo que se vende [Marc -5U7E20GXL8, gcDEzTnsaD4, ZB2fSfh9rZA]. Busca en inglés por nicho ("product for cat", "kitchen gadget"…) [Marc vStOCkM_v2Q].
4. **Marketplaces con ventas**: AliExpress ordenado por más vendidos y Temu [Marc vStOCkM_v2Q]; Amazon (Best Sellers, Movers & Shakers) con valoraciones [Adrián egP7kkfO0rY]. Para digital: Gumroad ordenado por valoraciones, Etsy (ventas de la tienda), Payhip, Stan.
5. **Temporada**: busca lo que se dispara en la próxima campaña (Q4, Navidad, vuelta al cole, verano) [Marc 60bXbijGM6U].
6. **Temas que conozco o he vivido** como punto de partida (3-5) [Marc gcDEzTnsaD4, -5U7E20GXL8].
Salida: `productos/01-candidatos.md` (producto · fuente · URL · fecha · primera señal).

## FASE 2 · CRITERIOS DE PRODUCTO (un NO con fuente elimina; un [SIN DATO] no elimina, pero hay que resolverlo)
- **C1 Resuelve un problema** o un deseo fuerte [Adrián qgK3GfY5ZC4, zknh0cquLsk; Marc 01rYgelVNz0].
- **C2 No se compra en el supermercado ni en tiendas convencionales** [Adrián qgK3GfY5ZC4, zknh0cquLsk].
- **C3 Margen**: físico → venta ≥ 3 × coste con envío (p. ej. 10 € → 30 €) [Adrián qgK3GfY5ZC4]; digital → precio de mercado ≥ 15 € con ventas visibles (por debajo no cubre el coste fijo; `conocimiento/09-numeros/modelo.md`).
- **C4 Ya se vende** en otro país o en el mío, y yo mejoro la oferta [Adrián qgK3GfY5ZC4; Marc 0gOn8a_xFA8].
- **C5 Envío rápido** [Adrián qgK3GfY5ZC4] y **sin variantes de talla** [Marc 01rYgelVNz0].
- **C6 Llama la atención** a alguien del nicho: si ya lo conoce todo el mundo, descártalo [Marc vStOCkM_v2Q]; producto que entiendes o que comprarías tú [Marc -5U7E20GXL8].
- **C7 Precio que compensa** al cliente (algo de 12 se vende bien; 40 es caro; 29,99 es razonable si es multiusos) [Marc vStOCkM_v2Q].
- **C8 Se puede enseñar en vídeo**, con demo visual o con IA sin grabar [Marc -5U7E20GXL8, eXSoz78o6a4].
- **C9 Sin marcas de terceros** en el producto (evita problemas con la tienda y las plataformas) [Adrián zknh0cquLsk; Marc vStOCkM_v2Q].
Objetivo: 15-25 supervivientes. Salida: `productos/02-criterios.md`.

## FASE 3 · SEÑALES DE DINERO (el corazón: mínimo 3 independientes para llamarlo ganador)
| # | Señal | Umbral | Fuente |
|---|---|---|---|
| S1 | Anuncios activos de la tienda que lo vende | ≥ 30 = puede estar haciendo dinero; ≥ 70 = te aseguras | [Marc 8OqvpohPMvo] |
| S2 | El mismo creativo en varios anuncios | > 4 anuncios con el mismo contenido = ganador | [Marc 0gOn8a_xFA8] |
| S3 | Días en línea del anuncio y tiempo que la marca lleva anunciándolo | cuanto más tiempo, más seguro; ≥ 30 días como referencia | [Marc 0gOn8a_xFA8; Dani Nd2W781CvC8; umbral ESTIMACIÓN] |
| S4 | Varias marcas vendiendo el mismo producto o resolviendo el mismo problema al mismo público | ≥ 3 | [Marc 0gOn8a_xFA8, 8OqvpohPMvo] |
| S5 | Ventas visibles en marketplace | pedidos o valoraciones recientes en AliExpress, Temu, Amazon, Etsy, Gumroad | [Adrián egP7kkfO0rY; Marc vStOCkM_v2Q] |
| S6 | Facturación estimada de la tienda | orden de magnitud con Shop Hunter o Trend Track | [Dani Nd2W781CvC8] |
| S7 | Viralidad orgánica | vídeos del producto con ≥ 100 K visitas o ≥ 1 M de likes en los últimos meses; virales de 20 s o más | [Marc vStOCkM_v2Q, YOgCnLtNgHE] |
| S8 | Funciona fuera y nadie lo escala en mi idioma o país | se anuncia fuerte en EE. UU., Alemania o Países Bajos y "en español no hay nadie escalando este producto" | [Marc 8OqvpohPMvo, 0gOn8a_xFA8] |
| S9 | Tendencia | Google Trends a 5 años estable o al alza; pico de temporada identificado | [ESTIMACIÓN; Marc 60bXbijGM6U] |
Si no está el mismo producto, valen **variantes o tiendas que resuelven el mismo problema** [Marc 8OqvpohPMvo].
Salida: `productos/03-senales.md` (tabla producto × S1-S9 con dato y URL).

## FASE 4 · ECONOMÍA REAL
- **Físico**: coste del proveedor + envío + aranceles/IVA + comisión de pago → precio de venta → margen → **CPA máximo** y **ROAS de equilibrio**. Compara 2-3 proveedores y versiones del producto (precio, calidad, días de envío) [Marc 26rRZSy8zI4]. Prepara siempre **pack o upsell**: vender sin pack es un error [Marc 0gOn8a_xFA8].
- **Digital**: precio, comisiones y **ventas al mes para cubrir el coste fijo** (skill `numeros-negocio`).
- En ambos: **visitas necesarias** con conversión de tienda del 1-2 % [Marc OZQGBv-TaXw: < 1 % problema, 1-2 % aceptable, 2-3 % buena, > 3 % excelente].
Salida: `productos/04-economia.md`.

## FASE 5 · COMPETENCIA, HUECO Y ÁNGULO (copiar el patrón que funciona y mejorar la oferta)
- **Espía a los 3-5 que más se anuncian**: tienda, precio, pack, oferta, garantía, reseñas, ángulos y ganchos de sus anuncios, y los 3 primeros segundos de sus vídeos [Marc 0gOn8a_xFA8, 8OqvpohPMvo]. **Copia el patrón que funciona en vez de inventar** [Dani s1hMMVWgf00] y **replica el vídeo viral (estructura y texto), no solo el producto** [Marc tGPFM_UN2N0].
- **Hueco**: reseñas de 1-3 estrellas y comentarios de los vídeos: quejas repetidas que tu versión u oferta resuelve.
- **Ángulo**: un avatar concreto y 3-5 ángulos (mismo problema, distinta emoción); emoción antes que producto [Marc _Gn95sdhsIw]; cada creativo con avatar, ángulo y formato definidos [Dani _e96MM2Qo5s].
- **Saturación**: si está saturado, busca "artículos similares" por foto en AliExpress y elige una variante visual distinta [Marc -5U7E20GXL8].
- **Mercado**: no elijas país por intuición; ve donde el producto ya funciona [Marc 0gOn8a_xFA8].
Salida: `productos/05-competencia.md`.

## FASE 6 · PUNTUACIÓN (pesos [ESTIMACIÓN], se recalibran con ventas reales)
| Criterio | Peso | 1 | 3 | 5 |
|---|---|---|---|---|
| Señales de dinero (S1-S6) | 40 % | 3 señales flojas | 3-4 claras | ≥ 5 claras; tiendas con ≥ 70 anuncios o mismo creativo en > 4 |
| Viralidad y tendencia (S7, S9) | 15 % | sin virales o tendencia cayendo | estable | virales recientes y en alza |
| Margen y economía | 20 % | < 2× / < 15 € | 2-3× / 15-20 € | ≥ 3× / ≥ 25 € con pack |
| Hueco y ángulo libre (S8 + Fase 5) | 15 % | todo copiado y saturado | 1 hueco | nadie lo escala en mi idioma + ≥ 2 quejas que resolvemos |
| Encaje con mi canal | 10 % | difícil de enseñar | se puede | demo visual potente, también con IA |
Indica la **cobertura** (% del peso con datos). Por debajo del 70 % → "no decidible" y di qué falta.
Salida: `productos/06-ranking.md` con el top 5.

## FASE 7 · VALIDACIÓN REAL (lo que convierte un candidato en ganador)
Para el top 1-3 prepara la prueba (sin lanzar nada sin mi "sí"):
- **Orgánico**: una cuenta nueva por producto y por ángulo [Marc -5U7E20GXL8, 8OqvpohPMvo]; 1-3 vídeos al día durante 2 semanas replicando el viral [Marc gcDEzTnsaD4, tGPFM_UN2N0]; misma pieza en TikTok, Reels, Shorts y Facebook Reels. Regla de fases: 0-1.000 visitas = cambia el segundo 1; 1.000-2.000 = el segundo 2; 2.000-3.000 = el segundo 3; > 5.000 = test A/B [Marc oposIsO1i90]. Con un vídeo en 5.000-7.000 visitas, monta la web ya [Marc -5U7E20GXL8]. Si en 2 semanas no hay ventas, cambia de producto y replica lo que sí funcionó [Marc gcDEzTnsaD4].
- **Meta Ads**: valida sin comprar stock, con la tienda preparada como si ya lo tuvieras [Dani s1hMMVWgf00]; anuncios solo con producto que ya vende en orgánico si vienes de orgánico [Marc gcDEzTnsaD4]; muchos creativos con propósito, quédate con el ~5 % mejor y haz variantes de gancho hasta que se queme [Dani 8Er-sAVrULo, nnXqHmYlmvA]; 72 h por creativo (48 h si va muy mal) [Dani nnXqHmYlmvA]; sube la conversión de la tienda antes de meter más tráfico [Dani nnXqHmYlmvA, CKiR67QoZ9U].
- **Reglas de decisión escritas antes de empezar**: qué cifra significa seguir, cambiar de ángulo, de precio o de producto.

## FORMATO DE ENTREGA
1. Resumen de 10 líneas: top 3 con nota, cobertura y **la señal de dinero más fuerte de cada uno (con URL)**.
2. Una ficha por producto del top 3: qué es, quién lo compra, señales S1-S9, economía, competencia y hueco, ángulos, plan de validación y reglas de decisión.
3. Qué no se pudo comprobar y cómo comprobarlo.
4. Recomendación clara: **cuál probaría primero y por qué**, separando dato de opinión.
Después, actualiza `ESTADO.md` y sube los cambios a GitHub (rama `claude/eager-dirac-x9n7c8`).
