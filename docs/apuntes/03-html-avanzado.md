# HTML avanzado

---

**🎯 Objetivos del capítulo**

En este módulo aprenderás las etiquetas y estructuras más complejas y útiles de HTML:

* tablas para organizar información,    
* formularios para recopilar datos de los usuarios y     
* añadir elementos multimedia como audio y vídeo. 

---

## Tablas en HTML

Las **tablas** permiten presentar datos organizados en **filas** y **columnas**, como en hojas de cálculo. Aunque no se usan para maquetar páginas modernas, son fundamentales para datos.

### Etiquetas para tablas

**Las 4 etiquetas más importantes son:** `<table>`, `<tr>`, `<td>` y `<th>`. Con estas cuatro puedes crear cualquier tabla básica. Las demás son complementarias para estructura y estilos.

| Etiqueta | Descripción | Ejemplo |
|----------|-------------|---------|
| **`<table>`** | **Define una tabla completa.** Contenedor principal obligatorio. | `<table>...</table>` |
| **`<tr>`** | **Define una fila (table row).** Agrupa celdas horizontalmente. | `<tr><td>Celda</td></tr>` |
| **`<td>`** | **Define una celda de datos (table data).** Contenedor de contenido. | `<td>Contenido</td>` |
| **`<th>`** | **Define una celda de encabezado (table header).** Se muestra en negrita. | `<th>Título</th>` |
| `<thead>` | Agrupa el encabezado de la tabla (filas de títulos). | `<thead>...</thead>` |
| `<tbody>` | Agrupa el cuerpo o contenido principal de la tabla. | `<tbody>...</tbody>` |
| `<tfoot>` | Agrupa el pie de la tabla (totales, resúmenes). | `<tfoot>...</tfoot>` |
| `<caption>` | Define un título o descripción de la tabla. | `<caption>Mis datos</caption>` |
| `<colgroup>` | Agrupa columnas para aplicar estilos. | `<colgroup><col></colgroup>` |
| `<col>` | Define propiedades para una o varias columnas. | `<col style="width: 100px;">` |



**Ejemplo:**

=== "Código"
    ```html  linenums="1"
    <table>
        <thead>
            <tr>
                <th>Nombre</th>
                <th>Edad</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Ana</td>
                <td>17</td>
            </tr>
            <tr>
                <td>Luis</td>
                <td>18</td>
            </tr>
        </tbody>
    </table>
    ```
=== "Renderizado *(clic para expandir)*"
    <div>
    <table>
        <thead>
            <tr>
                <th>Nombre</th>
                <th>Edad</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Ana</td>
                <td>17</td>
            </tr>
            <tr>
                <td>Luis</td>
                <td>18</td>
            </tr>
        </tbody>
    </table>
    </div>


## Formularios en HTML

Un formulario permite a los usuarios **enviar información**. Está compuesto por diferentes campos de entrada como textos, contraseñas, emails, casillas y botones.

### Etiquetas para formularios

**Las 4 etiquetas  más importantes son:** `<form>`, `<input>`, `<label>` y `<button>`. Con estas cuatro puedes crear cualquier formulario básico funcional.

| Etiqueta | Descripción | Ejemplo |
|----------|-------------|---------|
| **`<form>`**| **Define un formulario completo.** Contenedor principal obligatorio. | `<form action="enviar.php" method="POST">...</form>` |
| **`<input>`** | **Define un campo de entrada.** El más versátil (texto, botón, checkbox, radio, etc.). | `<input type="text" name="nombre">` |
| **`<label>`** | **Define una etiqueta para un campo.** Mejora accesibilidad. | `<label for="email">Email:</label>` |
| **`<button>`** | **Define un botón interactivo.** Puede enviar o ejecutar acciones. | `<button type="submit">Enviar</button>` |
| `<textarea>` | **Define un área de texto multilínea.** Para textos largos. | `<textarea name="mensaje" rows="4"></textarea>` |
| `<select>` | **Define una lista desplegable.** Para seleccionar una opción. | `<select name="país">...</select>` |
| `<option>` | **Define una opción dentro de un select.** | `<option value="es">España</option>` |
| `<fieldset>` | Agrupa campos relacionados de un formulario. | `<fieldset><legend>Datos personales</legend></fieldset>` |
| `<legend>` | Define el título de un fieldset. | `<legend>Contacto</legend>` |
| `<datalist>` | Define una lista de opciones predefinidas para un input. | `<datalist id="ciudades"><option value="Madrid"></datalist>` |


**Ejemplo básico:**

=== "Código"
    ```html linenums="1"
    <form action="/enviar" method="POST">
    <label for="nombre">Nombre:</label>
    <input type="text" id="nombre" name="nombre" required>

    <label for="email">Email:</label>
    <input type="email" id="email" name="email">

    <button type="submit">Enviar</button>
    </form>
    ```
=== "Renderizado *(haz clic para expandir*)"
    <div style="background-color:#f5f5f5;">
        <form action="/enviar" method="POST">
        <label for="nombre">Nombre:</label>
        <input type="text" id="nombre" name="nombre" required>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email">
        <button type="submit">Enviar</button>
        </form>
    </div>


**Tips:**
- Usa siempre etiquetas `<label>` conectadas al campo con `for` e `id` para accesibilidad.
- `required` obliga a rellenar el campo.

**Ejemplo completo:**

=== "Código"
    ```html linenums="1"
        <form action="/enviar" method="POST">
            <fieldset>
                <legend>Información Personal</legend>
                
                <label for="nombre">Nombre:</label>
                <input type="text" id="nombre" name="nombre" required>
                
                <label for="apellido">Apellido:</label>
                <input type="text" id="apellido" name="apellido" required>
                
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                
                <label for="telefono">Teléfono:</label>
                <input type="tel" id="telefono" name="telefono">
                
                <label for="edad">Edad:</label>
                <input type="number" id="edad" name="edad" min="18" max="120">
            </fieldset>
            
            <fieldset>
                <legend>Asunto</legend>
                
                <label for="asunto">Selecciona un tema:</label>
                <select id="asunto" name="asunto" required>
                    <option value="">-- Elige una opción --</option>
                    <option value="consulta">Consulta general</option>
                    <option value="soporte">Soporte técnico</option>
                    <option value="sugerencia">Sugerencia</option>
                    <option value="otro">Otro</option>
                </select>
            </fieldset>
            
            <fieldset>
                <legend>Mensaje</legend>
                
                <label for="mensaje">Tu mensaje:</label>
                <textarea id="mensaje" name="mensaje" rows="5" cols="40" placeholder="Escribe tu mensaje aquí..." required></textarea>
                
                <label>
                    <input type="checkbox" name="privacidad" required>
                    Acepto la política de privacidad
                </label>
            </fieldset>
            
            <fieldset>
                <legend>Preferencias</legend>
                
                <label>
                    <input type="radio" name="contacto" value="email"> Preferencia por email
                </label>
                
                <label>
                    <input type="radio" name="contacto" value="telefono"> Preferencia por teléfono
                </label>
            </fieldset>
            
            <button type="submit">Enviar Formulario</button>
            <button type="reset">Limpiar</button>
            <button type="button" onclick="alert('Formulario en desarrollo')">Vista previa</button>
        </form>

    ```
=== "Renderizado"
    <form action="/enviar" method="POST">
        <fieldset>
            <legend>Información Personal</legend>
            <label for="nombre">Nombre:</label>
            <input type="text" id="nombre" name="nombre" required>
            <label for="apellido">Apellido:</label>
            <input type="text" id="apellido" name="apellido" required>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            <label for="telefono">Teléfono:</label>
            <input type="tel" id="telefono" name="telefono">
            <label for="edad">Edad:</label>
            <input type="number" id="edad" name="edad" min="18" max="120">
        </fieldset>
        <fieldset>
            <legend>Asunto</legend>
            <label for="asunto">Selecciona un tema:</label>
            <select id="asunto" name="asunto" required>
                <option value="">-- Elige una opción --</option>
                <option value="consulta">Consulta general</option>
                <option value="soporte">Soporte técnico</option>
                <option value="sugerencia">Sugerencia</option>
                <option value="otro">Otro</option>
            </select>
        </fieldset>
        <fieldset>
            <legend>Mensaje</legend>
            <label for="mensaje">Tu mensaje:</label>
            <textarea id="mensaje" name="mensaje" rows="5" cols="40" placeholder="Escribe tu mensaje aquí..." required></textarea>
            <label>
                <input type="checkbox" name="privacidad" required>
                Acepto la política de privacidad
            </label>
        </fieldset>
        <fieldset>
            <legend>Preferencias</legend>
            <label>
                <input type="radio" name="contacto" value="email"> Preferencia por email
            </label>
            <label>
                <input type="radio" name="contacto" value="telefono"> Preferencia por teléfono
            </label>
        </fieldset>
        <button type="submit">Enviar Formulario</button>
        <button type="reset">Limpiar</button>
        <button type="button" onclick="alert('Formulario en desarrollo')">Vista previa</button>
    </form>


## Elementos multimedia: audio y vídeo

Añadir audio y vídeo es muy sencillo con HTML5.

### Audio

Para insertar audio en HTML5, utiliza la etiqueta `<audio>` con controles básicos y múltiples formatos para compatibilidad. Aquí tienes un ejemplo completo.

=== "Código"
    ```html linenums="1"
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Audio en HTML5</title>
    </head>
    <body>
        <audio loop controls>
            <source src="../media/running-night.mp3" type="audio/mpeg">
            <source src="../media/running-night.ogg" type="audio/ogg">
            Su navegador no soporta el formato.
        </audio>
    </body>
    </html>
    ```
=== "Resultado"
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>AudioenHTML5</title>
    </head>
    <body>
        <audio loop controls>
            <source src="../media/running-night.mp3" type="audio/mpeg">
            <source src="../media/running-night.ogg" type="audio/ogg">
            Su navegador no soporta el formato.
        </audio>
    </body>
    </html>

**Explicación:**
- El navegador intentará reproducir el primer formato compatible (`mp3`).
- Si no lo soporta, probará con el siguiente (`ogg`).
- El texto final se muestra solo si ningún formato funciona.

#### Atributos del elemento `<audio>`

| Atributo | Descripción |
|----------|-------------|
| `controls` | Muestra los controles de reproducción (play, pausa, volumen, barra de progreso, etc.) en el reproductor. |
| `src` | Especifica la ruta del archivo de audio. Puede ir en `<audio>` directamente o dentro de etiquetas `<source>`. |
| `type` | Define el formato MIME del audio (usado en `<source>`) para que el navegador identifique el tipo de archivo. |
| `autoplay` | El audio se reproduce automáticamente al cargar la página. |
| `loop` | El audio se repite en bucle indefinidamente. |
| `muted` | El audio comienza silenciado. |
| `preload` | Indica cómo cargar el audio: `none` (no precargar), `metadata` (solo metadatos), `auto` (precarga completa). |

#### Formatos de audio y compatibilidad

| Formato | Tipo MIME | Navegadores compatibles |
|---------|-----------|-------------------------|
| **MP3** | `audio/mpeg` | Chrome, Firefox, Edge, Safari, Opera |
| **OGG** | `audio/ogg` | Firefox, Chrome, Opera |
| **WAV** | `audio/wav` | Safari, Firefox, Chrome, Edge |
| **AAC** | `audio/aac` | Safari, Chrome, Edge |
| **WebM** | `audio/webm` | Firefox, Chrome, Opera |   

**Notas importantes:**

1. Evita el `autoplay` en páginas web, puede ser molesto para los usuarios  
2. Siempre incluye un mensaje para navegadores antiguos  
3. Usa el atributo `preload="metadata"` para solo cargar información básica del audio  
4. Verifica que los archivos de audio estén en la ruta correcta  

¡Así tendrás un reproductor de audio funcional en todos los navegadores modernos! 🎵


### Video

Para insertar video en HTML5, utiliza la etiqueta `<video>` con controles básicos y múltiples formatos para compatibilidad. Aquí tienes un ejemplo básico.

=== "Código"
```
<video width="320" height="240" controls>
  <source src="video.mp4" type="video/mp4">
  Tu navegador no soporta video.
</video>
```
- Atributo `controls` añade los botones de reproducir y volumen.

#### Atributos del elemento `<video>`

| Atributo  | Descripción                                               | Valores posibles             | Uso típico                 |
|-----------|-----------------------------------------------------------|-----------------------------|----------------------------|
| src       | URL o ruta del archivo de vídeo                           | URL                         | Definir el vídeo a reproducir |
| controls  | Muestra controles de reproducción                         | Presencia (atributo booleano) | Mostrar controles (play, pausa, volumen) |
| width     | Ancho visual del reproductor en píxeles                   | Número                      | Ajustar tamaño ancho del vídeo |
| height    | Alto visual del reproductor en píxeles                    | Número                      | Ajustar tamaño alto del vídeo  |
| autoplay  | Reproducción automática al cargar la página               | Presencia (atributo booleano) | Iniciar reproducción sin interacción |
| loop      | Repetición automática del vídeo                           | Presencia (atributo booleano) | Reproducir en bucle continuo |
| muted     | Silenciar el audio al iniciar                             | Presencia (atributo booleano) | Silenciar para permitir autoplay sin sonido |
| poster    | Imagen mostrada antes de que empiece el vídeo             | URL a imagen                | Mostrar imagen de portada previa |
| preload   | Controla precarga de vídeo                                | none, metadata, auto        | Optimizar carga según dispositivo y contexto |

#### Formatos de video y compatibilidad

Aquí tienes una tabla resumen con los formatos de vídeo más comunes en HTML5, sus tipos MIME y la compatibilidad con navegadores principales:

| Formato  | Tipo MIME        | Navegadores compatibles                         |
|----------|------------------|------------------------------------------------|
| **MP4 (H.264)** | `video/mp4`     | Chrome, Firefox, Edge, Safari, Opera          |
| **WebM (VP8/VP9)** | `video/webm`    | Chrome, Firefox, Edge, Opera (no Safari)      |
| **Ogg Theora** | `video/ogg`     | Firefox, Chrome, Opera (no Edge ni Safari)    |
| **HEVC (H.265)** | `video/mp4`     | Safari, Edge (Windows 10+), Chrome (limitado) |
| **AV1**      | `video/mp4`     | Chrome, Firefox, Edge, Opera (no Safari)      |

- MP4 con códec H.264 es el formato más universalmente compatible.  
- WebM es un formato abierto que funciona muy bien en navegadores basados en Chromium y Firefox, pero no en Safari.  
- Ogg Theora tiene compatibilidad variada y es menos usado actualmente.  
- HEVC (H.265) tiene soporte en hardware moderno y Safari, pero no universal para todos los navegadores.  
- AV1 es un formato más nuevo con buena compatibilidad en navegadores modernos, menos en Safari.


## Iframes: contenido externo incrustado

Los iframes en HTML son elementos que permiten **incrustar contenido externo** dentro de una página web. Su función principal es mostrar **documentos HTML completos, vídeos, mapas u otros recursos** que provienen de otra página web distinta a la principal, sin que el usuario tenga que salir de la navegación actual.

### Puntos clave sobre iframes:

- La etiqueta es `<iframe>`, y uno de sus atributos principales es `src`, que indica la URL del contenido externo a mostrar.  
- Se pueden definir dimensiones con `width` (ancho) y `height` (alto), para controlar el tamaño visible del iframe.  
- El contenido incrustado opera de forma aislada, por lo que cualquier código o error en ese contenido no afecta a la página principal.  
- Es muy usado para insertar vídeos (por ejemplo de YouTube), mapas interactivos (como Google Maps), formularios o cualquier recurso externo.  
- Permite mejorar la experiencia del usuario al integrar contenido externo sin redireccionar ni recargar la página.  
- Tiene ventajas y desventajas en rendimiento, seguridad y SEO y debe usarse con cuidado especialmente si el contenido externo no es confiable.  

Ejemplo básico de uso: 

=== "Código"
    ```html
    <iframe src="https://www.youtube.com/embed/Imeq3GeRttw" width="560" height="315" title="Vídeo YouTube"></iframe>
    ```
=== "Resultado"
    <iframe src="https://www.youtube.com/embed/Imeq3GeRttw" width="560" height="315" title="Vídeo YouTube"></iframe>

--- 


<!-- ## 🎯 Ejercicios prácticos

1. **Crea una tabla** con 3 columnas (Nombre, Asignatura, Nota) y al menos tres alumnos.
2. **Crea un formulario de registro** que pida nombre, correo, curso y comentarios (área de texto), y un botón de enviar.
3. **Inserta en tu página** un vídeo de YouTube y un archivo de audio que tengas o uno libre de derechos.

---

## 🎯 Ejercicios

Ver [Ejercicios HTML Avanzado](../ejercicios/html-avanzado.md)

➡️ Sigue con el [Módulo 4: CSS Fundamentos](04-css-fundamentos.md) -->