# Ejercicios HTML Avanzado

## 🎯 Instrucciones generales

- Intenta resolver los ejercicios por tu cuenta antes de ver las soluciones
- Valida tu código con el [validador W3C](https://validator.w3.org/)
- Guarda todos los archivos en una carpeta `ejercicios-html-avanzado`
- Las soluciones están colapsadas. Haz clic para expandir.

---

## 🟢 Ejercicios Nivel Básico

### Ejercicio 1: Tu primera tabla

**Archivo:** `ejercicio-01.html`

**Objetivo:** Crear una tabla básica con tu horario de clases.

**Requisitos:**  
- Tabla con columnas: Hora, Lunes, Martes, Miércoles, Jueves, Viernes  
- Al menos 4 franjas horarias  
- Usa `<thead>` y `<tbody>`  

??? success "✅ Solución"
    ```html
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Mi Horario</title>
    </head>
    <body>
        <h1>Horario de 2º Bachillerato</h1>
        <table border="1">
            <thead>
                <tr>
                    <th>Hora</th>
                    <th>Lunes</th>
                    <th>Martes</th>
                    <th>Miércoles</th>
                    <th>Jueves</th>
                    <th>Viernes</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>8:00 - 9:00</td>
                    <td>Matemáticas</td>
                    <td>Lengua</td>
                    <td>Inglés</td>
                    <td>Historia</td>
                    <td>TIC</td>
                </tr>
                <tr>
                    <td>9:00 - 10:00</td>
                    <td>Física</td>
                    <td>Matemáticas</td>
                    <td>Lengua</td>
                    <td>TIC</td>
                    <td>Inglés</td>
                </tr>
                <tr>
                    <td>10:00 - 11:00</td>
                    <td>TIC</td>
                    <td>Historia</td>
                    <td>Matemáticas</td>
                    <td>Física</td>
                    <td>Lengua</td>
                </tr>
                <tr>
                    <td>11:00 - 12:00</td>
                    <td>Inglés</td>
                    <td>Física</td>
                    <td>Historia</td>
                    <td>Lengua</td>
                    <td>Matemáticas</td>
                </tr>
            </tbody>
        </table>
    </body>
    </html>
    ```

---

### Ejercicio 2: Formulario de contacto simple

**Archivo:** `ejercicio-02.html`

**Objetivo:** Crear un formulario básico funcional.

**Requisitos:**  
- Campos: Nombre, Email, Mensaje  
- Labels asociados  
- Botón "Enviar"  

??? success "✅ Solución"
    ```html
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Formulario de Contacto</title>
    </head>
    <body>
        <h1>Contacta con nosotros</h1>
        
        <form action="/enviar" method="POST">
            <label for="nombre">Nombre:</label>
            <input type="text" id="nombre" name="nombre" required>
            <br><br>
            
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            <br><br>
            
            <label for="mensaje">Mensaje:</label><br>
            <textarea id="mensaje" name="mensaje" rows="5" cols="40"></textarea>
            <br><br>
            
            <button type="submit">Enviar</button>
        </form>
    </body>
    </html>
    ```

---

### Ejercicio 3: Insertar multimedia

**Archivo:** `ejercicio-03.html`

**Objetivo:** Añadir audio, vídeo e iframe.

??? success "✅ Solución"
    ```html
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Mi Galería Multimedia</title>
    </head>
    <body>
        <h1>Mi Galería Multimedia</h1>
        
        <h2>Vídeo de YouTube</h2>
        <iframe width="560" height="315" 
                src="https://www.youtube.com/embed/dQw4w9WgXcQ" 
                allowfullscreen>
        </iframe>
        
        <h2>Audio</h2>
        <audio controls>
            <source src="audio.mp3" type="audio/mpeg">
            Tu navegador no soporta audio.
        </audio>
        
        <h2>Vídeo local</h2>
        <video width="320" height="240" controls>
            <source src="video.mp4" type="video/mp4">
            Tu navegador no soporta video.
        </video>
    </body>
    </html>
    ```

---

## 🟡 Ejercicios Nivel Intermedio

### Ejercicio 4: Tabla con fusión de celdas

**Archivo:** `ejercicio-04.html`

**Objetivo:** Usar `colspan` y `rowspan`.

**Requisitos:**  
- Tabla de notas con columnas: Asignatura, T1, T2, T3, Media  
- Fila final con "Media General" usando `colspan`  

??? success "✅ Solución"
    ```html
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Tabla de Notas</title>
    </head>
    <body>
        <h1>Mis Notas del Curso</h1>
        
        <table border="1">
            <thead>
                <tr>
                    <th>Asignatura</th>
                    <th>Trimestre 1</th>
                    <th>Trimestre 2</th>
                    <th>Trimestre 3</th>
                    <th>Media</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Matemáticas</td>
                    <td>7.5</td>
                    <td>8.0</td>
                    <td>8.5</td>
                    <td>8.0</td>
                </tr>
                <tr>
                    <td>Lengua</td>
                    <td>6.5</td>
                    <td>7.0</td>
                    <td>7.5</td>
                    <td>7.0</td>
                </tr>
                <tr>
                    <td>Inglés</td>
                    <td>8.0</td>
                    <td>8.5</td>
                    <td>9.0</td>
                    <td>8.5</td>
                </tr>
                <tr>
                    <td>Física</td>
                    <td>7.0</td>
                    <td>7.5</td>
                    <td>8.0</td>
                    <td>7.5</td>
                </tr>
                <tr>
                    <td>TIC</td>
                    <td>9.0</td>
                    <td>9.5</td>
                    <td>10.0</td>
                    <td>9.5</td>
                </tr>
            </tbody>
            <tfoot>
                <tr>
                    <td colspan="4"><strong>Media General</strong></td>
                    <td><strong>8.1</strong></td>
                </tr>
            </tfoot>
        </table>
    </body>
    </html>
    ```

---

### Ejercicio 5: Formulario de registro completo

**Archivo:** `ejercicio-05.html`

**Objetivo:** Formulario con múltiples tipos de campos.

??? success "✅ Solución"
    ```html
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Formulario de Registro</title>
    </head>
    <body>
        <h1>Registro de Usuario</h1>
        
        <form action="/registro" method="POST">
            <fieldset>
                <legend>Datos Personales</legend>
                
                <label for="nombre">Nombre completo:</label>
                <input type="text" id="nombre" name="nombre" required>
                <br><br>
                
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                <br><br>
                
                <label for="password">Contraseña:</label>
                <input type="password" id="password" name="password" required>
                <br><br>
                
                <label for="fecha">Fecha de nacimiento:</label>
                <input type="date" id="fecha" name="fecha">
                <br><br>
            </fieldset>
            
            <fieldset>
                <legend>Información Adicional</legend>
                
                <label>Género:</label><br>
                <input type="radio" id="hombre" name="genero" value="hombre">
                <label for="hombre">Hombre</label><br>
                
                <input type="radio" id="mujer" name="genero" value="mujer">
                <label for="mujer">Mujer</label><br>
                
                <input type="radio" id="otro" name="genero" value="otro">
                <label for="otro">Otro</label>
                <br><br>
                
                <label for="pais">País:</label>
                <select id="pais" name="pais">
                    <option value="">Selecciona...</option>
                    <option value="es">España</option>
                    <option value="mx">México</option>
                    <option value="ar">Argentina</option>
                    <option value="co">Colombia</option>
                    <option value="cl">Chile</option>
                </select>
                <br><br>
            </fieldset>
            
            <input type="checkbox" id="terminos" name="terminos" required>
            <label for="terminos">Acepto los términos y condiciones</label>
            <br><br>
            
            <button type="submit">Registrarse</button>
        </form>
    </body>
    </html>
    ```

---

### Ejercicio 6: Formulario de búsqueda avanzada

**Archivo:** `ejercicio-06.html`

**Objetivo:** Formulario con validaciones HTML5.

??? success "✅ Solución"
    ```html
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Búsqueda de Productos</title>
    </head>
    <body>
        <h1>Buscar Productos</h1>
        
        <form action="/buscar" method="GET">
            <label for="producto">Nombre del producto:</label>
            <input type="text" id="producto" name="producto">
            <br><br>
            
            <label for="precio-min">Precio mínimo (€):</label>
            <input type="number" id="precio-min" name="precio-min" min="0" step="0.01">
            <br><br>
            
            <label for="precio-max">Precio máximo (€):</label>
            <input type="number" id="precio-max" name="precio-max" min="0" step="0.01">
            <br><br>
            
            <label for="categoria">Categoría:</label>
            <select id="categoria" name="categoria">
                <option value="">Todas</option>
                <option value="electronica">Electrónica</option>
                <option value="ropa">Ropa</option>
                <option value="hogar">Hogar</option>
                <option value="deportes">Deportes</option>
            </select>
            <br><br>
            
            <input type="checkbox" id="oferta" name="oferta">
            <label for="oferta">Solo productos en oferta</label>
            <br><br>
            
            <label>Ordenar por:</label><br>
            <input type="radio" id="orden-precio" name="orden" value="precio" checked>
            <label for="orden-precio">Precio</label><br>
            
            <input type="radio" id="orden-nombre" name="orden" value="nombre">
            <label for="orden-nombre">Nombre</label><br>
            
            <input type="radio" id="orden-popular" name="orden" value="popularidad">
            <label for="orden-popular">Popularidad</label>
            <br><br>
            
            <button type="submit">Buscar</button>
            <button type="reset">Limpiar</button>
        </form>
    </body>
    </html>
    ```

---

## 📚 Recursos adicionales

- [MDN - Tablas HTML](https://developer.mozilla.org/es/docs/Learn/HTML/Tables)
- [MDN - Formularios HTML](https://developer.mozilla.org/es/docs/Learn/Forms)
- [HTML Validator](https://validator.w3.org/)

---

⬅️ Volver a [Apuntes HTML Avanzado](../apuntes/03-html-avanzado.md)

***