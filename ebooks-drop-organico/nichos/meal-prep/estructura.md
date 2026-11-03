# Estructura del ebook · Meal prep / batch cooking (alto en proteína) · EN líder
_Skill `estructura-ebook`, 03-nov-2026, modo continuo. Entradas: `00-ficha.md`, `avatar.md`, `frases.md` ([F#]/[E#] remiten a esa tabla, con enlace), `ebooks-mercado.md`, `conocimiento/09-numeros/modelo.md`. Etiquetas: [DATO] / [OPINIÓN mentor] / [ESTIMACIÓN] / [SIN DATO]._
_Decisiones ya tomadas (Fran/orquestador): 24,99 $ (pack ampliado 39,99 $ opcional), mejor versión desde el principio, sin prueba de pago previa. Avatar: "El que ya lo intentó" (Weeknight Rescuer). Ángulos prioritarios: A2 variedad, A1 domingo de 2 h, A4 aguanta hasta el jueves, A5 coste por ración, A3 proteína contada._

## 0. Avisos previos (honestidad sobre la base)
- Las frases del avatar salen sobre todo de **lectores de libros** (Goodreads, Gumroad), no del público de vídeo: YouTube y Amazon no dieron texto [`avatar.md` Crítica]. Las frases ⚠ (F14-F18) **no se usan como ancla** de ningún capítulo.
- **Competidor nuevo detectado al comprobar el nombre** [DATO, amazon.com, 03-nov-2026]: serie Kindle *Sunday High-Protein Meal Prep* (Cal Oakes, 4 libros): "5 days of meals in 2 hours on a tight budget", versión "for One or Two… cost per serving", **4,99 $ / gratis en Kindle Unlimited, 2 valoraciones**. Coincide en la promesa (2 h, presupuesto, 1-2 personas, coste por ración). Señal débil de venta, pero obliga a que nuestro diferencial **se vea en las imágenes**: hoja del domingo, tabla de conservación, tabla de combinaciones (no basta con decirlo).
- Ningún texto de la competencia copiado; solo estructura.

## 1. Mínimo del mercado + diferencial
### 1.1 Mínimo (de `ebooks-mercado.md`; obligatorio, no diferencia)
Macros por receta · ingredientes con cantidades exactas · PDF instantáneo · pasos simples · 100+ recetas **o** plan de 30 días · (en los de ≥27 $) lista de la compra, guía de meal prep, bonos.

### 1.2 Diferencial: ganar en los 3 huecos (cada uno con su fuente)
| Hueco | Qué hacemos | Ángulo | Fuente |
|---|---|---|---|
| **A. Sistema, no recetas sueltas** | Plan de 4 semanas donde cada semana = **una hoja de domingo** (orden de cocina minuto a minuto, cantidades por comida) + lista de la compra por pasillos + menú de 5 platos, todo enlazado a las fichas con macros. Y recetas por **componentes** (proteína + base + verdura + salsa) para "elegir y combinar". | A1, A2, A8 | F19-F22 (Goodreads, claridad, "no deviating from the set weeks"), F24 (monotonía), F9-F10 (plan + lista), hueco 1 de `ebooks-mercado.md` |
| **B. Conservación y coste por ración** | Cada ficha: días en nevera / congelador, cómo recalentar, qué guardar aparte (salsas, pasta). **Regla del día 5**: lo del viernes se congela el domingo. Coste por ración y coste de la semana. | A4, A5 | F25, F30, E2-E4 (sabor/textura al recalentar), F27-F29, F32-F33; hueco 2-3 de `ebooks-mercado.md` |
| **C. Macros con fuente oficial + alérgenos** | Macros calculadas con USDA FoodData Central SR Legacy (`herramientas/macros.py`), por componente **y** por plato; iconos de los 9 alérgenos principales de EE. UU. (FDA: leche, huevo, pescado, marisco, frutos de cáscara, cacahuete, trigo, soja, sésamo). | A3, A12 | F2, F4, F11; hueco 4 de `ebooks-mercado.md` |

Extra que nadie ofrece [ESTIMACIÓN, a partir de las páginas vistas]: **raciones para 1 o 2 personas** (columna ×2 en todas las listas) [Cook Once, Goodreads: "Our household has two adults…"] y **página de despensa** [F11 "list some of the items to keep stocked in your pantry", F13].

## 2. Pack y precio
### 2.1 Sistema combinatorio y número de recetas (la decisión clave)
**Fórmula del plato**: 1 proteína + 1 base + 1 verdura + 1 salsa (+ desayuno aparte). Las salsas son el motor de la variedad (A2, F24): la misma tanda de pollo cambia de plato al cambiar de salsa.

| Bloque | Nº recetas | Para qué |
|---|---|---|
| Proteínas | 10 | 6 de carne/pescado + 1 "estirada" con lenteja + 3 vegetales; intercambiables (A11, F27-F28) |
| Bases | 6 | arroz, quinoa, patata, boniato, pasta, wraps (sin cocinar) |
| Verduras | 6 | 4 al horno/sartén + 2 crudas (se montan el día) |
| Salsas | 12 | 3 por familia de sabor: México, Asia, Mediterráneo, Comfort (EE. UU.) |
| Desayunos | 8 | F23 ("only for one meal a day") |
| Bloque congelador (platos de una olla) | 10 | "cocina una vez, come dos" (A10, F1) |
| Snacks altos en proteína | 8 | completan el día |
| **Total recetas** | **60** | |
| **Platos firmados** (combinaciones probadas, con foto, macros y coste del plato montado) | **48** | 12 por familia de sabor |
| **Combinaciones compatibles** (tabla "Mix & Match" por reglas de sabor) | **2.106** | calculado por script: de 4.320 combinaciones posibles (10×6×6×12), las que respetan la familia de sabor de cada pieza |

**Por qué 60 y no 100-220** [ESTIMACIÓN argumentada]:
1. El dolor del avatar no es "me faltan recetas", es **aburrirse, perder el domingo y que no cuadre** (F3, F19-F22, F24, F26). 200 recetas sueltas reproducen el problema de F5 ("random recipes"); 60 componentes con sistema lo resuelven.
2. Valor percibido comparable sin inflar: **60 recetas + 48 platos montados con macros + plan de 4 semanas + tabla de 2.000+ combinaciones** (FeastRecipes 220 recetas a 29,99 $; Stealth Health 110 a ~25-30 $). En la página de producto se cuentan **60 recetas y 48 platos**, nunca "2.000 recetas".
3. Calidad verificable: cada receta lleva macros calculadas, conservación, coste y alérgenos. Con 60 es realista calcularlo todo bien (y que Fran cocine 3-5); con 200 no.
4. Las 2.106 combinaciones **no están probadas una a una**: se presentan como "tabla de emparejamientos"; las probadas son las 48. Las macros de cualquier combinación se suman con la tabla de macros por ración de cada componente (A3).

**Comprobación de macros** [DATO, `macros.py`, USDA SR Legacy]: plato muestra 140 g muslo de pollo asado + 150 g arroz + 100 g brócoli + 50 g yogur griego desnatado = **510 kcal, 46 g proteína**; 90 g ternera 93 % + 80 g lenteja + 150 g arroz + 100 g brócoli = **496 kcal, 38 g proteína, 10 g fibra**. → Objetivo realista: **platos de 450-600 kcal con 30-45 g de proteína**; los platos vegetales (tofu, garbanzo) bajarán a ~20-28 g y se muestra su cifra real, sin redondear al alza.

### 2.2 Qué incluye el pack (24,99 $)
| Pieza | Qué es | Ángulo / por qué | Extensión [ESTIMACIÓN] |
|---|---|---|---|
| 1. **Ebook principal "The Sunday Sheet"** (PDF pantalla, Letter, índice con enlaces, letra grande legible en móvil/tablet) | Método + plan 4 semanas + 60 recetas + 48 platos + referencia | A1, A2, A3, A4, A5 | ~165 págs. |
| 2. **Pack imprimible** (PDF, Letter y A4, apto blanco y negro) | 4 hojas de domingo rellenas + 1 en blanco · 4 listas de la compra por pasillos (×1 y ×2 personas) + 1 en blanco · **tabla de conservación** de las 60 recetas · tabla Mix & Match (póster de 1 pág.) · despensa (checklist) · etiquetas de tupper "comer antes de" (lun-vie) · hoja "monta tu plato" (suma de macros) · hoja de coste por ración | A1, A4, A5, A3 · F10, F11, F13, F20 | ~30 págs. |
| 3. **Tarjetas de nevera** (5 págs. del imprimible, formato media hoja) | Regla del día 5 + recalentado por componente + las 12 salsas en una vista | A4, A2 | incl. en 2 |

**Pack ampliado (opcional, 39,99 $)**: + semanas 5-12 (8 planes más con hoja de domingo y lista, reutilizando las 60 recetas) + hoja de cálculo editable (Google Sheets/Excel: escala ×1/×2, lista de la compra automática, macros y coste de cualquier combinación). No se recorta nada del pack de 24,99 $ para crear el ampliado.

### 2.3 Precio objetivo y ancla
- **24,99 $** [decidido; ESTIMACIÓN de mercado]. Rango del mercado digital: Kindle 4,99-14,99 $; Gumroad 17-30 $ (FeastRecipes 29,99 $, PrepWithDrew 27 $, Ozirats 27 $); Stealth Health 29,99 $ suelto / 49,99 $ pack de 2 [DATO, `ebooks-mercado.md`].
- **Ancla honesta (sin precios tachados falsos)**: (1) por debajo del ebook suelto de la marca líder (29,99 $) e igual a su precio por libro dentro del pack (25 $); (2) **por comida planificada**: 4 semanas × 10 comidas = 40 comidas → **0,62 $ por comida planificada**; (3) lo que ningún pack de ≤30 $ junta: plan + hoja de domingo + conservación + coste + macros USDA + alérgenos + imprimibles.
- **Por qué vale más que lo que ya existe**: frente al Kindle de 4,99 $ con la misma promesa, damos el *sistema visible* (hojas imprimibles, tabla de conservación, combinaciones con macros). Riesgo: si la página no lo enseña en imágenes, el comprador compara por nº de recetas y perdemos.
- **Impuestos**: EE. UU. sin IVA (algunos estados cobran *sales tax* sobre productos digitales: lo calcula Shopify; revisar en el módulo 7). UE: ebook al **4 %** (tipo español) mientras las ventas a otros países de la UE no superen 10.000 €/año; por encima, ventanilla OSS con el tipo de cada país. Precio en la UE con IVA incluido → ingreso neto ≈ 24,03 $.
- Margen: ≈ 91-93 % por venta [`modelo.md` §5]; equilibrio con alta B1 a ≥19,99 € = 7 ventas/mes.

### 2.4 Imagen "qué incluye" y mockups
(Kate [aEjAqXPJjJE], [OPINIÓN mentor]) Una imagen con: tablet con la portada · una **hoja de domingo** real impresa (protagonista) · tabla de conservación · tarjeta de las 12 salsas · móvil con una ficha (macros + alérgenos + "4 días nevera / 3 meses congelador"). Mockups con páginas reales del PDF (skill `imagenes-producto`), sin fotos de terceros.

## 3. Índice
**Formato elegido**: 4 partes (Sistema → Plan → Recetas → Referencia). Por qué: el mercado agrupa por tipo de plato (Stealth) o por momento del día (FeastRecipes) y por eso "no hay forma de salirse de las semanas fijas" [F22]; nosotros damos **plan cerrado para empezar** (A8) **y** componentes para combinar después (A2). Cada ficha de receta: rendimiento exacto en gramos y tuppers, macros por ración (USDA), coste por ración, alérgenos, nevera/congelador/recalentar, "va con" (salsas y bases compatibles).

| Nº | Título provisional (EN) | Problema que resuelve | Frase real (EN + enlace) | Ejercicio / herramienta | Resultado para el lector |
|---|---|---|---|---|---|
| 0 | Start Here: How This Book Works | No saber por dónde empezar con un libro de recetas más | F5 "way easier than trying to find random recipes online" · https://feastrecipes.gumroad.com/l/jbwsvt | Ruta de 3 caminos: "sigue la semana 1" / "monta tus platos" / "solo congelador". Aviso: no sustituye a un dietista; seguridad alimentaria según USDA FSIS | Sabe qué hacer el primer domingo |
| **Parte 1 · El sistema** | | | | | |
| 1 | Why Meal Prep Gets Old by Wednesday | Aburrimiento y abandono a mitad de semana | F24 "…got really old really fast" · https://www.goodreads.com/book/show/44765223-cook-once-eat-all-week ; F3 | Fórmula del plato (proteína + base + verdura + salsa) y las 4 familias de sabor | Entiende cómo 1 tanda da 5 platos distintos |
| 2 | The 2-Hour Sunday: Reading Your Sheet | Domingo perdido por instrucciones confusas | F19 "…more frustration than I wanted to put into a day off" · https://www.goodreads.com/en/book/show/44287434-batch-cooking | Anatomía de la hoja: horno → fuego → frío → montaje, con minutos y quién va primero | Cocina sin releer recetas ni improvisar el orden |
| 3 | Portions That Add Up | Raciones que no cuadran; libros "para 4" | F26 "recipe portions are inconsistent…" (Cook Once, enlace arriba); F20 | Tabla de gramos por plato y por tupper; columna ×1 / ×2 personas | Sabe cuánto sale antes de empezar |
| 4 | Will It Last Until Thursday? Storage, Freezing, Reheating | Miedo a que se estropee o sepa mal; tirar comida | F30 "is it fine to store my food like this for four-five days?" · https://www.reddit.com/r/MealPrepSunday/top/?t=year ; F25 | **Regla del día 5** (nevera 3-4 días según USDA FSIS → lo del viernes al congelador el domingo); enfriado rápido (arroz); salsas y aliños aparte; recalentado por componente | Come el jueves sin dudas y sin tirar nada |
| 5 | What a Plate Really Costs | Gastar de más; carne cara | F27 "This book calls for 4-5 lbs of meat minimum, each week." (Cook Once); F33 "108 meals for $246.31…" (Reddit, enlace arriba) | Método de coste por ración (fecha y fuente de precios), estirar carne con lenteja, comprar paquetes enteros | Conoce el coste de su semana y de cada plato |
| 6 | Protein You Can Count | Comida "de dieta" sin sabor o macros sin fiabilidad | F4 "…they just taste like normal food" (FeastRecipes); F11 "Presenting the macros is a great plus" · https://prepwithdrew.gumroad.com/l/mealplan | Cómo se calcularon (USDA, gramos cocinados vs crudos); hoja "monta tu plato" que suma componentes; clave de alérgenos | Sabe la proteína de cualquier combinación |
| 7 | Your Pantry & Gear on One Page | Comprar de todo cada semana; no saber qué tener | F11 "…list some of the items to keep stocked in your pantry"; F13 "…essential spices, sauces, equipment…" · https://chefcaleb.gumroad.com/l/cookbook | Checklist de despensa (≈25 básicos) + 6 utensilios | Compra una vez la base y la lista semanal se acorta |
| **Parte 2 · El plan de 4 semanas** | | | | | |
| 8 | Week 1 · The Starter Week (oven-only) | No tener que decidir nada la primera vez | F9 "I loved not having to figure out what to eat." (fragmento) · https://ozirats.gumroad.com/l/Get30DayPlan | Hoja de domingo + lista + menú de 5 platos + coste y macros de la semana | Primera semana hecha a la primera |
| 9 | Week 2 · The Budget Week | Coste semanal alto | F28 "…it gets expensive and hard to source all the meat…" (Cook Once) | Ídem; proteína estirada con lenteja y pollo en olla lenta | Semana más barata, misma proteína contada |
| 10 | Week 3 · The Freezer-Ahead Week | Falta de tiempo las semanas siguientes | F1 "Keep em in the freezer and you're good for weeks." · https://soberfitness.gumroad.com/l/thebigbean | Ídem + doble tanda de albóndigas al congelador | Reserva en el congelador para una semana sin domingo |
| 11 | Week 4 · The Mix-It-Yourself Week | Depender del libro; plan rígido | F22 "…pick and chose recipes to batch cook together. There is no deviating from the set weeks." (Batch Cooking, enlace arriba) | Semana guiada a medias: elige 2 salsas de la tabla, la hoja se rellena con plantilla | Sabe crear sus propias semanas |
| **Parte 3 · Recetas** | | | | | |
| 12 | Proteins (10) | Carne cara, siempre pollo | F27-F28 | Fichas + "cambia por" | Proteína base de la semana |
| 13 | Bases (6) | Pasta/arroz que saben mal al recalentar | (ES, para la adaptación) E3 "…lo caliento al micro me sabe fatal" · https://www.mediavida.com/foro/cocina/meal-prep-590373/8 [SIN DATO en EN] | Punto de cocción para recalentar, cómo guardar | Bases con textura el jueves |
| 14 | Vegetables (6) | Verdura blanda/aguada | [SIN DATO] (técnica estándar) | Asar vs crudo y cuándo montar | Verdura que aguanta |
| 15 | Sauces (12) · the variety engine | Monotonía | F11 "…you reuse a lot of ingredients, seasonings, and sauces…"; F24 | 12 salsas, 3 por familia, cada una con "va con" | 5 platos con 1 tanda |
| 16 | 48 Signature Plates + Mix & Match Chart | Combinar sin pensar | F22 | Platos montados (macros/coste/alérgenos del plato) + tabla de 2.106 emparejamientos | Más de un mes sin repetir plato |
| 17 | Breakfasts (8) | Solo cubrir una comida | F23 "…it's only for one meal a day…" (Batch Cooking) | Desayunos de tanda | Mañanas resueltas |
| 18 | The Freezer Block (10 one-pot meals) | Semanas sin domingo | F1 | Una olla, raciones a congelar, descongelar y recalentar | Comida de reserva |
| 19 | High-Protein Snacks (8) | Picar sin control de proteína | [SIN DATO] | Cajas de snack | Tentempiés con cifra |
| **Parte 4 · Referencia** | | | | | |
| 20 | Storage Chart (all 60 recipes) | Dudas de conservación | F30 | Tabla nevera/congelador/recalentar | Consulta en 5 s |
| 21 | Macro, Cost & Allergen Index | Buscar por proteína o alérgeno | F11 | Índice ordenable por proteína, kcal, coste y "sin X" | Encuentra el plato que encaja |
| 22 | When Things Go Wrong | Recetas que fallan y frustran | F21 "…If only someone had… written better instructions." (Batch Cooking) | 15 problemas típicos (pollo seco, arroz duro, salsa aguada…) y cómo arreglarlos | No abandona por un fallo |
| 23 | Blank Templates | Seguir solo tras la semana 4 | F10 "The grocery list and meal plan made everything so much easier." (fragmento, Ozirats) | Hoja de domingo, lista, monta tu plato, coste | Sigue el sistema sin el libro |

**Extensión objetivo** [ESTIMACIÓN]: ebook ~165 págs. (Parte 1 ≈ 22 · Parte 2 ≈ 20 · fichas de receta 60 ≈ 66 · 48 platos ≈ 26 · Parte 4 ≈ 22 · portada, índice, avisos ≈ 9) + imprimible ~30 págs. El mercado está en 86-132 págs. [DATO]; vamos algo por encima por las hojas y tablas, no por relleno.

### 3.1 Lista completa de recetas (60) — nombre EN · componente
**Proteínas (P)** — familia de sabor compatible entre paréntesis (MEX / ASI / MED / COM; "todas" = neutra)
P1 Lemon-Garlic Sheet-Pan Chicken Thighs (todas) · P2 Slow-Cooker Salsa Shredded Chicken (MEX, COM) · P3 Never-Dry Baked Chicken Breast (todas) · P4 Turkey Taco Crumble (MEX) · P5 Beef & Lentil Power Mince (MEX, MED, COM) · P6 Freezer Turkey Meatballs (MED, COM, ASI) · P7 Oven Pulled Pork Shoulder (MEX, COM, ASI) · P8 Simple Baked Salmon (todas; comer los 2 primeros días por calidad) · P9 Crispy Baked Tofu (ASI, MEX, MED) · P10 Smoky Spiced Chickpeas (MED, MEX)
**Bases (B)**: B1 Hands-Off Oven Rice · B2 Fluffy Quinoa · B3 Crispy Roasted Baby Potatoes · B4 Roasted Sweet Potato Cubes · B5 Reheat-Ready Pasta (al dente, aceitada) · B6 Wraps & Tortillas (sin cocinar: cómo guardar y montar)
**Verduras (V)**: V1 Charred Roasted Broccoli · V2 Sheet-Pan Fajita Peppers & Onions · V3 Roasted Zucchini & Red Onion · V4 Garlic Green Beans · V5 Sesame Cabbage-Carrot Slaw (crudo) · V6 Chopped Cucumber-Tomato Salad (crudo, se monta el día)
**Salsas (S)**: MEX: S1 Chipotle-Lime Yogurt · S2 Tomatillo Salsa Verde · S3 Quick Red Enchilada Sauce — ASI: S4 Lighter Teriyaki · S5 Peanut-Ginger · S6 Gochujang-Honey — MED: S7 Tzatziki · S8 Lemon-Tahini · S9 Chimichurri — COM: S10 Smoky BBQ (menos azúcar) · S11 Honey-Mustard Yogurt · S12 Creamy Tomato-Garlic
**Desayunos (D)**: D1 Spinach-Feta Egg Bites · D2 Turkey & Pepper Egg Bites · D3 Greek Yogurt Overnight Oats · D4 Peanut Butter-Banana Overnight Oats · D5 Freezer Breakfast Burritos · D6 Cottage Cheese Baked Oats · D7 Freezer Protein Pancakes · D8 Turkey Sausage & Sweet Potato Hash
**Bloque congelador (FM)**: FM1 Turkey Three-Bean Chili · FM2 Chicken Tikka-Style Curry · FM3 Beef & Lentil Ragù · FM4 Chicken Enchilada Bake · FM5 Turkey Sausage & Lentil Soup · FM6 Chicken Tortilla Soup · FM7 Teriyaki Chicken Fried Rice · FM8 Turkey Meatball & Orzo Bake · FM9 Black Bean & Sweet Potato Burritos · FM10 Creamy Chicken & Broccoli Pasta Bake
**Snacks (SN)**: SN1 Greek Yogurt Protein Cups (3 sabores) · SN2 Hummus & Veg Boxes · SN3 Perfect Hard-Boiled Eggs · SN4 Peanut Butter Oat Bites · SN5 Crunchy Roasted Chickpeas · SN6 Turkey & Cheese Roll-Ups · SN7 Cottage Cheese Ranch Dip · SN8 Edamame Snack Boxes

**48 platos firmados** (proteína + base + verdura + salsa)
- **MEX**: M1 P1+B1+V2+S1 · M2 P2+B1+V6+S2 · M3 P4+B4+V2+S1 · M4 P5+B6+V3+S3 · M5 P7+B1+V5+S2 · M6 P9+B2+V2+S1 · M7 P10+B6+V6+S2 · M8 P8+B1+V5+S1 · M9 P2+B3+V3+S2 · M10 P4+B1+V1+S1 · M11 P2+B6+V2+S3 · M12 P5+B3+V1+S1
- **ASI**: A1 P1+B1+V1+S4 · A2 P9+B2+V5+S5 · A3 P7+B1+V5+S6 · A4 P8+B2+V4+S4 · A5 P3+B4+V1+S5 · A6 P6+B1+V4+S6 · A7 P9+B1+V1+S6 · A8 P1+B5+V5+S5 · A9 P8+B1+V1+S6 · A10 P6+B5+V4+S4 · A11 P3+B4+V4+S6 · A12 P7+B2+V1+S5
- **MED**: D-1 P1+B1+V6+S7 · D-2 P10+B2+V3+S8 · D-3 P8+B2+V3+S9 · D-4 P3+B6+V6+S7 · D-5 P6+B2+V4+S9 · D-6 P5+B1+V6+S8 · D-7 P9+B2+V1+S8 · D-8 P1+B4+V1+S8 · D-9 P10+B6+V3+S7 · D-10 P8+B1+V6+S7 · D-11 P3+B3+V1+S8 · D-12 P6+B6+V6+S7
- **COM**: C1 P1+B3+V4+S10 · C2 P7+B4+V1+S10 · C3 P6+B5+V3+S12 · C4 P3+B1+V4+S11 · C5 P5+B3+V2+S10 · C6 P8+B3+V1+S11 · C7 P1+B5+V1+S12 · C8 P2+B6+V2+S10 · C9 P3+B6+V3+S11 · C10 P5+B5+V3+S12 · C11 P7+B1+V4+S10 · C12 P6+B4+V4+S11
(Los nombres comerciales de cada plato se escriben al redactar; aquí va la composición.)

### 3.2 Plan de 4 semanas (resumen) — 10 comidas (5 comidas + 5 cenas para 1, o 5 comidas para 2) + 5 desayunos
| Semana | Proteínas | Bases | Verduras | Salsas | Platos (cada uno ×2) | Desayuno | Notas [ESTIMACIÓN hasta cocinarlo] |
|---|---|---|---|---|---|---|---|
| 1 Starter (solo horno + arroz) | P1, P4 | B1, B4 | V1, V2 | S1, S4, S8 | M1, M3, M10, A1, D-8 | D1 | ≤ 2 h; ~1,9 kg carne cruda; viernes congelado |
| 2 Budget | P5, P2 | B3, B6 | V3, V2 | S3, S10, S2 | M4, M11, M9, C5, C8 | D3 | olla lenta trabaja sola; carne ~1,1 kg (lenteja estira) |
| 3 Freezer-ahead | P6 (doble), P8 | B5, B2 | V4, V3 | S12, S9, S4 | C3, D-5, A4, A10, D-3 | D5 | salmón lun-mar; 10 albóndigas extra al congelador |
| 4 Mix-it-yourself | P9, P7 | B1, B2 | V5, V1 | S6, S5, S2 | A3, M5, A2, A7, A12 | D2 | el lector elige 1 salsa con la tabla; carne ~0,9 kg |
Cada semana: hoja de domingo (1 pág. a doble cara si hace falta), lista de la compra por pasillos ×1/×2, coste total y por ración, macros medias por día.

## 4. Muestra gratis
**"The Mini Sunday"** (≈12 págs., PDF a cambio del email):
- 1 pág. del método (fórmula del plato + regla del día 5).
- **1 proteína (P1) + 1 base (B1) + 1 verdura (V1) + 3 salsas (S1, S4, S8) → 3 platos distintos, 5 tuppers**, en unos 60-75 min [ESTIMACIÓN].
- Su hoja de domingo, su lista de la compra (×1/×2), sus filas de la tabla de conservación, coste por ración, macros USDA y alérgenos.
- 1 pág. final: qué añade el pack (la tabla Mix & Match en miniatura, **recortada** a 1 familia de sabor).

**Por qué esta parte**: demuestra los 5 ángulos prioritarios a la vez con lo mínimo (A2 tres salsas, A1 hoja, A4 conservación, A5 coste, A3 macros) y es **útil por sí sola** (una semana corta real). Lleva al pack de forma natural: el lector ya probó el truco de las salsas y quiere las 12, la segunda proteína y las 4 semanas. Usa los mismos componentes que la semana 1, así el comprador empieza con algo conocido.
**Captación del email** (Kate [w2FbEhhhVMw], [OPINIÓN mentor]): enlace en la bio y fijado en vídeos de A2 ("same 3 bases… the sauce trick") → formulario → PDF por email + secuencia corta. RGPD y doble opt-in en módulo 7.

## 5. Idiomas
- **EN líder** (EE. UU.): Letter, onzas/libras **y** gramos, °F y °C, precios en $, tiendas y productos de EE. UU. (Costco aparece en F33), alérgenos FDA (9).
- **ES (después de validar EN)**: A4, gramos y °C, precios de supermercado español, alérgenos UE (14), y **ajuste de avatar, no traducción**: en ES pesa más el sabor/textura al recalentar (E2-E4) y el estilo mediterráneo (E1) → la familia MED y el capítulo 4 suben de peso; COM (BBQ, honey-mustard) se adapta. Precio ES 14,90 € (`00-ficha.md`).
- Control: revisor con modelo distinto + retrotraducción al español para Fran.

## 6. Qué falta antes de redactar (no bloquea)
1. Calcular con `macros.py` las 60 recetas y los 48 platos (gramos cocinados, entrada USDA correcta).
2. Coste por ración con fuente y fecha (precios medios BLS o un súper de EE. UU. concreto), mostrado como "aprox., varía por tienda".
3. Tabla de conservación con USDA FSIS (nevera 3-4 días sobras cocinadas; congelador calidad 2-4 meses; regla de las 2 horas).
4. **Cronometrar la semana 1 y la muestra** (Fran o alguien real) antes de usar "2 hours" en anuncios.
5. Comprobar marca en USPTO (TESS) para "The Sunday Sheet".

---
## Crítica (agente `critico`, una pasada, 03-nov-2026)
**Veredicto inicial: CAMBIOS. Tras aplicarlos: APROBADO CON RESERVAS.**

Coincide con los datos:
- Los 3 huecos están anclados en frases reales enlazadas o en `ebooks-mercado.md`; ningún capítulo usa frases ⚠. [DATO]
- Sin promesas de peso ni salud; se habla de tiempo, coste, variedad y proteína. [DATO]

Fallos detectados y aplicados:
1. **Riesgo de inflar el número**: sería tentador anunciar "2.000+ meals"; las combinaciones no están probadas → aplicado: se venden **60 recetas + 48 platos**; las 2.106 se llaman "tabla de emparejamientos" (§2.1 punto 4).
2. **"Hasta el jueves" vs seguridad alimentaria**: cocinar el domingo y comer el viernes son 5 días, por encima de los 3-4 de USDA FSIS. Aplicado: **regla del día 5** (viernes al congelador el domingo) y salmón los dos primeros días (§3, cap. 4; §3.2).
3. **Contradicción con el avatar**: F27 critica "4-5 lbs of meat each week" y la semana 1 lleva ~1,9 kg (≈4,2 lb) para una persona. Aplicado: se declara la cantidad por semana y las semanas 2 y 4 la bajan con lenteja y tofu (§3.2).
4. **Proteína de platos vegetales**: no llegan a 30 g; aplicado: se muestra la cifra real, sin promedio que la tape (§2.1).
5. **IVA**: el 4 % solo vale mientras las ventas a otros países UE < 10.000 €/año (luego OSS) y en EE. UU. puede haber sales tax estatal. Aplicado (§2.3).
6. **Competidor con la misma promesa a 4,99 $** (Cal Oakes): el precio solo se sostiene si el sistema se ve. Aplicado: imágenes con la hoja real y la tabla de conservación como protagonistas (§0, §2.4).
7. Cap. 13 se apoyaba en una frase ES para el ebook EN: marcado [SIN DATO en EN].

Lo que sigue débil (necesita datos, no redacción):
- **"2 hours"** no está comprobado: si la semana 1 cronometrada pasa de 2 h, cambiar a "about 2 hours" o recortar la semana. Riesgo principal.
- **60 recetas frente a 100-220** puede leerse como menos valor; se comprueba con la conversión de la página (métricas de lanzamiento) y, si cae, se sube el bloque de platos firmados antes que añadir recetas sueltas.
- Avatar de lector de libros, no de espectador de vídeo (heredado de `avatar.md`).
- Sin ESCALAR A FABLE: todo es reversible al redactar.
