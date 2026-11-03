"""Calcula calorías y macros de una receta con la base oficial USDA SR Legacy (dominio público).
Uso:  python3 herramientas/macros.py buscar "chicken breast roasted"
      python3 herramientas/macros.py receta receta.json
receta.json: {"raciones": 4, "ingredientes": [{"fdc_id": "171477", "g": 600, "nombre": "pechuga de pollo asada"}, ...]}
Los gramos son del alimento en el estado de la descripción USDA (crudo o cocinado: elegir la entrada correcta)."""
import csv, json, sys, os
T = os.path.join(os.path.dirname(__file__), 'usda', 'macros-100g.csv')
rows = list(csv.DictReader(open(T, encoding='utf-8')))
idx = {r['fdc_id']: r for r in rows}
if sys.argv[1] == 'buscar':
    q = sys.argv[2].lower().split()
    for r in [r for r in rows if all(w in r['descripcion'].lower() for w in q)][:15]:
        print(r['fdc_id'], '|', r['descripcion'], '|', r['kcal'], 'kcal', r['proteina_g'], 'g prot /100 g')
else:
    rec = json.load(open(sys.argv[2], encoding='utf-8'))
    tot = {k: 0.0 for k in ['kcal', 'proteina_g', 'grasa_g', 'carbohidratos_g', 'fibra_g', 'sodio_mg']}
    for ing in rec['ingredientes']:
        r = idx[str(ing['fdc_id'])]
        for k in tot: tot[k] += float(r[k] or 0) * ing['g'] / 100
    n = rec.get('raciones', 1)
    print(json.dumps({'por_racion': {k: round(v / n, 1) for k, v in tot.items()}, 'total': {k: round(v, 1) for k, v in tot.items()}, 'raciones': n, 'fuente': 'USDA FoodData Central SR Legacy (2018-04)'}, ensure_ascii=False))
