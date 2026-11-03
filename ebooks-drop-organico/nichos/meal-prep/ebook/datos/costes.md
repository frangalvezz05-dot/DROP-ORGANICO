# Costes (USDA ERS)

Generado por `herramientas/costes.py` el 2026-11-03.

- Carne, huevos y lacteos: USDA ERS (series BLS/ERS), Sep 2026.
- Frutas y verduras: USDA ERS, **2023 retail scanner data (Circana), latest ERS year** (precio medio de un ano concreto, no del mes actual).
- Despensa, especias, salsas y algunos cortes sin dato ERS: **[ESTIMACION]** propia, marcada en `herramientas/precios/precios-ingredientes.csv`.
- Sin factor de rendimiento (peso comprado = peso de la receta). Receta = suma(g/453,6 x $/lb). Plato = suma de sus 4 componentes por racion.
- Parte del coste que es [DATO ERS]: **36.0 %** del total de todas las recetas; el resto es [ESTIMACION].

## Por semana (recetas de semanas.json; semana 3 incluye P6 dos veces tal como esta en el plan)

| Semana | x1 | x2 | Media por plato | % DATO |
|---|---|---|---|---|
| 1 | $43.72 | $87.43 | $3.67 | 34.2 % |
| 2 | $47.15 | $94.30 | $3.64 | 61.8 % |
| 3 | $71.36 | $142.72 | $4.84 | 17.7 % |
| 4 | $39.63 | $79.26 | $3.23 | 26.6 % |

## Por plato (4 componentes, 1 racion)

| Plato | Componentes | $/plato | % DATO |
|---|---|---|---|
| M1 | Lemon-Garlic Sheet-Pan Chicken Thighs + Hands-Off Oven Rice + Sheet-Pan Fajita Peppers & Onions + Chipotle-Lime Yogurt | $2.83 | 19.9 % |
| M2 | Slow-Cooker Salsa Shredded Chicken + Hands-Off Oven Rice + Chopped Cucumber-Tomato Salad (raw) + Tomatillo Salsa Verde | $3.47 | 66.7 % |
| M3 | Turkey Taco Crumble + Roasted Sweet Potato Cubes + Sheet-Pan Fajita Peppers & Onions + Chipotle-Lime Yogurt | $4.15 | 27.7 % |
| M4 | Beef & Lentil Power Mince + Wraps & Tortillas (Store & Assemble) + Roasted Zucchini & Red Onion + Quick Red Enchilada Sauce | $3.38 | 76.2 % |
| M5 | Oven Pulled Pork Shoulder + Hands-Off Oven Rice + Sesame Cabbage-Carrot Slaw (raw) + Tomatillo Salsa Verde | $3.23 | 7.6 % |
| M6 | Crispy Baked Tofu + Fluffy Quinoa + Sheet-Pan Fajita Peppers & Onions + Chipotle-Lime Yogurt | $2.85 | 19.8 % |
| M7 | Smoky Spiced Chickpeas + Wraps & Tortillas (Store & Assemble) + Chopped Cucumber-Tomato Salad (raw) + Tomatillo Salsa Verde | $1.82 | 25.4 % |
| M8 | Simple Baked Salmon + Hands-Off Oven Rice + Sesame Cabbage-Carrot Slaw (raw) + Chipotle-Lime Yogurt | $5.51 | 4.2 % |
| M9 | Slow-Cooker Salsa Shredded Chicken + Crispy Roasted Baby Potatoes + Roasted Zucchini & Red Onion + Tomatillo Salsa Verde | $3.95 | 73.7 % |
| M10 | Turkey Taco Crumble + Hands-Off Oven Rice + Charred Roasted Broccoli + Chipotle-Lime Yogurt | $4.31 | 30.0 % |
| M11 | Slow-Cooker Salsa Shredded Chicken + Wraps & Tortillas (Store & Assemble) + Sheet-Pan Fajita Peppers & Onions + Quick Red Enchilada Sauce | $3.68 | 65.7 % |
| M12 | Beef & Lentil Power Mince + Crispy Roasted Baby Potatoes + Charred Roasted Broccoli + Chipotle-Lime Yogurt | $4.27 | 83.5 % |
| A1 | Lemon-Garlic Sheet-Pan Chicken Thighs + Hands-Off Oven Rice + Charred Roasted Broccoli + Lighter Teriyaki | $3.25 | 37.7 % |
| A2 | Crispy Baked Tofu + Fluffy Quinoa + Sesame Cabbage-Carrot Slaw (raw) + Peanut-Ginger Sauce | $2.44 | 9.4 % |
| A3 | Oven Pulled Pork Shoulder + Hands-Off Oven Rice + Sesame Cabbage-Carrot Slaw (raw) + Gochujang-Honey Sauce | $3.22 | 7.2 % |
| A4 | Simple Baked Salmon + Fluffy Quinoa + Garlic Green Beans + Lighter Teriyaki | $6.10 | 13.5 % |
| A5 | Never-Dry Baked Chicken Breast + Roasted Sweet Potato Cubes + Charred Roasted Broccoli + Peanut-Ginger Sauce | $3.98 | 90.2 % |
| A6 | Freezer Turkey Meatballs + Hands-Off Oven Rice + Garlic Green Beans + Gochujang-Honey Sauce | $3.82 | 22.5 % |
| A7 | Crispy Baked Tofu + Hands-Off Oven Rice + Charred Roasted Broccoli + Gochujang-Honey Sauce | $3.00 | 40.8 % |
| A8 | Lemon-Garlic Sheet-Pan Chicken Thighs + Reheat-Ready Pasta + Sesame Cabbage-Carrot Slaw (raw) + Peanut-Ginger Sauce | $2.54 | 9.1 % |
| A9 | Simple Baked Salmon + Hands-Off Oven Rice + Charred Roasted Broccoli + Gochujang-Honey Sauce | $6.19 | 19.8 % |
| A10 | Freezer Turkey Meatballs + Reheat-Ready Pasta + Garlic Green Beans + Lighter Teriyaki | $3.87 | 22.2 % |
| A11 | Never-Dry Baked Chicken Breast + Roasted Sweet Potato Cubes + Garlic Green Beans + Gochujang-Honey Sauce | $3.70 | 86.1 % |
| A12 | Oven Pulled Pork Shoulder + Fluffy Quinoa + Charred Roasted Broccoli + Peanut-Ginger Sauce | $4.26 | 28.7 % |
| D-1 | Lemon-Garlic Sheet-Pan Chicken Thighs + Hands-Off Oven Rice + Chopped Cucumber-Tomato Salad (raw) + Tzatziki | $2.70 | 17.3 % |
| D-2 | Smoky Spiced Chickpeas + Fluffy Quinoa + Roasted Zucchini & Red Onion + Lemon-Tahini Sauce | $2.12 | 30.0 % |
| D-3 | Simple Baked Salmon + Fluffy Quinoa + Roasted Zucchini & Red Onion + Chimichurri | $6.10 | 10.4 % |
| D-4 | Never-Dry Baked Chicken Breast + Wraps & Tortillas (Store & Assemble) + Chopped Cucumber-Tomato Salad (raw) + Tzatziki | $3.21 | 72.4 % |
| D-5 | Freezer Turkey Meatballs + Fluffy Quinoa + Garlic Green Beans + Chimichurri | $4.28 | 20.1 % |
| D-6 | Beef & Lentil Power Mince + Hands-Off Oven Rice + Chopped Cucumber-Tomato Salad (raw) + Lemon-Tahini Sauce | $3.16 | 75.6 % |
| D-7 | Crispy Baked Tofu + Fluffy Quinoa + Charred Roasted Broccoli + Lemon-Tahini Sauce | $3.37 | 36.3 % |
| D-8 | Lemon-Garlic Sheet-Pan Chicken Thighs + Roasted Sweet Potato Cubes + Charred Roasted Broccoli + Lemon-Tahini Sauce | $3.79 | 45.9 % |
| D-9 | Smoky Spiced Chickpeas + Wraps & Tortillas (Store & Assemble) + Roasted Zucchini & Red Onion + Tzatziki | $2.02 | 32.3 % |
| D-10 | Simple Baked Salmon + Hands-Off Oven Rice + Chopped Cucumber-Tomato Salad (raw) + Tzatziki | $5.58 | 8.4 % |
| D-11 | Never-Dry Baked Chicken Breast + Crispy Roasted Baby Potatoes + Charred Roasted Broccoli + Lemon-Tahini Sauce | $4.00 | 87.0 % |
| D-12 | Freezer Turkey Meatballs + Wraps & Tortillas (Store & Assemble) + Chopped Cucumber-Tomato Salad (raw) + Tzatziki | $3.76 | 13.4 % |
| C1 | Lemon-Garlic Sheet-Pan Chicken Thighs + Crispy Roasted Baby Potatoes + Garlic Green Beans + Smoky BBQ Sauce (Less Sugar) | $3.24 | 37.9 % |
| C2 | Oven Pulled Pork Shoulder + Roasted Sweet Potato Cubes + Charred Roasted Broccoli + Smoky BBQ Sauce (Less Sugar) | $4.41 | 39.4 % |
| C3 | Freezer Turkey Meatballs + Reheat-Ready Pasta + Roasted Zucchini & Red Onion + Creamy Tomato-Garlic Sauce | $3.84 | 17.5 % |
| C4 | Never-Dry Baked Chicken Breast + Hands-Off Oven Rice + Garlic Green Beans + Honey-Mustard Yogurt | $3.38 | 79.1 % |
| C5 | Beef & Lentil Power Mince + Crispy Roasted Baby Potatoes + Sheet-Pan Fajita Peppers & Onions + Smoky BBQ Sauce (Less Sugar) | $3.50 | 83.1 % |
| C6 | Simple Baked Salmon + Crispy Roasted Baby Potatoes + Charred Roasted Broccoli + Honey-Mustard Yogurt | $6.65 | 24.5 % |
| C7 | Lemon-Garlic Sheet-Pan Chicken Thighs + Reheat-Ready Pasta + Charred Roasted Broccoli + Creamy Tomato-Garlic Sauce | $3.53 | 34.7 % |
| C8 | Slow-Cooker Salsa Shredded Chicken + Wraps & Tortillas (Store & Assemble) + Sheet-Pan Fajita Peppers & Onions + Smoky BBQ Sauce (Less Sugar) | $3.69 | 65.4 % |
| C9 | Never-Dry Baked Chicken Breast + Wraps & Tortillas (Store & Assemble) + Roasted Zucchini & Red Onion + Honey-Mustard Yogurt | $3.38 | 73.7 % |
| C10 | Beef & Lentil Power Mince + Reheat-Ready Pasta + Roasted Zucchini & Red Onion + Creamy Tomato-Garlic Sauce | $3.47 | 74.1 % |
| C11 | Oven Pulled Pork Shoulder + Hands-Off Oven Rice + Garlic Green Beans + Smoky BBQ Sauce (Less Sugar) | $3.61 | 22.7 % |
| C12 | Freezer Turkey Meatballs + Roasted Sweet Potato Cubes + Garlic Green Beans + Honey-Mustard Yogurt | $4.38 | 31.4 % |

## Por receta

| ID | Receta | Raciones | $ receta | $/racion | % DATO |
|---|---|---|---|---|---|
| B1 | Hands-Off Oven Rice | 5 | $0.80 | $0.16 | 0 % |
| B2 | Fluffy Quinoa | 5 | $2.43 | $0.49 | 0 % |
| B3 | Crispy Roasted Baby Potatoes | 5 | $2.51 | $0.50 | 81 % |
| B4 | Roasted Sweet Potato Cubes | 5 | $3.00 | $0.60 | 86 % |
| B5 | Reheat-Ready Pasta | 5 | $1.39 | $0.28 | 0 % |
| B6 | Wraps & Tortillas (Store & Assemble) | 5 | $1.76 | $0.35 | 0 % |
| D1 | Spinach-Feta Egg Bites | 5 | $5.32 | $1.06 | 58 % |
| D2 | Turkey & Pepper Egg Bites | 5 | $6.06 | $1.21 | 52 % |
| D3 | Greek Yogurt Overnight Oats | 5 | $9.77 | $1.95 | 21 % |
| D4 | Peanut Butter-Banana Overnight Oats | 5 | $5.39 | $1.08 | 6 % |
| D5 | Freezer Breakfast Burritos | 5 | $7.43 | $1.49 | 67 % |
| D6 | Cottage Cheese Baked Oats | 5 | $9.51 | $1.90 | 29 % |
| D7 | Freezer Protein Pancakes | 5 | $4.67 | $0.94 | 19 % |
| D8 | Turkey Sausage & Sweet Potato Hash | 5 | $8.52 | $1.70 | 29 % |
| FM1 | Turkey Three-Bean Chili | 6 | $19.16 | $3.19 | 30 % |
| FM10 | Creamy Chicken & Broccoli Pasta Bake | 6 | $13.99 | $2.33 | 63 % |
| FM2 | Chicken Tikka-Style Curry | 6 | $17.03 | $2.84 | 18 % |
| FM3 | Beef & Lentil Ragù | 6 | $18.18 | $3.03 | 79 % |
| FM4 | Chicken Enchilada Bake | 6 | $19.07 | $3.18 | 53 % |
| FM5 | Turkey Sausage & Lentil Soup | 6 | $16.06 | $2.68 | 26 % |
| FM6 | Chicken Tortilla Soup | 6 | $21.65 | $3.61 | 59 % |
| FM7 | Teriyaki Chicken Fried Rice | 6 | $10.68 | $1.78 | 76 % |
| FM8 | Turkey Meatball & Orzo Bake | 6 | $17.52 | $2.92 | 9 % |
| FM9 | Black Bean & Sweet Potato Burritos | 6 | $11.13 | $1.85 | 31 % |
| P1 | Lemon-Garlic Sheet-Pan Chicken Thighs | 5 | $8.02 | $1.60 | 0 % |
| P10 | Smoky Spiced Chickpeas | 5 | $3.02 | $0.60 | 0 % |
| P2 | Slow-Cooker Salsa Shredded Chicken | 5 | $12.22 | $2.44 | 76 % |
| P3 | Never-Dry Baked Chicken Breast | 5 | $9.59 | $1.92 | 97 % |
| P4 | Turkey Taco Crumble | 5 | $12.42 | $2.48 | 3 % |
| P5 | Beef & Lentil Power Mince | 5 | $10.51 | $2.10 | 92 % |
| P6 | Freezer Turkey Meatballs | 5 | $12.36 | $2.47 | 2 % |
| P7 | Oven Pulled Pork Shoulder | 5 | $11.56 | $2.31 | 0 % |
| P8 | Simple Baked Salmon | 5 | $22.45 | $4.49 | 0 % |
| P9 | Crispy Baked Tofu | 5 | $6.48 | $1.30 | 0 % |
| S1 | Chipotle-Lime Yogurt | 5 | $1.82 | $0.36 | 0 % |
| S10 | Smoky BBQ Sauce (Less Sugar) | 5 | $0.97 | $0.19 | 0 % |
| S11 | Honey-Mustard Yogurt | 5 | $1.80 | $0.36 | 0 % |
| S12 | Creamy Tomato-Garlic Sauce | 5 | $1.72 | $0.34 | 0 % |
| S2 | Tomatillo Salsa Verde | 5 | $1.26 | $0.25 | 6 % |
| S3 | Quick Red Enchilada Sauce | 5 | $0.88 | $0.18 | 0 % |
| S4 | Lighter Teriyaki | 5 | $0.89 | $0.18 | 0 % |
| S5 | Peanut-Ginger Sauce | 5 | $0.79 | $0.16 | 0 % |
| S6 | Gochujang-Honey Sauce | 5 | $1.21 | $0.24 | 0 % |
| S7 | Tzatziki | 5 | $1.61 | $0.32 | 6 % |
| S8 | Lemon-Tahini Sauce | 5 | $1.41 | $0.28 | 0 % |
| S9 | Chimichurri | 5 | $1.87 | $0.37 | 0 % |
| SN1 | Greek Yogurt Protein Cups (3 flavors) | 5 | $11.62 | $2.32 | 9 % |
| SN2 | Hummus & Veg Boxes | 5 | $8.37 | $1.67 | 32 % |
| SN3 | Perfect Hard-Boiled Eggs | 5 | $1.92 | $0.39 | 98 % |
| SN4 | Peanut Butter Oat Bites | 5 | $3.07 | $0.61 | 0 % |
| SN5 | Crunchy Roasted Chickpeas | 5 | $2.61 | $0.52 | 0 % |
| SN6 | Turkey & Cheese Roll-Ups | 5 | $9.45 | $1.89 | 4 % |
| SN7 | Cottage Cheese Ranch Dip | 5 | $7.05 | $1.41 | 31 % |
| SN8 | Edamame Snack Boxes | 5 | $8.24 | $1.65 | 40 % |
| V1 | Charred Roasted Broccoli | 5 | $6.52 | $1.30 | 94 % |
| V2 | Sheet-Pan Fajita Peppers & Onions | 5 | $3.53 | $0.70 | 80 % |
| V3 | Roasted Zucchini & Red Onion | 5 | $3.74 | $0.75 | 85 % |
| V4 | Garlic Green Beans | 5 | $4.72 | $0.94 | 87 % |
| V5 | Sesame Cabbage-Carrot Slaw (raw) | 5 | $2.51 | $0.50 | 46 % |
| V6 | Chopped Cucumber-Tomato Salad (raw) | 5 | $3.07 | $0.61 | 73 % |
