# Plan de publicación · Meal prep (EN) · The Sunday Sheet
_Skill `plan-publicacion` · 03-nov-2026 · Entradas: `en/guiones-01.md` (14 guiones, 3 ganchos cada uno), `referentes-virales.md`. Claude no crea cuentas ni publica (regla 9): Fran sube cada vídeo. Etiquetas: [DATO] / [OPINIÓN mentor] / [ESTIMACIÓN]._

## 0. Antes de publicar el primer vídeo (bloqueos reales)
| # | Qué falta | Quién | Afecta a |
|---|---|---|---|
| 1 | PDF del ebook maquetado (para las capturas reales) | Claude, módulo de maquetado | Todos los guiones con 'CAPTURA REAL' (los 14) |
| 2 | "The Mini Sunday" (PDF de ~12 págs.) + formulario de email con doble opt-in | Claude (redacta) + Fran (conecta formulario) | CTA de los 14 |
| 3 | Tienda en borrador probada con el pago desde el navegador interno de TikTok/Instagram (Marc `kq0bZo65WNM`) | Fran | Enlace de perfil |
| 4 | Cronometrar la semana 1 y la muestra (pendiente 4 de `estructura.md`) | Fran | G07 y cualquier "about 2 hours" |
| 5 | Huecos del titular y revisión legal de la tienda (`legal/revision-legal.md`) | Fran | Publicar tienda |
| 6 | Comprobar nombre/handle libre en TikTok, Instagram y YouTube y marca en USPTO (`marca.json`) | Fran | Cuentas |
| 7 | Cap. 11 (semana 4) sin redactar: **no decir "4 weeks" en pantalla** hasta que exista | Claude | G04, G09 (ya evitado) |

## 1. Cuentas (las crea Fran)
- 1 cuenta por plataforma, en inglés: TikTok, Instagram (Reels), YouTube (Shorts). Nombre propuesto: **The Sunday Sheet** (handle a comprobar). Foto: logo/colores de `marca.json` (verde #1F3A2E, acento #D9572B).
- Bio EN (sin promesas): "Meal prep that doesn't get old. One Sunday, one sheet. Free Mini Sunday below." + enlace a la página de **Mini Sunday** (captación) y, cuando exista, desde ahí a la página de producto [Marc `kq0bZo65WNM`: al producto, no a la home].
- **TikTok**: el enlace de bio exige ~1.000 seguidores [OPINIÓN Marc `-5U7E20GXL8`, verificar en la app]. Mientras tanto, el CTA de TikTok se cambia a: "Free Mini Sunday: link in our Instagram or YouTube profile (same name)". Reels y Shorts llevan enlace desde el día 1 [ESTIMACIÓN: verificar requisitos].
- **Calentamiento** (Fran, 10-15 min/día, 3-5 días): ver enteros vídeos de meal prep, guardar y comentar; no usar la cuenta personal [OPINIÓN Marc `ZB2fSfh9rZA`].
- Una sola cuenta con 2 ángulos principales (A2 + A1) y 2 de apoyo (A4 + A5): decisión de la crítica (1 avatar, 1 cuenta por idioma; cuenta nueva por ángulo solo si uno despega).

## 2. Calendario de 14 días (28 huecos = 2 al día; misma pieza en las 3 plataformas)
Reglas: días 1-4 un guion de cada formato; días 5-14 originales que faltan + variantes del que mejor vaya. **Variante = solo cambia el gancho** (texto + primer plano); si baja el alcance por parecerse, rotar el audio [Marc `SQFnF0cgRwk`: >30 % similar limita; Dani `s1hMMVWgf00`: un solo cambio por variante. Se contradicen: empezamos por un cambio y vigilamos]. Dejar ≥2 días entre un guion y su variante.

| Día | Hueco 1 | Hueco 2 | Notas |
|---|---|---|---|
| 1 | **G06** A1 POV | **G01** A2 POV | Los dos POV de emoción primero |
| 2 | **G02** A2 lista | **G11** A4 lista manos | |
| 3 | **G03** A2 mini-lección | **G08** A1 mini-lección | |
| 4 | **G09** A1 hojeo | **G05** A2 frase + respuesta | Hojeo: PDF maquetado listo |
| 5 | **G12** A4 lista | Variante gancho 2 de G06 | Revisar datos 72 h de días 1-2 |
| 6 | **G13** A5 lista | Variante gancho 2 de G01 | |
| 7 | **G10** A1 frase + respuesta | Variante gancho 2 de G11 | **Resumen semanal 1** |
| 8 | **G04** A2 hojeo | Variante gancho 2 de G02 | |
| 9 | **G14** A5 lista | Variante gancho 2 de G03 | |
| 10 | **G07** A1 lista (solo si ya se cronometró) | Variante gancho 2 de G08 | Si no: variante extra del mejor |
| 11 | Variante gancho 2 de G09 | Variante gancho 2 de G05 | |
| 12 | Variante gancho 3 del 1.º del top 5 % | Variante gancho 3 del 2.º | Se eligen con datos |
| 13 | Variante gancho 3 del 3.º | Variante gancho 3 del 4.º | |
| 14 | Variante gancho 3 del 5.º | Variante gancho 3 del 6.º | **Resumen semanal 2 + decisión de los 14 días** |

Total: 14 originales + 14 variantes = 28 huecos. Si al día 5 hay un vídeo claramente ganador, las variantes de los días 8-14 se concentran en él (Dani `8Er-sAVrULo`: 5-10 variantes del top 5 %).

## 3. Cada vídeo, listo para subir (lo prepara Claude; lo sube Fran)
Checklist por pieza: guion en `en/guiones-01.md` · prompts en `en/prompts-escenas.md` · texto de pantalla · descripción + hashtags (en el guion) · **ETIQUETA IA activada** si hay imágenes realistas generadas · audio en tendencia de EE. UU. elegido en la app [Marc `lqt9TLhk20g`: audio que guste al público local] · enlace UTM · avisos de la descripción (A4: seguridad alimentaria; A5: coste estimado).
UTM: `utm_source=<tiktok|instagram|youtube>&utm_campaign=<a1|a2|a4|a5>` (ya en `registro.csv`).

## 4. Registro
`registro.csv`: 42 filas (14 guiones × 3 plataformas, todos con el gancho 1 y campos de métricas vacíos). Las variantes se añaden como filas nuevas con el mismo `id_guion` y `gancho_variante` H2/H3. Rellenar a 24 h y a 72 h, y anotar el "por qué" [Dani `YFpMEAuSgXQ`].

## 5. Reglas de decisión
- **< 300 visitas a 72 h** = sin alcance: revisar cuenta (calentamiento) y gancho [Marc `SQFnF0cgRwk`].
- **Regla de fases** [Marc `oposIsO1i90`]: 0-1.000 → cambiar el segundo 1; 1.000-2.000 → segundo 2; 2.000-3.000 → segundo 3; >5.000 → A/B de música, texto o fondo.
- **Top 5 %** por clics a la muestra/tienda (no solo visitas) → 5-10 variantes.
- **Día 14**: si ningún vídeo pasa 1.000 visitas → cambiar de ángulo (siguiente prioridad: A3 con otro gancho sin "high-protein", A6, A7). Cambiar de precio o nicho solo con `metricas-lanzamiento` (≥1.000 visitas a la tienda).
- Mide también el **clic a Mini Sunday → email → compra**: el ebook de 24,99 $ se vende más por la muestra que por el vídeo directo [ESTIMACIÓN].
- Sesgo conocido: los referentes son de personas cocinando y con voz; nuestro formato sin cara puede rendir menos. Si la retención cae en el plano 1-2, probar una variante con manos reales de Fran filmadas (sin cara y sin "yo") [ESTIMACIÓN].

## 6. Resumen semanal (cada lunes; alimenta `guiones-organicos`)
| Semana | Mejor vídeo y por qué | Peor y por qué | Ángulo que sube/baja | Siguiente cambio |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |

## 7. Orden recomendado de primeros vídeos
G06, G01, G11 (ver `en/mentor-marc.md`). Los tres no necesitan "about 2 hours" y solo G06 y G01 dependen de capturas del cap. 1-2.
