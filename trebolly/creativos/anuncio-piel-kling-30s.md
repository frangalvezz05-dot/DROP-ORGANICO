# Anuncio de PIEL en un solo clip de 30 s (Kling 4.0 Omni en Firefly) · 19-nov

## Datos de Firefly (lo que he podido comprobar)
- **Kling, en su propia guía de Kling 4.0:**
  - Duración: de 3 a 30 s, en pasos de 1 s. En el modo Omni, por defecto son 10 s: hay que subirlo a 30 a mano.
  - Imágenes de referencia: hasta 10.
  - Referencia de voz: sí, hasta 3 voces, cada una con 5-30 s de audio.
  - Prompt: hasta unos 8.000 tokens.
  - Audio: genera sonido y sincroniza los labios.
- **En Firefly no está confirmado.** La ayuda de Adobe (actualizada el 15-jul-2026) solo lista Kling 2.5 Turbo, 3.0 y 3.0 Omni. Un artículo dice que Adobe *planea* añadir Kling 4.0.
- **Mirad en la pantalla de Firefly:** la duración máxima, los créditos, si deja subir voz de referencia y el límite de caracteres. Mis prompts ocupan 3.648 caracteres (A) y 3.120 (B), parecido a vuestro borrador.

## Antes de generar: dos cambios que resuelven la mitad de los problemas
1. **Referencia 1: un fotograma de Marta con el jersey crudo, sacado de los anuncios de champú o tinte, no el retrato en albornoz.** Así la regla 3 se cumple de raíz: si la foto de referencia lleva albornoz, la IA tira hacia el albornoz por mucho que el texto diga lo contrario.
2. **Referencia de voz (si Firefly la acepta):** 15-20 s limpios de la voz de Marta sacados de los bloques de champú, sin agua ni música. Así la voz es la misma en los 3 anuncios. Sin esto, el de piel tendrá otra voz.

## 1) Prompt final, versión A (con diálogo) · 3648 caracteres
```
Vertical 9:16 smartphone UGC ad, 30 seconds, one continuous story in 6 shots with clean hard cuts. One woman, one bathroom and ONE shower head: only one shower head exists in the whole video. Unpolished iPhone look, natural skin texture, soft morning light from a frosted window on the left.

PRODUCT (reference image 2, copy it exactly in every shot): matte graphite-grey handheld shower head; deep cylindrical head with a round recessed face: silver-grey inner dish, dark central nozzle disc full of small holes, ring of black cone-shaped silicone bristles; straight graphite handle with a polished chrome collar and one round grey STOP button; thread at the bottom. No chrome ring on the face, no other buttons. Same shape, colour and size in every shot.

MARTA (reference image 1, same face in every shot): Spanish woman around 35, shoulder-length honey-blonde balayage hair, light freckles, no makeup, short nude nails, plain off-white knit jumper with the sleeves pushed up to the elbows in every shot. Never a bathrobe, never a towel.

BATHROOM: normal Spanish bathroom, white wall tiles with grey grout, glass shower screen, shower tray, chrome wall bracket with a silver hose, small white shelf with a few plain unbranded gel and cream bottles, folded muted-teal towel. No mirror.

VOICE: only Marta speaks, Spanish from Spain (Castilian accent), warm and lively like telling a friend, natural, never shouting, the same voice in every shot. Lines marked (voice-over) are spoken by Marta off screen; no mouth is visible in those shots.

Shot 1 [00:00-00:07] Phone propped on the shelf, medium close-up. From the very first frame she lifts a plain gel bottle toward the lens with raised eyebrows, then puts it back on the shelf; her other hand holds the shower head at chest height. She says: "Llevas años cambiando de gel y de crema..." Then she looks straight into the lens: "¿Y si lo que tienes que mirar es el agua?" Small nod, no smile.
Shot 2 [00:07-00:11] Close-up of her bare forearm; her other hand slowly runs along it. (voice-over) "El cloro del agua reseca la piel, ducha tras ducha."
Shot 3 [00:11-00:14] Close-up of two hands at the chrome wall bracket: they screw the thread of the shower head onto the silver hose by hand, then rest it in the bracket. (voice-over) "Este cabezal se enrosca a mano."
Shot 4 [00:14-00:18] Phone propped, close: she holds the shower head by the handle at chest height and points at the handle with the index finger of her other hand: "El filtro del mango retiene parte del cloro."
Shot 5 [00:18-00:25] Phone propped on the shower screen ledge, close-up of her hands over the shower tray: her right hand holds the shower head and water flows only from the nozzle disc; her thumb presses the STOP button on the chrome collar, the flow pauses and a few drops fall. (voice-over) "Y con este botón pausas el agua mientras te enjabonas." Then the soft spray comes back over her bare left forearm and hand. (voice-over) "Menos cloro sobre la piel."
Shot 6 [00:25-00:30] Phone propped, medium close-up: she brings the shower head a little closer to the camera: "Dos cabezales y diez filtros, cincuenta y nueve noventa y cinco." Then a brief half-smile under one second.

RULES: the shower head is always held in a hand or resting in the bracket; nothing floats. Never more than two hands in frame, five fingers each. Water comes only from the nozzle disc and only in Shot 5. Skin and hair look the same in every shot. No laughing and no faces after lines, except the final half-smile. No subtitles, no on-screen text, no logos, no music. Ambient sound of a small tiled bathroom. Nothing bends or melts.
```

**Qué he cambiado y por qué:**
- **De 7 planos distintos a 6.** El 0-3 y el 3-7 eran el mismo plano. El STOP y el chorro sobre el antebrazo pasan a ser un solo plano seguido. Cada corte es otra ocasión de que el cabezal cambie de forma.
- **Fuera el cabezal cromado viejo.** Es el plano más arriesgado: dos cabezales, muchas manos y un cambio en 4 s. Además, el "chrome" del viejo puede contagiar al nuestro (el aro cromado que no queremos). Ahora solo enrosca el nuestro. La frase no cambia.
- **"Only one shower head exists in the whole video":** evita que salgan dos cabezales en un mismo plano.
- **El STOP y el agua, sobre el plato de ducha y con el móvil apoyado en la mampara.** "Inside the shower" con jersey es raro e invita a la desnudez. Con el móvil apoyado tiene dos manos libres: una sujeta el cabezal y la otra recibe el agua. Antes, si sujetaba el móvil, el antebrazo con el agua no cuadraba.
- **"Then the spray comes back"** en vez de "presses again": no sabemos si el STOP se vuelve a pulsar o se suelta. No lo enseñamos.
- **Fotograma 0 más fuerte:** levanta el bote *hacia el objetivo*. Un objeto que se acerca a la cámara corta el scroll mejor que un bote cogido de lado.
- **El último plano, de 5 s en vez de 4:** el precio dicho son unos 4 s, y con la media sonrisa no cabía.
- **"Never a towel" y las mangas subidas "in every shot":** refuerza el jersey (sin desnudez) y deja los antebrazos al aire con sentido.
- **Voz en off marcada como "(voice-over)" y "no mouth is visible in those shots":** los planos con voz en off son de manos o de antebrazo, así no hay labios que tengan que cuadrar.
- **El agua, "only in Shot 5":** donde no hay agua, la IA no la inventa.
- **Las frases no cambian.** Todas caben a unas 2,5-3 palabras por segundo. La más justa es la del STOP (10 palabras en su tramo).

## 2) ¿Cuántos planos aguanta?
No tengo datos de Kling 4.0 que lo digan. Por cómo funcionan estos modelos, cada corte es otra oportunidad de que el producto o la cara cambien. Yo no pasaría de **5-6 planos en 30 s**, con una acción por plano. He dejado 6. Lo que se pierde respecto al borrador: el cabezal viejo (se enrosca solo el nuestro) y un corte entre el STOP y el chorro, que ahora es un mismo plano.

## 3) ¿Marcas de tiempo o "Shot 1…"? ¿Respetará la voz en off?
- **Las dos cosas a la vez ("Shot 1 [00:00-00:07]").** No tengo una prueba que diga cuál funciona mejor en Kling 4.0. Lo seguro es darle tanto la división en planos como los tiempos. Con Veo, las marcas de tiempo nos funcionaron en noviembre.
- **Voz en off:** es el punto débil. Puede pasar que mueva los labios de alguien, que se invente otra voz o que la diga con otro timbre. Para reducirlo:
  - los planos de voz en off no tienen boca visible;
  - las líneas van marcadas;
  - se usa la referencia de voz si existe.
- Si falla, **versión B** y la voz se pone en el montaje.

## 4) Versión B (sin diálogo, para poner la voz en el montaje) · 3120 caracteres
```
Vertical 9:16 smartphone UGC ad, 30 seconds, one continuous story in 6 shots with clean hard cuts. One woman, one bathroom and ONE shower head: only one shower head exists in the whole video. Unpolished iPhone look, natural skin texture, soft morning light from a frosted window on the left.

PRODUCT (reference image 2, copy it exactly in every shot): matte graphite-grey handheld shower head; deep cylindrical head with a round recessed face: silver-grey inner dish, dark central nozzle disc full of small holes, ring of black cone-shaped silicone bristles; straight graphite handle with a polished chrome collar and one round grey STOP button; thread at the bottom. No chrome ring on the face, no other buttons. Same shape, colour and size in every shot.

MARTA (reference image 1, same face in every shot): Spanish woman around 35, shoulder-length honey-blonde balayage hair, light freckles, no makeup, short nude nails, plain off-white knit jumper with the sleeves pushed up to the elbows in every shot. Never a bathrobe, never a towel.

BATHROOM: normal Spanish bathroom, white wall tiles with grey grout, glass shower screen, shower tray, chrome wall bracket with a silver hose, small white shelf with a few plain unbranded gel and cream bottles, folded muted-teal towel. No mirror.

SOUND: no speech at all. Marta never talks; her lips stay relaxed and closed. Only ambient sound of a small tiled bathroom, and running water in Shot 5.

Shot 1 [00:00-00:07] Phone propped on the shelf, medium close-up. From the very first frame she lifts a plain gel bottle toward the lens with raised eyebrows, then puts it back on the shelf; her other hand holds the shower head at chest height. Then she looks straight into the lens and gives a small nod, no smile.
Shot 2 [00:07-00:11] Close-up of her bare forearm; her other hand slowly runs along it.
Shot 3 [00:11-00:14] Close-up of two hands at the chrome wall bracket: they screw the thread of the shower head onto the silver hose by hand, then rest it in the bracket.
Shot 4 [00:14-00:18] Phone propped, close: she holds the shower head by the handle at chest height and points at the handle with the index finger of her other hand.
Shot 5 [00:18-00:25] Phone propped on the shower screen ledge, close-up of her hands over the shower tray: her right hand holds the shower head and water flows only from the nozzle disc; her thumb presses the STOP button on the chrome collar, the flow pauses and a few drops fall. Then the soft spray comes back over her bare left forearm and hand.
Shot 6 [00:25-00:30] Phone propped, medium close-up: she brings the shower head a little closer to the camera, then a brief half-smile under one second.

RULES: the shower head is always held in a hand or resting in the bracket; nothing floats. Never more than two hands in frame, five fingers each. Water comes only from the nozzle disc and only in Shot 5. Skin and hair look the same in every shot. No laughing and no faces after lines, except the final half-smile. No subtitles, no on-screen text, no logos, no music. Ambient sound of a small tiled bathroom. Nothing bends or melts.
```
- Los tiempos son los mismos que en A, así que las voces de champú y tinte (o la locución de ElevenLabs) encajan encima.
- En B no habla nunca. En los planos en que se le ve la cara, hace el gesto pero no mueve los labios, y queda como "voz en off" de toda la vida.

## 5) Si el máximo es de 15 s: dos clips que encajan
- **Clip 1 (15 s):** Shot 1 [0-7] + Shot 2 [7-11] + Shot 3 [11-15].
  - El Shot 3 alarga 1 s el final: el cabezal queda quieto en el soporte y las manos salen del plano.
  - **El último fotograma es el cabezal en el soporte, sin manos ni cara.** Es una imagen quieta y sencilla. Sin cara, no hay riesgo de que cambie en el empalme.
- **Clip 2 (15 s), con ese último fotograma como imagen de inicio:**
  - [0-1,5] su mano entra y coge el cabezal del soporte (la acción sigue sin corte);
  - Shot 4 [1,5-4,5], Shot 5 [4,5-10,5] y Shot 6 [10,5-15].
- **En el montaje:** los dos clips se pegan en ese fotograma. La voz tiene que ser la misma en los dos, así que la referencia de voz es obligatoria. Si no la hay, versión B.

## 6) Los 3 riesgos más probables y cómo los cubre el prompt
1. **El cabezal cambia de forma** (aro cromado, cabeza plana, otro tamaño):
   - el bloque PRODUCT va arriba, con la referencia 2 y "no chrome ring on the face";
   - solo existe un cabezal;
   - fuera el cabezal viejo;
   - 6 planos en vez de 8.
   - Se revisa plano a plano. Si falla en un solo plano, en el montaje se tapa con la demostración equivalente de champú o tinte.
2. **La voz** (otra voz, acento latinoamericano, labios que se mueven en la voz en off):
   - referencia de voz;
   - "Spanish from Spain (Castilian accent)";
   - voz en off sin boca visible.
   - Si falla: versión B, con la voz encima.
3. **Marta cambia** (sale en albornoz o con otra cara):
   - la referencia 1, con el jersey;
   - "never a bathrobe, never a towel" y las mangas "in every shot".
4. **El extra que siempre vigilamos (física):** nada flota, dos manos como mucho y agua solo en el Shot 5. Además, en cada plano está escrito quién sujeta el móvil (apoyado), para que no aparezca una tercera mano.

**Fuentes:**
- [Kling 4.0, guía de uso (Kling)](https://kling.ai/quickstart/kling-4-model-user-guide)
- [Kling AI lanza el modelo 4.0 con clips de 30 s (TechEdge AI)](https://techedgeai.com/kling-ai-launches-4-0-video-model-with-30-second-clips/)
- [Generar vídeos con Kling en Firefly (ayuda de Adobe)](https://helpx.adobe.com/ae_ar/firefly/web/work-with-audio-and-video/work-with-video/generate-videos-using-kling.html)
