# 06 - Verificación con navegador · datos crudos · 7 nichos · ES / EN

_03-nov-2026. Herramienta: `node herramientas/leer.js` (Chromium) en Gumroad, YouTube, Amazon y webs de tienda. Todo [PÁGINA] salvo lo marcado [BUSCADOR] (WebSearch, solo para descubrir URLs). Un robot, secuencial, sin saltar bloqueos._

## Limitaciones del día (qué NO se pudo)
- **DuckDuckGo html**: 403 (bloquea robots). No se intentó saltar. Las tiendas propias se descubrieron con WebSearch [BUSCADOR] y se abrieron después con el navegador [PÁGINA].
- **Payhip**: Cloudflare "Performing security verification" (403) en todas las fichas -> [SIN DATO] de Payhip. No se saltó.
- **Etsy y Biblioteca de anuncios de Meta**: no se intentaron (orden de Fran). Columna Biblioteca de anuncios = **PENDIENTE (Fran, navegador propio)** en todos los nichos.
- **Google Trends**: 429 al primer intento (https://trends.google.com/trends/explore?date=today%205-y&q=meal%20prep&geo=US). Estabilidad = [SIN DATO] en todos.
- **Amazon.es**: tras unas pocas peticiones devuelve 503 / "haz clic para seguir comprando" (control antirrobot). No se saltó. Solo hay rangos .es de 2 fichas (abajo). El resto ES Amazon = [SIN DATO].
- **Hueco** (reseñas negativas): no se recogió en esta ronda -> [SIN DATO].
- **Sin cara (Shorts)**: el texto de la página da título y visitas, pero no se ve si sale una persona. Se anotan los Shorts del tema con >=100 K; "sin persona" queda [SIN DATO] salvo que se diga lo contrario.

---
## A. PAGO (criterio corregido: alguien ya vende un ebook/pack del tema en su tienda o plataforma a >=15 con señales de venta)

Gumroad: cada "valoración" = comprador verificado. Listados con `sort=most_reviewed&min_price=15` (precio en USD que muestra Gumroad al detectar $).

### 1. Planificación de boda
**EN**
- Gumroad discover "wedding planner" >=15 $: https://gumroad.com/discover?query=wedding%20planner&sort=most_reviewed&min_price=15 (134 productos) [PÁGINA 03-nov-2026]
  - "Ultimate Wedding Planner" (The Modern Wed) 20 $, **5,0 con 18 valoraciones** - https://themodernwed.gumroad.com/l/rtkhkg [PÁGINA]. OJO: es una plantilla de **Notion**, no un ebook.
  - "Bliss" (Rismo) 20 $+, 5,0 (18) - https://rismo.gumroad.com/l/bliss
  - "The Event Industry Power Bundle" 49,99 $, 4,7 (11)
  - "The Complete Wedding Planner" 20 $ (3); "All-In-One Wedding Planner" 39,99 $+ (5); "Wedding Planner Pro" 17,99 $+ (2)
  - Español en el mismo listado: "Marcha nupcial..." 29,99 $ (7, 3, 3...) = partituras, otro tema.
- Tienda propia: Irish Wedding Blog, "The Ultimate Wedding Planning Guide Ireland E-Book pdf" **7,99 €** (PDF, Volumen 2, sin reseñas visibles) - https://irishweddingblog.ie/product/the-ultimate-wedding-planning-guide-ireland-e-book-pdf ; el libro en papel A5 17,50 € - https://irishweddingblog.ie/product-tag/wedding-planning-guide [PÁGINA]. No es Shopify (WooCommerce, no verificado). Sin señales de venta.
- Gumroad "Wedding Planner Printable PDF" (Mom Money Map) **9,99 $**, 108 páginas, sin valoraciones visibles - https://shopmommoneymap.gumroad.com/l/wedding-planner-printable-pdf [PÁGINA]
- [BUSCADOR] Payhip: bundle "40-Day Guide To Planning Your Wedding" 27 $ sin reseñas (no verificable, Cloudflare).
**ES**
- Gumroad "planificador boda": 0 resultados >=15; "organizar boda": 1 resultado ajeno (Green Card). https://gumroad.com/discover?query=planificador%20boda&sort=most_reviewed&min_price=15 [PÁGINA]
- Gumroad sin filtro de precio: "Plantilla Excel para PLANNING DE BODA" 5,60 $ (6 val.) - https://gumroad.com/discover?query=planificador%20boda [PÁGINA, 1ª búsqueda 03-nov].
- [BUSCADOR] Gumroad "Soluciones Digitales" organizador de boda en español 5 $; Pepapaper (tienda española) planificador en papel con envío.
- **No hay ningún ebook/pack de boda en español a >=15 € con ventas visibles.**

### 2. Meal prep / batch cooking
**EN**
- Gumroad "meal prep" >=15 $ (468 productos): https://gumroad.com/discover?query=meal%20prep&sort=most_reviewed&min_price=15 [PÁGINA]
  - "The Big Bean (meal prep guide)" Sober Fitness, **17,86 $+, 4,8 con 58 valoraciones**, PDF 11 págs. + vídeo MP4 - https://soberfitness.gumroad.com/l/thebigbean [PÁGINA]
  - "Meal Planner" Carol Mayes 15 $+ (24); "Plate For Health e-cookbook" 20 $ (49); "Simply Delicious E-book Bundle" 39,99 $ (18); "30 Meal Prep Recipes with Calories and Macros" 20 $ (10); "FeastRecipes Cookbook" 29,99 $ (63); "Massively Simple Recipes for Very Busy People" 59 $ (51); "4 Week Bariatric Diet Meal Plan" 37 $ (36).
- **Tienda propia Shopify**: Stealth Health Life, "The Meal Prep Bundle (Slow Cooker & Meal Prep eBooks)" - https://stealthhealthcookbook.com/products/mp-bundle-slow-cooker-meal-prep-ebooks [PÁGINA]
  - **Digital 49,99 $** (2 ebooks, 205 recetas: Slow Cooker 95 + Meal Prep 110; "25 $/ebook", ahorro 10 $); en tapa dura 94,99 $.
  - **4,8 estrellas, 1.046 reseñas** ("incluye clientes de ebook y tapa dura"; reseñas de hace 1 semana a 6 meses). Confirmado Shopify (`cdn.shopify.com`, `Shopify.theme` en el código).
  - Estructura: cada receta con calorías y proteína; capítulos por tipo (pasta, rice bowls, burritos, proteínas); recetas "que tu familia pide por nombre". Entrega PDF instantánea.
- Gumroad "Ultimate Meal Prep Bundle" (Kaia Bloom): 7 ebooks, 37,99 $ (antes 75,30 $), todos 0 valoraciones - https://kaiabloom.gumroad.com/l/ultimatemealprepbundle [PÁGINA] (señal débil: precio sin ventas).
- Gumroad "The Ultimate Guide To Food Prep Ebook + PDF Bundle" 12,99 $, 5,0 (6), hoy "no a la venta" - https://theleangreenbean.gumroad.com/l/foodprepebookpdfbundle [PÁGINA] (<15 $).
**ES**
- Gumroad "batch cooking" >=15 $ (58 resultados, casi todos en inglés): sin ningún producto en español de batch cooking con valoraciones; "Comer Bonito - Comer bien cuando el presupuesto importa" 19,99 $+ sin valoraciones. https://gumroad.com/discover?query=batch%20cooking&sort=most_reviewed&min_price=15 [PÁGINA]
- "menu semanal": 9 resultados, nada de pago relevante.
- Casa del Libro: "Batch cooking para principiantes" (T. Yoshida) eBook **9,49 €** - https://www.casadellibro.com/ebook-batch-cooking-para-principiantes/9798215083963/14798675 [PÁGINA] (<15 €, editorial).
- [BUSCADOR] Gumroad "batch cooking sain" (francés) 4,50 €; Kazidomi ebook otoño 7,49 €.
- **No hay ningún pack de batch cooking en español a >=15 € con ventas visibles.**

### 3. CV + LinkedIn cambio de carrera
**EN**
- Gumroad "career change resume" >=15 $ (87): https://gumroad.com/discover?query=career%20change%20resume&sort=most_reviewed&min_price=15 [PÁGINA]
  - "Roadmap to Becoming an Independent Adjuster" 37 $ (159) - otro tema (cambio a oficio concreto).
  - "UX/UI - Resume Guidebook & Figma Templates" 33,56 $ (15); "The UX Design Dream Job Guide Pack" 50 $ (13); "Cybersecurity LinkedIn Profile Optimization Guide" gratis+ (9); "Classroom to Corporate: Transition Guide for Teachers" 19,99 $ (3); "Developer Job Searching" 19 $ (6); "USD 400K resume template" 98 $ (10); resume en chino "简历操作系统" 49 $ (39).
- Gumroad **Sam Browne, "15 LinkedIn Guides & Templates"**: pack 100 $ / Ultimate 125 $, **655 ventas visibles, 4,9 con 27 valoraciones** - https://sambrowne.gumroad.com/l/linkedin-guide-pack [PÁGINA]. (LinkedIn es la mitad del nicho; no es "cambio de carrera".)
- Tienda propia: Blue Sky Resumes "Complete System for Career Change" **49 $**, descarga inmediata, sin reseñas ni ventas visibles - https://blueskyresumes.com/guide-to-complete-system-for-career-change [PÁGINA].
- Gumroad "Switching Careers: guide to writing a resume..." 5 $, 68 págs., sin valoraciones - https://neverjobless.gumroad.com/l/switching-careers [PÁGINA] (<15 $).
**ES**
- Gumroad "curriculum": 1.096 resultados, ninguno del tema (cursos, arquitectura, etc.). https://gumroad.com/discover?query=curriculum&sort=most_reviewed&min_price=15 [PÁGINA]
- [BUSCADOR] Gumroad "Check-list de CV y guía para optimizar LinkedIn" 2,97 $ (ES); guía foto CV/LinkedIn 0+.
- Hotmart: no se encontró guía de pago del tema [BUSCADOR].

### 4. Propuestas para freelance (EN)
- Gumroad "freelance proposal" >=15 $ (119): https://gumroad.com/discover?query=freelance%20proposal&sort=most_reviewed&min_price=15 [PÁGINA]
  - "The Complete Freelancing Bundle" (Kyle Prinsloo) **45 $, 5,0 con 277 valoraciones** (freelancing general, no solo propuestas).
  - "Inside My $75K Year: Real Proposals, Job Posts, Earnings & Reviews..." 105 $+ (14) - exacto en propuestas reales.
  - "Project Proposal & Contract Bundle" (Matt Olpinski) 59 $, 3,8 (6); "Proposal Template for Freelance Creatives" 70 $ (4); "Ultimate Freelance Client Portal & Project Proposal Notion Template" 20 $ (10); "Writing Proposals on Upwork" 0+ (5); "Upwork Client Magnet" 200 $ (12); "Freelancing Freedom" 21 $ (47).
- Gumroad bundle de Olpinski 99 $ (antes 166), sin reseñas aún - https://mattolpinski.gumroad.com/l/complete-freelancing-bundle [PÁGINA]; incluye "Freelancing 101" gratis con 22 val.
- Gumroad "Freelancer Proposal Templates Bundle" (noyanlimited) **14,99 $**, 24 archivos DOCX/MD/PDF, sin valoraciones - https://noyanlimited.gumroad.com/l/ejlasq [PÁGINA] (justo <15).
- Getly "SoloFlow Client Proposal Pro Pack" (-37 %; 17 $ según [BUSCADOR]) - https://www.getly.store/product/soloflow-client-proposal-pro-pack [PÁGINA] (sin cifras de venta visibles).
- ES (no pedido como mercado; solo comprobación): Gumroad "propuesta freelance" 4 resultados: "Plantilla de Notion Propuesta de Proyecto" 16,79 $, "Herramienta Freelance" 19 $, sin valoraciones. https://gumroad.com/discover?query=propuesta%20freelance&sort=most_reviewed&min_price=15

### 5. Oposiciones (ES)
- Gumroad "oposiciones" >=15 $ (64): https://gumroad.com/discover?query=oposiciones&sort=most_reviewed&min_price=15 [PÁGINA]
  - "bibliografía para temas de oposiciones primaria inglés" (La teacher Cris) 16,79 $, **5,0 (17)**
  - "Workshop: Creating Learning Situations" (Opoteachers) 32,47 $ (11); **"Conseguir Plaza de Oposiciones Para Valientes" (Opoteachers) 33,53 $ (10)**; "Full pack of topics + relation with the curriculum" 155,62 $ (8); "Annual Programming" 16,79 $ (4); "OPOPILL I: ¿Por dónde empiezo?" 24,63 $ (6, 4,0); "PACK PROGRAMACIÓ SITUACIONS D'APRENENTATGE" 55,98 $ (5).
  - Packs de temario de Andrea (LCL) 54-335 $ sin valoraciones; "Temario Maestros de Inglés" 195,92 $ (1).
  - Todo es **oposiciones docentes** (inglés/primaria/LCL); las valoraciones son pocas pero son compradores de >=15.
- Tienda propia Red Opositor: "Kit Primer Opositor" **6,95 €** (de 12,89 €), PDF + online + ePub, 14 días de garantía, sin valoraciones visibles - https://redopositor.com/tienda/bundle-primer-opositor/ [PÁGINA]. El "Planificador Pro 49 €" del archivo 02 **NO se confirma**: la página es un **planificador gratuito** - https://redopositor.com/productos/planificador-pro/ [PÁGINA].
- Gumroad opossanidad (3 €) -> 404 hoy; https://carlyshteacher.gumroad.com/l/opoplan no cargó datos.
- Amazon.es: "Oposiciones docentes. Vol. II. Planificación, métodos de estudio y estado mental" 9,49 € Kindle, **313 valoraciones, 4,7** (ver C).

### 6. Mudanza
**EN**
- Gumroad "moving planner" >=15 $ (145): resultados casi todos ajenos; relevantes: "Home renovation/Moving planner" 46 $ (5); "Apartment Hunting & Moving Planner (Notion)" 20 $+ (4). https://gumroad.com/discover?query=moving%20planner&sort=most_reviewed&min_price=15 [PÁGINA]
- Tienda propia: Organise My House "The Moving Planner" **35 $** (Teachable), sin reseñas ni ventas visibles - https://organisemyhouse.com/moving-planner/ [PÁGINA].
- Everyday Old House "Ultimate New Home Moving Checklist Bundle" **2,99 $**, 17 printables - https://everydayoldhouse.com/shop/moving-checklist-bundle [PÁGINA].
- [BUSCADOR] Etsy 1-39 $, típicos 3-10 $ (no verificado).
**ES**
- Gumroad "mudanza" >=15 $: 5 resultados, ninguno relevante (uno de 670 $ sin contexto, 2 val.). https://gumroad.com/discover?query=mudanza&sort=most_reviewed&min_price=15 [PÁGINA]
- [BUSCADOR] checklist de pago 2,99 EUR (Payhip, no verificable).

### 7. Cachorro nuevo (plan B)
**EN**
- Gumroad "puppy training guide" >=15 $ (19): https://gumroad.com/discover?query=puppy%20training%20guide&sort=most_reviewed&min_price=15 [PÁGINA]
  - "The Puppy Success System Bundle" 19,99 $, 4,9 (8); "The Puppy Planner: Everything A New Dog Parent Needs to Know" 15 $, 5,0 (3); "Brain Games..." 39 $ (4); "Raising The World Class Puppy" 29,99 $ y "PUPPY EBOOK - REAL PUPPY SURVIVAL" 25 $ (sin valoraciones).
  - "Dog Training Planner" (Your Doggy Day) **19 $, 4,9 con 201 valoraciones** (adyacente: entrenamiento, no solo cachorro) - listado "puppy": https://gumroad.com/discover?query=puppy&sort=most_reviewed&min_price=15
- AKC (tienda propia): "New Puppy Guide (Digital Download)" **4 $**, **4,8 con 183 reseñas**, PDF - https://shop.akc.org/products/new-puppy-guide [PÁGINA] (<15 $; marca potente).
- Payhip guías de cachorro 5,99-9,99 $ [BUSCADOR] (Cloudflare, no verificado).
**ES**
- Gumroad "cachorro": 1 resultado ajeno. https://gumroad.com/discover?query=cachorro&sort=most_reviewed&min_price=15 [PÁGINA]
- Hotmart: "Bienvenido a casa: la guía para recibir a tu cachorro" https://hotmart.com/es/marketplace/productos/bienvenido-a-casa-la-guia-para-recibir-a-tu-cachorro/V102174286G y "Educa a tu cachorro en 15 días" https://hotmart.com/es/marketplace/productos/educa-a-tu-cachorro-en-15-dias-guia-definitiva/D105086254N [PÁGINA]: existen, **precio y ventas no visibles** (se cargan por JS). Tienda sin señales de venta.

---
## B. DOLOR (YouTube, resultados de búsqueda filtrados a vídeos; solo vídeos de <=5 años, específicos del tema). Capturas 03-nov-2026. Los títulos ES aparecen traducidos por el navegador; entre paréntesis edad que muestra YouTube.
Comentarios de dolor: **no leídos** en esta ronda (por eso ningún Dolor llega a 5).
URLs: `https://www.youtube.com/results?search_query=<consulta>&sp=EgIQAQ%253D%253D`

| Nicho / idioma | Consulta | Vídeos específicos (visitas, edad, canal) |
|---|---|---|
| Boda EN | wedding planning checklist step by step | The Ultimate Free Wedding Planning Checklist 207 K (4a, Jamie Wolfer); How to Plan a Wedding wedding planner 225 K (5a, Wura Manola); Philippines wedding roadmap 73 K (5a); How to Plan a Wedding 32 K (3a); plan sin planner 29 K (4m) |
| Boda ES | cómo organizar una boda paso a paso | Guía organizar boda pequeña 7,5 K (7m); boda low-cost 29 K (1a); presupuesto boda 371 (9m); guía paso a paso 14 K (3a). Los grandes (Bodas.net 126 K, Consuelo Ibarra 133 K) tienen **6 años -> fuera** |
| Meal prep EN | meal prep for beginners | Beginner's Guide to Meal Prep 2,4 M (3a, Josh Cortis); Meal Prep Under an Hour 11 M (3a, Jack Ovens); Prep Like A Chef 1,6 M (6m); Beginner friendly 248 K (2a); How to Meal Prep for Beginners 265 K (1a) |
| Batch cooking ES | batch cooking para principiantes | Revolutionary Batch Cooking Method 477 K (9m, avozmechef); ultimate batch cooking 103 K (1a, Paula Gonu); riesgos del batch cooking 92 K (5a); preparar comida semana en 2 h 50 K (5m) |
| CV EN | career change resume 2026 | Refresh Your Resume For Your Next Career Change 470 K (3a, Indeed); Tailor your resume 117 K (2a); LinkedIn job search 2026 47 K (10m); How To Get a New Job in 2026 316 K (8m, general) |
| CV ES | currículum cambio de sector | Adaptar CV si cambias de sector 6,1 K (5a); CV sin experiencia 574 K (3a, Business Insider España); Cómo crear un gran CV 2026 153 K (9m); CV +50 entrevistas 79 K (1a). **Solo 1 sobre "cambio de sector", y pequeño** |
| Propuestas EN | freelance proposal template how to write | Upwork Proposals: 8 Golden Rules 1,1 M (4a, Evan Fisher); Business Proposal with FREE Template 395 K (4a, HubSpot); Upwork proposal + free template 93 K (4a); Upwork Proposal Guide 7,5 K (9m). (ProjectManager 2,8 M tiene 12 años -> fuera) |
| Oposiciones ES | cómo organizar el estudio oposiciones | Opositar, ¿por dónde empiezo? 249 K (1a, Paco Barbié); 7 claves para preparar oposiciones 134 K (5a); Cómo empezar a estudiar oposiciones 88 K (2a); planificar tu estudio 72 K (1a); recordar lo que lees 63 K (2a) |
| Mudanza EN | moving checklist first time tips | Best House Moving Tips 769 K (3a, Clutterbug); 20 Tips for Organized Moving Day 397 K (3a); ultimate moving out checklist 201 K (1a); First Apartment Checklist 138 K (1a) |
| Mudanza ES | cómo organizar una mudanza | Moving Expert 10 tips 75 K (2a); 10 Marie Kondo tips 38 K (4a); 8 tips 28 K (2a); 11 tips Home Depot México 24 K (4a). Los >100 K tienen 6-8 años -> fuera |
| Cachorro EN | new puppy first week what to expect | Your Complete First Week Puppy Training Plan 3,2 M (5a, McCann); Avoid THESE first week MISTAKES 2,1 M (4a); First Day/Night Plan 440 K (1a); Puppy Training First 24h 532 K (4a) |
| Cachorro ES | primeros días con un cachorro | Educar a un cachorro desde el día uno 745 K (5a, Canine-Service); Kiwoko "qué necesita tu cachorro" 79 K (5a); Entrenar cachorro desde cero 72 K (3a). Los >600 K tienen 6-7 años -> fuera |

## C. DEMANDA secundaria · Amazon (ficha del líder específico; Kindle)
Fecha 03-nov-2026 [PÁGINA]. Rango = "Best Sellers Rank" en Tienda Kindle.
| Nicho | Idioma | Ficha | Precio Kindle | Valoraciones | Rango |
|---|---|---|---|---|---|
| Boda | EN | The Budget-Savvy Wedding Planner & Organizer https://www.amazon.com/dp/B078WZRT8B | 4,99 $ (papel 17,56 $) | 10.490 (4,5) | #483.302 Kindle; **#1 Wedding Budgets, #3 Wedding Planners** |
| Meal prep | EN | Smart Meal Prep for Beginners (Amidor) https://www.amazon.com/dp/B0CZ38RFRS | 0 $ (KU) / 11,83 $ compra | 1.492 (4,3) | #94.500 Kindle; "Best Seller" |
| CV | EN | Switchers (Dawn Graham) https://www.amazon.com/dp/B0789Y665J ; Change Your Resume, Change Your Career https://www.amazon.com/dp/B0CZ1HH9XG | 0 $ (KU) ; 4,99 $ | 255 ; 58 | #315.303 (#8 Job Resumes libros) ; #1.426.642 (#117 Job Resumes Kindle) |
| Propuestas | EN | Freelance Proposal Toolkit https://www.amazon.com/dp/B0H78H25KB | 7,97 $ | sin valoraciones | [SIN DATO] (ficha sin rango; publicado oct-2026) |
| Mudanza | EN | Order Your Life Moving Guide https://www.amazon.com/dp/B07PNJ7MDN | 9,99 $ | 16 (4,1) | **#3.074 en Home Cleaning, Caretaking & Relocating** (rango general Kindle no mostrado) |
| Cachorro | EN | The Art of Raising a Puppy https://www.amazon.com/dp/B0047Y0FC8 ; Ultimate Guide to Raising a Puppy (Stilwell) https://www.amazon.com/dp/B07MPTLBVB | 14,99 $ ; 11,99 $ | 4.771 ; 438 | #100.026 (#3 Dog Training) ; #1.049.544 |
| Meal prep | ES | Batch Cooking para principiantes (Palfrader) https://www.amazon.es/dp/B0HF5JTP4L | 0 € (KU) | 5 (5,0) | #83.439 Tienda Kindle (libro nuevo, ago-2026) |
| Oposiciones | ES | Oposiciones docentes Vol. II (Caballero) https://www.amazon.es/dp/B08NXPJHDY | 9,49 € | 313 (4,7) | #203.250 Tienda Kindle; #1.986 en Educación |
| Boda, CV, Mudanza, Cachorro | ES | -- | -- | -- | [SIN DATO] (Amazon.es devolvió 503 / control antirrobot) |

## D. SIN CARA · YouTube Shorts (>=100 K visitas, tema específico)
Consultas `...+%23shorts&sp=EgIYAQ%253D%253D`. Solo se anotan Shorts del tema; "sin persona" no verificable por texto -> **[SIN DATO] en todos** (hay que mirarlos en pantalla).
- Boda EN: 1 (Planning My Wedding In 6 Weeks 1,3 M, vlog con persona). Resto <12 K.
- Boda ES: 0 sobre planificación (los >100 K son decoración/quinceañera).
- Meal prep EN: 24 Shorts >=100 K (p. ej. "1 HOUR MEAL PREP" 4,5 M; "Meal Prep for a week" 1,5 M; "2-Day Meal Prep on ONE tray" 1,8 M). **Formato de encimera/bandeja muy habitual** (por títulos), no confirmado.
- Batch cooking ES: 8 (p. ej. "5 Tupperware containers. One afternoon..." 124 K; haul Mercadona 167 K; "Batchcooking ideas saludables" 236 K).
- CV EN: 4 (resume format 1,4 M, upgrade strategies 1,4 M). CV ES: 9 (435 K-1,2 M; "plantilla CV" y "errores"). Formato texto/pantalla plausible, no confirmado.
- Propuestas EN: 0. Oposiciones ES: 1 sobre tema genérico de estudio (1,2 M). Mudanza EN: 8 (packing hacks 509 K, tips 1,9 M). Mudanza ES: 0.
- Cachorro EN: 14, Cachorro ES: 30 (casi todos con perro/persona; virales de mascota).

## E. Biblioteca de anuncios de Meta
| Nicho | ES | EN |
|---|---|---|
| Todos | PENDIENTE (Fran, navegador propio) | PENDIENTE (Fran, navegador propio) |

## F. Google Trends (Estabilidad)
[SIN DATO] en todos: 429 al primer intento. Un intento (regla de la skill).
