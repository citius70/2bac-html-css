# Módulo 5.4: CSS Grid

!!!note "CSS Grid"
    **CSS Grid** es un sistema de diseño en CSS que permite organizar y distribuir los elementos de una página en **dos dimensiones**: filas y columnas.  
    Es la herramienta **más potente para crear layouts web complejos y adaptativos**.

## ¿Por qué usar CSS Grid?

- Permite crear **layouts bidimensionales** (filas y columnas) fácilmente.
- Facilita la organización y alineación de elementos en la página.
- Es ideal para galerías, dashboards, zonas de contenido y diseños modernos.
- Hace que el **código sea más limpio y sencillo** que técnicas antiguas.

![flexgrid](../img/flex_grid.png) 

> La versatilidad de CSS Grid supera los límites de flexbox, por lo que es recomendable consultar recursos extra para profundizar:  
  * [CSS Grid Layout en MDN](https://developer.mozilla.org/es/docs/Web/CSS/CSS_Grid_Layout){:target="_blank"}  
  * [CSS Grid Generator](https://cssgrid-generator.netlify.app/){:target="_blank"}

![Grid cheatsheet](../img/gridcheatsheet.png)

## Elemento de Grid  
  ![grid2](../img/grid2.png){width=30%" align="right"}

- **CONTENEDOR (grid container):**  
  Es el elemento al que se le aplica `display: grid;`, controlando la disposición de filas y columnas, y el área donde estarán los ítems.  
- **ÍTEMs (grid item):**
  Elementos hijos directos del contenedor grid. Se ubican en celdas, áreas de la cuadrícula, y pueden ocupar varias filas o columnas.

> Piensa el **contenedor** como una *tabla grande* y los **ítems** como las *celdas individuales* que puedes mover, agrupar o expandir según tu diseño.

![grid3](../img/grid3.png "Web estructurada con Grid")  

<p style="text-align: center;"><em>Web estructurada con Grid</em></p>



## Propiedades principales del contenedor

* `display: grid;`: Activa Grid en el contenedor.  
  * `grid-template-columns`: Define el número y tamaño de columnas.  
  * `grid-template-rows`: Define las filas.  
  * `gap`: Espacio entre filas/columnas.  
  * `grid-template-areas`: Define zonas/áreas con nombres para un layout semántico.  

## Propiedades de los ítems

- `grid-column`: En qué columna empieza y termina el ítem.
- `grid-row`: En qué fila empieza y termina el ítem.
- `grid-area`: Asigna un área semántica definida en el contenedor.

## Unidad especial:

* fr = fracción del espacio disponible

  *Ejemplo: 1fr 2fr = La segunda columna es el doble de ancha

## Ejemplos básico

=== "| HTML 1"
    ```html linenums="1" hl_lines="2 3 4 5 6 7"
    ...
    <div class="contenedor">
        <div class="item">A</div>
        <div class="item">B</div>
        <div class="item">C</div>
        <div class="item">D</div>
    </div>
    ...
    ```
=== "CSS 1"
    ```css linenums="1" hl_lines="2 3 4 5 9"
    ...
    .contenedor {
        display: grid;
        grid-template-columns: 1fr 2fr 1fr;
        grid-template-rows: 100px 100px;
        gap: 16px;
        background: #f9e;
    }
    .item {
        background: #379;
        color: #fff;
        font-size: 1.3em;
        text-align: center;
        border-radius: 6px;
        padding: 25px 0;
    }
    ...
    ```
=== "Resultado 1 |"
    <style>
    .contenedor1 {
        display: grid;
        max-width: 200px;
        grid-template-columns: 1fr 1fr 1fr;
        grid-template-rows: 100px 100px;
        gap: 16px;
        background: #f9e;
        border: 0px solid navy;
    }
    .item1 {
        background: #379;
        color: #fff;
        font-size: 1.3em;
        text-align: center;
        border-radius: 0px;
        padding: 25px 0;
    }
    </style>
    <div class="contenedor1">
        <div class="item1">A</div>
        <div class="item1">B</div>
        <div class="item1">C</div>
        <div class="item1">D</div>
        <div class="item1">E</div>
        <div class="item1">F</div>
    </div>
    <p>Las cajas se organizan en una cuadrícula de tres columnas y dos filas, con espacio entre ellas.</p>

=== "| HTML 2"
    ```html linenums="1" hl_lines="2 3 4 5 6 7 8 9 10 11 12 13 14 15"
    ...
    <div class="contenedor">
        <div class="item">A</div>
        <div class="item">B</div>
        <div class="item">C</div>
        <div class="item">D</div>
        <div class="item">E</div>
        <div class="item">F</div>
        <div class="item">G</div>
        <div class="item">H</div>
        <div class="item">I</div>
        <div class="item">J</div>
        <div class="item">K</div>
        <div class="item">L</div>
    </div>
    ...
    ```
=== "CSS 2"
    ```css linenums="1" hl_lines="2 3 4 5 9"
    ...
    .contenedor {
        display: grid;
        grid-template-columns: 1fr 3fr 3fr 1fr;
        grid-template-rows: 1fr 3fr 1fr;
        gap: 16px;
        background: #f9e;
    }
    .item {
        background: #379;
        color: #fff;
        font-size: 1.3em;
        text-align: center;
        border-radius: 6px;
        padding: 25px 0;
    }
    ...
    ```
=== "Resultado 2 |"
    <style>
    .contenedor2 {
        display: grid;
        max-width: 100%;
        grid-template-columns: 1fr 3fr 6fr 1fr;
        grid-template-rows: 1fr 3fr 1fr;
        gap: 16px;
        background: #f9e;
        border: 0px solid navy;
    }
    .item2 {
        background: #379;
        color: #fff;
        font-size: 1.3em;
        text-align: center;
        border-radius: 0px;
        padding: 25px 0;
    }
    </style>
    <div class="contenedor2">
        <div class="item2">A</div>
        <div class="item2">B</div>
        <div class="item2">C</div>
        <div class="item2">D</div>
        <div class="item2">E</div>
        <div class="item2">F</div>
        <div class="item2">G</div>
        <div class="item2">H</div>
        <div class="item2">I</div>
        <div class="item2">J</div>
        <div class="item2">K</div>
        <div class="item2">L</div>
    </div>
    <p>Las cajas se organizan en una cuadrícula de cuatro columnas y tres filas de dimensiones desiguales, con espacio entre ellas.</p>




***

## ¿Para qué sirve CSS Grid?

- Layouts de página completa y dashboard
- Galerías de imágenes
- Estructuras de áreas y zonas adaptativas
- Posicionar y alinear elementos en dos dimensiones

**Consejo:**  
Flexbox es ideal para layouts de una sola dimensión. Si necesitas filas *y* columnas, utiliza CSS Grid. ¡Son herramientas complementarias!