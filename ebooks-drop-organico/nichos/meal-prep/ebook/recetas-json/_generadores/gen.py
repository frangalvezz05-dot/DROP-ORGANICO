import sys,json,subprocess,re
sys.path.insert(0,'/tmp/claude-0/-home-user-DROP-ORGANICO/4ce7a1d8-1de6-5411-8950-9de4ad94e99b/scratchpad')
from data import K,R
base='nichos/meal-prep/ebook/'
est=open('nichos/meal-prep/estructura.md',encoding='utf-8').read()
plates=re.findall(r'([A-Z]-?\d+) ((?:P|B|V|S)\d+(?:\+\w+)+)',est)
def goes(i):
    ps=[n for n,c in plates if i in c.split('+')]
    return ps
def r10(x): return int(round(x/10.0)*10)
summ=[]
for r in R:
    ings=[]
    for k,us,g in r['ing']:
        f,n,p,e=K[k]
        ings.append({'nombre_en':n,'cantidad_us':us,'g':g,'fdc_id':f,'pasillo':p,'estado':e})
    n_=5
    j={'id':r['id'],'nombre':r['nombre'],'componente':r['comp'],'familias':r['fam'],'raciones':5,'rinde_g_cocinado':r['yld'],'racion_g':round(r['yld']/5),
       'ingredientes':ings,'macros_por_racion':None,'alergenos':r['alerg'] or ['none'],'nevera_dias':r['fr'],'congelador_meses':r['fz'],'recalentar':r['reheat'],
       'tiempo_activo_min':r['act'],'tiempo_total_min':r['tot'],'horno_c':r['oven'][0] if r['oven'] else None,'horno_f':r['oven'][1] if r['oven'] else None}
    pth=f"{base}recetas-json/{r['id']}.json"
    json.dump(j,open(pth,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
    out=subprocess.run(['python3','herramientas/macros.py','receta',pth],capture_output=True,text=True,check=True).stdout
    m=json.loads(out)['por_racion']
    j['macros_por_racion']=m
    json.dump(j,open(pth,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
    oven=f"{r['oven'][1]} °F / {r['oven'][0]} °C" if r['oven'] else 'none'
    fz=f"{r['fz']} months" if r['fz'] else 'not recommended (texture)'
    fr=f"{r['fr']} days"+(' (opened package)' if r['id']=='B6' else '')
    al=', '.join(r['alerg']) or 'none'
    gw=goes(r['id']); gws=', '.join(gw) if gw else '-'
    L=[f"### {r['id']} · {r['nombre']}",'',
     f"**Makes:** 5 portions (about {round(r['yld']/5)} g cooked each) · **Active:** {r['act']} min · **Total:** {r['tot']} min · **Oven:** {oven}",
     f"**Per portion:** {r10(m['kcal'])} kcal · {round(m['proteina_g'])} g protein · {round(m['carbohidratos_g'])} g carbs · {round(m['grasa_g'])} g fat (USDA FoodData Central) · **Allergens:** {al}",
     f"**Fridge:** {fr} · **Freezer:** {fz} · **Reheat:** {r['reheat']}",
     f"**Goes with:** signature dishes {gws}"+(f" · flavour families {', '.join(r['fam'])}"),'','**Ingredients** (US + metric)']
    for k,us,g in r['ing']:
        L.append(f"- {us} {K[k][1]} ({g:g} g)" if not K[k][1] in us else f"- {us} ({g:g} g)")
    L+=['','**Steps**']+[f"{i}. {s}" for i,s in enumerate(r['steps'],1)]
    L+=['',f"**Sunday-sheet slot:** {r['slot_txt']}",'**Fix it:**']+[f"- {x}" for x in r['fix']]+['',f"**Swap:** {r['swap']}",'']
    open(f"{base}en/recetas/{r['id']}.md",'w',encoding='utf-8').write('\n'.join(L))
    summ.append((r['id'],r10(m['kcal']),round(m['proteina_g']),al,r['fr'],round(r['yld']/5),m))
t=['# Resumen P-B-V (macros por ración, calculadas con herramientas/macros.py; USDA SR Legacy)','','| ID | kcal | Proteína (g) | Carbs (g) | Grasa (g) | Alérgenos | Nevera (días) | g cocinados/ración |','|---|---|---|---|---|---|---|---|']
for i,k,p,a,f,g,m in summ: t.append(f"| {i} | {k} | {p} | {round(m['carbohidratos_g'])} | {round(m['grasa_g'])} | {a} | {f} | {g} |")
open(base+'recetas-json/_resumen-P-B-V.md','w',encoding='utf-8').write('\n'.join(t)+'\n')
print('\n'.join(t))
