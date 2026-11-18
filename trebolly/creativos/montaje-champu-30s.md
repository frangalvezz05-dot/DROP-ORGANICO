# Anuncio de champú · montaje y variedad entre bloques (18-nov)

## 1) La mueca: sí, en el montaje, con dos ajustes
- **Cortar en el montaje es lo correcto:** no cuesta créditos, y Flow siempre da 8 s aunque sobren.
- **Ajuste 1:** no cortar justo en la última sílaba, sino 3-5 fotogramas después (0,1-0,2 s), donde acaba la onda de la voz. Si se corta en seco, la palabra suena mordida y el corte se nota.
- **Ajuste 2, para los bloques que faltan:** el clip va a durar 8 s se le pida lo que se le pida. Si el prompt dice "no smile, no faces" y nada más, la IA rellena esos 2 s con algo raro o se queda congelada. Hay que decirle qué hacer después de la última palabra, con algo neutro y fácil de cortar:
  - bloques intermedios: "after the last word she glances down at the shower head in her hand";
  - último bloque: "after the last word, a brief half-smile under one second, then she glances down at the shower head".
- **La media sonrisa,** solo al final del anuncio y recortada a unos 0,6 s.

## 2) Para que no sea monótono: alternar cámara, distancia, sitio y gesto
**Reglas para todos los bloques:**
- Se alternan el móvil apoyado y el selfie.
- Se alternan el plano medio (desde la cintura o el pecho) y el plano cerca (desde los hombros).
- Dos sitios del mismo baño: delante de la balda o junto a la mampara.
- Un gesto distinto en cada bloque, y la misma ropa siempre (el jersey crudo).
- **Manos, escrito en cada prompt:** en el selfie, "one arm extended holding the phone out of frame; the other hand holds the shower head by the handle the whole clip; nothing else in her hands". Nunca se pide una acción que necesite una tercera mano.
- **Sin espejos en el plano:** la IA falla mucho con los reflejos.

**Champú (ya generado):**
- M1 y M2 salen igual (apoyado, con los dos cabezales). Por eso en el montaje **M2 no se ve: solo se usa su voz**, debajo de las demostraciones.
- Se ve M1 al principio, M3 un momento (otra acción y otra distancia) y M4 en selfie al final.

**Tinte y piel (por generar):**
| Bloque | Cámara y plano | Sitio | Gesto (uno solo) | Después de la última palabra |
|---|---|---|---|---|
| Tinte M1 | Apoyado, medio | Balda | Sujeta un mechón de sus puntas hacia la cámara desde el primer fotograma; niega suave con la cabeza en "no, no es el champú" | Mira el mechón y lo suelta |
| Tinte M2 | Selfie, cerca | Mampara | En "Este cabezal" mete el cabezal en el plano con la mano libre | Baja la vista al cabezal |
| Tinte M3 | Apoyado, cerca | Mampara | Una mano sujeta el mango y la otra señala el mango con el índice en "su filtro" | Baja la vista al cabezal |
| Tinte M4 | Selfie, cerca | Balda | Acerca el cabezal a la cámara en "dos cabezales" | Media sonrisa de menos de 1 s y baja la vista |
| Piel M1 | Apoyado, medio | Balda (geles y cremas) | Coge un bote de gel sin marca, lo enseña y lo vuelve a dejar; en la pregunta, cejas arriba | Baja la vista a la balda |
| Piel M2 | Selfie, cerca | Mampara | En "Este cabezal" mete el cabezal en el plano | Baja la vista al cabezal |
| Piel M3 | Apoyado, medio | Mampara | Pulsa el STOP con el pulgar de la mano que sujeta el mango, hacia la cámara | Baja la vista al cabezal |
| Piel M4 | Selfie, cerca | Balda | Se pasa la mano libre por el antebrazo en "menos cloro sobre la piel"; en selfie la mano libre es la que lleva el cabezal, así que lo apoya contra el pecho y se toca el antebrazo con esa misma mano | Media sonrisa de menos de 1 s |

"Arrancar a mitad de frase" no se genera: se hace en el montaje. La voz de un bloque empieza debajo de la demostración anterior, y Marta aparece cuando ya está hablando (corte en J). Así parece que la pillas a mitad de frase sin regenerar nada.

## 3) Guion de montaje del anuncio de champú (unos 27 s)
**Cómo leerlo:**
- Los segundos son del anuncio terminado.
- "Trozo" indica qué segundos del clip original se usan.
- Los cortes exactos se ajustan al terminar cada palabra en la onda: los números de abajo son la guía a 2,7-3 palabras por segundo.
- Si la voz de los 4 bloques suma unos 23 s, el anuncio dura unos 27 s con la tarjeta. **No se estira a 30.**

| Anuncio (s) | Imagen | Trozo del clip | Voz debajo | Rótulo | Paso al siguiente |
|---|---|---|---|---|---|
| 0,0-2,4 | M1, Marta con los dos cabezales | M1 desde la primera sílaba (~0,2 s) | "Vale, a todas las que tenéis la ducha llena…" | **Tu champú no tiene la culpa** (desde el fotograma 0) | Corte seco |
| 2,4-4,2 | V01, aparta los botes | Los 1,8 s en que la mano empuja | "…de botes…" (sigue M1) | — | Corte seco |
| 4,2-6,1 | M1 otra vez, con zoom al 110 % | M1 desde ~4,2 s hasta el final de "eh" + 4 fotogramas | "…el champú no tiene la culpa, eh." (inclina el cabezal) | — | Corte seco, con la voz de M2 entrando a la vez |
| 6,1-7,7 | V07, chorro a contraluz | El mejor tramo de 1,6 s | "Mira el agua." (M2) | **Mira el agua** | Corte seco |
| 7,7-9,0 | V02, quita el viejo | Hasta que el cabezal viejo sale de la manguera | "Quitas el tuyo," | **Se enrosca a mano** | Corte en acción (sale el viejo y entra el nuevo) |
| 9,0-10,3 | V03, enrosca el nuestro | Desde que la rosca toca la manguera | "…enroscas este a mano," | (sigue) | Corte seco |
| 10,3-13,6 | V06, filtro en el mango | Cartucho saliendo y entrando | "…y el mango lleva un filtro. Retiene parte del cloro." (M2 → M3) | **Filtro en el mango** → **Retiene parte del cloro** | Corte seco |
| 13,6-15,2 | M3, Marta tocando los conos | El tramo de M3 en que dice "Y con el cepillo" | "Y con el cepillo…" | **Cepillo de silicona** | Corte seco |
| 15,2-17,2 | V04, chorro en el pelo → cepillo | El paso del chorro al cepillo | "…te masajeas mientras te lavas." | (sigue) | Corte seco, con la voz de M4 entrando |
| 17,2-19,6 | V05, pulsa STOP y se enjabona | Desde el pulgar en el botón hasta que se enjabona | "Con este botón pausas el agua." (M4) | **Botón STOP** | Corte seco |
| 19,6-21,9 | V08, pack de 2 | Plano fijo del pack | "Dos cabezales y diez filtros," | **2 cabezales + 10 filtros · 59,95 €** | Corte seco |
| 21,9-24,2 | M4, selfie | El tramo de M4 con el precio + media sonrisa recortada a 0,6 s | "…cincuenta y nueve noventa y cinco." | (sigue el del precio) | Corte seco |
| 24,2-27,2 | Tarjeta final | 3 s fijos | (solo ambiente y música) | 2 cabezales + 10 filtros · 59,95 € · Envío gratis · Garantía de entrega · logo | Fin |

**El sonido es lo que más delata los cortes:**
- **Ambiente continuo:** una sola pista de ambiente de baño a unos −30 dB bajo todo el anuncio, y el fondo de cada clip bajado. Si no, el ruido de fondo cambia en cada corte y se nota.
- **Fundido de 2-3 fotogramas** en cada unión de voces (M1 → M2 → M3 → M4).
- **Agua:** donde sale agua (V07, V04 y V05), su sonido mezclado bajo la voz.
- **Música con licencia,** muy baja (−24 dB), igual en todo el anuncio.
- **Comprobar que la voz de los 4 bloques es la misma.** Si cambia el timbre, pasar todas por el mismo cambiador de voz de ElevenLabs: mantiene el ritmo, así que los labios siguen cuadrando.

**Sin fundidos ni transiciones animadas:** solo corte seco, el corte en acción y el zoom de M1. Los fundidos parecen de anuncio de televisión.

## 4) Para que parezca más real y menos IA
1. **Unificar el color:** la misma corrección (temperatura y exposición) en todos los clips, porque la IA da tonos distintos en cada uno. Añadir un grano muy ligero (2-3 %): la piel de la IA es demasiado lisa y el grano lo disimula.
2. **Zoom de golpe al 110 %** cuando se vuelve a un mismo clip (M1). Es el truco de los creadores para que el salto no se note.
3. **Subtítulos en estilo de redes:** palabra a palabra o de 2-3 palabras, en una letra de sistema gruesa, blancos con contorno oscuro, en el tercio de abajo pero por encima de la zona que tapa Reels. Las palabras clave (filtro, cepillo, STOP), en color agua. La letra de marca, solo en la tarjeta final.
4. **Revisar fotograma a fotograma las manos** de cada trozo elegido: dedos y cabezal. Se usa el tramo más limpio de cada clip, no el clip entero.
5. **No repetir ninguna demostración** en el mismo anuncio.
6. **Los números:** escuchar que "cincuenta y nueve noventa y cinco" se entiende bien. Si no, se rehace solo M4.
7. **Versión 4:5:** no basta con recortar el 9:16. Hay que recolocar los rótulos y los subtítulos, porque el recorte se come arriba y abajo.
8. **Etiqueta de IA** al publicar, como está acordado.
