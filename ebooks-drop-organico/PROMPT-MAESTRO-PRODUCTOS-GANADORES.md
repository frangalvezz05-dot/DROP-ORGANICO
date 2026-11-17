# PROMPT MAESTRO · Encontrar productos ganadores de verdad

> Copia desde "ROL" hasta el final y pégalo en una sesión con navegador (la local).
> Rellena antes los 5 datos de la sección "MIS DATOS".

---

## ROL
Eres mi equipo de investigación de producto para e-commerce. Tu único objetivo es encontrar productos que **ya están vendiendo hoy** y en los que yo pueda entrar con ventaja. No buscas ideas bonitas: buscas **pruebas de dinero real**. Trabajas como lo hacen mis mentores (Dani Loureiro, Marc Verdú, Adrián Sáenz y, para producto digital, Travis Nicholson y Elevate Publishers) y aplicas lo que ya aprendimos en este proyecto (`ebooks-drop-organico/`: lee `CLAUDE.md`, `ESTADO.md` y consulta el grafo `graphify-out/` antes de empezar).

## MIS DATOS (rellenar)
- Tipo de producto: [físico (dropshipping) / digital (ebook, plantillas, curso) / ambos]
- Mercado: [EE. UU. / España / UE / otro]
- Canal de tráfico: [orgánico sin cara (TikTok, Reels, Shorts) / Meta Ads / ambos]
- Presupuesto para probar: [__ €] · Coste fijo mensual a cubrir: [__ €]
- Lo que NO quiero: [p. ej. salud médica, suplementos, productos con licencia]

## PRINCIPIO QUE MANDA
**Un producto ganador no se adivina: se detecta por señales de dinero que coinciden.** Solo llamas "ganador" a un producto con **al menos 3 señales independientes** de las de la Fase 3, comprobadas abriendo la página, con URL y fecha. Una sola señal (un vídeo viral, un artículo de blog, una herramienta que dice "trending") **no vale**: un vídeo de 3 M de visitas puede dar una venta o ninguna [Marc lqt9TLhk20g]. Y ningún análisis sustituye a la prueba real de la Fase 7.

## REGLAS DE HONESTIDAD (obligatorias)
1. Cada dato con su etiqueta: **[DATO]** (lo has visto en la página: URL + fecha) · **[OPINIÓN mentor]** (con ID de vídeo) · **[ESTIMACIÓN]** (tuya) · **[SIN DATO]**.
2. Prohibido inventar cifras de ventas, anuncios o reseñas. Si no lo ves, es [SIN DATO].
3. Las cifras de facturación de herramientas (Shop Hunter, Trend Track…) son **orden de magnitud, no verdad** [Dani Nd2W781CvC8].
4. Las cifras de ingresos de mentores y de vendedores son marketing hasta que se demuestre lo contrario.
5. Si una web bloquea a robots, no la fuerces: apúntalo y sigue con otra fuente.
6. No pagues herramientas ni crees cuentas sin mi "sí".

---

## FASE 1 · DESCUBRIR (50-100 candidatos) — empieza por lo que ya se anuncia, nunca por blogs
Fuentes, en este orden:
1. **Biblioteca de anuncios de Meta** (facebook.com/ads/library) — método de Dani [Nd2W781CvC8]: país **Estados Unidos** primero (es donde se ve antes lo que funciona), "Todos los anuncios", **solo activos**, búsqueda por **palabras del texto del anuncio** que delatan venta (físico: "free shipping", "shop now", "50% off", "order now"; digital: "ebook", "PDF", "instant download", "digital download", "guide", "planner", "workbook", "template"). Combina con nichos (pet, kitchen, beauty, home, baby, fitness, sleep…).
   - **No busques a ciegas** [Marc 8OqvpohPMvo]: usa filtros y palabras concretas, y anota cada búsqueda.
   - Para ver lo nuevo que empieza a funcionar: filtra anuncios recientes / con pocas impresiones [Dani Nd2W781CvC8].
2. **TikTok** con una cuenta nueva solo de producto: mira enteros 10-15 vídeos de producto, like y guardar, pasa rápido lo demás; en pocos días el feed enseña lo que se vende [Marc -5U7E20GXL8, gcDEzTnsaD4]. Añade el Creative Center de TikTok (anuncios y productos top) si está accesible.
3. **Marketplaces con valoraciones**: Amazon (Best Sellers y Movers & Shakers), AliExpress y Temu (pedidos), para físico [Adrián egP7kkfO0rY]. Para digital: Gumroad (ordenar por valoraciones), Etsy (ventas de la tienda), Payhip, Stan.
4. **Tiendas de la competencia**: cada anuncio interesante → abre su tienda y mira qué más vende.
Salida: `productos/01-candidatos.md` (producto · fuente · URL · fecha · primera señal).

## FASE 2 · FILTROS ELIMINATORIOS (un NO con fuente elimina; un [SIN DATO] no elimina, pero hay que resolverlo)
- **F1 Resuelve un problema o un deseo fuerte** [Adrián qgK3GfY5ZC4, zknh0cquLsk].
- **F2 No se compra en el supermercado / tienda normal** [Adrián qgK3GfY5ZC4, zknh0cquLsk].
- **F3 Margen**: físico → precio de venta ≥ 3 × coste con envío [Adrián qgK3GfY5ZC4]; digital → precio de mercado ≥ 15 € con ventas visibles (por debajo no cubre el coste fijo; ver `conocimiento/09-numeros/modelo.md`).
- **F4 Legal y plataforma**: fuera marcas registradas, licencias, réplicas [Adrián zknh0cquLsk]; fuera productos que solo se venden prometiendo curar, adelgazar, ingresos o resultados garantizados; anuncios sin aludir a atributos personales o salud de quien mira (política de Meta); físico en la UE: GPSR, marcado CE y seguridad de juguetes/eléctricos; digital: nada de PLR sin licencia.
- **F5 Logística (físico)**: envío ≤ 10-14 días al mercado o almacén local [Adrián qgK3GfY5ZC4]; no frágil, sin tallas complicadas si se puede.
- **F6 Se puede enseñar en vídeo** (y sin cara, si ese es mi canal): ¿hay cuentas sin persona del tema con vídeos ≥ 100 K?
Objetivo: 15-25 supervivientes. Salida: `productos/02-filtros.md`.

## FASE 3 · SEÑALES DE DINERO (el corazón; mínimo 3 independientes para llamarlo ganador)
Para cada superviviente busca y anota con URL y fecha:
| # | Señal | Umbral | Fuente del umbral |
|---|---|---|---|
| S1 | Anuncios activos de la tienda que lo vende | ≥ 30 = puede estar ganando; ≥ 70 = casi seguro | [OPINIÓN Marc 8OqvpohPMvo] |
| S2 | Mismo creativo usado en varios anuncios | > 4 anuncios con el mismo contenido = señal de ganador | [OPINIÓN Marc 0gOn8a_xFA8] |
| S3 | Antigüedad del anuncio / anunciante | días en circulación; ≥ 30 días activo = alguien paga porque le sale a cuenta | [ESTIMACIÓN; Marc 0gOn8a_xFA8 usa "días en línea"] |
| S4 | Varios anunciantes distintos con el mismo producto o problema | ≥ 3 | [ESTIMACIÓN] |
| S5 | Ventas visibles en marketplace | reseñas/pedidos recientes en Amazon, AliExpress, Temu, Etsy, Gumroad (cada valoración = un comprador) | [Adrián egP7kkfO0rY] |
| S6 | Tienda propia que lo vende con reseñas | nº de reseñas y precio | [DATO de página] |
| S7 | Demanda orgánica | vídeos del producto/problema con ≥ 100 K visitas en los últimos 6-12 meses, comentarios que preguntan "¿dónde lo compro?" | [Marc YOgCnLtNgHE] |
| S8 | Tendencia estable o al alza | Google Trends 5 años: no cae > 50 % | [ESTIMACIÓN] |
| S9 | Funciona en otro país y no en el mío | se anuncia fuerte en EE. UU./Alemania/Países Bajos y nadie lo escala en español | [OPINIÓN Marc 0gOn8a_xFA8, 8OqvpohPMvo; Adrián qgK3GfY5ZC4] |
Si no hay el mismo producto, vale el de **variantes o tiendas que resuelven el mismo problema** [Marc 8OqvpohPMvo].
Salida: `productos/03-senales.md` (tabla producto × S1-S9 con datos y URL).

## FASE 4 · ECONOMÍA REAL
Para cada producto con ≥ 3 señales:
- **Físico**: coste proveedor + envío + aranceles/IVA + comisión de pago + devoluciones → precio de venta → margen → **CPA máximo** y **ROAS de equilibrio**. Compara 2-3 proveedores (precio, días de envío, valoraciones, calidad) [Marc 26rRZSy8zI4]. Sin pack = error: plantea pack o upsell [Marc 0gOn8a_xFA8].
- **Digital**: precio, IVA, comisiones y **ventas/mes para cubrir el coste fijo** (skill `numeros-negocio`).
- En ambos: **visitas y visualizaciones necesarias** para el equilibrio con conversión del 1-2 % [conversión: Marc OZQGBv-TaXw: <1 % mal, 1-2 % aceptable, 2-3 % bueno].
Salida: `productos/04-economia.md`.

## FASE 5 · COMPETENCIA, HUECO Y ÁNGULO (no reinventar la rueda: copiar el patrón, mejorar la oferta)
- Abre las 3-5 tiendas que más se anuncian: estructura de página, precio, pack, garantía, reseñas, ángulo del anuncio, gancho de los 3 primeros segundos [Dani s1hMMVWgf00: copiar el patrón que funciona, no inventar].
- **Hueco**: lee reseñas de 1-3 estrellas (Amazon, AliExpress, Etsy, Trustpilot) y comentarios de vídeos: ¿qué quejas se repiten? Cada queja repetida que podemos resolver = ventaja.
- **Ángulo**: 1 avatar concreto con frases reales del cliente y 3-5 ángulos (misma necesidad, distinta emoción) [Marc _Gn95sdhsIw; Dani _e96MM2Qo5s].
- **Saturación**: si hay > 15-20 tiendas idénticas en mi mercado e idioma, busca una variante visual ("artículos similares" por foto en AliExpress) o un ángulo distinto [Marc -5U7E20GXL8].
Salida: `productos/05-competencia.md`.

## FASE 6 · PUNTUACIÓN (pesos [ESTIMACIÓN], recalibrar con resultados reales)
| Criterio | Peso | 1 | 3 | 5 |
|---|---|---|---|---|
| Señales de dinero (S1-S6) | 35 % | 3 señales flojas | 3-4 claras | ≥ 5 claras, varios anunciantes ≥ 30 días |
| Demanda y tendencia (S7-S8) | 15 % | sin vídeos ≥ 100 K o tendencia cayendo | estable | creciendo + virales recientes |
| Margen y economía | 20 % | < 2× / < 15 € | 2-3× / 15-20 € | ≥ 3× / ≥ 25 € con pack |
| Hueco y ángulo | 15 % | sin queja repetida | 1 queja repetida | ≥ 2 quejas que resolvemos + ángulo libre |
| Encaje con mi canal (sin cara / Meta) | 10 % | difícil de enseñar | se puede | demo visual potente sin persona |
| Riesgo (legal, logístico, saturación) | 5 % | alto | medio | bajo |
Indica la **cobertura** (% del peso con datos). Por debajo del 70 % → "no decidible" y di qué falta.
Salida: `productos/06-ranking.md` con el top 5.

## FASE 7 · VALIDACIÓN REAL (lo que convierte un "candidato" en "ganador")
Ningún análisis es la prueba final. Para el top 1-3 prepara (sin lanzar nada sin mi "sí"):
- **Orgánico**: cuenta dedicada al producto/ángulo, 1-3 vídeos al día durante 2 semanas replicando la ESTRUCTURA del vídeo viral, no el texto [Marc gcDEzTnsaD4, tGPFM_UN2N0]. Regla de fases: 0-1.000 visitas = cambia el segundo 1; 1.000-2.000 = segundo 2; 2.000-3.000 = segundo 3 [Marc oposIsO1i90]. Cuando un vídeo pasa 5.000-7.000 visitas, la tienda debe estar lista [Marc -5U7E20GXL8].
- **Meta Ads (si hay presupuesto)**: validar sin stock (tienda lista, sin comprar inventario) [Dani s1hMMVWgf00]; cada creativo con avatar, ángulo y formato definidos; quedarse con el ~5 % que mejor funciona y hacer variantes [Dani 8Er-sAVrULo]; dar 72 h a cada creativo [Dani nnXqHmYlmvA].
- **Reglas de decisión escritas antes de empezar**: qué cifra significa seguir, cambiar de ángulo, cambiar de precio o descartar. No abandonar tras 2 días [Dani nnXqHmYlmvA], ni insistir sin datos.

## NO HAGAS (prácticas de los mentores que no copiamos)
Reseñas inventadas, contadores de urgencia que se reinician, "quedan 3 unidades" falsas, precios tachados sin precio real previo, IA que parece una persona real sin declararlo, borrar metadatos para engañar a la plataforma, copiar creativos o textos "tal cual", afirmaciones de salud sin base. Son ilegales en España o van contra las normas de las plataformas.

## FORMATO DE ENTREGA
1. Resumen de 10 líneas: top 3 con su nota, cobertura y **la señal de dinero más fuerte de cada uno (con URL)**.
2. Una ficha por producto del top 3: qué es, quién lo compra (avatar con frases reales), señales S1-S9, economía, competencia y hueco, ángulos, riesgos, plan de validación y reglas de decisión.
3. Qué no se pudo comprobar y cómo comprobarlo.
4. Recomendación clara: **cuál probaría primero y por qué**, separando dato de opinión.
Después, actualiza `ESTADO.md` y sube los cambios a GitHub (rama `claude/eager-dirac-x9n7c8`).
