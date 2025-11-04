# Ejercicios CSS Básico

## 🎯 Instrucciones generales

- Lee bien cada enunciado antes de empezar
- Valida tu CSS y HTML con las herramientas correspondientes
- Guarda todos los archivos en una carpeta `ejercicios-css`
- Usa nombres descriptivos para tus archivos
- Comenta tu código CSS cuando sea necesario

---

## 🟢 Ejercicios Nivel Básico

### Ejercicio 1: Mi primer CSS

**Archivo:** `ejercicio-01.html` y `ejercicio-01.css`

**Objetivo:** Crear una página con CSS externo básico.

**Requisitos:**  
- Página HTML con estructura completa  
- Archivo CSS externo vinculado  
- Aplicar color a encabezados y párrafos  
- Cambiar el tamaño de letra  
- Usar al menos 3 colores diferentes  

??? success "✅ Solución"
    **HTML (ejercicio-01.html):**
    ```html
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mi Primer CSS</title>
        <link rel="stylesheet" href="ejercicio-01.css">
    </head>
    <body>
        <h1>Bienvenido a mi página</h1>
        <p>Este es mi primer ejercicio con CSS externo.</p>
        <h2>Una sección importante</h2>
        <p>Aquí aplicamos colores y tipografía con CSS.</p>
    </body>
    </html>
    ```
    
    **CSS (ejercicio-01.css):**
    ```css
    h1 {
        color: #2563eb;
        font-size: 36px;
    }
    
    h2 {
        color: #dc2626;
        font-size: 24px;
    }
    
    p {
        color: #374151;
        font-size: 16px;
    }
    ```

---

### Ejercicio 2: Selectores CSS

**Archivo:** `ejercicio-02.html` y `ejercicio-02.css`

**Objetivo:** Practicar selectores de elemento, clase e ID.

**Requisitos:**
- Usar selector de elemento (etiquetas)  
- Usar selector de clase (mínimo 2 clases)  
- Usar selector de ID  
- Aplicar estilos diferentes según corresponda  

??? success "✅ Solución"
    **HTML:**
    ```
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Selectores CSS</title>
        <link rel="stylesheet" href="ejercicio-02.css">
    </head>
    <body>
        <h1 id="titulo-principal">Selectores CSS</h1>
        <p>Este es un párrafo normal.</p>
        <p class="destacado">Este párrafo está destacado.</p>
        <p class="importante">Este párrafo es importante.</p>
        <p class="destacado importante">Este tiene dos clases.</p>
    </body>
    </html>
    ```
    
    **CSS:**
    ```
    /* Selector de elemento */
    p {
        line-height: 1.6;
        margin-bottom: 10px;
    }
    
    /* Selector de ID */
    #titulo-principal {
        color: #1e40af;
        font-size: 32px;
        border-bottom: 3px solid #1e40af;
        padding-bottom: 10px;
    }
    
    /* Selector de clase */
    .destacado {
        background-color: #fef3c7;
        padding: 10px;
    }
    
    .importante {
        color: #dc2626;
        font-weight: bold;
    }
    ```

---

### Ejercicio 3: Colores y tipografía

**Archivo:** `ejercicio-03.html` y `ejercicio-03.css`

**Objetivo:** Trabajar con diferentes formatos de color y fuentes.

**Requisitos:**
- Usar colores en hexadecimal, RGB y nombres  
- Aplicar diferentes estilos de texto (bold, italic, uppercase)
- Usar Google Fonts  
- Cambiar peso de fuente  

??? success "✅ Solución"
    **HTML:**
    ```
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Colores y Tipografía</title>
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="ejercicio-03.css">
    </head>
    <body>
        <h1>Colores y Tipografía</h1>
        <p class="intro">Introducción al uso de colores y fuentes en CSS.</p>
        <h2>Sección importante</h2>
        <p class="normal">Texto normal con fuente por defecto.</p>
        <p class="enfasis">Texto con énfasis y cambios de color.</p>
        <p class="mayusculas">Texto transformado a mayúsculas</p>
    </body>
    </html>
    ```
    
    **CSS:**
    ```
    * {
        font-family: 'Roboto', sans-serif;
    }
    
    h1 {
        font-family: 'Playfair Display', serif;
        color: #1f2937;
        font-size: 42px;
        text-align: center;
    }
    
    h2 {
        color: rgb(37, 99, 235);
        font-size: 28px;
        font-weight: 700;
    }
    
    .intro {
        color: #6b7280;
        font-size: 18px;
        font-style: italic;
    }
    
    .normal {
        color: black;
        font-size: 16px;
        line-height: 1.6;
    }
    
    .enfasis {
        color: rgba(220, 38, 38, 0.8);
        font-weight: bold;
        font-size: 16px;
    }
    
    .mayusculas {
        text-transform: uppercase;
        color: #1e3a8a;
        letter-spacing: 2px;
    }
    ```

---

### Ejercicio 4: Espaciado con margen y padding

**Archivo:** `ejercicio-04.html` y `ejercicio-04.css`

**Objetivo:** Entender margin, padding y sus diferencias.

**Requisitos:**
- Crear cajas con padding visible  
- Usar margen para separar elementos  
- Aplicar bordes para visualizar mejor  
- Mostrar la diferencia entre margin y padding  

??? success "✅ Solución"
    **HTML:**
    ```
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Margen y Padding</title>
        <link rel="stylesheet" href="ejercicio-04.css">
    </head>
    <body>
        <div class="contenedor">
            <div class="caja caja-1">
                <p>Caja con padding</p>
            </div>
            <div class="caja caja-2">
                <p>Caja con margen</p>
            </div>
            <div class="caja caja-3">
                <p>Caja con ambos</p>
            </div>
        </div>
    </body>
    </html>
    ```
    
    **CSS:**
    ```
    * {
        box-sizing: border-box;
    }
    
    .contenedor {
        background: #f3f4f6;
        padding: 20px;
    }
    
    .caja {
        background: white;
        border: 2px solid #dbeafe;
    }
    
    .caja-1 {
        padding: 30px;
        margin-bottom: 10px;
    }
    
    .caja-2 {
        margin: 30px 0;
    }
    
    .caja-3 {
        padding: 20px;
        margin: 20px 0;
        border: 2px solid #3b82f6;
    }
    
    .caja p {
        margin: 0;
        font-weight: bold;
    }
    ```

---

### Ejercicio 5: Bordes y esquinas redondeadas

**Archivo:** `ejercicio-05.html` y `ejercicio-05.css`

**Objetivo:** Trabajar con bordes y border-radius.

**Requisitos:**
- Crear bordes de diferentes estilos (solid, dashed, dotted)
- Aplicar diferentes anchos de borde
- Usar border-radius en diferentes valores
- Combinar estilos

??? success "✅ Solución"
    **HTML:**
    ```
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Bordes</title>
        <link rel="stylesheet" href="ejercicio-05.css">
    </head>
    <body>
        <h1>Estilos de bordes</h1>
        <div class="caja borde-solido">Borde sólido</div>
        <div class="caja borde-punteado">Borde punteado</div>
        <div class="caja borde-discontinuo">Borde discontinuo</div>
        <div class="caja borde-redondeado">Borde redondeado</div>
        <div class="caja borde-radio-circulo">Radio circular</div>
    </body>
    </html>
    ```
    
    **CSS:**
    ```
    body {
        padding: 20px;
        background: #f9fafb;
    }
    
    .caja {
        padding: 20px;
        margin: 15px 0;
        background: white;
        font-weight: bold;
        text-align: center;
    }
    
    .borde-solido {
        border: 3px solid #3b82f6;
    }
    
    .borde-punteado {
        border: 3px dotted #ef4444;
    }
    
    .borde-discontinuo {
        border: 3px dashed #10b981;
    }
    
    .borde-redondeado {
        border: 2px solid #8b5cf6;
        border-radius: 10px;
    }
    
    .borde-radio-circulo {
        border: 2px solid #f59e0b;
        border-radius: 50%;
        width: 150px;
        height: 150px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto;
    }
    ```

---

## 🟡 Ejercicios Nivel Intermedio

### Ejercicio 6: Tarjetas de producto

**Archivo:** `ejercicio-06.html` y `ejercicio-06.css`

**Objetivo:** Combinar selectores, colores, tipografía y espaciado.

**Requisitos:**
- Crear 3 tarjetas de producto  
- Usar clases para estilizar  
- Aplicar padding, margin y bordes  
- Añadir efectos hover (cambio de color)  

??? success "✅ Solución"
    **HTML:**
    ```
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Tarjetas de Producto</title>
        <link rel="stylesheet" href="ejercicio-06.css">
    </head>
    <body>
        <div class="contenedor">
            <div class="tarjeta">
                <div class="tarjeta-header">Producto 1</div>
                <div class="tarjeta-body">
                    <p>Descripción del producto 1</p>
                    <p class="precio">$29.99</p>
                </div>
            </div>
            
            <div class="tarjeta">
                <div class="tarjeta-header">Producto 2</div>
                <div class="tarjeta-body">
                    <p>Descripción del producto 2</p>
                    <p class="precio">$39.99</p>
                </div>
            </div>
            
            <div class="tarjeta">
                <div class="tarjeta-header">Producto 3</div>
                <div class="tarjeta-body">
                    <p>Descripción del producto 3</p>
                    <p class="precio">$49.99</p>
                </div>
            </div>
        </div>
    </body>
    </html>
    ```
    
    **CSS:**
    ```
    * {
        box-sizing: border-box;
    }
    
    body {
        background: #f3f4f6;
        padding: 40px 20px;
    }
    
    .contenedor {
        display: flex;
        gap: 20px;
        max-width: 1200px;
        margin: 0 auto;
        flex-wrap: wrap;
    }
    
    .tarjeta {
        background: white;
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        flex: 1;
        min-width: 280px;
        transition: transform 0.3s ease;
    }
    
    .tarjeta:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 6px rgba(0,0,0,0.15);
    }
    
    .tarjeta-header {
        background: #3b82f6;
        color: white;
        padding: 20px;
        font-weight: bold;
        font-size: 20px;
    }
    
    .tarjeta-body {
        padding: 20px;
    }
    
    .tarjeta-body p {
        margin: 10px 0;
        color: #6b7280;
    }
    
    .precio {
        font-size: 24px;
        font-weight: bold;
        color: #dc2626;
        margin-top: 15px;
    }
    ```

---

## 🔴 Ejercicios Nivel Avanzado

### Ejercicio 7: Página de galería con CSS

**Archivo:** `ejercicio-07.html` y `ejercicio-07.css`

**Objetivo:** Crear una galería con múltiples estilos y efectos.

**Requisitos:**
- Galería de al menos 6 imágenes  
- Usar diferentes selectores  
- Aplicar efectos hover  
- Titulo y descripciones estilizadas  

??? success "✅ Solución"
    **HTML:**
    ```
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Galería CSS</title>
        <link rel="stylesheet" href="ejercicio-07.css">
    </head>
    <body>
        <h1>Mi Galería Fotográfica</h1>
        
        <div class="galeria">
            <div class="imagen-item">
                <img src="https://via.placeholder.com/300x200?text=Foto+1" alt="Foto 1">
                <p>Descripción 1</p>
            </div>
            <div class="imagen-item">
                <img src="https://via.placeholder.com/300x200?text=Foto+2" alt="Foto 2">
                <p>Descripción 2</p>
            </div>
            <div class="imagen-item">
                <img src="https://via.placeholder.com/300x200?text=Foto+3" alt="Foto 3">
                <p>Descripción 3</p>
            </div>
            <div class="imagen-item">
                <img src="https://via.placeholder.com/300x200?text=Foto+4" alt="Foto 4">
                <p>Descripción 4</p>
            </div>
            <div class="imagen-item">
                <img src="https://via.placeholder.com/300x200?text=Foto+5" alt="Foto 5">
                <p>Descripción 5</p>
            </div>
            <div class="imagen-item">
                <img src="https://via.placeholder.com/300x200?text=Foto+6" alt="Foto 6">
                <p>Descripción 6</p>
            </div>
        </div>
    </body>
    </html>
    ```
    
    **CSS:**
    ```
    * {
        box-sizing: border-box;
    }
    
    body {
        background: #1f2937;
        color: white;
        padding: 40px 20px;
        font-family: Arial, sans-serif;
    }
    
    h1 {
        text-align: center;
        font-size: 36px;
        margin-bottom: 40px;
    }
    
    .galeria {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .imagen-item {
        flex: 0 1 calc(33.333% - 14px);
        background: #374151;
        border-radius: 10px;
        overflow: hidden;
    }
    
    .imagen-item img {
        width: 100%;
        height: 200px;
        object-fit: cover;
        display: block;
    }
    
    .imagen-item p {
        padding: 15px;
        margin: 0;
        text-align: center;
    }
    
    .imagen-item:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 20px rgba(0,0,0,0.3);
    }
    ```

---

## ✅ Criterios de evaluación

Tu código será evaluado según:

- ✅ **Sintaxis CSS correcta:** Sin errores
- ✅ **Selectores apropiados:** Uso correcto de elemento, clase e ID
- ✅ **Propiedades CSS:** Aplicadas correctamente
- ✅ **Organización:** Código limpio, comentado
- ✅ **Resultado visual:** Se ve como se esperaba

---

## 💡 Consejos

!!! tip "Desarrollo"
    - Abre las DevTools (F12) para ver cambios en tiempo real
    - Usa la pestaña "Elements" para inspeccionar estilos
    - Prueba cambios antes de guardar

!!! tip "CSS"
    - Usa nombres de clases descriptivos
    - Agrupa estilos relacionados
    - Comenta secciones importantes
    - Valida siempre con CSS Validator

---

## 📚 Recursos adicionales

- [MDN - CSS](https://developer.mozilla.org/es/docs/Web/CSS)
- [CSS Tricks](https://css-tricks.com/)
- [Google Fonts](https://fonts.google.com/)
- [CSS Validator](https://jigsaw.w3.org/css-validator/)

---

<!-- ## ⬅️ Volver

Volver a [Apuntes CSS Fundamentos](../apuntes/04-css-fundamentos.md)
 -->