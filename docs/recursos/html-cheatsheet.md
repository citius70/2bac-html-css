# Cheatsheet HTML - Referencia Rápida

Esta es una referencia rápida de las etiquetas y conceptos HTML más importantes. Úsala como consulta mientras trabajas en tus proyectos.

---

## 🧰 Estructura mínima (boilerplate)

```html
<!doctype html>
<html lang="es">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>Mi página</title>
    <link rel="stylesheet" href="styles.css">
  </head>
  <body>
    <!-- Contenido -->
    <script src="app.js" defer></script>
  </body>
</html>
```

!!! tip "Atajo VS Code"
    Escribe `!` y presiona `Tab` para generar esta estructura automáticamente.

---

## 📄 Estructura semántica (layout)

```html
<header>...</header>      <!-- Cabecera -->
<nav>...</nav>            <!-- Navegación -->
<main>...</main>          <!-- Contenido principal -->
<article>...</article>    <!-- Artículo independiente -->
<section>...</section>    <!-- Sección temática -->
<aside>...</aside>        <!-- Contenido relacionado -->
<footer>...</footer>      <!-- Pie de página -->
```

**Uso**: Prioriza etiquetas semánticas para SEO y accesibilidad.

---

## 🅷 Encabezados, párrafos y texto

```html
<h1>Principal</h1>
<h2>Subtítulo</h2>
<h3>Sub-subtítulo</h3>

<p>Párrafo con <strong>énfasis fuerte</strong> y <em>énfasis</em>.</p>

<small>Texto secundario</small>
<mark>Texto resaltado</mark>
<del>Texto eliminado</del>
<ins>Texto insertado</ins>

<blockquote>Cita larga</blockquote>
<hr>  <!-- Línea horizontal -->
<br>  <!-- Salto de línea -->
```

---

## 🔗 Enlaces y anclas

```html
<!-- Enlace externo -->
<a href="https://example.com" target="_blank" rel="noopener noreferrer">
  Enlace externo
</a>

<!-- Enlace interno -->
<a href="pagina.html">Ir a otra página</a>

<!-- Ancla (a sección) -->
<a href="#seccion-id">Ir a sección</a>

<!-- Email -->
<a href="mailto:email@example.com">Enviar email</a>

<!-- Teléfono -->
<a href="tel:+34123456789">Llamar</a>
```

**Atributos importantes:**
- `href` - URL de destino
- `target="_blank"` - Abrir en nueva pestaña
- `rel="noopener noreferrer"` - Seguridad con target blank

---

## 🖼️ Imágenes

```html
<img src="ruta/imagen.jpg" alt="Descripción" width="300" height="200">
```

**Atributos obligatorios:**
- `src` - Ruta de la imagen
- `alt` - Texto alternativo (accesibilidad)

**Formatos recomendados:**
- **JPG**: Fotografías
- **PNG**: Logos, iconos, transparencias
- **SVG**: Gráficos vectoriales escalables
- **WebP**: Formato moderno con mejor compresión

---

## 📋 Listas

### Lista desordenada
```html
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
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

### Lista de definición
```html
<dl>
  <dt>Término</dt>
  <dd>Definición del término</dd>
</dl>
```

### Lista anidada
```html
<ul>
  <li>Item principal
    <ul>
      <li>Sub-item 1</li>
      <li>Sub-item 2</li>
    </ul>
  </li>
</ul>
```

---

## 📊 Tablas
```html
<table>
  <thead>
    <tr>
      <th>Encabezado 1</th>
      <th>Encabezado 2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Dato 1</td>
      <td>Dato 2</td>
    </tr>
    <tr>
      <td>Dato 3</td>
      <td>Dato 4</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td>Pie 1</td>
      <td>Pie 2</td>
    </tr>
  </tfoot>
</table>
```

**Atributos útiles:**
- `colspan="2"` - Celda que ocupa 2 columnas
- `rowspan="2"` - Celda que ocupa 2 filas

---

## 📝 Formularios

### Estructura básica
```html
<form action="/enviar" method="POST">
  
  <!-- Campo de texto -->
  <label for="nombre">Nombre:</label>
  <input type="text" id="nombre" name="nombre" required>
  
  <!-- Email -->
  <label for="email">Email:</label>
  <input type="email" id="email" name="email" required>
  
  <!-- Contraseña -->
  <label for="password">Contraseña:</label>
  <input type="password" id="password" name="password">
  
  <!-- Área de texto -->
  <label for="mensaje">Mensaje:</label>
  <textarea id="mensaje" name="mensaje" rows="4"></textarea>
  
  <!-- Checkbox -->
  <input type="checkbox" id="acepto" name="acepto">
  <label for="acepto">Acepto términos</label>
  
  <!-- Radio buttons -->
  <input type="radio" id="opcion1" name="opciones" value="1">
  <label for="opcion1">Opción 1</label>
  
  <input type="radio" id="opcion2" name="opciones" value="2">
  <label for="opcion2">Opción 2</label>
  
  <!-- Select -->
  <label for="pais">País:</label>
  <select id="pais" name="pais">
    <option value="">Selecciona...</option>
    <option value="es">España</option>
    <option value="mx">México</option>
  </select>
  
  <!-- Botón -->
  <button type="submit">Enviar</button>
  
</form>
```

### Tipos de input

| Tipo | Uso |
|------|-----|
| `text` | Texto simple |
| `email` | Email (validación automática) |
| `password` | Contraseña (oculta texto) |
| `number` | Números |
| `tel` | Teléfono |
| `url` | URL |
| `date` | Fecha |
| `time` | Hora |
| `file` | Subir archivo |
| `checkbox` | Casilla de verificación |
| `radio` | Botón de opción |
| `submit` | Botón de envío |

### Atributos importantes

| Atributo | Función |
|----------|---------|
| `required` | Campo obligatorio |
| `placeholder` | Texto de ayuda |
| `value` | Valor por defecto |
| `min` / `max` | Valores mínimo/máximo |
| `pattern` | Patrón de validación (regex) |
| `disabled` | Deshabilitado |
| `readonly` | Solo lectura |

---

## 🎬 Multimedia

### Audio
```html
<audio controls>
  <source src="audio.mp3" type="audio/mpeg">
  <source src="audio.ogg" type="audio/ogg">
  Tu navegador no soporta audio.
</audio>
```

### Video
```html
<video width="640" height="360" controls>
  <source src="video.mp4" type="video/mp4">
  <source src="video.webm" type="video/webm">
  Tu navegador no soporta video.
</video>
```

### Iframe (incrustar contenido)
```html
<iframe 
  src="https://www.youtube.com/embed/VIDEO_ID" 
  width="560" 
  height="315" 
  frameborder="0" 
  allowfullscreen>
</iframe>
```

---

## 🔤 Formato de texto

| Etiqueta | Uso |
|----------|-----|
| `<strong>` | Texto importante (negrita) |
| `<em>` | Énfasis (cursiva) |
| `<mark>` | Texto resaltado |
| `<small>` | Texto pequeño |
| `<del>` | Texto eliminado (tachado) |
| `<ins>` | Texto insertado (subrayado) |
| `<sub>` | Subíndice (H₂O) |
| `<sup>` | Superíndice (x²) |
| `<code>` | Código inline |
| `<pre>` | Texto preformateado |
| `<kbd>` | Teclas del teclado |
| `<samp>` | Salida de programa |

---

## 📦 Contenedores

```html
<div>...</div>        <!-- Contenedor de bloque genérico -->
<span>...</span>      <!-- Contenedor inline genérico -->
```

**Cuándo usar:**
- `<div>`: Para agrupar elementos en bloque
- `<span>`: Para estilizar partes de texto inline
- **Prioriza etiquetas semánticas** cuando sea posible

---

## 🔣 Entidades HTML

| Carácter | Entidad | Descripción |
|----------|---------|-------------|
| < | `&lt;` | Menor que |
| > | `&gt;` | Mayor que |
| & | `&amp;` | Ampersand |
| " | `&quot;` | Comillas dobles |
| ' | `&apos;` | Apóstrofo |
| (espacio) | `&nbsp;` | Espacio no separable |
| © | `&copy;` | Copyright |
| ® | `&reg;` | Marca registrada |
| € | `&euro;` | Euro |
| ← | `&larr;` | Flecha izquierda |
| → | `&rarr;` | Flecha derecha |

---

## 📌 Meta tags útiles

```html
<head>
  <!-- Codificación -->
  <meta charset="UTF-8">
  
  <!-- Responsive -->
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- SEO -->
  <meta name="description" content="Descripción de la página">
  <meta name="keywords" content="html, css, tutorial">
  <meta name="author" content="Tu nombre">
  
  <!-- Open Graph (redes sociales) -->
  <meta property="og:title" content="Título">
  <meta property="og:description" content="Descripción">
  <meta property="og:image" content="imagen.jpg">
  
  <!-- Favicon -->
  <link rel="icon" type="image/png" href="favicon.png">
  
  <!-- CSS -->
  <link rel="stylesheet" href="styles.css">
  
  <!-- JavaScript -->
  <script src="script.js" defer></script>
</head>
```

---

## 💡 Atributos globales

Estos atributos se pueden usar en **cualquier** etiqueta HTML:

| Atributo | Uso |
|----------|-----|
| `id="identificador"` | Identificador único |
| `class="clase1 clase2"` | Clases CSS (múltiples) |
| `style="color: red;"` | Estilos inline (evitar) |
| `title="Tooltip"` | Texto al pasar el ratón |
| `lang="es"` | Idioma del contenido |
| `hidden` | Oculta el elemento |
| `data-*="valor"` | Atributos personalizados |
| `tabindex="1"` | Orden de tabulación |

---

## ✅ Buenas prácticas

!!! tip "HTML semántico"
    Usa etiquetas semánticas (`<header>`, `<article>`, etc.) en lugar de `<div>` cuando sea posible.

!!! tip "Accesibilidad"
    - Siempre incluye el atributo `alt` en imágenes
    - Usa etiquetas `<label>` con formularios
    - Mantén una jerarquía de encabezados lógica
    - Usa suficiente contraste de colores

!!! tip "Validación"
    Valida tu HTML en [validator.w3.org](https://validator.w3.org/)

!!! tip "Organización"
    - Usa indentación consistente (2 o 4 espacios)
    - Cierra todas las etiquetas
    - Comenta secciones importantes
    - Usa nombres de archivos descriptivos en minúsculas

---

## 🔗 Recursos adicionales

- [MDN Web Docs - HTML](https://developer.mozilla.org/es/docs/Web/HTML)
- [W3Schools - HTML Tutorial](https://www.w3schools.com/html/)
- [HTML Validator](https://validator.w3.org/)
- [Can I Use](https://caniuse.com/) - Compatibilidad de navegadores

---

⬅️ [Volver al inicio](../index.md)
```

***