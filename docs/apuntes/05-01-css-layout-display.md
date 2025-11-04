# Módulo 5.1: Display

!!!note "Dispay"
    La propiedad `display` controla cómo se comporta un elemento **en el flujo del documento**, es decir, *cómo se muestra, ocupa espacio y se relaciona con otros elementos*. 
    Es fundamental para entender cómo se colocan los elementos en la página.

**Sintaxis básica**:

```css
elemento {
  display: valor;
}
```
El **elemento** puede ser cualquier entidad de HTML: párrafo, título, imagen.... Pero, ¿qué **valores** puede tomar?

## Valores principales

```css
/* Bloque: ocupa todo el ancho disponible */
display: block;

/* En línea: solo ocupa el espacio de su contenido */
display: inline;

/* En línea pero con dimensiones */
display: inline-block;

/* Oculto (no ocupa espacio) */
display: none;

/* Flexbox (lo veremos más adelante) */
display: flex;

/* Grid (lo veremos más adelante) */
display: grid;
```

<div>
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Ejemplo propiedad display</title>
  <style>
    .caja {
      width: 120px;
      height: 60px;
      background-color: lightblue;
      border: 2px solid navy;
      margin: 5px;
      text-align: center;
      line-height: 60px;
    }
  </style>
</head>
<body>

  <h2>display: block (por defecto en div)</h2>
  <div class="caja" style="display: block;">Caja 1</div>
  <div class="caja" style="display: block;">Caja 2</div>
  <div class="caja" style="display: block;">Caja 3</div>
  <!-- ✅ Cada caja ocupa toda la línea -->

  <h2>display: inline</h2>
  <div class="caja" style="display: inline;">Caja 1</div>
  <div class="caja" style="display: inline;">Caja 2</div>
  <div class="caja" style="display: inline;">Caja 3</div>
  <!-- ✅ Todas las cajas se colocan en la misma línea -->

  <h2>display: inline-block</h2>
  <div class="caja" style="display: inline-block;">Caja 1</div>
  <div class="caja" style="display: inline-block;">Caja 2</div>
  <div class="caja" style="display: inline-block;">Caja 3</div>
  <!-- ✅ En la misma línea, pero mantienen su tamaño -->

  <h2>display: none</h2>
  <div class="caja" style="display: none;">Caja oculta</div>
  <div class="caja" style="display: inline-block;">Caja visible</div>
  <!-- ✅ La primera no se muestra ni ocupa espacio -->

</body>
</html>
</div>



| Valor          | Qué hace                                                                             | Ejemplo típico          |
| -------------- | ------------------------------------------------------------------------------------ | ----------------------- |
| `block`        | El elemento ocupa **todo el ancho disponible** y empieza en una **línea nueva**.     | `<div>`, `<p>`, `<h1>`  |
| `inline`       | El elemento **no rompe la línea** y solo ocupa **el espacio necesario**.             | `<span>`, `<a>`         |
| `inline-block` | Se comporta como `inline`, pero permite **definir ancho, alto, márgenes y padding**. | `<img>`                 |
| `none`         | **Oculta completamente** el elemento (no ocupa espacio).                             | —                       |
| `flex`         | Activa el **modelo Flexbox** para el diseño flexible de los elementos hijos.         | Contenedores adaptables |
Se comporta como un elemento de lista (añade viñeta por defecto).                    | `<li>`                  |
| `grid`         | Activa el **modelo Grid**, permitiendo dividir el espacio en filas y columnas.       | Diseños complejos       |
| `table`        | Hace que el elemento se comporte como una tabla HTML.                                | Estructuras tabulares   |
| `list-item`    | 



## Block vs Inline vs Inline-block

## Elementos con **display: block**

Un elemento con `display: block` ocupa todo el ancho disponible, comienza en una línea nueva y respeta todas sus dimensiones y espacios. NO fluye con el texto.

**Características clave de `display: block`:**

- ✅ **Respeta `width` y `height`**: Puedes definir el tamaño exacto del elemento y se aplicará correctamente.  
- ✅ **Respeta `margin` y `padding` en todas direcciones**: Los espacios interior (padding) y exterior (margin) funcionan arriba, abajo, izquierda y derecha.  
- ✅ **Ocupa todo el ancho disponible**: Aunque el elemento tenga `width: 200px`, reserva toda la línea horizontal. Ningún otro elemento puede colocarse a su lado.  
- 🔄 **Siempre empieza en línea nueva**: No importa dónde lo pongas en el código, siempre se mostrará en su propia línea.  
- 🔄 **Obliga al siguiente elemento a nueva línea**: El elemento que venga después tampoco podrá estar en la misma línea, será empujado hacia abajo.


**Elementos HTML con `display: block` por defecto:**

*   **Principales:** `<div>`, `<p>`, `<h1>` a `<h6>`, `<section>`, `<article>`, `<header>`, `<footer>`, `<nav>`, `<main>`, `<aside>`

* **Listas:** `<ul>`, `<ol>`, `<li>`

* **Otros:** `<form>`, `<table>`, `<blockquote>`, `<pre>`, `<hr>`, `<figure>`

> **Regla simple:** La mayoría de elementos **estructurales y de contenido** son block por defecto.

**Sintaxis general**:

```css
elemento (p, h1, h2...) {
    display: block;  /* Por defecto */
}
```

**Ejemplo**:

=== "Código CCS"
    ```css linenums="1" hl_lines="4"
    ...
    <style>
        .caja {
            display: block;
            width: 180px;
            height: 60px;
            background-color: lightblue;
            border: 2px solid navy;
            margin: 5px;
            text-align: center;
            line-height: 60px;
        }
    </style>
    ...
    ```
=== "Código HTML"
    ```html linenums="1" hl_lines="2 4 6"
    ... 
     <div class="caja">Caja 1</div>
    <p>Soy un párrafo que  molesta a la Caja 1</p>
    <div class="caja">Caja 2</div>
    <p>Soy otro párrafo empujado por la Caja 2</p>
    <div class="caja">Caja 3</div>
    ...
    ```
=== "Renderizado *(clic para expandir)*"
    <div style= "background-color: #f5f5f5">
    <html lang="es">
    <head>
    <meta charset="UTF-8">
    <title>Ejemplo display block</title>
    <style>
        .caja_block {
            display: block;
            width: 180px;
            height: 60px;
            background-color: lightblue;
            border: 2px solid navy;
            margin: 5px;
            text-align: center;
            line-height: 60px;
        }
    </style>
    </head>
    <body> 
    <div class="caja_block">Caja 1</div>
    <p>Soy un párrafo que  molesta a la Caja 1</p>
    <div class="caja_block">Caja 2</div>
    <p>Soy otro párrafo empujado por la Caja 2</p>
    <div class="caja_block">Caja 3</div>
    <!-- ✅ Cada caja ocupa toda la línea -->
    </body>
    </html>
    </div>


## Elementos con **display: inline**

Un elemento con `display: inline`que fluye con el texto, ocupa solo el espacio de su contenido y no respeta `width` ni `height`. SÍ fluye con el texto.

**Características clave de `display: inline`:**

- ❌ NO respeta `width` y `height`: Puedes definirlos pero serán ignorados completamente
- ⚠️ Solo respeta `margin-left` y `margin-right`: El margen vertical (top/bottom) no funciona
- ✅ Respeta `padding` en todas direcciones: Aunque no mueve otros elementos verticalmente
- ✅ Fluye con el texto naturalmente: Los elementos se alinean horizontalmente como palabras
- ✅ No rompe la línea: Otros elementos pueden estar a su lado


**Elementos HTML con `display: inline` por defecto:**

* **De formato de texto:** `<span>`, `<a>`, `<strong>`, `<em>`, `<b>`, `<i>`, `<u>`, `<small>`, `<sub>`, `<sup>`

* **Interactivos:** `<button>`, `<input>`, `<label>`, `<select>`, `<textarea>`

* **Multimedia:** `<img>`, `<video>`, `<audio>`

* **Otros:** `<code>`, `<mark>`, `<abbr>`, `<cite>`

> **Regla simple:** Elementos que están **dentro de texto** o son **pequeños** suelen ser inline por defecto.


**Sintaxis:**
```css
elemento (span, a, strong, ...) {
    display: inline;  /* Por defecto */
}
```

**Ejemplo completo:**

=== "Código CSS"
    ```css linenums="1" hl_lines="4"
    ...
    <style>
        .caja {
            display: inline;
            background-color: lightgreen;
            border: 2px solid darkgreen;
            padding: 5px 10px;
            /* ⚠️ width y height NO funcionan con inline */
            width: 200px;
            height: 100px;
        }
    </style>
    ...
    ```
=== "Código HTML"
    ```html
    ...
    <p>
        Este es un párrafo con elementos inline 
        <span class="caja">Caja 1</span>
        <span class="caja">Caja 2</span>
        y como ves no rompen línea
        <span class="caja">Caja 3</span>
        permitiendo elementos a su lado.
    </p>
    ...
    ```
=== "Resultado visual"
    <div style= "background-color: #f5f5f5">
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Ejemplo display inline</title>
        <style>
            .caja_inline {
                display: inline;
                background-color: lightgreen;
                border: 2px solid darkgreen;
                padding: 5px 10px;
                /* ⚠️ width y height NO funcionan con inline */
                width: 500px;
                height: 200px;
            }
        </style>
    </head>
    <body>
        <p>Este es un párrafo entre elementos inline
        <span class="caja_inline">Caja 1</span>
        <span class="caja_inline">Caja 2</span>
        y como ves no rompen línea
        <span class="caja_inline">Caja 3</span>
        permitiendo elementos a su lado.</p>
        <!-- ✅ Los elementos fluyen con el texto -->
    </body>
    </html>
    </div>


## Elementos con **display: inline-block** (lo mejor de ambos)

Un elemento con `display: in-line` fluye en línea con otros pero respeta `width`, `height` y todos los `márgenes` (lo mejor de block e inline combinados)

**Características clave de `display: inline-block`:**

- ✅ Respeta `width` y `height`: Puedes definir tamaños exactos
- ✅ Respeta `margin` y `padding` en todas direcciones
- ✅ Fluye en línea: No rompe la línea, coexiste con otros elementos
- 🔄 Sin saltos de línea forzados: A diferencia de block
- ✅ Útil para menús, botones, tarjetas en fila

```
.elemento {
    display: inline-block;
}
```

**Elementos HTML con `display: inline-block` por defecto:** `<button>`, `<input>`, `<select>`, `<textarea>`, `<img>`, `<video>`, `<audio>`

> **Regla simple:** Elementos interactivos y multimedia tienen `inline-block` por defecto (o similar).

**Ejemplo práctico:**

## display: inline-block

**Sintaxis:**
```css
.elemento {
    display: inline-block;
}
```

**Ejemplo completo:**

=== "Código"
    ```html linenums="1" hl_lines="6 7 8 9 10 11 12 13 14 15 16 17 21 22 23 24 25 26"
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Ejemplo display inline-block</title>
        <style>
            .caja {
                display: inline-block;
                width:120px;
                height: 60px;
                background-color: lightyellow;
                border: 2px solid orange;
                margin: 30px;
                margin-top: 5px:
                text-align: center;
                line-height: 80px;
            }
        </style>
    </head>
    <body>
        <p>
            Esto es un párrafo que contiene elementos con que fluyen en línea pero respetan dimensiones:
            <span class="caja">Caja 1</span>
            <span class="caja">Caja 2</span>
            <span class="caja">Caja 3</span>
        </p>
        <!-- ✅ Fluyen en línea PERO respetan width y height -->
    </body>
    </html>
    ```

=== "Resultado visual"
    <div style= "background-color: #f5f5f5">
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Ejemplo display inline-block</title>
        <style>
            .caja {
                display: inline-block;
                width:120px;
                height: 60px;
                background-color: lightyellow;
                border: 2px solid orange;
                margin: 30px;
                margin-top: 5px:
                text-align: center;
                line-height: 80px;
            }
        </style>
    </head>
    <body>
        <p>
            Esto es un párrafo que contiene elementos con display: inline-block
            <span class="caja">Caja 1</span>
            que fluyen con el texto
            <span class="caja">Caja 2</span>
            pero respetan dimensiones.
            <span class="caja">Caja 3</span>
        </p>
        <!-- ✅ Fluyen en línea PERO respetan width y height -->
    </body>
    </html>
    </div>    

---

## ➡️ Siguiente módulo

[Módulo 6: CSS Avanzado](06-css-avanzado.md) - Transiciones, animaciones y efectos
```

***