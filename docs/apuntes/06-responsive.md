# Módulo 06: Responsive design (Media queries)

El **diseño responsivo** es fundamental porque hoy la mayoría de personas **navega desde el teléfono o la tablet, no solo desde la computadora**. Si una página no se adapta, el usuario va a tener dificultades para leer, hacer clic o navegar y probablemente abandone el sitio. Además, Google prioriza en sus búsquedas las páginas que ofrecen una buena experiencia en todos los dispositivos, así que adaptar tu web ayuda a que más gente la encuentre. En resumen, el diseño responsivo asegura que todos los usuarios puedan acceder fácilmente a la página y mejora la visibilidad del sitio en internet.

## ¿Cómo se consigue?

El método principal para conseguirlo es gracias a las **media queries** que son reglas de CSS que permiten cambiar el diseño o los estilos de una web dependiendo de:
- El ancho y alto de la pantalla del dispositivo (viewport)
- La orientación (vertical/horizontal)
- La resolución
- Si se trata de pantalla, impresión u otras salidas

## ¿Cómo funcionan?

Se usan con la palabra clave `@media`, combinada con condiciones.
Las más comunes utilizan el **ancho mínimo** (`min-width`) o **ancho máximo** (`max-width`):

=== "CSS"
    ```css
    /* Estilos base: para móvil */
    body {
    font-size: 1em;
    background: #eef;
    }
    @media (min-width: 600px) {
    body {
        background: #aaf;
        font-size: 1.2em;
    }
    }
    @media (min-width: 1024px) {
    body {
        background: #afa;
        font-size: 1.3em;
        margin: 0 auto;
        max-width: 1200px;
    }
    }
    ```
Las reglas dentro del bloque solo se aplican si la condición se cumple.
=== "HTML"
    ```html
    <body>
        Cambia el tamaño de la vemtana para ver cómo cambia el diseño.
    </body>
    ```

=== "Resultado"
    <div>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Media Queries Básicas</title>
            <style>
                body {
                    font-size: 1em; 
                    background: #eef;
                    font-family: Arial, sans-serif;
                    margin: 20px;
                }
                
                @media (min-width: 600px) {
                    body {
                        background: #aaf;
                        font-size: 1.2em;
                    }
                }
                
                @media (min-width: 1024px) {
                    body {
                        background: #afa;
                        font-size: 1.3em;
                        margin: 0 auto;
                        max-width: 1200px;
                    }
                }
            </style>
        </head>
        <body>
            Cambia el tamaño de la ventana para ver cómo cambia el diseño.
        </body>
        </html>
    </div>

## Ejemplo básico

```css linenums="1" hl_lines="2 3 4 5 6 7"
/* Estilos base: para móvil */
body {
  font-size: 1em;
  background: #eef;
}
@media (min-width: 600px) {
  body {
    background: #aaf;
    font-size: 1.2em;
  }
}
@media (min-width: 1024px) {
  body {
    background: #afa;
    font-size: 1.3em;
    margin: 0 auto;
    max-width: 1200px;
  }
}
```
Prueba cambiando el tamaño de la ventana: ¡el fondo y el tamaño cambian automáticamente!


## Ejemplo avanzado con Grid

```css
.cuadricula {
  display: grid;
  grid-template-columns: 1fr;
}
@media (min-width: 700px) {
  .cuadricula {
    grid-template-columns: 1fr 1fr;
  }
}
@media (min-width: 1000px) {
  .cuadricula {
    grid-template-columns: 1fr 1fr 1fr;
  }
}
```
Esto permite que tus listas de productos, fotos, etc., se organicen automáticamente según el ancho de pantalla.


## Propiedades y valores útiles en media queries

- `width`, `min-width`, `max-width`: Ancho del viewport
- `height`, `min-height`, `max-height`: Alto del viewport
- `orientation: portrait | landscape`: Orientación de la pantalla
- `resolution`: Densidad de píxeles (útil para pantallas retina)

**Ejemplo:**
```css
@media (max-width: 500px) and (orientation: portrait) {
  /* Estilos exclusivos para móviles en vertical */
}
```


## Concepto "Mobile first"

Significa escribir primero los estilos para la pantalla más pequeña y luego, con media queries, añadir mejoras para pantallas más grandes.  
Esto asegura que la web funciona siempre en móvil y crece gradualmente.



## Breakpoints frecuentes y recomendados

- **Móvil pequeño (portrait):** 0–600px
- **Móvil grande/tablet vertical:** 601px–900px
- **Tablet horizontal/portátiles pequeños:** 901px–1200px
- **Escritorio:** 1201px en adelante

Adáptalos según el público objetivo y diseño.


## Consejos para un buen diseño responsive

- Usa porcentajes o unidades relativas (`em`, `rem`, `vw`, `vh`, `%`) en vez de `px`.
- Define imágenes fluidas:  
  ```css
  img {
    max-width: 100%;
    height: auto;
  }
  ```
- Prueba tu web en dispositivos reales, no solo en el navegador.
- Muestra/oculta elementos si son innecesarios en móvil.
- Simplifica el layout para pantallas pequeñas.


## Herramientas útiles

- DevTools del navegador (modo responsivo)
- [Can I use...](https://caniuse.com/) para comprobar compatibilidad
- [Responsinator](https://www.responsinator.com/)
- [Screenfly](https://screenfly.org/)


**Resumen:**  
Media queries y el diseño responsive son imprescindibles para que tu web funcione y luzca perfecta en cualquier dispositivo, desde un smartphone hasta una pantalla 4K. Esto mejora la experiencia del usuario y la visibilidad online.