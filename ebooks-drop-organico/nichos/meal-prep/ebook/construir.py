"""Genera datos derivados del ebook a partir de recetas-json/: platos firmados, semanas (listas de la compra),
tabla de conservación e índice de macros. Uso: python3 construir.py  -> escribe en datos/"""
import json, glob, os, re, collections
R = {os.path.basename(f)[:-5]: json.load(open(f, encoding='utf-8')) for f in glob.glob('recetas-json/*.json')}
os.makedirs('datos', exist_ok=True)
M = ['kcal', 'proteina_g', 'carbohidratos_g', 'grasa_g', 'fibra_g', 'sodio_mg']
PLATOS = {}
estr = open('../estructura.md', encoding='utf-8').read()
for cod, comp in re.findall(r'\b(M\d+|A\d+|D-\d+|C\d+) (P\d+\+B\d+\+V\d+\+S\d+)', estr):
    PLATOS[cod] = comp.split('+')
def plato(cod):
    ids = PLATOS[cod]; m = {k: round(sum(R[i]['macros_por_racion'].get(k, 0) or 0 for i in ids), 1) for k in M}
    al = sorted({a for i in ids for a in R[i]['alergenos'] if a != 'none'})
    return {'id': cod, 'componentes': ids, 'nombres': [R[i]['nombre'] for i in ids], 'macros': m,
            'kcal_redondeo': int(round(m['kcal'] / 10) * 10), 'proteina_redondeo': int(round(m['proteina_g'])),
            'alergenos': al or ['none'], 'nevera_dias_min': min(R[i]['nevera_dias'] for i in ids)}
platos = [plato(c) for c in PLATOS]
json.dump(platos, open('datos/platos.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
SEM = {1: (['P1', 'P4'], ['B1', 'B4'], ['V1', 'V2'], ['S1', 'S4', 'S8'], ['M1', 'M3', 'M10', 'A1', 'D-8'], ['D1']),
       2: (['P5', 'P2'], ['B3', 'B6'], ['V3', 'V2'], ['S3', 'S10', 'S2'], ['M4', 'M11', 'M9', 'C5', 'C8'], ['D3']),
       3: (['P6', 'P6', 'P8'], ['B5', 'B2'], ['V4', 'V3'], ['S12', 'S9', 'S4'], ['C3', 'D-5', 'A4', 'A10', 'D-3'], ['D5']),
       4: (['P9', 'P7'], ['B1', 'B2'], ['V5', 'V1'], ['S6', 'S5', 'S2'], ['A3', 'M5', 'A2', 'A7', 'A12'], ['D2'])}
semanas = {}
for n, (p, b, v, s, pl, d) in SEM.items():
    recs = p + b + v + s + d
    lista = collections.defaultdict(lambda: collections.defaultdict(float))
    for r in recs:
        for ing in R[r]['ingredientes']:
            lista[ing.get('pasillo', 'other')][ing['nombre_en']] += ing['g']
    falt = [c for c in pl if c not in PLATOS]
    ps = [x for x in platos if x['id'] in pl]
    semanas[n] = {'recetas': recs, 'platos': pl, 'faltan_platos': falt,
                  'lista_g_x1': {k: {i: round(g) for i, g in sorted(v.items())} for k, v in lista.items()},
                  'media_plato': {k: round(sum(x['macros'][k] for x in ps) / max(len(ps), 1), 1) for k in M},
                  'carne_pescado_cruda_g': round(sum(g for k, v in lista.items() if k in ('meat', 'seafood', 'fish') for g in v.values()))}
json.dump(semanas, open('datos/semanas.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
with open('datos/conservacion.md', 'w', encoding='utf-8') as f:
    f.write('| ID | Recipe | Fridge (days) | Freezer (months) | Reheat |\n|---|---|---|---|---|\n')
    for i in sorted(R, key=lambda x: (re.sub(r'\d', '', x), int(re.sub(r'\D', '', x) or 0))):
        r = R[i]; fz = r.get('congelador_meses') or 0
        f.write(f"| {i} | {r['nombre']} | {r['nevera_dias']} | {fz if fz else 'not recommended'} | {r.get('recalentar','')} |\n")
with open('datos/indice-macros.md', 'w', encoding='utf-8') as f:
    f.write('| Plate | kcal | Protein g | Carbs g | Fat g | Allergens | Fridge days |\n|---|---|---|---|---|---|---|\n')
    for x in sorted(platos, key=lambda x: -x['macros']['proteina_g']):
        m = x['macros']; f.write(f"| {x['id']} | {x['kcal_redondeo']} | {x['proteina_redondeo']} | {round(m['carbohidratos_g'])} | {round(m['grasa_g'])} | {', '.join(x['alergenos'])} | {x['nevera_dias_min']} |\n")
print(len(platos), 'platos;', {n: (s['faltan_platos'], s['carne_pescado_cruda_g'], s['media_plato']['kcal'], s['media_plato']['proteina_g']) for n, s in semanas.items()})
print('kcal', min(x['kcal_redondeo'] for x in platos), max(x['kcal_redondeo'] for x in platos), 'prot', min(x['proteina_redondeo'] for x in platos), max(x['proteina_redondeo'] for x in platos))
