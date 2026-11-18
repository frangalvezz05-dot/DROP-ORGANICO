# Música de los 3 anuncios (19-nov)
**Marcas:** [EXPERIENCIA] = criterio propio, sin fuente · [NO SEGURO] = no comprobado.
Las licencias las mira el asesor (D-044).

## 0. Antes de nada
1. **Si los anuncios ya están publicados, no cambiéis ahora el vídeo.**
   - Cambiar el vídeo de un anuncio en marcha lo manda otra vez a revisión y reinicia el aprendizaje y el reloj de las 72 h. Además, no es un «fallo técnico» de la regla.
   - Mi voto: preparar las versiones con la música nueva y probarlas en la siguiente ronda, como variable aparte, sobre el ángulo ganador.
2. **El vídeo de piel dice «El cloro reseca la piel»: choca con D-073.**
   - Es voz en off sobre el antebrazo, sin labios, así que se cambia solo la voz.
   - La frase acordada: «Ducha tras ducha, el cloro del agua cae sobre tu piel».

## 1. ¿Una música por ángulo o la misma? La misma, y en una sola pista
- **Los 3 se prueban a la vez para saber qué ángulo gana.**
  - Si cada uno lleva su música, la diferencia en el gancho (lo que se ve en los 3 primeros segundos, justo cuando más suena la música) podría deberse a la música y no al mensaje.
  - Dani: probar cambiando un solo elemento [s1hMMVWgf00].
- **Una sola pista, generada una vez y montada en los 3 vídeos.** Si se genera una por vídeo, la IA da una melodía distinta en cada una, aunque el texto sea el mismo.
- **Ventaja extra:** las tres usan el mismo sonido, y eso ayuda a que se reconozca la marca.
- **La música por ángulo se prueba después,** sobre el ganador y con la música como única variable.

## 2. Estilo común y golpes de cada vídeo
**Estilo:**
- pop-house alegre con toque funky, como un Reels de belleza en 2026;
- positiva y con ritmo, sin épica ni sonido de anuncio de tele (nada de ukelele ni silbidos).

**Ficha técnica:**
- **120 BPM:** un golpe cada 0,5 s y un compás cada 2 s. Mover un corte al golpe más cercano lo desplaza como mucho 0,25 s.
- **Instrumentos:**
  - bombo con pegada, palmas y chasquidos en 2 y 4, y shaker;
  - bajo funky;
  - plucks burbujeantes, «de agua» (encajan con la ducha), guitarra funky apagada y acordes de piano eléctrico.
- **Sin voces de ningún tipo,** ni trocitos de voz: chocan con la de Marta.
- **Que deje hueco a la voz:** sin melodía mientras ella habla; los ganchos, cortos y en los huecos.
- **En el altavoz del móvil el bajo casi no se oye:** el ritmo lo tienen que llevar las palmas y los plucks [EXPERIENCIA].

**Duraciones para que el bucle caiga en el golpe** (compases enteros a 120 BPM):
- **Champú:** 24,0 s (12 compases). La tarjeta final pasa de 23,3 s a 24,0 s (+0,7 s).
- **Tinte:** 26,0 s (13 compases). La tarjeta final, +~1 s.
- **Piel:** 26,0 s (13 compases). La tarjeta final, +0,5 s.

**El tema maestro (32 s = 16 compases):**
- 0 s: golpe y ritmo;
- 12-14 s: subida;
- 14 s: silencio de un golpe y ritmo filtrado hasta los 16 s;
- 16-28 s: toda la energía;
- 28-32 s: final con un redoble que vuelve al golpe del principio.

Las versiones de 24 y 26 s se hacen quitando compases enteros del tramo de 16-28 s.

### Champú (24,0 s)
- **0,00 s · golpe de entrada junto al chorro que arranca.** A los 0,15 s la música baja para el «Tu champú no tiene la culpa».
- **Cortes:** en los golpes (cada 0,5 s).
- **12-14 s · subida:** redoble que lleva al STOP.
- **Fotograma exacto del clic del STOP:** la música, a cero de golpe, sin fundido.
  - Solo se oyen el clic y las gotas.
  - Vuelve en el siguiente golpe, al menos 0,4 s después, filtrada.
  - A partir del siguiente compás (16 s), con toda la energía.
- **Precio:** con toda la energía y bajada bajo la voz.
- **Tarjeta final:** sin voz, la música sube; el último golpe es un redoble que enlaza con el principio. Sin fundido de salida.

### Tinte (26,0 s)
- **0,00 s · golpe** cuando el mechón roza la lente.
- **0,5-3,0 s · casi silencio**, solo un fondo suave filtrado, debajo de «Noventa euros de mechas… y a las pocas semanas…». Es la tensión.
- **3,0 s · golpe fuerte en «¡apagadas!»** (cae justo en un golpe a 120 BPM). Desde ahí entra el ritmo, con «Y no, no es el champú».
- **«…se come tu color»:** un acento pequeño en «color» (opcional).
- **Chorro sobre las mechas:** se abre el filtro y entra toda la energía.
- **Precio:** golpe al empezar la frase. **Tarjeta final:** como en champú.

### Piel (26,0 s)
- **0,00 s · golpe** con el bote de gel contra la lente («¡Llevas años cambiando de gel y de crema!»).
- **12-14 s · subida.**
- **Clic del STOP (~14,3 s):** silencio de golpe, igual que en champú. Vuelve filtrada y, en el siguiente compás, con toda la energía, mientras el agua cae sobre el antebrazo.
- **«Lo enroscas y listo»:** golpe en «listo».
- **Tarjeta final:** como en champú.

**El silencio del STOP se hace en el montaje, no en la generación.** La IA no clava los segundos [EXPERIENCIA]: se pone a cero en el fotograma exacto del clic, aunque no caiga en un golpe.

## 3. Prompts para ElevenLabs Music
- **Opción recomendada:** el prompt maestro. Generad 3-4 versiones, elegid una y montadla en los 3 vídeos.
- **Opción B:** solo si los fundadores quieren una pista por vídeo. Comparten el mismo estilo, pero cada una tendrá una melodía distinta.
- **Antes de montar:**
  - comprobad el BPM real con un detector;
  - si sale entre 118 y 122, se ajusta a 120 sin que se note.
- **En la interfaz, marcad «instrumental»** si existe la opción [NO SEGURO del nombre].

**Maestro · 32 s**
```
Upbeat feel-good pop-house instrumental for a fresh beauty and self-care social media video, modern TikTok/Reels style. 120 BPM, 4/4, bright major key. Punchy kick, crisp claps and finger snaps on 2 and 4, shaker and light tambourine, bouncy funky bass, bubbly water-like synth plucks, muted funk guitar chops, warm electric piano chords. Positive, playful, confident. Leave space in the midrange for a spoken female voice: no lead melody while the groove plays, short melodic hooks only in the gaps. Instrumental only: no vocals, no vocal chops, no humming, no lyrics. No ukulele, no whistling, no corporate stock-music feel, no epic or cinematic elements, no orchestral hits, no big EDM drop, no long reverb tails.
Exactly 32 seconds, 16 bars. 0:00 starts instantly on a punchy hit on the first downbeat (kick, clap and bright synth stab together), no intro, no fade-in, groove starts right away at medium energy. 0:02-0:12 steady bouncy groove with a short drum fill every 4 bars. 0:12-0:14 one-bar build with a snare roll and a rising filter. 0:14 full stop: one beat of total silence, then the groove returns low-pass filtered and quiet until 0:16. 0:16-0:28 full energy: brighter, extra percussion, chord stabs, a short catchy synth hook in the gaps. 0:28-0:32 same groove, ending with a one-beat drum fill that leads straight back into the opening hit so it loops seamlessly. No fade-out; the last sound ends exactly at 0:32.
```

**Opción B · Champú · 24 s**
```
Upbeat feel-good pop-house instrumental for a fresh beauty and self-care social media video, modern TikTok/Reels style. 120 BPM, 4/4, bright major key. Punchy kick, crisp claps and finger snaps on 2 and 4, shaker and light tambourine, bouncy funky bass, bubbly water-like synth plucks, muted funk guitar chops, warm electric piano chords. Positive, playful, confident. Leave space in the midrange for a spoken female voice: no lead melody while the groove plays, short melodic hooks only in the gaps. Instrumental only: no vocals, no vocal chops, no humming, no lyrics. No ukulele, no whistling, no corporate stock-music feel, no epic or cinematic elements, no orchestral hits, no big EDM drop, no long reverb tails.
Exactly 24 seconds, 12 bars. 0:00 starts instantly on a punchy splash-like hit on the first downbeat, no intro, no fade-in, groove starts right away at medium energy. 0:02-0:12 steady bouncy groove with a short drum fill at 0:08. 0:12-0:14 one-bar build with a snare roll and a rising filter. 0:14 full stop: one beat of total silence, then the groove returns low-pass filtered until 0:16. 0:16-0:22 full energy, brighter, chord stabs. 0:22-0:24 same groove ending with a one-beat drum fill that leads back into the opening hit for a seamless loop. No fade-out; ends exactly at 0:24.
```

**Opción B · Tinte · 26 s**
```
Upbeat feel-good pop-house instrumental for a fresh beauty and self-care social media video, modern TikTok/Reels style. 120 BPM, 4/4, bright major key. Punchy kick, crisp claps and finger snaps on 2 and 4, shaker and light tambourine, bouncy funky bass, bubbly water-like synth plucks, muted funk guitar chops, warm electric piano chords. Positive, playful, confident, a little sassy. Leave space in the midrange for a spoken female voice: no lead melody while the groove plays, short melodic hooks only in the gaps. Instrumental only: no vocals, no vocal chops, no humming, no lyrics. No ukulele, no whistling, no corporate stock-music feel, no epic or cinematic elements, no orchestral hits, no big EDM drop, no long reverb tails.
Exactly 26 seconds, 13 bars. 0:00 one short bright hit, then almost silence: only a soft filtered pad and a ticking hi-hat to build suspense until 0:03. 0:03 a big punchy hit on the downbeat and the full groove starts. 0:03-0:14 steady bouncy groove with a short drum fill at 0:10. 0:14-0:16 the filter opens up into a lift. 0:16-0:24 full energy, brighter, extra percussion, chord stabs. 0:24-0:26 same groove ending with a one-beat drum fill that leads back into the opening hit for a seamless loop. No fade-out; ends exactly at 0:26.
```

**Opción B · Piel · 26 s**
```
Upbeat feel-good pop-house instrumental for a fresh beauty and self-care social media video, modern TikTok/Reels style. 120 BPM, 4/4, bright major key. Punchy kick, crisp claps and finger snaps on 2 and 4, shaker and light tambourine, bouncy funky bass, bubbly water-like synth plucks, muted funk guitar chops, warm electric piano chords. Positive, playful, warm. Leave space in the midrange for a spoken female voice: no lead melody while the groove plays, short melodic hooks only in the gaps. Instrumental only: no vocals, no vocal chops, no humming, no lyrics. No ukulele, no whistling, no corporate stock-music feel, no epic or cinematic elements, no orchestral hits, no big EDM drop, no long reverb tails.
Exactly 26 seconds, 13 bars. 0:00 starts instantly on a punchy hit with a quick whoosh on the first downbeat, no intro, no fade-in, groove starts right away at medium energy. 0:02-0:12 steady bouncy groove with a short drum fill at 0:08. 0:12-0:14 one-bar build with a snare roll and a rising filter. 0:14 full stop: one beat of total silence, then the groove returns low-pass filtered until 0:16. 0:16-0:24 full energy, brighter, chord stabs, a short catchy synth hook in the gaps. 0:24-0:26 same groove ending with a one-beat drum fill that leads back into the opening hit for a seamless loop. No fade-out; ends exactly at 0:26.
```

## 4. Biblioteca de sonidos de Meta (si se prefiere)
- **Palabras clave:** upbeat pop, feel good, funky house, nu disco, happy, fresh, beauty, fashion, summer.
- **Filtros:**
  - género Pop / Dance / Electronic;
  - estado de ánimo Happy / Energetic / Playful;
  - 115-125 BPM;
  - instrumental.
- **Pegas:**
  - no sé dónde está hoy la biblioteca ni qué filtros tiene [NO SEGURO];
  - si la música solo se puede añadir dentro del Administrador de anuncios, no se puede bajar bajo la voz ni poner el silencio del STOP;
  - sirve solo si se puede descargar y montar.

## 5. Volúmenes y bajada bajo la voz
**Volúmenes** [EXPERIENCIA; Meta no publica un objetivo oficial que yo conozca]:
- **Mezcla final:** ~−14 LUFS de media y picos ≤ −1 dBTP.
- **Música:**
  - bajo la voz de Marta: 12-15 dB por debajo de la voz;
  - sin voz (demostraciones sin hablar y tarjeta final): 6 dB por debajo del nivel de la voz;
  - el golpe del fotograma 0 y la vuelta después del STOP, a tope un instante, y luego baja si entra la voz.
- **Agua:**
  - con voz, 4-6 dB por debajo de ella;
  - sin voz, el agua manda (al nivel de la voz).
- **Clic del STOP:** picos de ~−10 dBFS, en el silencio de la música.

**Bajada automática:** la música baja 8 dB cuando habla Marta.
- Entrada: 30-50 ms.
- Recuperación: 300-400 ms.

**Bajada a mano:**
- empieza a bajar 3 fotogramas antes de la frase;
- vuelve a subir en 8-10 fotogramas después de la frase.

**Ecualización:** quitar ~3 dB a la música entre 2 y 4 kHz, que es donde se entiende la voz.

**El −24 dB de antes no tenía referencia.** Ahora la cuenta es «12-15 dB por debajo de la voz», y sin voz, «6 dB por debajo».

**Comprobación final:** escuchar los 3 en el altavoz del móvil y con cascos. Que cada frase se entienda a la primera y que las palmas se oigan en el altavoz.

**Las versiones 4:5 llevan la misma mezcla.**
