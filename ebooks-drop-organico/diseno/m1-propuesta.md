# Módulo 1 · Propuesta de diseño v2 (paso 4, SIN CREAR)

_14-oct-2026 · Opus · v2 tras `pruebas/consejo-prueba-1.md` (veredicto CAMBIOS, todos aplicados). Base: `conocimiento/01-nichos/02-critica-travis-vs-elevate.md` y `ESTADO.md`._

## Piezas
| Pieza | Tipo | Modelo | Qué hace |
|---|---|---|---|
| `puntuar-nicho` | skill | Sonnet dirige; búsquedas con Haiku | Candidatos → filtros → pruebas → puntuación **por idioma (ES y EN por separado)**. Salida: tabla + ficha por nicho en `pruebas/` |
| `avatar-angulos` | skill | Sonnet | Modo **ligero** (3 finalistas): miedo central + 5 frases reales por idioma + 5 ganchos. Modo **completo** (solo el nicho elegido): 3 Circles + ≥10 frases reales por idioma + banco de ángulos. Se reutilizará en ebook, web y guiones |
| `mentor-nichos-travis-nicholson` | agente | Sonnet | Opina sobre la lista corta como Travis. Solo sabe su `01-analisis.md` + grafo |
| `mentor-nichos-elevate-publishers` | agente | Sonnet | Opina como Elevate. Solo sabe su `01-analisis.md` + grafo |
| `critico` | agente reutilizable (todos los módulos) | Opus | Compara a los mentores y decide qué aplicar en nuestro caso con datos |

- Mentores y crítico actúan **solo sobre la lista corta (máx. 3)**.
- **Prohibido** usar los agentes y skills antiguos (`investigador-avatar`, `investigador-ebooks`, `ds-*`, `nicho-ebooks`) — regla 8.

## Flujo
1. **Candidatos** (10-15) desde mercados con dolor fuerte (relaciones, salud no médica, dinero personal, crianza…) + lo que sugieran los datos. [ESTIMACIÓN] lista inicial.
2. **Filtros eliminatorios** (sí/no):
   - F1 Dolor estable; modas solo como ángulo dentro de un nicho estable (crítica §3, decisión usuario 14-oct).
   - F2 Sabemos su miedo (círculo central) — Elevate [rO4h5ofNWic].
   - F3 Cabe un ebook de acción **que no exija autoridad profesional ni experiencia vivida** (riesgo nº 1, crítica §4).
   - F4 Riesgo de plataforma/legal manejable. Finanzas y salud: sin promesas de resultado ni asesoramiento personalizado (decisión 14-oct; verificar en mód. 7).
   - F5 Idioma: nota ≥3,5 en un idioma y ≥2,5 en el otro [ESTIMACIÓN] (decisión 14-oct).
   - F6 Funciona **sin cara**: existen cuentas sin personaje con tracción en el tema, y etiquetar el contenido IA (obligatorio en TikTok/Meta) no lo invalida.
3. **Puntuación 1-5 por idioma.** Pesos y anclas son [ESTIMACIÓN] a calibrar en la prueba:
   | Criterio | Peso | 1 | 3 | 5 | Origen |
   |---|---|---|---|---|---|
   | Dolor repetido | 20 % | <5 quejas distintas en 12 meses | 5-20 | >20 con palabras parecidas | Travis [6JXBC5kaDUw], Elevate [1yuuEaz2cvs] |
   | Pruebas de pago | 20 % | ningún competidor con señal | 1-3 con señal moderada | ≥4 con señal fuerte | crítica §6 |
   | Avatar nítido y alcanzable | 15 % | solo demografía | estilo de vida + algún miedo | miedo central claro con frases reales | Elevate [sE5B7ApMX8E], regla 10 |
   | Potencia de ángulos | 15 % | <5 ganchos | 5-9 | ≥10 distintos para público inconsciente | Elevate [IZCVZQtV2TI][GEfbMGW_45U] |
   | Hueco en competencia | 10 % | reseñas negativas sin patrón | 1 queja repetida | ≥2 quejas repetidas que un ebook de acción resuelve | Elevate [CimmheHK8hg] |
   | Precio ≥15 € plausible | 10 % | competencia <8 € | 8-15 € | ≥15 € con ventas visibles | crítica §3, `datos/idioma-es-vs-en.md` |
   | Estabilidad | 10 % | Google Trends cae >50 % en 5 años | estable | crece | crítica §6 (no Travis: él usa Trends a 48 h para modas) |

   **Señal de pago por plataforma**: Amazon = nº de reseñas y ranking de los 10 primeros; Etsy = ventas visibles de la tienda; Hotmart = "temperatura"; Gumroad = contador de ventas o valoraciones si se muestran. Si una plataforma no muestra nada → **[SIN DATO]**, nunca se rellena con una suposición.
4. **Lista corta** (top 3) → `avatar-angulos` ligero → mentores → crítico.
5. **Elección** del nicho por el usuario (punto de aprobación) → `avatar-angulos` completo para el elegido.

## Reglas comunes
- Consultar el grafo antes de leer material o buscar fuera; lo nuevo entra al grafo.
- Toda cifra con fuente y fecha. Etiquetas [DATO] / [OPINIÓN mentor] / [ESTIMACIÓN] / [SIN DATO].
- **Frases del avatar**: reales, con enlace, buscadas **en el idioma correspondiente** (nada de traducir Reddit EN para el avatar ES). **RGPD**: se guarda la frase y el enlace, sin nombre de usuario; en textos públicos (web, vídeos) se usa paráfrasis.
- No se copian prácticas engañosas de los mentores (crítica §4).

## Pendiente fuera de este módulo
- **Prueba de pago real** (aprobada en crítica §3): tras elegir nicho y **antes de redactar el ebook completo**. Se diseña al abrir el módulo 2 (página con precio o lista de espera + vídeos).

## Prueba prevista (paso 6)
Caso real desde cero en `pruebas/m1-prueba-1/`. Aprobada si: (a) cada puntuación tiene fuente o [SIN DATO], (b) cada finalista trae 5 frases reales por idioma enlazadas, (c) el crítico da una recomendación argumentada que puedas entender y cuestionar.
