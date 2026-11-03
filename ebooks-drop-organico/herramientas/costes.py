"""Coste por racion, plato y semana con precios USDA ERS (descargados en herramientas/precios/).
Uso (desde ebooks-drop-organico):  python3 herramientas/costes.py
Lee:  herramientas/precios/*.csv  y  nichos/meal-prep/ebook/{recetas-json,datos}
Escribe: herramientas/precios/precios-ingredientes.csv, ebook/datos/costes.json, ebook/datos/costes.md
Reglas: [DATO ERS] = el numero sale de un CSV oficial del ERS (con conversion de unidades si hace falta).
        [ESTIMACION] = referencia propia razonable (o producto sustituto), NO es dato oficial.
Simplificaciones: no se aplica factor de rendimiento (el precio es por lb comprada); 1 lb = 453.6 g."""
import csv, json, glob, os, re, collections
B = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(B, 'precios')
E = os.path.join(B, '..', 'nichos', 'meal-prep', 'ebook')
LB = 453.6
FECHA = '2026-11-03'
PER_CARNE = 'Sep 2026'
PER_FV = '2023 retail scanner data (Circana), latest ERS year'
def rd(f): return list(csv.DictReader(open(os.path.join(P, f), encoding='utf-8-sig')))
carne = {}
for r in rd('carne-lacteos.csv'):
    if r['Value'] not in ('NA', ''): carne[r['Data_Item']] = float(r['Value'])  # ultimo valor numerico (orden cronologico)
def fv(f, nombre, forma):
    for r in rd(f):
        if r[list(r)[0]] == nombre and r['Form'] == forma: return float(r['AverageRetailPrice'])
    raise KeyError(nombre)
V = lambda n, f='Fresh': fv('verduras.csv', n, f)
F = lambda n, f='Fresh': fv('frutas.csv', n, f)
huevo_lb = carne['Eggs, Grade A large retail price'] / (12 * 50 / LB)      # huevo grande ~50 g
leche_lb = carne['Milk, fresh, whole, fortified-gallon retail price'] / (3785 * 1.03 / LB)
S_C = 'USDA ERS/BLS retail meat-dairy-eggs, ' + PER_CARNE
S_V = 'USDA ERS Vegetable Prices, ' + PER_FV
S_F = 'USDA ERS Fruit Prices, ' + PER_FV
D, X = 'DATO ERS', 'ESTIMACION'
# (regex sobre nombre_en en minusculas, precio $/lb, fuente, tipo, nota). Primera coincidencia gana.
EST = 'Estimacion propia (referencia supermercado EE. UU.)'
R = [
 (r'^water$', 0, 'agua del grifo', D, 'coste 0'),
 (r'chicken breast', carne['Chicken boneless breast retail price'], S_C, D, ''),
 (r'chicken thighs', 3.50, EST, X, 'boneless; el ERS solo publica pechuga y muslo con hueso'),
 (r'ground beef|beef \(90', carne['Lean & extra lean ground beef retail price'], S_C, D, 'lean & extra lean'),
 (r'ground turkey', 5.50, EST, X, ''),
 (r'pork shoulder', 3.60, EST, X, 'ERS no publica paleta'),
 (r'salmon', 11.00, EST, X, ''),
 (r'turkey sausage', 6.50, EST, X, ''),
 (r'deli turkey', 10.00, EST, X, ''),
 (r'\begg', huevo_lb, S_C + ' (docena -> lb, huevo ~50 g)', D, ''),
 (r'1% milk', leche_lb, S_C + ' (galon entero -> lb)', X, 'sustituto: leche entera'),
 (r'cheddar', carne['Cheddar cheese, natural retail price'], S_C, D, ''),
 (r'mozzarella|mexican-blend|monterey|swiss', carne['Cheddar cheese, natural retail price'], S_C, X, 'sustituto: precio del cheddar'),
 (r'parmesan', 9.00, EST, X, ''),
 (r'feta', 7.50, EST, X, ''),
 (r'cottage cheese', 3.50, EST, X, ''),
 (r'cream cheese', 4.50, EST, X, ''),
 (r'greek yogurt', 3.80, EST, X, ''),
 (r'^butter', 5.00, EST, X, ''),
 (r'baby carrots', V('Carrots, baby'), S_V, D, ''),
 (r'carrots', V('Carrots, raw whole'), S_V, D, ''),
 (r'baby red potatoes', V('Potatoes'), S_V, D, 'patata fresca'),
 (r'sweet potatoes', V('Sweet potatoes'), S_V, D, ''),
 (r'baby spinach', V('Spinach, eaten raw'), S_V, D, ''),
 (r'red bell pepper', V('Red peppers'), S_V, D, ''),
 (r'bell pepper', (V('Green peppers') + V('Red peppers')) / 2, S_V, D, 'media pimiento verde y rojo'),
 (r'broccoli', V('Broccoli florets'), S_V, D, ''),
 (r'celery', V('Celery, trimmed bunches'), S_V, D, ''),
 (r'cherry tomatoes', V('Tomatoes, grape and cherry'), S_V, D, ''),
 (r'tomatoes \(roma', V('Tomatoes, Roma and plum'), S_V, D, 'Roma'),
 (r'cucumber', V('Cucumbers with peel'), S_V, D, ''),
 (r'frozen corn', V('Corn', 'Frozen'), S_V, D, ''),
 (r'frozen mixed', V('Mixed vegetables, carrots, peas, corn, and green beans', 'Frozen'), S_V, D, ''),
 (r'edamame', 3.50, EST, X, ''),
 (r'green beans', V('Green beans'), S_V, D, ''),
 (r'green cabbage', V('Cabbage, green'), S_V, D, ''),
 (r'kale', V('Kale'), S_V, D, ''),
 (r'zucchini', V('Zucchini'), S_V, D, ''),
 (r'onion powder', 9.00, EST, X, ''),
 (r'onion', V('Onions'), S_V, D, ''),
 (r'banana', F('Bananas'), S_F, D, ''),
 (r'blueberries', F('Blueberries'), S_F, D, 'fresca'),
 (r'strawberries', F('Strawberries'), S_F, D, 'fresca'),
 (r'black beans', V('Black beans', 'Canned'), S_V, D, 'enlatadas'),
 (r'kidney beans', V('Kidney beans', 'Canned'), S_V, D, 'enlatadas'),
 (r'pinto beans', V('Pinto beans', 'Canned'), S_V, D, 'enlatadas'),
 (r'lentils', V('Lentils', 'Dried'), S_V, D, 'secas'),
 (r'chickpeas', 1.40, EST, X, 'no esta en el CSV del ERS'),
 (r'crushed tomatoes|diced tomatoes', V('Tomatoes', 'Canned'), S_V, D, 'tomate enlatado'),
 (r'tomato paste', 4.00, EST, X, ''),
 (r'tomato sauce|marinara|enchilada', 2.00, EST, X, ''),
 (r'chipotle', 4.50, EST, X, ''),
 (r'coconut milk', 2.60, EST, X, ''),
 (r'broth', 1.30, EST, X, ''),
 (r'salsa', 3.00, EST, X, ''),
 (r'tofu', 2.80, EST, X, ''),
 (r'garlic powder', 8.00, EST, X, ''),
 (r'garlic', 4.00, EST, X, ''),
 (r'ginger, ', 4.00, EST, X, ''),
 (r'jalape', 2.50, EST, X, ''),
 (r'scallions', 3.50, EST, X, ''),
 (r'cilantro|parsley', 5.00, EST, X, 'hierba fresca'),
 (r'tomatillos', 2.50, EST, X, ''),
 (r'lemon juice|lime juice', 4.50, EST, X, ''),
 (r'vinegar', 2.00, EST, X, ''),
 (r'rice, cooked', 0.80, EST, X, 'arroz cocido (~1/3 del coste en seco por peso)'),
 (r'rice', 1.00, EST, X, ''),
 (r'oats', 1.80, EST, X, ''),
 (r'quinoa', 4.00, EST, X, ''),
 (r'barley', 1.50, EST, X, ''),
 (r'pasta|spaghetti|orzo', 1.60, EST, X, ''),
 (r'tortilla', 3.20, EST, X, ''),
 (r'flour', 0.80, EST, X, ''),
 (r'breadcrumbs', 2.50, EST, X, ''),
 (r'cornstarch', 1.80, EST, X, ''),
 (r'baking powder', 3.50, EST, X, ''),
 (r'sugar', 1.50, EST, X, ''),
 (r'honey', 4.50, EST, X, ''),
 (r'maple', 12.00, EST, X, ''),
 (r'olive oil', 5.50, EST, X, ''),
 (r'canola|cooking spray', 2.00, EST, X, ''),
 (r'sesame oil', 10.00, EST, X, ''),
 (r'sesame seeds', 7.00, EST, X, ''),
 (r'chia', 6.00, EST, X, ''),
 (r'flaxseed', 4.00, EST, X, ''),
 (r'walnuts', 8.00, EST, X, ''),
 (r'almonds', 8.00, EST, X, ''),
 (r'peanut butter', 3.20, EST, X, ''),
 (r'tahini', 7.00, EST, X, ''),
 (r'hummus', 5.50, EST, X, ''),
 (r'cocoa', 8.00, EST, X, ''),
 (r'vanilla', 60.00, EST, X, ''),
 (r'soy sauce|teriyaki', 3.00, EST, X, ''),
 (r'worcestershire', 3.50, EST, X, ''),
 (r'mustard', 2.20, EST, X, ''),
 (r'ketchup', 1.80, EST, X, ''),
 (r'sriracha', 4.00, EST, X, ''),
 (r'gochujang', 6.00, EST, X, ''),
 (r'salt', 1.50, EST, X, 'sal'),
 (r'black pepper', 14.00, EST, X, 'especia, por gramo usado'),
 (r'cayenne|chili powder|red pepper flakes|paprika|everything', 9.00, EST, X, 'especia, por gramo usado'),
 (r'cumin|curry|turmeric|ginger|cinnamon|oregano|thyme|dill', 12.00, EST, X, 'especia, por gramo usado'),
]
def precio(n):
    k = n.lower()
    for rx, p, s, t, nota in R:
        if re.search(rx, k): return p, s, t, nota
    raise KeyError('SIN PRECIO: ' + n)
rec = {os.path.basename(f)[:-5]: json.load(open(f, encoding='utf-8')) for f in glob.glob(os.path.join(E, 'recetas-json', '*.json'))}
nombres = sorted({i['nombre_en'] for r in rec.values() for i in r['ingredientes']})
pr = {n: precio(n) for n in nombres}
with open(os.path.join(P, 'precios-ingredientes.csv'), 'w', encoding='utf-8', newline='') as fh:
    w = csv.writer(fh); w.writerow(['nombre_en', 'usd_por_lb', 'fuente', 'fecha', 'tipo', 'nota'])
    for n in nombres:
        p, s, t, nota = pr[n]; w.writerow([n, round(p, 3), s, FECHA, '[%s]' % t, nota])
def coste_receta(cod):
    r = rec[cod]; tot = dato = 0.0
    for i in r['ingredientes']:
        p, s, t, _ = pr[i['nombre_en']]; c = i['g'] / LB * p
        tot += c; dato += c if t == D else 0
    n = r['raciones']
    return {'id': cod, 'nombre': r['nombre'], 'raciones': n, 'coste_receta': round(tot, 3), 'coste_racion': round(tot / n, 3), 'dato': round(dato, 3)}
RC = {c: coste_receta(c) for c in sorted(rec)}
platos = json.load(open(os.path.join(E, 'datos', 'platos.json'), encoding='utf-8'))
PC = []
for p in platos:
    cs = [RC[c] for c in p['componentes']]
    tot = sum(c['coste_racion'] for c in cs); d = sum(c['dato'] / c['raciones'] for c in cs)
    PC.append({'id': p['id'], 'nombres': p['nombres'], 'coste_plato': round(tot, 3), 'pct_dato': round(100 * d / tot, 1)})
sem = json.load(open(os.path.join(E, 'datos', 'semanas.json'), encoding='utf-8'))
SC = {}
for n, s in sem.items():
    t = sum(RC[c]['coste_receta'] for c in s['recetas']); d = sum(RC[c]['dato'] for c in s['recetas'])
    SC[n] = {'recetas': s['recetas'], 'platos': s['platos'], 'x1': round(t, 2), 'x2': round(2 * t, 2), 'pct_dato': round(100 * d / t, 1),
             'media_plato': round(sum(next(p['coste_plato'] for p in PC if p['id'] == x) for x in s['platos']) / len(s['platos']), 3)}
td = sum(r['coste_receta'] for r in RC.values()); dd = sum(r['dato'] for r in RC.values())
res = {'periodos': {'carne_lacteos_huevos': PER_CARNE + ' (ERS/BLS, ultimo mes del CSV; el CSV cubre sep 2024 - sep 2026)',
                    'frutas_verduras': PER_FV + ' (precio medio anual, no mensual)'},
       'descarga': FECHA, 'pct_dato_global': round(100 * dd / td, 1), 'media_plato': round(sum(p['coste_plato'] for p in PC) / len(PC), 3),
       'recetas': RC, 'platos': PC, 'semanas': SC}
json.dump(res, open(os.path.join(E, 'datos', 'costes.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
r5 = lambda x: round(round(x / 0.05) * 0.05, 2)
L = ['# Costes (USDA ERS)', '', 'Generado por `herramientas/costes.py` el %s.' % FECHA, '',
     '- Carne, huevos y lacteos: USDA ERS (series BLS/ERS), %s.' % PER_CARNE,
     '- Frutas y verduras: USDA ERS, **%s** (precio medio de un ano concreto, no del mes actual).' % PER_FV,
     '- Despensa, especias, salsas y algunos cortes sin dato ERS: **[ESTIMACION]** propia, marcada en `herramientas/precios/precios-ingredientes.csv`.',
     '- Sin factor de rendimiento (peso comprado = peso de la receta). Receta = suma(g/453,6 x $/lb). Plato = suma de sus 4 componentes por racion.',
     '- Parte del coste que es [DATO ERS]: **%.1f %%** del total de todas las recetas; el resto es [ESTIMACION].' % res['pct_dato_global'], '',
     '## Por semana (recetas de semanas.json; semana 3 incluye P6 dos veces tal como esta en el plan)', '',
     '| Semana | x1 | x2 | Media por plato | % DATO |', '|---|---|---|---|---|']
for n, s in SC.items(): L.append('| %s | $%.2f | $%.2f | $%.2f | %s %% |' % (n, s['x1'], s['x2'], s['media_plato'], s['pct_dato']))
L += ['', '## Por plato (4 componentes, 1 racion)', '', '| Plato | Componentes | $/plato | % DATO |', '|---|---|---|---|']
for p in PC: L.append('| %s | %s | $%.2f | %s %% |' % (p['id'], ' + '.join(p['nombres']), p['coste_plato'], p['pct_dato']))
L += ['', '## Por receta', '', '| ID | Receta | Raciones | $ receta | $/racion | % DATO |', '|---|---|---|---|---|---|']
for c, r in RC.items(): L.append('| %s | %s | %s | $%.2f | $%.2f | %.0f %% |' % (c, r['nombre'], r['raciones'], r['coste_receta'], r['coste_racion'], 100 * r['dato'] / r['coste_receta'] if r['coste_receta'] else 0))
open(os.path.join(E, 'datos', 'costes.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
# ---- ebook: fichas y capitulo 5
NOTA = 'US average retail prices, USDA ERS (meat, eggs, dairy: %s; fruit and vegetables: 2023 data); your store will differ.' % PER_CARNE
n_f = 0
for f in glob.glob(os.path.join(E, 'en', 'recetas', '*.md')):
    cod = os.path.basename(f)[:-3]
    if cod not in RC: continue
    t = open(f, encoding='utf-8').read()
    if '**Cost/portion:**' in t: continue
    t2 = re.sub(r'(\*\*Per portion:\*\*[^\n]*\n)', lambda m: m.group(1) + '**Cost/portion:** about $%.2f (%s)\n' % (r5(RC[cod]['coste_racion']), NOTA), t, count=1)
    if t2 != t: open(f, 'w', encoding='utf-8').write(t2); n_f += 1
tabla = ['| Week | Plates (avg. per plate) | One batch | Double batch (x2) |', '|---|---|---|---|']
for n, s in SC.items(): tabla.append('| %s | $%.2f | $%.2f | $%.2f |' % (n, r5(s['media_plato']), r5(s['x1']), r5(s['x2'])))
ct = ['The table below uses the recipes of each weekly sheet. "One batch" is the full shopping for that week as written in the recipes; "double batch" is the same plan cooked twice. A plate is one protein + one base + one vegetable + one sauce, one portion each.', '', *tabla, '',
      'Across all 48 signature plates the average is about **$%.2f per plate** (cheapest $%.2f, priciest $%.2f).' % (r5(res['media_plato']), r5(min(p['coste_plato'] for p in PC)), r5(max(p['coste_plato'] for p in PC))), '',
      '*%s Pantry items, spices and sauces without a USDA figure are our own reference estimates (about %.0f%% of the total comes from USDA data). Rounded to the nearest 5 cents; no yield loss from trimming is applied.*' % (NOTA, res['pct_dato_global'])]
c5 = os.path.join(E, 'en', '05-cost.md'); t = open(c5, encoding='utf-8').read()
t = re.sub(r'\[COST_TABLE\]\n\n<!-- \[COST_TABLE\][^\n]*-->', '\n'.join(ct), t)
open(c5, 'w', encoding='utf-8').write(t)
print(json.dumps({'fichas': n_f, 'media_plato': res['media_plato'], 'pct_dato': res['pct_dato_global'], 'semanas': {k: (v['x1'], v['x2'], v['pct_dato']) for k, v in SC.items()},
                  'min': min(PC, key=lambda p: p['coste_plato'])['coste_plato'], 'max': max(PC, key=lambda p: p['coste_plato'])['coste_plato']}))
