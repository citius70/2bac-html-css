# Módulo 2: HTML Básico

## 🎯 Objetivos del módulo

Al finalizar este módulo serás capaz de:

- Crear la estructura básica de una página HTML válida  
- Utilizar etiquetas semánticas correctamente  
- Trabajar con encabezados, párrafos y formato de texto  
- Insertar enlaces e imágenes  
- Crear listas ordenadas y desordenadas  
- Estructurar contenido con elementos semánticos  

## 2.1. Estructura básica de un documento HTML

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
|----------|---------|
| `<!DOCTYPE html>` | Declara que es un documento HTML5 |
| `<html lang="es">` | Etiqueta raíz. `lang="es"` indica idioma español |
| `<head>` | Contiene metadatos (info que no se ve) |
| `<meta charset="UTF-8">` | Codificación de caracteres (tildes, ñ, etc.) |
| `<meta name="viewport"...>` | Hace la página responsive |
| `<title>` | Título que aparece en la pestaña |
| `<body>` | Contiene todo el contenido visible |

!!! tip "Atajo en VS Code"
    Escribe `!` y presiona `Tab` para generar automáticamente esta estructura.

## 2.2. Encabezados y jerarquía

HTML tiene 6 niveles de encabezados:

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
    <h1>Título principal - Solo uno por página</h1>
    <h2>Subtítulo importante</h2>
    <h3>Subtítulo de nivel 3</h3>
    <h4>Subtítulo de nivel 4</h4>
    <h5>Subtítulo de nivel 5</h5>
    <h6>Subtítulo de nivel 6</h6>
    </div>

!!! warning "Reglas importantes"
    - Solo debe haber **un `<h1>` por página**
    - No saltes niveles: después de `<h2>` va `<h3>`, no `<h5>`
    - Los encabezados estructuran el contenido para SEO

## 2.3. Párrafos y saltos de línea

### Párrafos

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

## 2.4. Formato de texto

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
    <div style="background-color: #f8f8f8ff; padding: 20px;">
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
    </div>

## 2.5. Enlaces (links)

### Enlaces externos

=== "Código HTML"
    ```html
    <a href="https://www.google.com">Ir a Google</a>
    <a href="https://www.wikipedia.org" target="_blank">Abrir en nueva pestaña</a>
    ```
=== "Renderizado *(clic para expandir)*"
    <div style="background-color: #f8f8f8ff; padding: 20px;">
    <a href="https://www.google.com">Ir a Google</a>  
    <a href="https://www.wikipedia.org" target="_blank">Abrir en nueva pestaña</a>
    </div>



### Enlaces internos

=== "Código HTML"
    ```html
    <a href="index.html">Inicio</a>
    <a href="about.html">Sobre nosotros</a>
    <a href="contacto.html">Contacto</a>
    ```
=== "Renderizado *(clic para expandir)*"
    <div style="background-color: #f8f8f8ff; padding: 20px;">
    <a href="about.html">Sobre nosotros</a>  
    <a href="contacto.html">Contacto</a>
    </div>

### Enlaces a secciones (anclas)

=== "Código HTML"
    ```html
    <!-- El destino -->
    <h3 id="seccion-contacto">Contacto</h3>

    <!-- El enlace -->
    <a href="#seccion-contacto">Ir a la sección Contacto</a>
    ```
=== "Renderizado *(clic para expandir)*"
    <div style="background-color: #f8f8f8ff; padding: 20px;">
    <!-- El destino -->
    <h3 id="seccion-contacto">Contacto</h3>

    <a href="#seccion-contacto">Ir a la sección Contacto</a>
    </div>

### Enlaces de correo
=== "Código HTML"
    ```html
    <a href="mailto:contacto@ejemplo.com">Enviar email</a>
    ```
=== "Renderizado *(clic para expandir)*"
    <div style="background-color: #f8f8f8ff; padding: 20px;">
    <a href="mailto:contacto@ejemplo.com">Enviar email</a>
    </div>


!!! warning "Seguridad con target='_blank'"
    Cuando uses `target="_blank"`, añade siempre `rel="noopener noreferrer"`:
    ```
    <a href="https://ejemplo.com" target="_blank" rel="noopener noreferrer">Enlace seguro</a>
    ```

## 2.6. Imágenes

```html
<img src="ruta/a/la/imagen.jpg" alt="Descripción de la imagen">
```

### Ejemplo completo

```html
<img 
    src="img/logo.png" 
    alt="Logo de mi empresa" 
    width="200" 
    height="100"
>
```

### Formatos recomendados
```html
<img 
    src="img/logo.png" 
    alt="Logo de mi empresa" 
    width="200" 
    height="100"
>
```

### Formatos recomendados

| Formato | Uso |
|---------|-----|
| **JPG/JPEG** | Fotografías |
| **PNG** | Logos, iconos, transparencias |
| **SVG** | Iconos escalables |
| **WebP** | Formato moderno, mejor compresión |

## 2.7. Listas

### Lista desordenada

```html
<ul>
    <li>Primer elemento</li>
    <li>Segundo elemento</li>
    <li>Tercer elemento</li>
</ul>
```

### Lista ordenada

```html
<ol>
    <li>Primer paso</li>
    <li>Segundo paso</li>
    <li>Tercer paso</li>
</ol>
```

### Listas anidadas

```html
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

## 2.8. Estructura semántica HTML5

```html
<header>
    <!-- Cabecera: logo, navegación -->
    <h1>Mi Sitio Web</h1>
    <nav>
        <ul>
            <li><a href="index.html">Inicio</a></li>
            <li><a href="about.html">Sobre mí</a></li>
        </ul>
    </nav>
</header>

<main>
    <!-- Contenido principal -->
    <article>
        <h2>Título del artículo</h2>
        <p>Contenido...</p>
    </article>
    
    <section>
        <h2>Sección de comentarios</h2>
        <p>Comentarios...</p>
    </section>
    
    <aside>
        <!-- Contenido relacionado -->
        <h3>Artículos relacionados</h3>
    </aside>
</main>

<footer>
    <!-- Pie de página -->
    <p>&copy; 2025 Mi Sitio Web</p>
</footer>
```

### Etiquetas semánticas

| Etiqueta | Uso |
|----------|-----|
| `<header>` | Cabecera de página o sección |
| `<nav>` | Navegación principal |
| `<main>` | Contenido principal (solo uno) |
| `<article>` | Contenido independiente |
| `<section>` | Sección temática |
| `<aside>` | Contenido relacionado (sidebar) |
| `<footer>` | Pie de página |

## 2.9. Entidades HTML

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

## 📝 Resumen

En este módulo has aprendido:
- ✅ Estructura básica de HTML5
- ✅ Encabezados y jerarquía
- ✅ Formato de texto
- ✅ Enlaces e imágenes
- ✅ Listas
- ✅ Etiquetas semánticas
- ✅ Entidades HTML

## 🎯 Ejercicios

Ver [Ejercicios HTML Básico](../ejercicios/html-basico.md)

## ➡️ Siguiente módulo

[Módulo 3: HTML Avanzado](03-html-avanzado.md)

***