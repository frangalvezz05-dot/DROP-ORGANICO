# Revisión de calidad · Parte 1 + capítulo 0 · The Sunday Sheet (EN)
_03-nov-2026 · Redacción final (Opus) + una pasada propia con la lista de `.claude/agents/revisor-calidad.md`. Archivos: `ebook/en/00-start-here.md` a `07-pantry-gear.md`._

## Veredicto: **APROBADO** (con 6 pendientes de datos, no de redacción)

## Extensión
| Capítulo | Palabras (sin marcas) |
|---|---|
| 0 · Start Here | 778 |
| 1 · Why Meal Prep Gets Old by Wednesday | 850 |
| 2 · Your Sunday, One Sheet | 1.035 |
| 3 · Portions That Add Up | 724 |
| 4 · Storage, Freezing, Reheating | 1.064 |
| 5 · What a Plate Really Costs | 793 |
| 6 · Protein You Can Count | 917 |
| 7 · Pantry & Gear | 682 |
| **Total** | **6.843** (≈ 22 págs. A5 con tablas) |

## Lista de control
| # | Punto | Resultado | Nota |
|---|---|---|---|
| 1 | Anclaje en frase real EN | OK | 8/8 capítulos abren con frase literal de `frases.md` (F5, F24, F19, F26, F25, F27, F4, F13), "— reader review", sin nombre, enlace en comentario HTML. Ninguna ⚠. Cap. 4 abre con F25 (sí es reseña) en vez de F30 (es título de hilo de Reddit, no reseña): F30 se cita dentro como "thread titled", no como reseña. |
| 2 | Acción al final | OK | Cada capítulo termina en plantilla/ejercicio: hoja de camino (0), test de 5 tuppers (1), ensayo previo + hoja de tiempo real (2), plan de raciones (3), mapa de nevera + tracker (4), hoja de coste (5), hoja "monta tu plato" (6), checklist de despensa (7). Las secciones intermedias son explicativas y desembocan en esa acción. |
| 3 | Relleno y clichés | OK tras cambio | Sin frases de la lista prohibida. Cambiado: "Most people don't quit meal prep because…" (generalización sin dato) → "Meal prep often doesn't fail at the stove". No hay frases nuevas que añadir a la lista. |
| 4 | Promesas prohibidas | OK tras cambio | Sin peso ni salud. "2 hours" siempre como "about 2 hours", "design target, not a promise". Quitado: "usually drops by the second or third week" (promesa sin dato) y "takes about 5 minutes" (pesar) → "a few minutes". Título del cap. 2 cambiado de "The 2-Hour Sunday" a "Your Sunday, One Sheet: How to Read It" para que no suene a garantía (el nombre de archivo se mantiene). |
| 5 | Datos con fuente | OK con pendientes | USDA FSIS (3-4 días, 40 °F, 0 °F, 2 h / 1 h a >90 °F, recalentar a 165 °F, temperaturas internas, descongelado), FDA (9 alérgenos; *B. cereus* en Bad Bug Book), USDA FoodData Central SR Legacy. Macros del ejemplo del cap. 6 **calculadas** con `herramientas/macros.py` (pollo 560 kcal/48 g; tofu 560 kcal/38 g; IDs USDA 173627, 168877, 170379, 170894, 171413, 172475). Precios: solo método + ejemplo con números inventados declarados como tales + marcador **[COST_TABLE]**. |
| 6 | Coherencia avatar/ángulo | OK | A2 (cap. 1), A1 (cap. 2), A6/A7 (cap. 3), A4 (cap. 4), A5 (cap. 5), A3 (cap. 6), F11/F13 (cap. 7). Responde a la crítica de F27: cap. 5 declara la carne prevista por semana. |
| 7 | Avisos | OK | Cap. 0: no sustituye a dietista/médico; 9 alérgenos FDA + "lee tu etiqueta"; seguridad USDA FSIS. Cap. 2 y 4 repiten temperaturas y regla de 2 h. |
| 8 | Legibilidad | OK | Frases cortas, 2.ª persona, unidades EE. UU. + métricas, °F + °C. |
| 9 | Copia | OK | Texto original; no se ha usado texto de libros del mercado ni de mentores. Las frases de clientes son citas breves y atribuidas. |
| 10 | Licencias | N/A | No hay PDF todavía. |

## Pendientes (para Fran / siguientes fases)
1. **[COST_TABLE]** (cap. 5): rellenar con el script de costes, con tienda, región y fecha.
2. **Cronometrar la semana 1** antes de usar "about 2 hours" en anuncios (ya estaba en `estructura.md` §6).
3. **Carne por semana** (cap. 5): cifras de `estructura.md` §3.2, todavía [ESTIMACIÓN]; la semana 3 dice "listed on the week's sheet". Revisar cuando estén las recetas.
4. **Compromisos con partes posteriores** que deben cumplirse al redactarlas: la olla lenta (P2) necesita alternativa de horno; cada lista de la compra anota sobrantes; tarjeta de nevera con aviso del jueves; cada ficha lleva su "wake it up" (lima/limón/hierbas).
5. **Las filas de ejemplo de la hoja del domingo** (cap. 2) son ilustrativas; si la hoja real de la semana 1 usa otras temperaturas u orden, ajustar el ejemplo.
6. Comprobar que las URLs de las fuentes (títulos de páginas FSIS/FDA) siguen vivas antes de maquetar.

---

# Retrotraducción al español · resumen por capítulo (para Fran)
_Traducción fiel del contenido, resumida. No añade ni mejora nada._

## 0 · Empieza aquí: cómo funciona este libro
**Frase de apertura** (reseña de un comprador de otro libro): "mucho más fácil que buscar recetas sueltas por internet".

El libro dice que no te faltan recetas: te falta saber qué cocinar el domingo, en qué orden, cuánto y cuánto dura. Por eso es primero un sistema y después un recetario.

**Contenido**: Parte 1, el sistema (cap. 1-7, unas 20 páginas, se lee una vez). Parte 2, plan de 4 semanas: cada semana es una hoja de domingo, una lista de la compra por pasillos (1 o 2 personas) y 5 platos. Parte 3, 60 recetas por piezas (10 proteínas, 6 bases, 6 verduras, 12 salsas, 8 desayunos, 10 platos de congelador, 8 snacks), 48 platos firmados y la tabla de combinaciones. Parte 4, referencia: conservación, índice de macros/coste/alérgenos, arreglos y plantillas. Todas las fichas ponen lo mismo en el mismo sitio.

**Tres caminos**:
- **A · Sigue la semana 1**: para no decidir nada. Lees los cap. 2 y 4 (unos 15 min), vas al 8, compras y cocinas. Acabas con 10 tuppers y 5 desayunos (comida y cena de lunes a viernes para 1, o comida para 2).
- **B · Monta tus platos**: si ya has hecho meal prep. Cap. 1, 3 y 6, luego salsas (15) y tabla (16); planificas en la plantilla del cap. 23.
- **C · Solo congelador**: si ahora no puedes dar un domingo o te cansas del mismo tupper al tercer día. Cap. 4 y bloque de congelador (18): cocinas una olla cualquier tarde, congelas raciones y sacas de una en una.
Si dudas, camino A.

**"Unas 2 horas"**: es un objetivo de diseño, no una promesa. El primer domingo tardarás más; no cuenta la compra ni el último fregado. Cronométrate y apunta tu tiempo real cada semana.

**Tres avisos**: (1) no es consejo médico ni nutricional; las cifras salen de datos USDA pero el libro no dice cuánto comer; si tienes una condición médica, embarazo o dieta pautada, habla con un dietista o médico. (2) Alérgenos: los 9 principales de EE. UU.; las marcas cambian (la salsa de soja suele llevar trigo); lee la etiqueta de lo que compras. (3) Seguridad alimentaria según el USDA FSIS; usa termómetro; "ante la duda, tíralo".

**Acción**: rellenar camino elegido, horario del domingo, para cuántos cocinas, alérgenos de casa y día de compra.

## 1 · Por qué el meal prep cansa el miércoles
**Frase**: "los mismos ingredientes precocinados y recolocados de formas un poco distintas se volvieron aburridos muy rápido".

El meal prep no suele fallar en la cocina, sino el miércoles delante de la nevera, con el tercer tupper del mismo pollo con arroz. Recolocar la misma comida no lo arregla: si el pollo sabe a limón y ajo el lunes, sabe igual el jueves. Lo que más cambia un plato es el sabor que se añade al final (salsa, ácido, especias). Por eso las piezas grandes se cocinan con poco condimento y el sabor va en las salsas.

**Fórmula del plato**: 1 proteína + 1 base + 1 verdura + 1 salsa. La proteína, la base y la verdura son la tanda; la salsa es "el volante".

**Cuatro familias de sabor**, 3 salsas cada una: MEX (lima, chipotle, comino, cilantro: yogur chipotle-lima, salsa verde de tomatillo, salsa roja de enchilada), ASI (soja, jengibre, sésamo: teriyaki ligera, cacahuete-jengibre, gochujang-miel), MED (limón, ajo, hierbas, yogur: tzatziki, limón-tahini, chimichurri), COM (ahumado, dulce-ácido, cremoso: BBQ, miel-mostaza, tomate-ajo cremoso). Algunas proteínas valen para todas; otras solo para una (el picado de pavo, solo MEX).

**Ejemplo de la semana 1**: una bandeja de muslos de pollo al limón y ajo da 3 platos distintos (MEX, ASI, MED). Con una segunda proteína (pavo) salen 5 platos con 2 proteínas, 2 bases, 2 verduras y 3 salsas.

**Dos reglas**: ninguna salsa dos días seguidos; algo crujiente al menos dos veces por semana.

**48 platos y tabla Mix & Match**: 48 combinaciones trabajadas con calorías, proteína, alérgenos y coste. La tabla lista 2.106 emparejamientos que siguen las reglas de sabor, pero **no se han cocinado uno a uno**: es un mapa.

**Acción, "test de los 5 tuppers"**: planear 5 tuppers en una tabla y comprobar: sin salsa repetida en días seguidos, 2 con algo crudo, máximo 2 proteínas/2 bases/2 verduras, al menos 2 familias. Si falla, cambiar primero la salsa.

## 2 · Tu domingo en una hoja: cómo leerla
**Frase**: "fue más frustración de la que quería meter en un día libre".

Los domingos perdidos se parecen: lees una receta, empiezas, la siguiente pide otra temperatura, el horno está vacío mientras cortas, todo acaba a la vez o algo acaba 40 minutos tarde, y no sabes cuánto va en cada tupper. No es falta de habilidad, es el orden. La hoja une todas las recetas de la semana en una sola línea de tiempo.

**Partes de la hoja**: (1) cabecera: semana, 1 o 2 personas, nº de tuppers, temperatura, tiempo estimado (unas 2 h para una persona) y hueco para tu tiempo real; (2) "antes del minuto 0": unos 10 min de preparar encimera, bandejas, báscula, termómetro y tuppers; (3) línea de tiempo en cuatro bloques siempre en este orden: **HORNO → FUEGO → FRÍO → MONTAJE** (el horno primero porque tarda más y te necesita menos; el fuego en ratos cortos mientras tanto; lo frío llena huecos; el montaje al final). Las tareas que se hacen "mientras el horno va" llevan un ⏱. (4) tabla de montaje: gramos por tupper, cuáles a nevera y cuáles al congelador.

**Cada fila**: reloj (minutos desde que empiezas), puesto, qué hacer, **señal de hecho** y cantidad. La señal de hecho es la columna clave: el temporizador dice cuándo mirar, la señal dice cuándo parar. Las filas del ejemplo son ilustrativas; las reales están en los cap. 8-11.

**Temperaturas internas seguras (USDA FSIS)**: pollo y pavo, también picados, 74 °C/165 °F; ternera y cerdo picados 71 °C/160 °F; piezas de cerdo 63 °C/145 °F + 3 min de reposo; pescado 63 °C/145 °F; platos de huevo 71 °C/160 °F. El pavo picado es ave: 165 °F. El cerdo desmechado es seguro a 145 °F pero necesita más cocción para deshacerse.

**Cinco hábitos**: leer la hoja la noche antes; un temporizador con nombre por bandeja; tachar filas con lápiz; fregar en los huecos; no adelantar bloques por aburrimiento.

**Sobre "unas 2 horas"**: objetivo, no garantía. Para dos personas se añade sobre todo corte y reparto; el horno tarda casi lo mismo si la comida cabe en una capa. Si se amontona, se cuece al vapor: usa otra bandeja.

**Acción, "ensayo"**: la noche antes leer la hoja, revisar bandejas, contar tuppers, hacer sitio en la nevera y apuntar la hora de inicio; al acabar, apuntar hora real, minutos, paso más lento y un cambio para la semana siguiente.

## 3 · Raciones que cuadran
**Frase**: "las raciones de las recetas son inconsistentes. A veces nos salían 4 raciones justas, a veces 6, a veces más".

"Para 4" es una suposición. En una semana, el error aparece el jueves como un tupper con medio pollo. El libro no usa "raciones para": usa gramos y tuppers. Cada ficha empieza con "Rinde: 5 raciones · unos 700 g cocinados · unos 140 g por ración". Las calorías y la proteína son de una de esas raciones.

**Método de dividir la tanda**: el peso cocinado nunca es exacto (el pollo pierde agua, el arroz la absorbe). Así que se pesa lo que sale: bol en la báscula, tara, se echa toda la tanda, se divide entre los tuppers y se llena cada tupper hasta esa cifra. Ejemplo: 690 g ÷ 5 = 138 g. Así cada tupper es de verdad una quinta parte y los macros de la ficha siguen siendo correctos. Lleva unos minutos.

**Ración de referencia** (para montar tus platos): proteína 130-140 g cocinada (≈180 g cruda); base 150-170 g de arroz/quinoa/pasta cocidos (60 g en seco; pasta 70 g); patata asada 170-200 g; verdura 100 g asada u 80-100 g cruda; salsa 40-50 g (≈3 cucharadas). La columna en crudo es orientativa para comprar; manda la báscula.

**×1 o ×2**: ×1 = 10 tuppers (comida y cena de lunes a viernes para 1, o comida para 2) + 5 desayunos; ×2 = 20 tuppers + 10 desayunos. No se duplica el tiempo de cocción (misma señal de hecho, más bandejas) y la comida debe ir en una sola capa.

**Reparto en la semana (×1)**: 2 tuppers por día; lunes a jueves en nevera, **viernes al congelador** (cap. 4).

**Acción**: plan de raciones antes de comprar (personas, comidas, cenas, total de tuppers, cuántos a nevera y a congelador, tarritos de salsa, desayunos) y, el domingo, tabla por componente: peso de la tanda ÷ tuppers = gramos por tupper.

## 4 · ¿Aguanta hasta el jueves? Conservar, congelar, recalentar
**Frase**: "el sabor de la comida acabó siendo tan malo que terminábamos tirando comida cada semana…".

La comida preparada acaba en la basura por dos motivos: dudas de que siga siendo segura o sabe cansada. Se cita también el título de un hilo de foro muy votado: "¿está bien guardar mi comida así cuatro o cinco días?". Cuatro sí; en cinco cambia la respuesta.

**Regla del día 5**: el USDA FSIS dice que las sobras cocinadas duran **3-4 días** en nevera a 4 °C o menos. Domingo es el día 0; el jueves es el día 4; el viernes es el día 5, fuera. Por tanto: **lo que vas a comer el día 5 se congela el domingo**, y el **jueves por la mañana** se pasa a la nevera para comerlo el viernes. El salmón se come el día 1 o 2 (por calidad, no por seguridad). Congelar no reinicia el reloj: un tupper con 3 días de nevera sale del congelador como "día 3".

**Enfriar rápido**: zona de peligro entre 4 y 60 °C; a la nevera **en menos de 2 horas** (1 hora si hace más de 32 °C). Se puede meter caliente si va en recipientes poco hondos (unos 5 cm), con separación y tapas apoyadas los primeros 20-30 min.
**Arroz**: puede llevar esporas de *Bacillus cereus* que sobreviven a la cocción; si se deja horas templado pueden crecer y producir una toxina que no se destruye al recalentar. Extenderlo en capa fina, dejar salir el vapor unos 10 min y a la nevera, **todo en menos de 2 h**. Igual con quinoa y pasta.

**Congelador**: a −18 °C la comida es segura mientras siga congelada; la **calidad** es otro reloj (guisos y sopas, mejor en 2-3 meses; carne cocinada, 2-6 meses; cada ficha da su cifra). Fecha en cada tupper. Descongelar en nevera (un tupper, un día); nunca en la encimera; si se olvida, microondas en descongelar y comer enseguida.

**Recalentar a 74 °C/165 °F**: tapa apoyada, calentar, remover, volver a calentar; humeante en el centro o con termómetro.

**Guardar por partes**: salsas en tarrito aparte (se añaden después); salsas de yogur nunca se calientan; crujientes aparte (ensalada de pepino-tomate se corta el día); pasta 2 min menos y con un poco de aceite; patatas en freidora de aire u horno 5-8 min; arroz con 1 cucharada de agua y tapado; pollo con 1 cucharada de agua o salsa, potencia media. **Tupper de dos zonas**: sacar lo frío, calentar el resto y volver a poner lo frío. **Despertar el sabor**: lima, limón, sal o hierbas justo antes de comer.

**Acción, "mapa de la nevera"** el domingo por la noche: nevera ≤4 °C, congelador ≤−18 °C, etiquetas "comer antes de" y fecha, viernes en el congelador, salmón marcado lunes/martes, salsas en la nevera, aviso del móvil para el jueves. Más un registro semanal de lo comido y lo tirado con el motivo.

## 5 · Lo que cuesta de verdad un plato
**Frase**: "este libro pide como mínimo 4-5 libras de carne cada semana".

La carne es la partida más grande del tique. El capítulo da un método para saber el coste antes de comprar y declara cuánta carne usa cada semana.

**Los precios cambian**: por semana, tienda, ciudad y marca. Todo coste del libro lleva tienda, región y fecha; es una referencia, no un presupuesto. Tu tique es la cifra real. Aquí va el marcador **[COST_TABLE]** (tabla que se añadirá después).

**Método**: coste por ración = precio del paquete ÷ raciones que da. Para lo que se usa poco a poco (aceite, especias): precio ÷ tamaño del paquete × cantidad usada. Ejemplo con **números inventados** (declarados como tales): paquete de muslos 10 $ ÷ 5 = 2 $; arroz 3 $ ÷ 15 raciones = 0,20 $; 7 g de aceite de una botella de 500 g a 8 $ = 0,11 $. La suma da el coste del plato; la lista entera más la parte de despensa, el de la semana.

**Etiqueta de la estantería**: mira el precio por unidad (por libra u onza), no el del paquete; el paquete grande no siempre sale más barato; la marca blanca a menudo sí.

**Carne prevista (×1)**: semana 1 unas 4 lb (1,9 kg); semana 2 unas 2,5 lb (1,1 kg) gracias a la lenteja; semana 3, en su hoja; semana 4 unas 2 lb (0,9 kg) con tofu. Son cantidades previstas que pueden ajustarse. Si la semana 1 es demasiado para tu presupuesto, empieza por la 2.

**Cinco formas de abaratar**: estirar la carne picada con lenteja; muslo antes que pechuga (a menudo más barato y más jugoso; mira el precio por unidad); usar paquetes enteros (las recetas intentan usar tamaños estándar y las listas anotan sobrantes); verdura congelada (mismo precio todo el año, no se pone mustia); comprar la despensa una vez. No se usa verdura ya cortada: ahorra tiempo pero suele costar más; el corte va en la hoja mientras el horno trabaja.

**Acción, "hoja de coste"**: con el tique de la primera compra, rellenar tienda, fecha, precio, tamaño, uso, raciones y coste por ración de cada producto; total de la semana ÷ tuppers = coste por tupper. La semana siguiente, cambiar una cosa y comparar.

## 6 · Proteína que puedes contar
**Frase**: "las recetas no parecen 'sanas' en el mal sentido; saben a comida normal".

La comida alta en proteína tiene fama de pollo seco y arroz sin salsa. Aquí son platos normales con las cifras ya calculadas.

**De dónde salen las cifras** (calculadas, no estimadas): base USDA FoodData Central, SR Legacy; cada ingrediente en gramos **en crudo o en seco, como se compra**, emparejado con la entrada USDA del mismo estado; cuenta todo (aceite, salsa, miel, queso); total de la tanda ÷ raciones; kcal redondeadas a la decena y proteína al gramo. **Por qué en crudo**: es lo que compras y pesas; el peso cocinado cambia con el tiempo de horno porque se va sobre todo agua, y la proteína se queda. **Límites**: en cortes grasos parte de la grasa queda en la bandeja (las kcal reales pueden ser algo menores); en productos envasados manda la etiqueta de tu marca.

**Cómo leer la línea**: "Por ración: 560 kcal · 48 g proteína · 56 g hidratos · 15 g grasa". Por ración = un tupper. Las cifras describen la comida; no dicen cuánto debes comer (eso, con un dietista o médico).

**Plato de ejemplo (simplificado, no es una ficha)**, calculado con `macros.py`: muslo de pollo 180 g crudo (220 kcal, 35 g), arroz 60 g en seco (220 kcal, 4 g), brócoli 100 g + 7 g de aceite (100 kcal, 3 g), yogur griego desnatado 50 g (30 kcal, 5 g). **Total: 560 kcal, 48 g de proteína**. Las filas suman 570 y 47 por el redondeo; manda el total.
**Cambio a tofu firme (150 g crudo)**: 560 kcal y **38 g** de proteína. Los platos vegetales suelen tener menos proteína; se publica la cifra real, sin redondear al alza. Para subirla: más ración, salsa a base de yogur o tofu, o edamame (recalculando).

**Alérgenos del plato combinado**: el plato lleva todos los alérgenos de sus piezas (pollo + arroz: ninguno; con teriyaki de soja normal: soja y trigo). Tabla de los habituales: salsa de soja (soja, trigo; el tamari suele ir sin trigo), gochujang (soja, a menudo trigo), tahini y aceite de sésamo (sésamo), salsa de cacahuete (cacahuete, soja), salsas de yogur y feta (leche), tortillas y pasta (trigo), egg bites (huevo, leche).

**Acción, "monta tu plato"**: tabla para copiar la línea por ración de cada pieza (proteína, base, verdura, salsa, extra) y sumar kcal, proteína y alérgenos; el redondeo puede desviar unos 10 kcal y 1-2 g.

## 7 · Tu despensa y tus utensilios en una página
**Frase**: "me encanta que las primeras páginas te digan las especias, salsas, utensilios, etc. esenciales que necesitas".

Si cada receta pide un bote nuevo, la lista crece y el armario se llena de botes a medias. Las 60 recetas comparten una despensa pequeña: se compra una vez y la lista semanal queda casi solo en frescos.

**Despensa de 26 productos** (con la familia que los usa y sus alérgenos): aceites y vinagres (oliva, neutro, vinagre de arroz, de manzana); especias (sal kosher, pimienta, ajo en polvo, pimentón ahumado, comino, chile en polvo, orégano, copos de guindilla); salsas y botes (soja baja en sal o tamari, aceite de sésamo tostado, gochujang, crema de cacahuete natural, tahini, miel, mostaza Dijon, chipotles en adobo); secos y latas (arroz largo, quinoa, copos de avena, lenteja seca, garbanzo en lata, tomate triturado). Consejos: congelar en plano los chipotles sobrantes; remover crema de cacahuete y tahini y guardarlos en nevera si la etiqueta lo pide. Si empiezas con una o dos familias, compra solo esas filas.

**En la lista semanal, no en la despensa**: ajo, jengibre, limones, limas, cilantro, perejil, yogur griego, huevos, tortillas, pasta, patatas, boniatos y toda la carne, pescado y tofu.

**6 utensilios**: 2 bandejas de horno con borde (media bandeja, 46 × 33 cm); fuente de 23 × 33 cm (arroz al horno); sartén grande de unos 30 cm; olla con tapa de 4 L o más; báscula digital con tara; termómetro de lectura rápida ("el único que no deberías saltarte"). Además: 10 tuppers y 5 tarritos de salsa para ×1 (el doble para ×2), aptos para microondas y congelador; papel de horno, aluminio, cinta y rotulador, termómetro de nevera. Opcionales: olla lenta (la semana 2 la usa; la receta dará opción de horno), freidora de aire, buen cuchillo.

**Regla para no quedarte sin nada**: cuando abras el último, apúntalo en la lista de la semana siguiente (no cuando se acabe).

**Acción, "revisión de despensa"**: marcar con lápiz lo que tienes y anotar qué despensa y utensilios comprar, tuppers que tienes/necesitas y con qué familias empiezas. Lo que falte va arriba en la lista de la semana 1: esa primera compra cuesta más; las siguientes son casi solo frescos.
