# HTML básico

---

**🎯 Objetivos del capítulo**

> - Crear la estructura básica de una página HTML válida  
> - Utilizar etiquetas semánticas correctamente  
> - Trabajar con encabezados, párrafos y formato de texto  
> - Insertar enlaces e imágenes  
> - Crear listas ordenadas y desordenadas  
> - Estructurar contenido con elementos semánticos  

---

## ¿Qué es HTML?

**HTML** significa **HyperText Markup Language**, que en español sería **“Lenguaje de Marcado de Hipertexto”**.

Es el lenguaje estándar que se usa para **crear páginas web** y estructurar su contenido en internet.

### Qué significa cada parte:

* **HyperText (Hipertexto):**
   Se refiere a que el contenido puede incluir **enlaces** que conectan a otros documentos o páginas web. Por ejemplo, un enlace a Google:

   ```html
   <a href="https://www.google.com">Ir a Google</a>
   ```

* **Markup (Marcado):**
   Significa que usamos **etiquetas (tags)** para indicar la estructura y el significado del contenido, no solo el texto plano. Por ejemplo:

   ```html
   <h1>Este es un título</h1>
   <p>Este es un párrafo.</p>
   ```

   Aquí `<h1>` marca un título y `<p>` marca un párrafo.

* **Language (Lenguaje):**
   Es un **lenguaje formal**, con reglas específicas, que los navegadores entienden para mostrar correctamente los contenidos de la web.

## Estructura básica de un documento HTML

```html title="estructura-basica.html"
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Título de la página</title>
</head>
<body>
    <!-- Aquí va todo el contenido visible -->
</body>
</html>
```

### Desglose de cada elemento

| Elemento | Función |
|----------|-----------------------------|
| `<!DOCTYPE html>` | Declara que es un documento HTML5 |
| `<html lang="es">` | Etiqueta raíz. `lang="es"` indica idioma español |
| `<head>` | Contiene metadatos (info que no se ve) |
| `<meta charset="UTF-8">` | Codificación de caracteres (tildes, ñ, etc.) |
| `<meta name="viewport"...>` | Hace la página responsive: Muestra la página adaptada al ancho del dispositivo y sin ampliarla ni reducirla |
| `<title>` | Título que aparece en la pestaña del navegador |
| `<body>` | Contiene todo el contenido visible |

!!! tip "Atajo en VS Code"
    Escribe `!` y presiona `Tab` para generar automáticamente esta estructura.

## Encabezados (o Títulos) y jerarquía

HTML tiene 6 niveles de encabezados.

* **Etiqueta**:  `<h>...</h>`

=== "Código"
    ```html 
    <h1>Título principal - Solo uno por página</h1>
    <h2>Subtítulo importante</h2>
    <h3>Subtítulo de nivel 3</h3>
    <h4>Subtítulo de nivel 4</h4>
    <h5>Subtítulo de nivel 5</h5>
    <h6>Subtítulo de nivel 6</h6>
    ```
=== "Renderizado *(click para expandir)*"
    <div style="background-color: #f8f8f8ff; padding: 20px;">
    <p style="font-size: 2em">Título principal - Solo uno por página</p>
    <p style="font-size: 1.8em">Subtítulo importante</p>
    <p style="font-size: 1.6em">Subtítulo de nivel 3</p>
    <p style="font-size: 1.4em">Subtítulo de nivel 4</p>
    <p style="font-size: 1.2em">Subtítulo de nivel 5</p>
    <p style="font-size: 1em">Subtítulo de nivel 6</p>
    </div>

!!! warning "Reglas importantes"
    - Solo debe haber **un `<h1>` por página**
    - No saltes niveles: después de `<h2>` va `<h3>`, no `<h5>`
    - Los encabezados estructuran el contenido para SEO

## Párrafos y saltos de línea

### Párrafos

Un párrafo es una unidad de texto que contiene una idea completa o un conjunto de ideas relacionadas. Es la forma básica de organizar la escritura en casi cualquier texto, ya sea un artículo, un ensayo, un libro o una página web.

* **Etiqueta**:  `<p>...</p>`

=== "Código"
    ```html
    <p>Este es un párrafo completo de texto.</p>
    <p>Este es otro párrafo.</p>
    ```
=== "Renderizado *(click para expandir)*"
    <div style="background-color: #f8f8f8ff; padding: 20px;">
    <p>Este es un párrafo completo de texto.</p>
    <p>Este es otro párrafo.</p>
    </div>

### Saltos de línea

* **Etiqueta**:  `<br>`

=== "Código"
    ```html
    <p>Primera línea<br>
    Segunda línea<br>
    Tercera línea</p>
    ```
=== "Renderizado *(click para expandir)*"
    <div style="background-color: #f8f8f8ff; padding: 20px;">
    <p> Primera línea<br>
    Segunda línea<br>
    Tercera línea
    </p>
    </div>


### Línea horizontal

* **Etiqueta**:  `<hr>`

=== "Código"
    ```html
    <p>Contenido de una sección</p>
    <hr>
    <p>Contenido de otra sección</p>
    ```
=== "Renderizado *(click para expandir)*"
    <div style="background-color: #f8f8f8ff; padding: 20px;">
    <p>Contenido de una sección</p>
    <hr>
    <p>Contenido de otra sección</p>
    </div>

## Formato de texto

En caso de querer dar formato a una parte de un párrafo, utilizaremos las siguientes marcas:

=== "Código"
    ```html
    <!-- Énfasis (cursiva) -->
    <p>Esto es <em>importante</em> de recordar.</p>

    <!-- Importancia fuerte (negrita) -->
    <p>Esto es <strong>muy importante</strong>.</p>

    <!-- Texto pequeño -->
    <small>Copyright © 2025</small>

    <!-- Texto marcado/resaltado -->
    <p>Busca la palabra <mark>resaltada</mark>.</p>

    <!-- Texto eliminado -->
    <p>El precio era <del>50€</del> ahora 35€</p>

    <!-- Subíndice y superíndice -->
    <p>H<sub>2</sub>O es agua</p>
    <p>E = mc<sup>2</sup></p>
    ```
=== "Renderizado *(click para expandir)*"
    <!-- Énfasis (cursiva) -->
    <p>Esto es <em>importante</em> de recordar.</p>

    <!-- Importancia fuerte (negrita) -->
    <p>Esto es <strong>muy importante</strong>.</p>

    <!-- Texto pequeño -->
    <small>Copyright © 2025</small>

    <!-- Texto marcado/resaltado -->
    <p>Busca la palabra <mark>resaltada</mark>.</p>

    <!-- Texto eliminado -->
    <p>El precio era <del>50€</del> ahora 35€</p>

    <!-- Subíndice y superíndice -->
    <p>H<sub>2</sub>O es agua</p>
    <p>E = mc<sup>2</sup></p>


## Enlaces (links)

### Enlaces externos

En el caso de enlazar a una web externa utilaremos:

* **Etiqueta**: `<a href="URL" target="..."> Texto o contenido del enlace </a>`

| Atributo | Descripción                                                                      
| -------- | ------------------------------------------------------------------------------ |   
| target   | Indica dónde se abrirá el enlace:_self(por defecto),_blank(nueva pestaña), etc.| 
| title    | Texto que aparece como tooltip al pasar el cursor sobre el enlace.             |

**Ejemplos**: 

=== "Código HTML"
    ```html
    <a href="https://www.google.com">Ir a Google</a>
    <a href="https://www.wikipedia.org" target="_blank">Abrir en nueva pestaña</a>
    ```
=== "Renderizado *(clic para expandir)*"
    <a href="https://www.google.com">Ir a Google</a>  
    <a href="https://www.wikipedia.org" target="_blank">Abrir en nueva pestaña</a>
    



### Enlaces internos

Los enlaces internos se utilizan para navegar entre las diferentes páginas de un mismo sitio web. En vez de poner una URL completa, se pone el nombre del archivo HTML al que quieres llevar al usuario.

Por ejemplo, si tienes los archivos index.html, about.html y contacto.html en la raíz de tu proyecto, los enlaces internos serían así:

=== "Código HTML"
    ```html
    <a href="index.html">Inicio</a>
    <a href="about.html">Sobre nosotros</a>
    <a href="contacto.html">Contacto</a>
    ```
=== "Renderizado *(clic para expandir)*"
    <a href="about.html">Sobre nosotros</a>  
    <a href="contacto.html">Contacto</a>

### Enlaces a secciones (anclas)

Los enlaces a secciones (o anclas) permiten que el usuario salte directamente a una parte específica de la misma página, como, por ejemplo, bajando directamente al formulario de contacto.

Formato:

* Se coloca un atributo id en el elemento que será el destino (por ejemplo, un título o cualquier etiqueta).

*  El enlace usa el símbolo # seguido del nombre del id.

=== "Código HTML"
    ```html
    <!-- El destino -->
    <h3 id="seccion-contacto">Contacto</h3>

    <!-- El enlace -->
    <a href="#seccion-contacto">Ir a la sección Contacto</a>
    ```
=== "Renderizado *(clic para expandir)*"
    <!-- El destino -->
    <h3 id="seccion-contacto">Contacto</h3>

    <a href="#seccion-contacto">Ir a la sección Contacto</a>

### Enlaces de correo


Un enlace de correo permite que el usuario abra directamente su cliente de correo para escribir un mensaje a una dirección específica.
Se usa la etiqueta <a> con el atributo href que empieza con mailto: seguido de la dirección de email.

Ejemplo:

=== "Código HTML"
    ```html
    <a href="mailto:contacto@ejemplo.com">Enviar email</a>
    ```
=== "Renderizado *(clic para expandir)*"
    <a href="mailto:contacto@ejemplo.com">Enviar email</a>


!!! warning "Seguridad con target='_blank'"
    Cuando uses `target="_blank"`, añade siempre `rel="noopener noreferrer"`:
    ```
    <a href="https://ejemplo.com" target="_blank" rel="noopener noreferrer">Enlace seguro</a>
    ```

## Imágenes

La etiqueta `<img>` se utiliza en HTML para insertar imágenes en una página web.

**Formato general:**
```html
<img src="ruta/a/la/imagen.jpg" alt="Descripción de la imagen">
```

- **`src`**: Indica la ruta de la imagen (puede ser local o una URL).
- **`alt`**: Texto alternativo que describe la imagen. Es fundamental para accesibilidad y aparece si la imagen no se carga.

**Ejemplo:**
=== "Código"
    ```html
    <img src="ruta/al/logo.png" alt="Logo de la empresa">
    ```
=== "Renderizado"
    <img src="ruta/al/logo.png" alt="Logo de la empresa">


**Importancia del atributo `alt`:**

- Ayuda a las personas con discapacidad visual usando lectores de pantalla.
- Mejora el SEO.
- Informa al usuario si la imagen falla al cargar.

**Puedes ajustar el tamaño añadiendo atributos como `width` y `height`:**
```html
<img src="ruta/a/la//foto.jpg" alt="Persona sonriente" width="200" height="150">
```

**Formatos recomendados**:

| Formato | Uso |
|---------|-----|
| **JPG/JPEG** | Fotografías |
| **PNG** | Logos, iconos, transparencias |
| **SVG** | Iconos escalables |
| **WebP** | Formato moderno, mejor compresión |

## Listas

### Lista desordenada

**Etiqueta:** `<ul>...</ul>`

=== "Código"
    ```html linenums="1"
    <ul>
        <li>Primer elemento</li>
        <li>Segundo elemento</li>
        <li>Tercer elemento</li>
    </ul>
    ```
=== "Renderizado *(clic aquí)*"
    <ul>
        <li>Primer elemento</li>
        <li>Segundo elemento</li>
        <li>Tercer elemento</li>
    </ul>

### Lista ordenada

**Etiqueta:** `<ol>...</ol>`

=== "Código HTML"
    ```html linenums="1"
    <ol>
        <li>Primer paso</li>
        <li>Segundo paso</li>
        <li>Tercer paso</li>
    </ol>
    ```
=== "Renderizado *(clic aquí)*"
    <ol>
        <li>Primer elemento</li>
        <li>Segundo elemento</li>
        <li>Tercer elemento</li>
    </ol>

### Listas anidadas

=== "Código HTML"
    ```html linenums="1"
    <ul>
        <li>Frutas
            <ul>
                <li>Manzana</li>
                <li>Naranja</li>
            </ul>
        </li>
        <li>Verduras
            <ul>
                <li>Lechuga</li>
                <li>Tomate</li>
            </ul>
        </li>
    </ul>
    ```
=== "Renderizado *(clic aquí)*"
    <ul>
        <li>Frutas
            <ol>
                <li>Manzana</li>
                <li>Naranja</li>
            </ol>
        </li>
        <li>Verduras
            <ul>
                <li>Lechuga</li>
                <li>Tomate</li>
            </ul>
        </li>
    </ul>



***




## Entidades HTML

| Carácter | Entidad | Descripción |
|----------|---------|-------------|
| < | `&lt;` | Menor que |
| > | `&gt;` | Mayor que |
| & | `&amp;` | Ampersand |
| " | `&quot;` | Comillas dobles |
| © | `&copy;` | Copyright |
| € | `&euro;` | Euro |

### Ejemplo

```html
<p>Para escribir HTML usa &lt;etiquetas&gt;</p>
<p>Copyright &copy; 2025</p>
```
<!-- 
## 📝 Resumen

En este Capítulo has aprendido:
- ✅ Estructura básica de HTML5
- ✅ Encabezados y jerarquía
- ✅ Formato de texto
- ✅ Enlaces e imágenes
- ✅ Listas
- ✅ Etiquetas semánticas
- ✅ Entidades HTML

## 🎯 Ejercicios

Ver [Ejercicios HTML Básico](../ejercicios/html-basico.md)

## ➡️ Siguiente Capítulo

[Capítulo 3: HTML Avanzado](03-html-avanzado.md)

*** -->
