# Módulo 2 · Propuesta de diseño v2 (paso 4, SIN CREAR)

_14-oct-2026 · Opus · v2 tras revisión del `consejo-diseno` (CAMBIOS, todos aplicados). Base: `conocimiento/02-redaccion/02-critica.md` (aprobada). Todas las piezas son genéricas: el nicho entra como dato desde `nichos/<nicho>/` (regla 11). Todas consultan el grafo antes de leer material._

## Piezas
| Pieza | Tipo | Modelo | Qué hace | Salida |
|---|---|---|---|---|
| `analizar-ebooks-mercado` | skill | Haiku + navegador | Ingeniería inversa de 8-12 [ESTIMACIÓN] ebooks/cuadernos del nicho (ES y EN): estructura, extensión, ejercicios, extras, precio, señales de venta. Solo estructura, nunca texto. "Ejemplos encontrados" si no hay señal de ventas. Reutiliza datos ya existentes en `nichos/<n>/` antes de abrir el navegador | `nichos/<n>/ebooks-mercado.md` (se renombra el actual `ebooks-lideres.md`) |
| `estructura-ebook` | skill | Sonnet; revisión del `critico` (Opus, **única** revisión cara antes de la prueba) | Avatar completo + ángulos + mínimo del mercado + diferencial → **pack** (qué incluye; precio objetivo [ESTIMACIÓN]) + **índice** (cada capítulo/día: problema, frase real, ejercicio, resultado) + **muestra gratis**. Incluye las reglas útiles de Kate sobre muestra gratis e imagen de "qué incluye" | `nichos/<n>/estructura.md` |
| `redactar-ebook` | skill | **Sonnet** para la muestra y todo lo previo a la prueba de pago; **Opus** solo para el ebook completo y solo si la prueba pasa | Redacta en el idioma líder y **adapta** al otro. Reglas anti-genérico (abajo) | `nichos/<n>/ebook/<idioma>/` |
| `revisor-calidad` | agente | Sonnet + Haiku (retrotraducción) | Lista de control: relleno y clichés, promesas prohibidas, datos sin fuente, coherencia con el avatar, legibilidad, avisos de contenido, **licencias de fuentes e imágenes**, nada copiado del mercado. Retrotraduce al español para el usuario. APROBADO / CAMBIOS. Si no aprueba tras 2 vueltas [ESTIMACIÓN] → entra el `critico` | `nichos/<n>/ebook/revision.md` |
| `maquetar-pdf` | skill | Sonnet (código) | HTML + CSS → PDF con el navegador Edge de Windows (**verificar en el paso 5** con una página de prueba). Plantilla editorial fija + kit de marca del nicho (`nichos/<n>/marca.json`). Páginas imprimibles (trackers/plantillas). Portada por código. Incluye las reglas de Kate sobre kit de marca y mockups. Solo fuentes con licencia libre para incrustar (OFL o similar) | `nichos/<n>/ebook/<idioma>/*.pdf` |
| `prueba-pago` | skill | Sonnet | **Solo diseño** (la ejecución va en módulos 3-5 con "sí" del usuario). Reutiliza los ganchos de `avatar-angulos` (no crea guiones). Diseña **dos opciones para que el usuario elija**: **(a) preventa real** con fecha de entrega y reembolso garantizado; **(b) puerta falsa transparente**: el precio y el botón se ven, y antes de pedir el email se dice claramente que aún no está disponible. Mide **clics en comprar / pagos**, no solo emails. Umbrales [ESTIMACIÓN]. RGPD del formulario. Ambas opciones marcadas para revisión legal en el módulo 7 | `nichos/<n>/prueba-pago.md` |
| `mentor-redaccion-kate-hayes` | agente | Sonnet | **Una llamada por nicho**: opina sobre producción, diseño, mockups, kit de marca y muestra gratis. Solo lee su `01-analisis.md` y cita el ID de vídeo en cada opinión. **Prohibido**: cifras de ingresos, la cifra "6x en email", ventas flash sin matiz UE y recomendar herramientas patrocinadas | — |
| `critico` | agente (ya existe) | Opus | Revisa solo estructura y pack (el texto lo revisa `revisor-calidad`) | — |

**Decisión para el usuario**: el valor útil de Kate (unas 6 reglas) ya va dentro de `estructura-ebook` y `maquetar-pdf`. Opciones: mantener su agente con una sola llamada por nicho (cumple "dos mentores por módulo") o eliminarlo (ahorra una llamada). Recomendación: mantenerlo con una llamada.

## Reglas anti-genérico
1. Cada capítulo/día se apoya en ≥1 frase real del avatar **en ese idioma** (con enlace). Si no hay frase en un idioma: [SIN DATO], usar el ángulo del avatar sin cita y avisar. **Nunca** presentar una frase traducida como real.
2. Cada sección termina en una acción (ejercicio, plantilla o decisión).
3. Ejemplos concretos en lugar de generalidades.
4. Lista de frases prohibidas (vacías o cliché), que crece con cada revisión.
5. Sin promesas de resultado, testimonios inventados ni urgencias falsas; avisos de contenido según el nicho.
6. Nada copiado ni parafraseado de cerca del mercado ni de mentores.

## Reglas editoriales (valores [ESTIMACIÓN]; se sustituyen por valores con fuente al crear la skill)
Tamaño como variable de nicho e idioma: **A4 para ES/UE y Letter para EN/EE. UU.** (las páginas imprimibles lo exigen). Cuerpo 11-12 pt, interlineado ~1,4, márgenes amplios, jerarquía de 3 niveles, índice con enlaces, espacios para escribir.

## Orden de uso con un nicho
avatar completo (`avatar-angulos`) → `analizar-ebooks-mercado` → `estructura-ebook` (+ `critico`) → `mentor-redaccion-kate-hayes` (1 llamada) → `redactar-ebook` **solo la muestra** (Sonnet) → `revisor-calidad` → `maquetar-pdf` de la muestra → `prueba-pago` (diseño) → [módulos 3-5 ejecutan la prueba] → si pasa: ebook completo (Opus) + revisión + maquetación.

## Prueba prevista (paso 6) con el nicho de ejemplo
Avatar completo + estructura y pack + muestra en EN adaptada a ES + revisión + PDF de la muestra con portada + diseño de la prueba de pago (dos opciones).
Aprobada si: (a) cada sección se apoya en una frase real enlazada o declara [SIN DATO]; (b) el revisor no encuentra relleno ni promesas prohibidas en ≤2 vueltas; (c) el PDF queda **igual o mejor que los dos competidores más completos** (cuaderno de Payhip con trackers y el de 90 días de Amazon.es), comparados lado a lado por el usuario **y** cumple la lista objetiva: índice con enlaces, espacios para escribir, páginas imprimibles, contraste legible, fuentes con licencia; (d) se calcula el coste en tokens de un ebook completo.
