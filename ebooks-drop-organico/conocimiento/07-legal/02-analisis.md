# Módulo 7 · Análisis crítico: qué es obligatorio, recomendable o para el gestor

_03-nov-2026 · Opus · Fuentes: `fiscal.md` y `consumo-datos-publicidad.md` (+ "Verificación 2"). Información verificada en fuentes oficiales, **no asesoramiento legal**. Vale para cualquier nicho; lo propio de un tema se marca._

## 1. OBLIGATORIO antes de vender
| # | Qué | Fuente | Afecta a |
|---|---|---|---|
| 1 | **Alta en Hacienda (modelo 036)** antes de la primera venta | [DATO] `fiscal.md` §1 | Usuario |
| 2 | **IVA**: ebook al 4 % (art. 91.Dos.1.2º LIVA); por debajo de 10.000 €/año de ventas UE, IVA español; Reino Unido cerrado (alta desde la 1.ª venta) | [DATO] `fiscal.md` §3-4, §6 | `montar-tienda-shopify` (impuestos, mercados) |
| 3 | **Precio final con IVA incluido** al consumidor | [DATO] `consumo…` §4 | `pagina-producto`, tienda |
| 4 | **Información precontractual** (identidad del vendedor, características, precio, funcionalidad e interoperabilidad del contenido digital, desistimiento) | [DATO] `consumo…` §1 | Página y condiciones |
| 5 | **Excepción de desistimiento en contenido digital**: (a) consentimiento expreso antes de la descarga, (b) reconocimiento de que se pierde el derecho, (c) confirmación en soporte duradero (email). Si falta uno: 14 días; sin información: hasta 12 meses | [DATO BOE art. 103.m y 98.7 TRLGDCU] | Checkout (casilla con app), email de confirmación |
| 6 | **Páginas legales**: aviso legal LSSI (datos del titular), condiciones de venta, privacidad RGPD, cookies (rechazar tan fácil como aceptar) | [DATO] `consumo…` §6 | `montar-tienda-shopify` |
| 7 | **Emails comerciales** solo con consentimiento previo y baja sencilla en cada email (LSSI arts. 21-22); mayores de 14 años | [DATO, verificación 2] | Formulario de la muestra (mód. 8) |
| 8 | **Nada de prácticas desleales**: urgencia falsa, reseñas o testimonios falsos (Ley 3/1991); si hay reseñas, informar de si se verifican (TRLGDCU art. 20) | [DATO, verificación 2] | Ya prohibido en todas las skills ✔ |
| 9 | **Rebajas**: el "precio anterior" es el más bajo de los 30 días previos (Ley 7/1996 art. 20) | [DATO; aplicación expresa a digital SIN DATO] | `metricas-lanzamiento` (pruebas de precio por periodos, sin tachados) ✔ |
| 10 | **Etiquetar contenido realista hecho con IA** en TikTok | [DATO] `consumo…` §9 | Módulo 5 |
| 11 | **Anuncios de Meta**: prohibido aludir a enfermedades mentales u otros atributos personales de quien ve el anuncio | [DATO, política 27-jun-2024] | Módulo 6 (ganchos POV ya previstos ✔) |

## 2. RECOMENDABLE (bajo coste, quita riesgo)
- **Botón de desistimiento** aunque el derecho se pierda por la excepción: obligatorio desde 19-jun-2026 para contratos con derecho de desistimiento; España sin transponer y sin confirmar si aplica tras la excepción [SIN DATO] → ponerlo (página "Desistir del contrato aquí" + confirmación + acuse por email).
- **Doble confirmación del email** (doble opt-in): la AEPD no la exige, pero sirve para **probar** el consentimiento [DATO verificación 2].
- **Edición humana sustancial** del ebook: un texto 100 % IA probablemente no está protegido por derechos de autor [DATO secundario] → ya lo cubre el revisor y nuestra revisión; anotar qué se editó.
- **Fuentes OFL** en PDF comercial: permitido [DATO]; no renombrar ni vender las fuentes; "Source" es nombre reservado.
- **Garantía de conformidad del contenido digital** (que funcione y sea lo descrito) → describir bien formato, páginas y dispositivos.

## 3. PARA EL GESTOR (depende de la situación personal; no decidirlo solos)
1. **Alta en autónomos (RETA)**: no hay umbral oficial; ganar menos que el SMI no excluye la habitualidad [DATO secundario: sentencia del Supremo citada por fuentes no oficiales]. Cuota mínima ≈ 206 €/mes [ESTIMACIÓN] y tarifa plana 2026 [SIN DATO].
2. **Epígrafe del IAE** (476.1 / 659.4 candidatos) [SIN DATO oficial].
3. **IVA de plantillas y del pack mixto** (4 % o 21 %) → posible consulta vinculante a la DGT.
4. Declaraciones periódicas (303, 390, 130) y OSS (369) si se superan 10.000 €.
5. Compatibilidad con ser estudiante (becas, IRPF de los padres, etc.).
6. Las demás dudas listadas al final de `fiscal.md`.

## 4. Lo que más cambia el negocio
- **Coste fijo de autónomo** (si el gestor confirma que hay que darse de alta): ≈ 206 €/mes [ESTIMACIÓN] → con un pack a ~15 € (≈ 14,4 € sin IVA al 4 %, menos comisiones) hacen falta **≈ 16 ventas al mes solo para cubrirlo** [ESTIMACIÓN]. Va al módulo 9 y refuerza hacer la búsqueda amplia de nicho (B) antes de lanzar.
- **El IVA del pack** puede pasar del 4 % al 21 % si las plantillas pesan mucho: diseñar el pack para que el ebook sea el producto principal y las plantillas, parte del libro [ESTIMACIÓN, confirmar con el gestor/DGT].

## 5. Cambios en lo ya construido
| Pieza | Cambio |
|---|---|
| `montar-tienda-shopify` | Mercados: España/UE (y EE. UU. si se decide); Reino Unido cerrado. Impuestos digitales UE activados. App de casilla en el checkout con el texto de la excepción. Email de confirmación con el reconocimiento. Página "Desistir del contrato aquí". Banner de cookies con "Rechazar". |
| `revision-tienda` (pasada 2) | Sustituir la lista genérica por la tabla del §1 y los recomendables del §2. |
| `pagina-producto` | Precio con IVA; información precontractual (formato, páginas, dispositivos, requisitos para abrirlo); enlace a condiciones y desistimiento; garantía = conformidad, sin promesas. |
| `redactar-ebook` / `revisor-calidad` | Registrar la edición humana; sin cambio de método. |
| Módulos 5, 6 y 8 | Etiquetado IA; anuncios sin atributos personales; consentimiento y baja en emails. |

## 6. Qué propondré en el paso 4 (sin crear)
Skill **`textos-legales`** (genérica: aviso legal, condiciones, privacidad, cookies, desistimiento, texto de la casilla y del email, con huecos para los datos del usuario), agente **`revisor-legal`** (lista de comprobación del §1-2 con sus fuentes; no sustituye a un profesional) y un documento **`consulta-gestor.md`** con las preguntas del §3. Actualizar `montar-tienda-shopify`, `revision-tienda` y `pagina-producto`.
