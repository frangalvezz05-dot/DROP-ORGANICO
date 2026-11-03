# Revisión de calidad: muestra "Kit SOS contacto cero / No Contact SOS Kit" (cap. 3 + tarjeta + hoja)

Fecha: 2026-10-14. Vuelta 1. Archivos: `ebook/en/muestra.md`, `ebook/es/muestra.md`. Contexto: estructura v2, avatar v2 (§8 recursos), frases.md, 00-ficha.md, marca.json.
Retrotraducción EN->ES (fiel, no publicable): `ebook/en/muestra-retrotraduccion-es.md`.

## VEREDICTO: CAMBIOS (vuelta 1 de 2)

La muestra está bien construida (pasos primero, acción al final de cada sección, avisos presentes, sin promesas ni citas literales). Hay 4 fallos que corregir antes de maquetar; ninguno obliga a rehacer el texto.

## Tabla de la lista de control

| # | Punto | EN | ES | Detalle |
|---|---|---|---|---|
| 1 | Anclaje | OK | OK con reservas | Todos los códigos (EN1, EN13, EN14, EN15, EN25; ES14, ES19, ES24, ES26) existen en avatar.md con su URL y coinciden con `frases.md` (que no numera: la numeración vive en avatar.md). Ninguna frase traducida se presenta como real. Reservas ES: (a) el registro de ES14/19/24/26 es latinoamericano y la muestra lo declara en la cabecera (correcto, pendiente de la decisión de voz de España); (b) ES24 ("la cague reclamandole") es recaída de escribir al ex, no de mirar redes: ancla débil para la sección "Si has mirado igualmente" (usar [SIN DATO] o ES14/ES19, que sí hablan de mirar); (c) el caso "en el trabajo" y el caso "abusiva" en ES solo tienen respaldo EN (EN15, EN25): marcar [SIN DATO] ES en esos puntos en vez de "referencia interna". |
| 2 | Acción | OK | OK | Todas las secciones acaban en acción. "Why ten minutes" y "Today's checklist" también. |
| 3 | Relleno y clichés | OK menor | OK menor | Ninguna frase de la lista prohibida. Débiles: "La vida real complica las cosas / Real life gets in the way" (relleno, borrar y empezar por "Elige el caso que te encaje"); "La idea de trabajo de este capítulo es sencilla / The working idea ... is simple" (borrar el adjetivo); repetición triple de "no es un fracaso / not a failure" (tarjeta, sección, cierre): dejar solo la tarjeta. "Cuando no es limpio" es vago: "Cuando no es tan limpio / Cuando no puedes cortar del todo". |
| 4 | Promesas prohibidas | OK | OK | No promete resultados, ni recuperar al ex, ni testimonios, ni urgencias. El ejemplo de las 23:40 lleva "ejemplo, no garantía" (bien). Mejora: decir explícitamente que es un ejemplo imaginado ("Imagina un martes..."), para que no se lea como caso real con cifras 8->6->3. |
| 5 | Datos | FALLO | FALLO | Ver fallos F2 y F3. |
| 6 | Coherencia con avatar y ángulo | OK | OK con reserva | A1 (impulso de mirar redes), pasos primero (A13), neutral y sin dar por hecho que se quiere volver (A12, EN25). Reserva ES: el texto usa masculino fijo ("Le ves", "evitarle", "le etiquetan", "un amigo"), contra la regla de género neutro de estructura §5 (ver F4). |
| 7 | Avisos de contenido | FALLO parcial | OK | Aviso, límites y recursos presentes en ambos. EN omite que el 016 no atiende a hombres (ver F1). ES: "gratuita" junto al 024 no figura en avatar.md §8 (añadir fuente o quitar). Pendiente general: vigencia de los teléfonos sin reverificar (avatar §8 lo declara). |
| 8 | Legibilidad | OK menor | OK menor | Frases cortas, tono correcto. Incoherencia de nombres: "trigger sheet / hoja de disparadores" vs "tracker / registro" para lo mismo (secciones "If you looked anyway", "Why ten minutes"). Unificar. ES: "versiones imprimible y editable" -> "versión imprimible y versión editable". |
| 9 | Copia | OK | OK | No se detecta copia ni paráfrasis cercana de los productos de `ebooks-mercado.md`. El "plan de recaída" y el "tracker" son mínimos del mercado (ya anotado en avatar v2). |
| 10 | Licencias | n/a | n/a | No es PDF. Pendiente al maquetar: Inter y Source Serif 4 (marca.json) son OFL, comprobarlo al incrustar. |

## Teléfonos contra avatar.md §8

| Recurso | avatar §8 | EN | ES |
|---|---|---|---|
| Emergencias | 112 / 911 | 911 y 112 OK | 112 OK |
| Crisis / suicidio | 024 / 988 (llamada, SMS o chat) | 988 y 024 OK | 024 OK ("gratuita" sin fuente en §8) |
| Violencia de pareja | 016 (no atiende a hombres; alternativa 112 u Oficinas de Asistencia a las Víctimas) / 1-800-799-7233 o START al 88788 | 1-800-799-7233 y START 88788 OK; **016 sin la excepción para hombres: FALLO** | 016 con excepción OK |
| Texto fijo "Si no estás en España o EE. UU., busca la línea de tu país" | Sí | OK | OK |

## Fallos, ordenados por gravedad, con cambio propuesto

**F1 (grave, seguridad). EN, "Where to call", línea Spain.** Dice "016 (violence against women)" sin avisar de que no atiende a hombres; el kit se declara neutral en género.
Cambio: "Spain: 112 (emergency), 024 (suicide prevention), 016 (violence against women; it does not take calls from men: if you are a man, call 112 or go to a Victim Assistance Office)."

**F2 (datos sin fuente). Nombres y funciones del móvil.**
- ES: `(en iPhone, "Tiempo de uso"; en Android, "Bienestar digital")`. Los nombres no tienen fuente en el proyecto y los menús varían por versión y fabricante. Además, "pide a alguien de confianza que ponga el código" presupone un código que en Android no existe en "Bienestar digital" tal cual. [SIN DATO, no verificable sin internet en esta sesión]
- EN: "Set a daily time limit ... in your phone settings, and ask someone you trust to set the passcode if you can": mismo problema, formulado más genérico.
Cambio (ambos): "Pon un límite diario a la aplicación con la función de tiempo de uso que traiga tu móvil (búscala en Ajustes). Si tu móvil permite un código para ese límite, pide a alguien de confianza que lo ponga." Si se quieren los nombres, citar la página de soporte de Apple y de Google tras verificarlas.

**F3 (datos sin fuente). Afirmaciones factuales generales.**
- "Most people don't check the profile directly. They arrive through a friend's post." / "Mucha gente no entra al perfil directamente: llega por la publicación de un amigo." Cifra implícita sin fuente. Cambio: "Es fácil llegar al perfil por un rodeo: una foto etiquetada, la historia de una amistad común." (sin generalizar a "la mayoría").
- "Es un minuto y corta el reflejo de deslizar el dedo / interrupts the scroll reflex": afirmación de eficacia sin fuente. Cambio: "Es un minuto y te saca de la postura de deslizar el dedo."
- "Why ten minutes": "Checking gives a quick hit of relief and then leaves you feeling worse" y "urge comes in waves" se afirman como hechos. El texto ya dice "hipótesis de trabajo, no clínica" (bien). Cambio mínimo: cambiar "Checking gives..." por "Mi hipótesis de trabajo es que mirar da un alivio rápido y luego te deja peor...", y anotar internamente [ESTIMACIÓN] hasta tener fuente.
- "Punishing is another way of staying in the loop": opinión presentada como hecho; sustituir por "Castigarte suele mantener el bucle" o quitar.

**F4 (coherencia, género y promesa pendiente). ES.**
- Masculino fijo: "Le ves en el trabajo", "cuando no puedes evitarle", "en las que le etiquetan", "la publicación de un amigo". Cambio: "A esa persona la ves en el trabajo...", "cuando no puedes evitar a esa persona", "fotos en las que etiquetan a esa persona", "la publicación de una amistad".
- "Te dejó y te pidió que no insistieras" y su equivalente EN son un caso legítimo (D3), pero queda muy cerca de ES26 (frase de cliente). No es cita literal; aceptable, solo vigilar que no se acerque más.
- "mira el capítulo 12 del kit completo": estructura §5 y §6.5 dejan el cap. 12 en ES como "versión corta o fuera, decisión del usuario pendiente". Cambio: si el cap. 12 no entra en ES, sustituir por "en el kit completo hay una guía para encuentros inevitables" o dejar la referencia sin número. Sin decisión, no prometerlo en la muestra.

**F5 (menor).**
- Cabecera ES y comentarios `<!-- -->` citan IDs y juicios internos ("registro latinoamericano"): confirmar que `maquetar-pdf` elimina todos los comentarios HTML. Revisado: el texto visible no cita frases literales ni IDs.
- ES: "pila" (fregadero) -> "fregadero" (más neutro en España); "estés tranquilo o tranquila" -> "cuando estés con calma".
- Ejercicio físico (sentadillas/flexiones) dirigido a un público que puede llevar días sin comer o dormir: añadir "si te encuentras con fuerzas".
- Marca: "comprobar que el título no exista antes de lanzar" (marca.json); fuera del alcance de esta revisión.

## Español de España (ES)
Registro correcto: "móvil", "aplicación", "temporizador", "vosotros" (compartís), "23:40", "sentadillas/flexiones", "WhatsApp", "lavavajillas". Sin latinoamericanismos en el texto visible. Los latinoamericanismos están solo en las frases ancla (no visibles), ya declarado. Corregir los puntos de F4/F5.

## Cita literal de comentarios en texto público
Comprobado contra frases.md y avatar.md: ninguna frase de cliente aparece entre comillas ni casi literal en el texto público de EN ni ES. Única cercanía: F4 (caso "me dejó"), aceptable.

## Frases nuevas para la lista de prohibidas de `redactar-ebook`
Añadidas con fecha 2026-10-14: "la vida real complica las cosas / real life gets in the way"; "es sencilla / is simple" como introducción de una explicación.

## Siguiente paso
Aplicar F1-F4 (y F5 si procede), volver a pasar por revisión (vuelta 2). Si tras la vuelta 2 sigue en CAMBIOS: PASAR AL CRÍTICO. Retrotraducción para el usuario: `ebook/en/muestra-retrotraduccion-es.md`.

---

## Vuelta 2 (2026-10-15)

### VEREDICTO: APROBADO (con 3 retoques menores opcionales)

Comprobado contra el informe de la vuelta 1:
- F1 (grave) resuelto: EN añade que el 016 no atiende a hombres (112 u Oficina de Asistencia a las Víctimas). Teléfonos EN y ES coinciden con avatar.md §8.
- F2 resuelto: desaparecen "Tiempo de uso" y "Bienestar digital"; ahora "la función de tiempo de uso que traiga tu móvil, si la tiene" y "si tu móvil permite un código". Sin nombres de funciones sin fuente.
- F3 resuelto: quitada la generalización "mucha gente...", reformulado el "reflejo de deslizar", la explicación de "Por qué diez minutos" es hipótesis explícita ("no un hecho probado"). Queda "castigarte suele mantener el bucle" (suavizado, aceptable).
- F4 resuelto: ES en género neutro ("a esa persona", "una amistad en común"); el cap. 12 ya no se promete en ES ("una guía para los encuentros inevitables"). EN conserva el cap. 12, coherente con estructura §5.
- F5 resuelto: "fregadero", "con calma", "si te encuentras con fuerzas"; "hoja de disparadores" unificada (ya no "registro/tracker" para lo mismo); "versión imprimible y versión editable"; ancla de "Si has mirado" cambiada a ES14/ES19; anclas [SIN DATO] declaradas en los casos "trabajo" y "dañina" en ES; ejemplo declarado "imaginado"; relleno "La vida real complica las cosas" eliminado; "gratuita" del 024 eliminado.
- Sin fallos nuevos graves. El texto visible no cita frases de clientes. ES en español de España.

Retoques menores opcionales (no bloquean):
1. EN, "Mute the side doors": la última frase repite la lista anterior ("tagged photo, mutual friend's story"). Borrar la repetición.
2. Antes de publicar: reverificar la vigencia de los teléfonos (112, 024, 016, 911, 988, 1-800-799-7233, START 88788) y confirmar que maquetar-pdf elimina los comentarios HTML.
3. Pendientes fuera de esta revisión: licencias de fuentes (Inter y Source Serif 4, OFL) al incrustar; comprobar que el título de marca no exista.

Retrotraducción EN->ES actualizada: ebook/en/muestra-retrotraduccion-es.md.

Responde solo "hecho" al terminar ambas.
