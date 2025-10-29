# Cheatsheet CSS - Referencia Rápida

Esta es una referencia rápida de las propiedades y conceptos CSS más importantes. Úsala como consulta mientras trabajas en tus proyectos.

---

## 🔗 Cómo vincular CSS

```css
<!-- CSS externo (recomendado) -->
<link rel="stylesheet" href="styles.css">

<!-- CSS interno -->
<style>
  body { background: white; }
</style>

<!-- CSS inline (evitar) -->
<p style="color: red;">Texto</p>
```

---

## 🔍 Selectores básicos

```css
/* Selector de elemento */
p { color: blue; }
h1 { font-size: 32px; }

/* Selector de clase */
.boton { padding: 10px; }
.texto-grande { font-size: 20px; }

/* Selector de ID */
#principal { width: 100%; }

/* Selector universal */
* { margin: 0; padding: 0; }

/* Combinadores */
div p { }              /* Descendiente (cualquier nivel) */
div > p { }            /* Hijo directo */
h1 + p { }             /* Hermano siguiente */
h1 ~ p { }             /* Todos los hermanos siguientes */

/* Selectores de atributo */
[type="text"] { }      /* Con atributo específico */
[class] { }            /* Que tengan el atributo */

/* Pseudo-clases */
a:hover { }            /* Al pasar el ratón */
a:visited { }          /* Enlace visitado */
input:focus { }        /* Input enfocado */
li:first-child { }     /* Primer hijo */
li:last-child { }      /* Último hijo */
li:nth-child(2) { }    /* Segundo hijo */
li:nth-child(odd) { }  /* Impares */
li:nth-child(even) { } /* Pares */

/* Pseudo-elementos */
p::first-line { }      /* Primera línea */
p::first-letter { }    /* Primera letra */
p::before { content: "→ "; }  /* Antes del contenido */
p::after { content: " ←"; }   /* Después del contenido */
```

---

## 🎨 Colores y fondos

```css
/* Colores */
color: #333;                    /* Hexadecimal */
color: rgb(255, 0, 0);          /* RGB */
color: rgba(255, 0, 0, 0.5);    /* RGB + transparencia */
color: hsl(120, 100%, 50%);     /* HSL */
color: hsla(120, 100%, 50%, 0.5); /* HSL + transparencia */

/* Fondos */
background-color: #f5f5f5;
background-image: url("fondo.jpg");
background-size: cover;          /* cover, contain, auto */
background-position: center;     /* top, bottom, left, right, center */
background-repeat: no-repeat;    /* repeat, repeat-x, repeat-y, no-repeat */
background-attachment: fixed;    /* scroll, fixed */

/* Atajo */
background: #fff url("bg.jpg") no-repeat center/cover;

/* Gradientes */
background: linear-gradient(90deg, #2563eb, #60a5fa);
background: linear-gradient(to right, red, blue);
background: radial-gradient(circle, #fff, #000);

/* Opacidad */
opacity: 0.5;  /* 0 (transparente) a 1 (opaco) */
```

---

## 🔠 Tipografía

```css
/* Familia de fuente */
font-family: "Segoe UI", Arial, sans-serif;
font-family: 'Georgia', serif;
font-family: 'Courier New', monospace;

/* Tamaño */
font-size: 16px;
font-size: 1.5rem;   /* Relativo a raíz */
font-size: 1.5em;    /* Relativo al padre */

/* Peso (grosor) */
font-weight: normal;     /* 400 */
font-weight: bold;       /* 700 */
font-weight: 600;        /* 100-900 */

/* Estilo */
font-style: normal;
font-style: italic;
font-style: oblique;

/* Alineación */
text-align: left;
text-align: center;
text-align: right;
text-align: justify;

/* Transformación */
text-transform: uppercase;    /* MAYÚSCULAS */
text-transform: lowercase;    /* minúsculas */
text-transform: capitalize;   /* Primera Letra */

/* Decoración */
text-decoration: none;
text-decoration: underline;
text-decoration: line-through;

/* Espaciado */
line-height: 1.6;        /* Altura de línea */
letter-spacing: 2px;     /* Entre letras */
word-spacing: 5px;       /* Entre palabras */

/* Sombra */
text-shadow: 2px 2px 4px rgba(0,0,0,0.3);

/* Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
font-family: 'Roboto', sans-serif;
```

---

## 📦 Modelo de caja (Box Model)

```css
/* Dimensiones */
width: 300px;
height: 200px;
max-width: 100%;
min-height: 300px;

/* Márgenes (exterior) */
margin: 10px;                    /* Todos los lados */
margin: 10px 20px;               /* vertical horizontal */
margin: 10px 20px 30px 40px;    /* top right bottom left */
margin-top: 10px;
margin-right: 20px;
margin-bottom: 30px;
margin-left: 40px;
margin: 0 auto;                  /* Centrar horizontalmente */

/* Relleno (interior) */
padding: 10px;
padding: 10px 20px;
padding: 10px 20px 30px 40px;
padding-top: 10px;

/* Bordes */
border: 2px solid #333;
border-width: 2px;
border-style: solid;    /* dashed, dotted, double, none */
border-color: #333;
border-radius: 10px;    /* Esquinas redondeadas */
border-top-left-radius: 5px;

/* Sombras */
box-shadow: 5px 5px 10px rgba(0,0,0,0.2);
box-shadow: 0 2px 4px rgba(0,0,0,0.1);
box-shadow: inset 0 0 10px rgba(0,0,0,0.5);  /* Interior */

/* Box-sizing */
box-sizing: content-box;  /* Por defecto */
box-sizing: border-box;   /* Incluye padding y border */

/* Recomendado para todos los elementos */
* {
  box-sizing: border-box;
}
```

---

## 📐 Display y Position

```css
/* Display */
display: block;         /* Ocupa todo el ancho */
display: inline;        /* En línea con el texto */
display: inline-block;  /* En línea pero con dimensiones */
display: none;          /* Oculto (no ocupa espacio) */
display: flex;          /* Flexbox */
display: grid;          /* Grid */

/* Visibility */
visibility: hidden;     /* Oculto (sí ocupa espacio) */
visibility: visible;

/* Position */
position: static;       /* Por defecto */
position: relative;     /* Relativo a su posición */
position: absolute;     /* Relativo al ancestro posicionado */
position: fixed;        /* Relativo a la ventana */
position: sticky;       /* Mezcla de relative y fixed */

/* Propiedades de posicionamiento */
top: 10px;
right: 20px;
bottom: 30px;
left: 40px;
z-index: 10;            /* Orden de apilamiento */
```

---

## 🔲 Flexbox

### Contenedor flex

```css
.contenedor {
  display: flex;
  
  /* Dirección */
  flex-direction: row;           /* row, column, row-reverse, column-reverse */
  
  /* Ajuste de línea */
  flex-wrap: wrap;               /* nowrap, wrap, wrap-reverse */
  
  /* Alineación horizontal (eje principal) */
  justify-content: center;       /* flex-start, flex-end, center, 
                                    space-between, space-around, space-evenly */
  
  /* Alineación vertical (eje cruzado) */
  align-items: center;           /* flex-start, flex-end, center, stretch, baseline */
  
  /* Alineación de líneas (con wrap) */
  align-content: space-between;  /* flex-start, flex-end, center, 
                                    space-between, space-around, stretch */
  
  /* Espaciado */
  gap: 20px;
  row-gap: 10px;
  column-gap: 20px;
}
```

### Elementos flex

```css
.elemento {
  /* Tamaño flexible */
  flex: 1;                /* Atajo: flex-grow flex-shrink flex-basis */
  flex-grow: 1;           /* Crecimiento proporcional */
  flex-shrink: 1;         /* Encogimiento proporcional */
  flex-basis: 200px;      /* Tamaño base */
  
  /* Orden */
  order: 2;               /* Cambia el orden visual */
  
  /* Alineación individual */
  align-self: flex-end;   /* Sobrescribe align-items */
}
```

---

## 🎲 CSS Grid

### Contenedor grid

```css
.contenedor {
  display: grid;
  
  /* Definir columnas */
  grid-template-columns: 200px 1fr 2fr;
  grid-template-columns: repeat(3, 1fr);
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  
  /* Definir filas */
  grid-template-rows: 100px auto 100px;
  
  /* Espaciado */
  gap: 20px;
  row-gap: 10px;
  column-gap: 20px;
  
  /* Alineación */
  justify-items: center;     /* Horizontal dentro de celda */
  align-items: center;       /* Vertical dentro de celda */
  justify-content: center;   /* Horizontal del grid */
  align-content: center;     /* Vertical del grid */
}
```

### Elementos grid

```
.elemento {
  /* Posicionamiento */
  grid-column: 1 / 3;        /* Columnas 1 a 3 */
  grid-row: 1 / 2;           /* Filas 1 a 2 */
  
  /* Atajo */
  grid-column: span 2;       /* Ocupa 2 columnas */
  grid-row: span 3;          /* Ocupa 3 filas */
  
  /* Áreas nombradas */
  grid-area: header;
}

/* Áreas de grid */
.contenedor {
  grid-template-areas:
    "header header header"
    "sidebar main main"
    "footer footer footer";
}
```

---

## 📱 Diseño Responsive

```css
/* Media Queries */

/* Móvil pequeño */
@media (max-width: 480px) {
  .contenedor {
    flex-direction: column;
  }
}

/* Tablet */
@media (min-width: 768px) and (max-width: 1024px) {
  .columna {
    width: 50%;
  }
}

/* Escritorio */
@media (min-width: 1024px) {
  .contenedor {
    max-width: 1200px;
  }
}

/* Orientación */
@media (orientation: landscape) {
  /* Estilos para horizontal */
}

@media (orientation: portrait) {
  /* Estilos para vertical */
}

/* Unidades relativas */
width: 50%;
font-size: 1.5rem;      /* Relativo a raíz (16px por defecto) */
font-size: 1.5em;       /* Relativo al padre */
width: 50vw;            /* 50% del viewport width */
height: 100vh;          /* 100% del viewport height */
```

---

## ✨ Transiciones y animaciones

### Transiciones

```css
.elemento {
  transition: all 0.3s ease;
  transition: property duration timing-function delay;
  
  /* Propiedades específicas */
  transition-property: background-color, transform;
  transition-duration: 0.3s;
  transition-timing-function: ease;  /* ease, linear, ease-in, ease-out, ease-in-out */
  transition-delay: 0.1s;
}

.elemento:hover {
  background-color: blue;
  transform: scale(1.1);
}
```

### Animaciones

```css
/* Definir animación */
@keyframes deslizar {
  0% {
    transform: translateX(0);
    opacity: 0;
  }
  100% {
    transform: translateX(100px);
    opacity: 1;
  }
}

/* Aplicar animación */
.elemento {
  animation: deslizar 2s ease infinite;
  animation-name: deslizar;
  animation-duration: 2s;
  animation-timing-function: ease;
  animation-delay: 0.5s;
  animation-iteration-count: infinite;  /* O un número */
  animation-direction: alternate;       /* normal, reverse, alternate */
  animation-fill-mode: forwards;        /* none, forwards, backwards, both */
}
```

---

## 🔄 Transformaciones

```css
/* 2D */
transform: translate(50px, 100px);
transform: translateX(50px);
transform: translateY(100px);
transform: rotate(45deg);
transform: scale(1.5);
transform: scaleX(2);
transform: scaleY(0.5);
transform: skew(10deg, 20deg);

/* 3D */
transform: rotateX(45deg);
transform: rotateY(45deg);
transform: rotateZ(45deg);
transform: perspective(500px);

/* Múltiples transformaciones */
transform: translateX(50px) rotate(45deg) scale(1.2);

/* Transform origin */
transform-origin: center;
transform-origin: top left;
transform-origin: 50% 50%;
```

---

## 🎯 Variables CSS

```css
:root {
  --color-primario: #2563eb;
  --color-secundario: #60a5fa;
  --espaciado: 20px;
  --fuente-principal: 'Roboto', sans-serif;
}

.elemento {
  color: var(--color-primario);
  padding: var(--espaciado);
  font-family: var(--fuente-principal);
  
  /* Valor por defecto */
  margin: var(--espaciado-grande, 40px);
}

/* Cambiar variables con media queries */
@media (max-width: 768px) {
  :root {
    --espaciado: 10px;
  }
}
```

---

## 🔧 Propiedades útiles

```css
/* Overflow */
overflow: hidden;       /* visible, hidden, scroll, auto */
overflow-x: auto;
overflow-y: scroll;

/* Cursor */
cursor: pointer;        /* default, pointer, grab, text, wait, help, etc. */

/* Opacidad */
opacity: 0.5;           /* 0 (transparente) a 1 (opaco) */

/* Filtros */
filter: blur(5px);
filter: brightness(150%);
filter: contrast(200%);
filter: grayscale(100%);
filter: sepia(100%);

/* Object-fit (para imágenes) */
object-fit: cover;      /* contain, cover, fill, none, scale-down */
object-position: center;

/* Clipping */
clip-path: circle(50%);
clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%);

/* Pointer events */
pointer-events: none;   /* Ignora eventos del ratón */
```

---

## ✅ Buenas prácticas

!!! tip "Organización del CSS"
    ```
    /* 1. Variables */
    :root { ... }
    
    /* 2. Reset/Normalize */
    * { ... }
    
    /* 3. Estilos globales */
    body { ... }
    
    /* 4. Layout */
    .contenedor { ... }
    
    /* 5. Componentes */
    .boton { ... }
    
    /* 6. Utilities */
    .oculto { ... }
    
    /* 7. Media queries */
    @media { ... }
    ```

!!! tip "Nomenclatura"
    - Usa nombres descriptivos: `.boton-primario` mejor que `.btn1`
    - Metodología BEM: `.bloque__elemento--modificador`
    - Evita IDs para estilos, usa clases

!!! tip "Rendimiento"
    - Minimiza selectores complejos
    - Evita `!important`
    - Usa shorthand properties
    - Optimiza animaciones (usa `transform` y `opacity`)

!!! tip "Mobile-first"
    ```
    /* Estilos base (móvil) */
    .elemento {
      width: 100%;
    }
    
    /* Tablet y superior */
    @media (min-width: 768px) {
      .elemento {
        width: 50%;
      }
    }
    ```

---

## 🔗 Recursos adicionales

- [MDN Web Docs - CSS](https://developer.mozilla.org/es/docs/Web/CSS)
- [CSS Tricks](https://css-tricks.com/)
- [Can I Use](https://caniuse.com/) - Compatibilidad
- [Flexbox Froggy](https://flexboxfroggy.com/) - Juego Flexbox
- [Grid Garden](https://cssgridgarden.com/) - Juego Grid
- [CSS Validator](https://jigsaw.w3.org/css-validator/)

---

⬅️ [Volver al inicio](../index.md)


***