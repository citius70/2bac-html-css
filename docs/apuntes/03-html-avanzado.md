# Módulo 3: HTML Avanzado

En este módulo aprenderás las etiquetas y estructuras más complejas y útiles de HTML:  
* tablas para organizar información,
* formularios para recopilar datos de los usuarios y 
* añadir elementos multimedia como audio y vídeo.

---

## 3.1. Tablas en HTML

Las **tablas** permiten presentar datos organizados en **filas** y **columnas**, como en hojas de cálculo. Aunque no se usan para maquetar páginas modernas, son fundamentales para datos.

**Estructura básica:**

=== "Código"
    ```html
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

**Explicación:**    
- `<table>`: define la **tabla**.  
- `<tr>`: **fila** de la tabla.  
- `<th>`: celda de **encabezado** (negrita).  
- `<td>`: celda de **datos**.  

**Atributos útiles:**  
- `colspan`: Celda ocupa varias columnas.  
- `rowspan`: Celda ocupa varias filas.

---

## 3.2. Formularios HTML

Un formulario permite a los usuarios enviar información. Está compuesto por diferentes campos de entrada como textos, contraseñas, emails, casillas y botones.

**Ejemplo básico:**

=== "Código"
```html
<form action="/enviar" method="POST">
  <label for="nombre">Nombre:</label>
  <input type="text" id="nombre" name="nombre" required>

  <label for="email">Email:</label>
  <input type="email" id="email" name="email">

  <button type="submit">Enviar</button>
</form>
```
=== "Renderizado *(haz clic para expandir*)"
<div>
<form action="/enviar" method="POST">
  <label for="nombre">Nombre:</label>
  <input type="text" id="nombre" name="nombre" required>

  <label for="email">Email:</label>
  <input type="email" id="email" name="email">

  <button type="submit">Enviar</button>
</form>
<\div>

- `<input type="text">`: Campo de texto corto.
- `<input type="email">`: Campo para email (comprueba formato).
- `<button type="submit">`: Botón para enviar el formulario.

**Otros campos útiles:**  
- `<textarea>`: área de texto largo.  
- `<input type="checkbox">`: casilla.  
- `<input type="radio">`: opción única.  
- `<select>...</select>`: menú desplegable.

**Tips:**
- Usa siempre etiquetas `<label>` conectadas al campo con `for` e `id` para accesibilidad.
- `required` obliga a rellenar el campo.

---

## 3.3. Elementos multimedia: audio y vídeo

Añadir audio y vídeo es muy sencillo con HTML5.

**Audio:**
```
<audio controls>
  <source src="musica.mp3" type="audio/mpeg">
  Tu navegador no soporta audio.
</audio>
```

**Vídeo:**
```
<video width="320" height="240" controls>
  <source src="video.mp4" type="video/mp4">
  Tu navegador no soporta video.
</video>
```
- Atributo `controls` añade los botones de reproducir y volumen.

---

## 3.4. Iframes: contenido externo incrustado

Los iframes sirven para mostrar dentro de tu web contenido de otras webs, como mapas o vídeos de YouTube.

```
<iframe src="https://www.youtube.com/embed/ID_VIDEO" width="560" height="315" allowfullscreen></iframe>
```

--- 

## 📝 Resumen

En este módulo has aprendido:
- Cómo crear tablas para organizar datos.
- Cómo crear formularios con campos útiles y buenas prácticas.
- Cómo insertar audio y vídeo en la web.
- Cómo incrustar contenido externo con iframes.

---

## 🎯 Ejercicios prácticos

1. **Crea una tabla** con 3 columnas (Nombre, Asignatura, Nota) y al menos tres alumnos.
2. **Crea un formulario de registro** que pida nombre, correo, curso y comentarios (área de texto), y un botón de enviar.
3. **Inserta en tu página** un vídeo de YouTube y un archivo de audio que tengas o uno libre de derechos.

---

## 🎯 Ejercicios

Ver [Ejercicios HTML Avanzado](../ejercicios/html-avanzado.md)

➡️ Sigue con el [Módulo 4: CSS Fundamentos](04-css-fundamentos.md)