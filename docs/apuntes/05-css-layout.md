# Módulo 5: CSS Layout

Ya conoces los fundamentos de CSS: selectores, colores, tipografía y el modelo de caja. Ahora es momento de aprender a **estructurar y posicionar elementos** en la página para crear layouts profesionales.

## 5.1. Display

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

### Valores principales

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



### Block vs Inline vs Inline-block

### Elementos con **display: block**

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

=== "Código"
    ```html linenums="1" hl_lines="6 7 8 9 10 11 12 13 14 15 20 21 22 23 24 25 26"
    <!DOCTYPE html>
    <html lang="es">
    <head>
    <meta charset="UTF-8">
    <title>Ejemplo display block</title>
    <style>
        .caja {
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

    <p>Esto es un párrafo con varios elementos block insertados... 
    <div class="caja" style="display: block;">Caja 1</div> 
    y como ves los elementos block... 
    <div class="caja" style="display: block;">Caja 2</div>
    rompen las líneas...
    <div class="caja" style="display: block;">Caja 3</div>
    no permitiendo ningún elemento más a su lado.
    <!-- ✅ Cada caja ocupa toda la línea -       

    </body>
    </html>
    ```
=== "Renderizado *(clic para expandir)*"
    <div style= "background-color: #f5f5f5">
    <html lang="es">
    <head>
    <meta charset="UTF-8">
    <title>Ejemplo display block</title>
    <style>
        .caja {
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

    <p>Esto es un párrafo con varios elementos block insertados... 
    <div class="caja" style="display: block;">Caja 1</div> 
    y como ves los elementos block... 
    <div class="caja" style="display: block;">Caja 2</div>
    rompen las líneas...
    <div class="caja" style="display: block;">Caja 3</div>
    no permitiendo ningún elemento más a su lado.

    <!-- ✅ Cada caja ocupa toda la línea -->

    </body>
    </html>
    </div>

---

### Elementos con **display: inline**

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

=== "Código"
    ```html linenums="1" hl_lines="6 7 8 9 10 11 12 13 14 15 18 19 20 21 22 23 24 25 26"
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Ejemplo display inline</title>
        <style>
            .caja {
                background-color: lightgreen;
                border: 2px solid darkgreen;
                padding: 5px 10px;
                /* ⚠️ width y height NO funcionan con inline */
                width: 200px;
                height: 100px;
            }
        </style>
    </head>
    <body>
        <p>
            Este es un párrafo con elementos inline 
            <span class="caja" style="display: inline;">caja 1</span>
            y como ves
            <span class="caja" style="display: inline;">caja 2</span>
            no rompen línea
            <span class="caja" style="display: inline;">caja 3</span>
            permitiendo elementos a su lado.
        </p>
        <!-- ✅ Los elementos fluyen con el texto -->
    </body>
    </html>
    ```

=== "Resultado visual"
    <div style= "background-color: #f5f5f5">
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Ejemplo display inline</title>
        <style>
            .caja {
                background-color: lightgreen;
                border: 2px solid darkgreen;
                padding: 5px 10px;
                /* ⚠️ width y height NO funcionan con inline */
                width: 200px;
                height: 100px;
            }
        </style>
    </head>
    <body>
        <p>
            Este es un párrafo con elementos inline 
            <span class="caja" style="display: inline;">caja 1</span>
            y como ves
            <span class="caja" style="display: inline;">caja 2</span>
            no rompen línea
            <span class="caja" style="display: inline;">caja 3</span>
            permitiendo elementos a su lado.
        </p>
        <!-- ✅ Los elementos fluyen con el texto -->
    </body>
    </html>
    </div>


### Elementos con **display: inline-block** (lo mejor de ambos)

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

### display: inline-block

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



## 5.2. Position

!!!notion "Position"
    La propiedad `position` controla **cómo se posiciona un elemento en la página**.
    Es esencial para crear layouts complejos y efectos avanzados.

### Static (por defecto)

```
position: static;
```

El elemento sigue el flujo normal del documento. Las propiedades `top`, `right`, `bottom`, `left` no tienen efecto.

### Relative

```
.elemento {
    position: relative;
    top: 20px;    /* Se desplaza 20px hacia abajo */
    left: 30px;   /* Se desplaza 30px hacia la derecha */
}
```

El elemento se desplaza **desde su posición original**, pero el espacio original se mantiene reservado. Otros elementos no se mueven.

**Cuándo usarlo:**
- Para ajustes pequeños de posición
- Como referencia para elementos `absolute` dentro de él

### Absolute

```
.elemento {
    position: absolute;
    top: 0;
    right: 0;
}
```

El elemento se posiciona respecto al **ancestro más cercano con `position` distinto de `static`** (normalmente un padre con `position: relative`). Se saca del flujo normal: otros elementos lo ignoran.

**Ejemplo común:**
```
<div style="position: relative;">
    <div style="position: absolute; top: 10px; right: 10px;">
        Insignia
    </div>
</div>
```

**Cuándo usarlo:**
- Tooltips, insignias, overlays
- Elementos decorativos
- Posicionamiento preciso dentro de un contenedor

### Fixed

```
.header {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
}
```

El elemento se posiciona respecto a la **ventana del navegador** y permanece fijo al hacer scroll.

**Cuándo usarlo:**
- Headers o menús de navegación fijos
- Botones flotantes (volver arriba, chat)
- Barras de notificaciones

### Sticky

```
.menu {
    position: sticky;
    top: 0;
}
```

El elemento es `relative` hasta que alcanza cierta posición al hacer scroll, entonces se vuelve `fixed`. Cuando su contenedor sale de la vista, deja de ser fijo.

**Cuándo usarlo:**
- Headers que se fijan al hacer scroll
- Menús de navegación de secciones

---

## 5.3. Flexbox

Flexbox es un sistema de layout **unidimensional** (trabaja con filas O columnas) perfecto para distribuir elementos de forma flexible.

### Contenedor flex

Para activar Flexbox, aplica `display: flex` al contenedor:

```
.contenedor {
    display: flex;
}
```

**Propiedades principales del contenedor:**

```
.contenedor {
    display: flex;
    
    /* Dirección: fila o columna */
    flex-direction: row;           /* row | column | row-reverse | column-reverse */
    
    /* Alineación horizontal (eje principal) */
    justify-content: center;       /* flex-start | flex-end | center | space-between | space-around | space-evenly */
    
    /* Alineación vertical (eje cruzado) */
    align-items: center;           /* flex-start | flex-end | center | stretch | baseline */
    
    /* Permitir salto de línea */
    flex-wrap: wrap;               /* nowrap | wrap | wrap-reverse */
    
    /* Espaciado entre elementos */
    gap: 20px;
}
```

**Valores comunes de justify-content:**
- `flex-start`: al inicio (izquierda si es row)
- `flex-end`: al final (derecha si es row)
- `center`: centrados
- `space-between`: espacio entre elementos, sin espacio en los bordes
- `space-around`: espacio alrededor de cada elemento
- `space-evenly`: espacio igual entre todos

**Valores comunes de align-items:**
- `flex-start`: arriba
- `flex-end`: abajo
- `center`: centrados verticalmente
- `stretch`: estiran para ocupar toda la altura

### Elementos flex

```
.elemento {
    /* Cuánto crece el elemento */
    flex-grow: 1;
    
    /* Cuánto se encoge el elemento */
    flex-shrink: 1;
    
    /* Tamaño base del elemento */
    flex-basis: 200px;
    
    /* Atajo: flex-grow flex-shrink flex-basis */
    flex: 1;
    
    /* Cambiar el orden visual */
    order: 2;
}
```

**Ejemplo práctico: menú horizontal centrado**

```
<nav class="menu">
    <a href="#">Inicio</a>
    <a href="#">Sobre mí</a>
    <a href="#">Proyectos</a>
    <a href="#">Contacto</a>
</nav>
```

```
.menu {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 30px;
    background: #333;
    padding: 20px;
}

.menu a {
    color: white;
    text-decoration: none;
}
```

**Ejemplo: tres columnas iguales**

```
<div class="contenedor">
    <div class="columna">Columna 1</div>
    <div class="columna">Columna 2</div>
    <div class="columna">Columna 3</div>
</div>
```

```
.contenedor {
    display: flex;
    gap: 20px;
}

.columna {
    flex: 1;  /* Todas crecen igual */
    padding: 20px;
    background: #f0f0f0;
}
```

---

## 5.4. CSS Grid

Grid es un sistema **bidimensional** (trabaja con filas Y columnas simultáneamente) ideal para layouts complejos.

### Contenedor grid

```
.contenedor {
    display: grid;
    
    /* Definir columnas */
    grid-template-columns: 200px 1fr 1fr;
    grid-template-columns: repeat(3, 1fr);
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    
    /* Definir filas */
    grid-template-rows: 100px auto 100px;
    
    /* Espaciado */
    gap: 20px;
    row-gap: 10px;
    column-gap: 20px;
}
```

**Unidad `fr` (fracción):**
`1fr` significa "una fracción del espacio disponible". Si tienes `1fr 2fr`, el segundo elemento será el doble de ancho.

### Elementos grid

```
.elemento {
    /* Ocupar desde columna 1 hasta columna 3 */
    grid-column: 1 / 3;
    
    /* Ocupar 2 columnas */
    grid-column: span 2;
    
    /* Ocupar desde fila 1 hasta fila 3 */
    grid-row: 1 / 3;
    
    /* Ocupar 2 filas */
    grid-row: span 2;
}
```

**Ejemplo: layout de página completa**

```
<div class="contenedor">
    <header>Header</header>
    <aside>Sidebar</aside>
    <main>Main Content</main>
    <footer>Footer</footer>
</div>
```

```
.contenedor {
    display: grid;
    grid-template-columns: 250px 1fr;
    grid-template-rows: auto 1fr auto;
    gap: 20px;
    min-height: 100vh;
}

header {
    grid-column: 1 / 3;  /* Ocupa ambas columnas */
    background: #333;
    color: white;
    padding: 20px;
}

aside {
    background: #f0f0f0;
    padding: 20px;
}

main {
    background: white;
    padding: 20px;
}

footer {
    grid-column: 1 / 3;  /* Ocupa ambas columnas */
    background: #333;
    color: white;
    padding: 20px;
}
```

**Ejemplo: galería responsive**

```
.galeria {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
}
```

Esto crea columnas automáticas: cada elemento mide mínimo 250px y crece para llenar el espacio disponible.

---

## 5.5. Unidades responsive

```
/* Porcentajes (relativo al padre) */
width: 50%;

/* Viewport units (relativo a la ventana) */
width: 50vw;        /* 50% del ancho de la ventana */
height: 100vh;      /* 100% del alto de la ventana */
font-size: 5vw;     /* 5% del ancho de la ventana */

/* Relativas a fuente */
font-size: 1rem;    /* Relativo a la raíz (html, por defecto 16px) */
font-size: 1.5em;   /* Relativo al padre */
padding: 2rem;

/* Máximos y mínimos */
max-width: 1200px;
min-height: 500px;
```

**Truco común para contenedores:**
```
.contenedor {
    max-width: 1200px;
    margin: 0 auto;     /* Centrado */
    padding: 0 20px;    /* Espacio en móviles */
}
```

---

## 5.6. Media Queries (Responsive)

Las media queries permiten aplicar estilos según el tamaño de la pantalla, orientación u otras características del dispositivo.

### Sintaxis básica

```
/* Estilos base (móvil primero) */
.contenedor {
    flex-direction: column;
    padding: 10px;
}

/* Tablet (768px y superior) */
@media (min-width: 768px) {
    .contenedor {
        flex-direction: row;
        padding: 20px;
    }
}

/* Desktop (1024px y superior) */
@media (min-width: 1024px) {
    .contenedor {
        max-width: 1200px;
        margin: 0 auto;
    }
}
```

### Breakpoints comunes

```
/* Móvil pequeño */
@media (max-width: 480px) { }

/* Móvil / Tablet */
@media (min-width: 481px) and (max-width: 767px) { }

/* Tablet */
@media (min-width: 768px) and (max-width: 1023px) { }

/* Desktop */
@media (min-width: 1024px) { }

/* Desktop grande */
@media (min-width: 1440px) { }
```

### Otras características útiles

```
/* Orientación */
@media (orientation: landscape) {
    /* Horizontal */
}

@media (orientation: portrait) {
    /* Vertical */
}

/* Preferencia de tema */
@media (prefers-color-scheme: dark) {
    /* Modo oscuro */
}
```

**Ejemplo completo responsive:**

```
/* Móvil (por defecto) */
.galeria {
    display: grid;
    grid-template-columns: 1fr;
    gap: 10px;
}

/* Tablet */
@media (min-width: 768px) {
    .galeria {
        grid-template-columns: repeat(2, 1fr);
        gap: 20px;
    }
}

/* Desktop */
@media (min-width: 1024px) {
    .galeria {
        grid-template-columns: repeat(3, 1fr);
        gap: 30px;
    }
}
```

---

## 📝 Resumen

En este módulo has aprendido:

- La propiedad `display` y sus valores (block, inline, inline-block, none)
- Posicionamiento con `position` (static, relative, absolute, fixed, sticky)
- Flexbox para layouts unidimensionales
- CSS Grid para layouts bidimensionales complejos
- Unidades responsive (%, vw, vh, rem, em)
- Media queries para diseño responsive

---

## 🎯 Ejercicios

Ver [Ejercicios CSS Layout](../ejercicios/css-layout.md)

---

## ➡️ Siguiente módulo

[Módulo 6: CSS Avanzado](06-css-avanzado.md) - Transiciones, animaciones y efectos
```

***

✅ **Módulo 5 reelaborado sin Box Model**, enfocado completamente en layout: display, position, Flexbox, Grid y responsive.

¿Te parece bien así o necesitas ajustes?