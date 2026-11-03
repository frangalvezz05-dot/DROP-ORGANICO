# Formato común de ficha de receta (EN) — The Sunday Sheet

Cada receta: un archivo `ebook/en/recetas/<ID>.md` y su `ebook/recetas-json/<ID>.json`.

## JSON (para recalcular macros, coste y listas de la compra)
{"id":"P1","nombre":"Lemon-Garlic Sheet-Pan Chicken Thighs","componente":"proteina","familias":["MEX","ASI","MED","COM"],
 "raciones":5,"rinde_g_cocinado":750,"racion_g":150,
 "ingredientes":[{"nombre_en":"boneless skinless chicken thighs","cantidad_us":"2 lb","g":907,"fdc_id":"<id USDA crudo>","pasillo":"meat","estado":"raw"}, ...],
 "macros_por_racion": <salida de herramientas/macros.py: por_racion>,
 "alergenos":["none" | "milk","egg","fish","shellfish","tree nuts","peanuts","wheat","soy","sesame"],
 "nevera_dias":3, "congelador_meses":3, "recalentar":"...", "tiempo_activo_min":10, "tiempo_total_min":35, "horno_c":220, "horno_f":425}
- Gramos del ingrediente en el estado de la entrada USDA (crudo si la entrada es cruda). Aceite y salsas cuentan.
- Conservación según USDA FSIS (nevera 3-4 días para carne cocinada; congelador 2-6 meses según producto). Temperaturas internas seguras: aves 165 °F/74 °C; carne picada 160 °F/71 °C; cerdo 145 °F/63 °C + reposo; pescado 145 °F/63 °C.
- Coste: NO se calcula ahora (lo hará un script con una tabla de precios oficial).

## Ficha (Markdown, inglés, tono del avatar: frases cortas, 2.ª persona)
### <ID> · <Nombre>
**Makes:** 5 portions (150 g each) · **Active:** 10 min · **Total:** 35 min · **Oven:** 425 °F / 220 °C
**Per portion:** XXX kcal · XX g protein · XX g carbs · XX g fat (USDA FoodData Central) · **Allergens:** ...
**Fridge:** 3 days · **Freezer:** 3 months · **Reheat:** ...
**Goes with:** bases / salsas / platos firmados que la usan (IDs de `estructura.md` §3.1)

**Ingredients** (US + métrico)
**Steps** (numerados, 4-8, cada uno con una señal visible de "hecho": color, textura, temperatura)
**Sunday-sheet slot:** horno / fuego / frío y en qué minuto encaja
**Fix it:** 1-2 fallos típicos y cómo arreglarlos
**Swap:** 1 cambio (alergia, presupuesto o gusto)

Reglas: técnicas estándar y seguras; nada copiado de otros libros; sin promesas de peso/salud; kcal redondeadas a 10, proteína a 1 g.
