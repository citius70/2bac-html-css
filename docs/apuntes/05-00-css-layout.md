# Módulo 5: CSS Layout

Ya conoces los fundamentos de CSS: selectores, colores, tipografía y el modelo de caja. Ahora es momento de aprender a **estructurar y posicionar elementos** en la página para crear layouts profesionales.

Probablemente, una de las partes más complejas de CSS sea la creación de layouts, colocación y distribución de los elementos a lo largo de una página, y sin duda el que más le cuesta a los desarrolladores que están comenzando. Sin embargo, es una parte fundamental dentro de CSS, y es necesario entenderla correctamente para que resulte más fácil de trabajar y crear nuestros diseños.

## ¿Qué es CSS Layout?

CSS **Layout** es el conjunto de técnicas y propiedades que controlan **cómo se organizan y posicionan los elementos en una página web**. Define la estructura visual y la distribución del contenido.

## ¿Por qué es importante?

- ✅ Permite crear diseños profesionales y organizados
- ✅ Facilita la creación de páginas responsive (adaptables a diferentes dispositivos)
- ✅ Mejora la experiencia del usuario con layouts intuitivos
- ✅ Es fundamental para el diseño web moderno


## Técnicas principales

1. **Display**
Controla el comportamiento del elemento en el flujo del documento (block, inline, inline-block, none).

2. **Position**
Determina el tipo de posicionamiento del elemento (static, relative, absolute, fixed, sticky).

3. **Flexbox**
Sistema de layout unidimensional (fila O columna) para organizar elementos de forma flexible.

4. **Grid**
Sistema de layout bidimensional (filas Y columnas) para crear estructuras complejas.

5. **Media Queries**
Permite adaptar el diseño según el tamaño de la pantalla (responsive design).








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

<!-- ## 📝 Resumen

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

[Módulo 05.01: Display](05-01-css-layout.display.md) - Layout con Display


*** -->