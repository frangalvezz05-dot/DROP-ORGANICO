# Módulo 3 (+4) · Tienda, cobro y entrega — Propuesta de diseño v2 (paso 4, SIN CREAR)

_15-oct-2026 · Opus · v2 tras `consejo-diseno` (CAMBIOS, todos aplicados). Base: `conocimiento/03-tienda/02-critica.md` (aprobada). Decisión del usuario: Shopify + Shopify Payments. Todo genérico (regla 11). Antes de crear las piezas se añade el material del módulo 3 al grafo._

## Comprobaciones previas
- **Herramienta de Shopify**: instalada pero **sin autorizar** (15-oct). El usuario debe conectarla en la configuración de conectores de claude.ai. **Plan B**: la skill genera una guía paso a paso que ejecuta el usuario.
- **Capturas con Edge** (`--screenshot`): [DATO] probado en el módulo 2 (portadas).
- **Requisitos de enlace en la bio** de TikTok e Instagram: [SIN DATO]; según Marc, TikTok lo da a partir de 1.000 seguidores [kq0bZo65WNM] [OPINIÓN mentor]. Se verifica en el módulo 5; la medición no depende de ello (ver reglas).

## Piezas
| Pieza | Tipo | Modelo | Qué hace | Salida |
|---|---|---|---|---|
| `montar-tienda-shopify` | skill | Sonnet | Con la herramienta de Shopify (o guía para el usuario): tema gratuito, idiomas, **mercados solo los aprobados en el mód. 7 (por defecto solo España/UE; Reino Unido y resto CERRADOS)**, producto digital con la app oficial de descargas (no físico), páginas (inicio, producto, FAQ, contacto, legales "pendiente mód. 7"), formulario de email para la muestra gratis (consentimiento "pendiente mód. 7"), contraseña de tienda activa (se prueba sin publicar). **Todo en borrador.** La cuenta la crea el usuario; contratar plan, instalar apps de pago o publicar requiere "sí" explícito. Sin enlaces de afiliado de los mentores | Tienda en borrador + `nichos/<n>/tienda/montaje.md` |
| `pagina-producto` | skill | Sonnet | Lleva **dentro** las reglas destiladas de Adrián y Marc (sin llamar a sus agentes después de escribir). Orden final [ESTIMACIÓN: adaptación a digital del orden de Marc OZQGBv-TaXw]: título con beneficio · imágenes · 3-4 beneficios · qué incluye · precio [con IVA: ESTIMACIÓN hasta mód. 7] · botón (fijo en móvil) · vista previa del ebook (de la crítica, no de los mentores) · FAQ [wWC8SoeQ_Fk] · descripción problema → dolor → solución desde avatar y ángulos · garantía "pendiente mód. 7". **Cambios frente a Marc**: sin estrellas ni reseñas hasta que existan reales, sin barra de urgencia. Declara avatar y ángulo (regla 10) | `nichos/<n>/tienda/pagina-producto.md` |
| `imagenes-producto` | skill | **Haiku** (plantilla de código escrita una vez con Sonnet al crear la skill) | 5 tipos de Adrián [VyGaE-cp1GI]: portada, escaparate, lista de lo que incluye, perspectivas, extras. Marcos de móvil/tablet por código con páginas REALES del PDF y colores de `marca.json`. Sin imágenes de terceros. Declara avatar y ángulo | `nichos/<n>/tienda/imagenes/*.png` |
| `revision-tienda` | skill | **Haiku** + navegador (lista) y Sonnet (solo para juzgar prácticas engañosas) | **Dos pasadas**: (1) **técnica**, ahora: móvil, velocidad, enlaces, entrega del archivo, mercados, coherencia de mensajes (causas de "visitas sin ventas" de Marc [oEFWZdCw5FQ]); **pago de prueba desde el navegador de TikTok/Instagram en un móvil ajeno, iOS y Android, con la contraseña de la tienda** [kq0bZo65WNM]; (2) **legal**, después del mód. 7: solo precios con IVA, casilla de desistimiento, impuestos, políticas y garantía | `nichos/<n>/tienda/revision.md` |
| `mentor-tienda-adrian-saenz` | agente | Sonnet | **Opcional**, 1 llamada por nicho **antes** de redactar la página: montaje, marca, imágenes. Solo su `01-analisis.md` | — |
| `mentor-tienda-marc-verdu` | agente | Sonnet | **Opcional**, 1 llamada por nicho **antes** de redactar: conversión, página, TikTok. Solo su `01-analisis.md` | — |
| `critico` | agente (ya existe) | Opus | **Una sola llamada** al final de la revisión técnica, con la página incluida | — |

## Decisión para el usuario: PayPal
Los dos mentores recomiendan Shopify Payments **+ PayPal** [4JGeKANrv7g][rFa_w8eD-mA]. A favor: más gente puede pagar. En contra: otra cuenta, posibles comisiones extra (dato contradictorio en `datos-shopify.md`). Recomendación [ESTIMACIÓN]: empezar solo con Shopify Payments (incluye tarjetas y Apple/Google Pay) y añadir PayPal si la revisión muestra abandonos en el pago.

## Reglas comunes
- Prohibido: reseñas inventadas, contadores o escasez falsos, fotos o textos de otras tiendas, temas/apps de pago o enlaces de afiliado sin aprobación.
- Lo legal (políticas, desistimiento, garantía, IVA, alta fiscal, mercados) queda "pendiente mód. 7" con marcador visible; nada se publica sin él.
- **Medición** (la regla vive solo en `metricas-lanzamiento`, que se actualiza): UTM **por plataforma y por periodo** (no por vídeo, porque la bio tiene un solo enlace) + pregunta posterior a la compra "¿dónde nos conociste?" [ESTIMACIÓN].
- Coste: con estos cambios, por nicho ≈ 1 llamada a Opus y ~3 a Sonnet [ESTIMACIÓN del consejo].

## Orden de uso con un nicho
(mentores opcionales) → `imagenes-producto` → `pagina-producto` → `montar-tienda-shopify` (borrador) → `revision-tienda` técnica → `critico` → [mód. 7] → `revision-tienda` legal → "sí" del usuario → publicar.

## Prueba prevista (paso 6) con el nicho de ejemplo
Requiere: tienda de Shopify creada por el usuario (prueba gratuita) y herramienta de Shopify conectada (o plan B). Aprobada si: (a) la página cumple el orden y las reglas; (b) las 5 imágenes se generan con páginas reales; (c) la entrega funciona en un pedido de prueba; (d) se prueba el pago desde TikTok/Instagram en móvil ajeno y se documenta (si exige plan de pago, se pide "sí" antes); (e) el usuario juzga la página igual o mejor que 2 competidores.
