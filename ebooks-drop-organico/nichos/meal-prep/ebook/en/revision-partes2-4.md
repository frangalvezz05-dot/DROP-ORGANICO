# Revisión de calidad · Partes 2-4 + muestra + imprimible · The Sunday Sheet (EN)
_03-nov-2026 · Redacción final (Opus) + una pasada propia con la lista de `.claude/agents/revisor-calidad.md`. Sin git._

## Veredicto: **APROBADO CON CAMBIOS DE DATOS PENDIENTES** (la redacción está lista; hay 4 decisiones de datos que debe ver Fran o el orquestador, abajo)

## Extensión
| Archivo | Palabras | Págs. aprox. [ESTIMACIÓN] |
|---|---|---|
| 08-week-1.md | 2.650 | 6 |
| 09-week-2.md | 2.650 | 6 |
| 10-week-3.md | 2.550 | 6 |
| 11-week-4.md | 3.030 | 7 |
| 12-19-recipe-intros.md (portadillas 12-15, 17-19) | 3.130 | 7 |
| 16-signature-plates.md (48 platos + Mix & Match) | 6.140 | 22 |
| 20-storage-chart.md | 2.550 | 5 |
| 21-macro-allergen-index.md | 1.980 | 4 |
| 22-when-things-go-wrong.md | 1.210 | 4 |
| 23-blank-templates.md | 590 | 2 |
| muestra/the-mini-sunday.md | 4.170 | ~12 |
| imprimible.md (contenido de ~30 págs.) | 2.050 | 30 (casi todo tablas) |
| **Total** | **≈32.700** | |

## ⚠ Lo más importante que he encontrado (datos, no redacción)

1. **Error en `construir.py` (corregido).** Las macros de los 48 platos NO sumaban las salsas: las fichas de salsas y desayunos guardan las macros en otro formato y el script las leía como 0. Ejemplo: D-3 salía 710 kcal y en realidad son 850 (chimichurri = 140 kcal). He añadido una línea al script (`mpr()`), lo he vuelto a ejecutar y `datos/platos.json`, `semanas.json` e `indice-macros.md` ya están bien. Copia de los datos antiguos en el scratchpad de la sesión. **Todo lo escrito usa las cifras corregidas.** Consecuencia: los platos van de **510 a 850 kcal**, por encima del objetivo de `estructura.md` (450-600 kcal). No es una promesa rota (nunca se anunció), pero conviene saberlo para la página de producto.
2. **El plan de 4 semanas no cuadra con "1 receta = 5 raciones".** Cada semana tiene 5 platos ×2 = 10 cajas, pero una proteína sale en 6 cajas y la otra en 4 (lo mismo con bases y verduras). He comprobado por script que en las semanas 2 y 4 no existe ningún reparto que lo cuadre. **Solución aplicada:** método del cap. 3 ("pesa la tanda y divide entre sus cajas"); cada semana trae su tabla de montaje con gramos por caja y las kcal/proteína **de esas cajas reales** (calculadas por script, no a mano). Por eso el menú de una semana no coincide con la cifra "estándar" del plato en el cap. 16 (p. ej. M3 en la semana 1 = 850 kcal; estándar = 690). Está explicado en el texto. **Alternativa para decidir:** escalar recetas (×1,2 / ×0,8) para que todas las cajas lleven ración estándar. Cambia las listas de la compra.
3. **Combinaciones: 1.815, no 2.106.** Con las familias de sabor que tienen las fichas reales, la regla da 1.815. He usado 1.815 y he corregido el cap. 1 (decía 2.106). **Hay que cambiar 2.106 en `estructura.md`, la página de producto y cualquier anuncio.** Además, 3 platos firmados rompen la regla (D-8, C5, C8): están señalados en el cap. 16 como "cruces a propósito".
4. **Carne por semana distinta de lo planeado.** Real (de las listas): S1 4 lb · S2 3,2 lb · S3 6 lb (2 lb son reserva de congelador) · S4 3,5 lb + tofu. El plan decía S2 ≈ 2,5 lb y S4 ≈ 2 lb. He corregido la tabla del cap. 5. La crítica F27 ("4-5 lbs of meat each week") sigue viva en S1 y S3.

## Lista de control
| # | Punto | Resultado | Nota |
|---|---|---|---|
| 1 | Anclaje en frase real EN | OK | Semanas: F9, F28, F1, F22. Portadillas: F27, F11, F23, F1; caps. 13, 14 y 19 declaran **[SIN DATO]** (la frase de bases es española, E3, y no se traduce). Cap. 16 F22, 20 F30 (marcada como título de hilo, no reseña), 21 F11, 22 F21, 23 F10, muestra F24. Fragmentos de F9/F10 sin la parte con promesa de peso. Ninguna ⚠. |
| 2 | Acción al final | OK | Cada archivo termina en checklist o tabla para rellenar (tiempo real, elección de salsa, plan de la semana 5, 3 platos propios, registro de fallos…). |
| 3 | Relleno y clichés | OK | Sin frases de la lista prohibida. Sin frases nuevas que añadir. |
| 4 | Promesas prohibidas | OK | Nada de peso ni salud. "About 2 hours" siempre como objetivo + "time yours"; la muestra dice "about 1½ hours, first time" y que no está cronometrada. Las kcal diarias se presentan como "what the boxes hold, not a target". Sin urgencias: la llamada al pack termina con "si la muestra te basta, sigue usándola". |
| 5 | Datos con fuente | OK con marcadores | Macros: USDA FoodData Central (por script). Conservación: fichas + USDA FSIS. Alérgenos: FDA 9. Coste: solo **[COST_TABLE]** (existe `datos/costes.md`, hecho por otro proceso; no lo he usado porque la orden era dejar el marcador). Conversiones a lb/oz calculadas; los tamaños de envase son "common US sizes; yours may differ". |
| 6 | Coherencia avatar/ángulo | OK | A1 (hoja), A2 (salsas), A4 (regla del día 5, salmón días 1-2), A5 (coste, marcador), A3 (macros reales, incluidos platos <40 g sin redondear al alza), A8 (plan cerrado → semana 4 a medias). |
| 7 | Avisos | OK | Alérgenos por plato y por semana, aviso de etiquetas, pescado en Worcestershire, aviso de cacahuete en semana 4, "no es consejo médico" en muestra, índice e imprimible; reglas FSIS en caps. 20 y 22. |
| 8 | Legibilidad | OK | Frases cortas, 2.ª persona, unidades EE. UU. + métricas, °F + °C. Las fichas de 48 platos son plantilla repetida (mismo orden siempre) a propósito. |
| 9 | Copia | OK | Texto propio; nombres comerciales de los 48 platos inventados, sin marcas registradas. |
| 10 | Licencias | N/A | No hay PDF todavía. |

**Retrotraducción:** no he podido lanzar un subagente Haiku desde aquí. En su lugar, abajo va un resumen fiel en español de cada archivo.

## Resumen en español, archivo por archivo

- **08-week-1.md · Semana 1 "de arranque".** Para quien empieza. Pollo (contramuslo) y pavo picado, arroz al horno y boniato, brócoli y pimientos, 3 salsas (chipotle, teriyaki, tahini), desayuno de mini-tortillas de huevo con espinaca y feta. Hoja minuto a minuto: horno 450 °F (brócoli) → 425 °F (pollo, boniato, pimientos, arroz) → 350 °F (huevo), con la sartén y las salsas en los huecos; acaba hacia 2:05. Tabla de montaje (gramos por caja), menú lunes-viernes con kcal/proteína de cada caja real (550-850 kcal), media diaria ≈1.580 kcal y 109 g de proteína. Viernes: A1 ×2 al congelador el domingo. Lista de la compra por pasillos en lb/oz ×1 y ×2, especias, sobras y [COST_TABLE].
- **09-week-2.md · Semana 2 "barata".** Ternera estirada con lenteja y pollo en olla lenta con salsa de bote (se enciende 2,5 h antes). Patata, tortillas, calabacín y pimientos; salsas enchilada, BBQ y verde; avena nocturna. Todo el horno a 425 °F y el gratinador al final. Alternativa sin olla lenta: P3 (pechuga al horno), con aviso [SIN DATO] porque la ficha P2 no tiene método de horno. Viernes: M11 (wrap) congelado. Media ≈1.580 kcal y 112 g. Alérgenos: trigo, pescado (Worcestershire), leche.
- **10-week-3.md · Semana 3 "adelanta congelador".** Albóndigas de pavo ×2 (una tanda para la semana, 24 albóndigas de reserva al congelador) y salmón (lunes y martes; la 5.ª pieza es la cena del domingo). Pasta, quinoa, judías verdes, calabacín; salsas tomate cremosa, chimichurri, teriyaki; burritos de desayuno. Horno 425 → 400 °F. Es la semana más pesada: ≈2.110 kcal y 127 g/día; el texto lo dice y sugiere reducir la base si sobra. Viernes: A10 + D-5 y un burrito congelados.
- **11-week-4.md · Semana 4 "mézclalo tú".** Cerdo desmechado (entra al horno 4,5 h antes) y tofu crujiente; arroz y quinoa; col cruda y brócoli; salsas gochujang y cacahuete + **una salsa que elige el lector** para el plato M5, con tabla de 7 opciones compatibles (kcal, proteína, alérgenos, cuándo hacerla, si congela). El lector cambia él mismo la hoja, la lista y el menú. Termina con la plantilla para planear la semana 5. Media ≈1.820 kcal y 133 g con la salsa por defecto. Aviso de alergia al cacahuete.
- **12-19-recipe-intros.md · Portadillas de la Parte 3.** Una página por bloque (proteínas, bases, verduras, salsas, desayunos, congelador, snacks): cómo usar el bloque y tabla de recetas con ración, kcal, proteína, nevera, congelador, alérgenos (y familias de sabor). El cap. 16 va aparte.
- **16-signature-plates.md · 48 platos + tabla Mix & Match.** Cómo leer un plato; 4 bloques de 12 (México, Asia, Mediterráneo, Comfort). Cada plato: nombre comercial, composición, kcal y proteína estándar, alérgenos, días de nevera, si congela y montaje en 3 líneas (qué va en la caja, qué va aparte, cómo recalentar y rematar). Después: 3 platos que cruzan familias, la regla ("elige salsa; vale todo lo que tenga ✓ en su familia"), 4 tablas de ✓, 4 comprobaciones, un ejemplo de suma de macros y ejercicio de 3 platos propios.
- **20-storage-chart.md · Tabla de conservación.** Las 7 reglas FSIS (nevera 40 °F y 3-4 días, regla del día 5, 2 h a temperatura ambiente, congelador 0 °F, descongelar en nevera, recalentar a 165 °F, "en la duda, tíralo") + las 60 recetas con nevera, congelador y recalentado.
- **21-macro-allergen-index.md · Índice.** Los 48 platos ordenados por proteína (kcal, proteína, hidratos, grasa, nevera, alérgenos), listas de platos "sin X" para 7 alérgenos, cambios que abren más platos y [COST_TABLE].
- **22-when-things-go-wrong.md · Cuando algo falla.** 15 problemas (pollo seco, salmón, albóndigas, cerdo que no se deshace, tofu blando, lenteja dura, arroz, pasta, verdura aguada, patata blanda, salsas cortadas, mini-tortillas crudas, sabor plano el jueves, ir tarde con la hoja, caja del viernes congelada) con por qué, arreglo ya y próxima vez. Registro de fallos al final.
- **23-blank-templates.md · Plantillas.** Qué plantilla hay en el imprimible y cuándo se usa; cómo rellenar una hoja de domingo en blanco en 5 pasos.
- **muestra/the-mini-sunday.md · Muestra gratis.** Pollo + arroz + brócoli + 3 salsas = 3 comidas distintas en 5 tuppers (lunes-viernes, viernes congelado). Método en 1 página, los 3 platos (640-690 kcal, 46-49 g), hoja minuto a minuto (≈1,5 h la primera vez, sin cronometrar), lista ×1/×2, las 6 fichas completas (sin la línea de coste), conservación, [COST_TABLE] y página final con lo que añade el pack (24,99 $, [LINK_TIENDA]) y la tabla Mix & Match recortada a la familia mexicana. Sin urgencia.
- **imprimible.md · Pack imprimible.** Mapa de 30 páginas; las rellenas (hojas y listas de las 4 semanas, tabla de conservación, póster Mix & Match) se copian literalmente de los capítulos; contenido completo de hoja en blanco, lista en blanco, "monta tu plato", hoja de coste, etiquetas de tupper y 3 tarjetas de nevera (regla del día 5, recalentado por componente, las 12 salsas).

## Cambios hechos fuera de las Partes 2-4
- `construir.py`: lectura de macros de salsas y desayunos (ver punto 1). Datos regenerados.
- `01-why-it-gets-old.md`: 2.106 → 1.815 combinaciones.
- `05-cost.md`: tabla de carne por semana con las cifras reales de las listas.

## Pendientes (para Fran / siguientes fases)
1. **Decidir el punto 2** (dividir tandas vs. escalar recetas). Si se escala, regenerar listas y menús.
2. **Rellenar [COST_TABLE]** (semanas, índice, muestra, imprimible) con `datos/costes.md`. Comprobar que la semana 2 es de verdad la más barata; si no, cambiarle el título.
3. **Cronometrar** la semana 1 y la Mini Sunday antes de usar "2 hours" o "90 minutes" en anuncios.
4. **Ficha P2:** añadir método de horno (ahora la semana 2 remite a P3).
5. Corregir **2.106 → 1.815** en `estructura.md` y en la página de producto.
6. **Ejemplo del cap. 2** (Parte 1): usa salsa de 50 g y otro orden de horno; la hoja real de la semana 1 empieza a 450 °F. Ajustar el ejemplo o dejarlo como ilustrativo.
7. Los nombres comerciales de los 48 platos son nuevos [ESTIMACIÓN]: revisar que ninguno choque con una marca registrada antes de usarlos en anuncios.
