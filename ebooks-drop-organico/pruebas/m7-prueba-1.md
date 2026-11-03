# Prueba módulo 7 (legal) · nicho ruptura-contacto-cero · 03-nov-2026

## Qué se probó
Skill `textos-legales` (8 textos en ES + casilla y email en EN) y agente `revisor-legal` (13 puntos) sobre los 8 textos y `tienda/pagina-producto.md`. Salida en `nichos/ruptura-contacto-cero/legal/`.

## Resultado
- Vuelta 1: 5 FALLOS corregibles en mis textos (nota interna en condiciones §4; enlace ODR con [SIN DATO] en el texto público; afirmación sin fuente sobre ley del consumidor; etiquetas [SIN DATO]/[ESTIMACIÓN] en privacidad; instrucciones de montaje visibles en la casilla).
- Vuelta 2: textos sin fallos propios. Pendientes ajenos a Claude: huecos del titular, apps de entrega y email, tarifa de IVA del pack, lista de cookies.
- Página de producto: 8 puntos con cambio propuesto (ver `revision-legal.md`). Lo grave: ES-13 "PENDIENTE MÓDULO 7", correo de soporte sin hueco {{...}}, sin enlaces a condiciones/desistimiento, sin registro de edición humana.
- Incoherencia hallada fuera de legal: `estructura.md` §2.2 usa IVA 21 % y `fiscal.md` dice 4 %.

## Problemas de la skill `textos-legales`
1. Faltan huecos: elige app de entrega y de email pero no hay hueco para ellas (usé `{{APP_ENTREGA}}`, `{{APP_EMAIL}}`). Añadirlos a la lista.
2. No dice cómo marcar las variables del pedido en el email (nº pedido, fecha, enlace). Usé corchetes [ ] para no chocar con `{{...}}`. Fijar la convención.
3. La regla "etiquetas solo en comentario" es difícil de cumplir en frases con dato dudoso (plazos, ODR, conservación): decir qué hacer con ellas (omitir la frase o redactar neutra). Yo fallé 5 veces en esto.
4. Límite de descargas, plazos de conservación y de reembolso: la skill pide límite de descargas pero no hay fuente ni dato. Especificar "indicar que lo fija la app; no poner cifra".
5. EN: pide solo casilla y email, pero estos enlazan a condiciones en inglés que no existen; aclarar o pedir condiciones EN.
6. No cubre la tienda inglesa/EE. UU. (sales tax, derecho de desistimiento no aplicable): conviene una nota o texto aparte.
7. No hay sitio para la lista de cookies hasta montar la tienda; el orden módulo 7 antes de montar la deja vacía.

## Problemas del agente `revisor-legal`
1. Punto 1 vs veredicto: huecos vacíos son "BLOQUEADO" en el punto, pero APROBADO los admite con "no publicar". Unificar.
2. Sin regla para etiquetas dentro del texto público (lo detecté yo): añadir un punto o subpunto.
3. Los puntos 10 y 11 son NO APLICA al revisar textos y página; el agente debería poder revisar un conjunto por separado (textos / página / tienda / vídeos).
4. Punto 6 (pie y banner) no se puede verificar antes de montar la tienda: añadir estado "NO VERIFICABLE".
5. No comprueba coherencia con otros archivos (IVA 21 % vs 4 %).

## Veredicto final
Skill utilizable con ajustes menores; agente útil. Revisor: **CAMBIOS** (textos corregidos; faltan datos del titular y cambios en la página). No publicar.
