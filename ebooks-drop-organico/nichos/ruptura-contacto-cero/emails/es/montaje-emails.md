# Montaje de los emails ES · Shopify Email (borrador)

Todo lo hace Fran o se deja en borrador; Claude no envía ni activa nada (regla 9). Herramienta: **Shopify Email** (10.000 envíos/mes gratis [DATO, `09-numeros/datos-costes.md`]). {{APP_EMAIL}} sigue sin elegir en `legal/formulario-email.md`: confirmar antes de nada.
Fuente de textos: `emails/es/secuencia.md`. Estado de todo: **sin montar**; lo marcado [SIN VERIFICAR] no se ha podido comprobar (Shopify no está conectado en esta sesión).

## Pasos
1. **Formulario** de la página de muestra: email + casilla 1 (obligatoria, no premarcada) + casilla 2 (opcional, no premarcada) con los textos de `legal/formulario-email.md`. Guardar fecha, hora y texto aceptado.
2. **Doble confirmación**: activar en Shopify la confirmación de suscripción (opt-in confirmado) y poner el email 0 como plantilla [SIN VERIFICAR: ajuste exacto y si permite texto propio].
3. **Entrega (email 1)**: el archivo de la muestra se aloja como enlace de descarga. Debe llegar a quien solo marcó casilla 1: Shopify Email solo envía a clientes suscritos a marketing, así que el email 1 **no** puede ir por la automatización de marketing. Opción: plantilla de notificación o app de formularios con envío transaccional [SIN VERIFICAR; decisión pendiente].
4. **Automatización de bienvenida (emails 2-5)**: crear en borrador una serie con disparador "se suscribe a marketing", esperas de 1, 2 y 2 días y 3 días desde el email 1 (días 1, 3, 5, 8). Se envía solo a suscritos (casilla 2).
5. **Compra**: email 6 = notificación "confirmación de pedido" de Shopify con el texto de `legal/email-confirmacion.md` y la copia literal del consentimiento.
6. **Post-compra (email 7)**: automatización a 3 días de la compra, solo a suscritos [SIN VERIFICAR si Shopify Email permite esa espera].
7. **Pie**: titular, motivo de recepción, enlace de baja con un clic y los avisos de ayuda en todos los emails 1-5 y 7.
8. **Precio** del email 4: usar la variable de precio del producto si la herramienta la admite; si no, escribirlo a mano solo cuando el precio esté decidido y comprobarlo contra página y checkout.

## Pruebas antes de activar
- Enviarse cada email de prueba a un correo propio: enlaces, móvil, baja con un clic, remitente.
- Probar el flujo de formulario sin casilla 2: debe recibir 0 y 1 y nada más.
- Probar con casilla 2: debe recibir 0, 1 y luego 2-5 en los días indicados.
- Comprobar que el email 6 sale con la copia literal del consentimiento.

## Pendientes (de Fran / del titular)
- Rellenar {{NOMBRE_TITULAR}}, {{NIF}}, {{DOMICILIO}}, {{EMAIL_CONTACTO}}, {{NOMBRE_TIENDA}}, {{APP_EMAIL}}.
- Decidir el precio (prueba 14,99 / 19,99) y la fecha de envío.
- Revisar con `revisor-legal` (punto 7 y 14) la secuencia final antes de activar.
- Confirmar vigencia de 112 / 024 / 016.
- Dar un "sí" explícito antes de activar cualquier automatización.

## Métricas a mirar (con lo que da Shopify Email)
Aperturas y clics por email (la apertura es poco fiable por la protección de privacidad de los clientes de correo [ESTIMACIÓN]), bajas y ventas atribuidas. Una campaña manual por semana al empezar y limpiar inactivos hacia los 180 días [OPINIÓN mentor, Dani 8Er-sAVrULo].
