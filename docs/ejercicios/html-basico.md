# Ejercicios HTML Básico

## 🎯 Instrucciones generales

- Intenta resolver cada ejercicio por tu cuenta antes de ver la solución
- Valida tu código con el [validador W3C](https://validator.w3.org/)
- Guarda todos los archivos en una carpeta `ejercicios-html`
- Usa nombres descriptivos para tus archivos
- Comenta tu código cuando sea necesario

---

## 🟢 Ejercicios Nivel Básico

### Ejercicio 1: Mi primera página completa

**Archivo:** `ejercicio-01.html`

**Objetivo:** Crear una página HTML válida con estructura básica.

**Requisitos:**
- Estructura HTML5 completa (`<!DOCTYPE>`, `<html>`, `<head>`, `<body>`)
- Título en la pestaña: "Mi primera página"
- Un encabezado `<h1>` con tu nombre
- Tres párrafos sobre ti (quién eres, qué estudias, qué te gusta)
- Usa al menos una etiqueta `<strong>` y una `<em>`

??? success "✅ Solución"
    ```
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mi primera página</title>
    </head>
    <body>
        <h1>Juan García López</h1>
        <p>Hola, mi nombre es <strong>Juan García</strong> y estudio 2º de Bachillerato en el IES ejemplo.</p>
        <p>Me apasiona la <em>tecnología</em> y por eso elegí la asignatura de TIC. Quiero aprender a crear mis propias páginas web.</p>
        <p>En mi tiempo libre me gusta jugar al baloncesto, leer novelas de ciencia ficción y escuchar música.</p>
    </body>
    </html>
    ```

---

### Ejercicio 2: Biografía de un personaje famoso

**Archivo:** `ejercicio-02.html`

**Objetivo:** Practicar encabezados, párrafos y formato de texto.

**Requisitos:**
- Elige un personaje histórico o celebridad
- `<h1>` con el nombre del personaje
- `<h2>` "Biografía"
- 2-3 párrafos sobre su vida
- `<h2>` "Logros importantes"
- Lista con sus logros
- Usa `<strong>`, `<em>`, `<mark>` donde sea apropiado

??? success "✅ Solución"
    ```
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Marie Curie</title>
    </head>
    <body>
        <h1>Marie Curie</h1>
        
        <h2>Biografía</h2>
        <p><strong>Marie Curie</strong> (1867-1934) fue una física y química polaca naturalizada francesa, pionera en el campo de la radiactividad.</p>
        <p>Nació en Varsovia, Polonia, y se trasladó a París para estudiar en la Universidad de la Sorbona. Allí conoció a <em>Pierre Curie</em>, con quien se casó en 1895.</p>
        <p>Fue la <mark>primera mujer</mark> en recibir un Premio Nobel y la primera persona en recibir dos premios Nobel en diferentes disciplinas científicas.</p>
        
        <h2>Logros importantes</h2>
        <ul>
            <li><strong>Pionera</strong> en la investigación de la radiactividad</li>
            <li>Descubrimiento de dos elementos químicos: <mark>polonio</mark> y <mark>radio</mark></li>
            <li>Premio Nobel de Física (1903) junto a Pierre Curie y Henri Becquerel</li>
            <li>Premio Nobel de Química (1911) en solitario</li>
            <li>Primera mujer profesora en la Universidad de París</li>
        </ul>
    </body>
    </html>
    ```

---

### Ejercicio 3: Lista de compras

**Archivo:** `ejercicio-03.html`

**Objetivo:** Practicar listas ordenadas y desordenadas.

**Requisitos:**
- `<h1>` "Mi lista de compras"
- `<h2>` "Frutas y verduras"
- Lista desordenada con 5 items
- `<h2>` "Productos de limpieza"
- Lista desordenada con 3 items
- `<h2>` "Pasos para hacer la compra"
- Lista ordenada con 4 pasos

??? success "✅ Solución"
    ```
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Mi Lista de Compras</title>
    </head>
    <body>
        <h1>Mi lista de compras</h1>
        
        <h2>Frutas y verduras</h2>
        <ul>
            <li>Manzanas</li>
            <li>Plátanos</li>
            <li>Zanahorias</li>
            <li>Tomates</li>
            <li>Lechuga</li>
        </ul>
        
        <h2>Productos de limpieza</h2>
        <ul>
            <li>Detergente para ropa</li>
            <li>Lejía</li>
            <li>Bayetas de microfibra</li>
        </ul>
        
        <h2>Pasos para hacer la compra</h2>
        <ol>
            <li>Revisar la nevera y despensa</li>
            <li>Hacer la lista de la compra</li>
            <li>Ir al supermercado</li>
            <li>Pagar y guardar los productos en casa</li>
        </ol>
    </body>
    </html>
    ```

---

### Ejercicio 4: Galería de imágenes

**Archivo:** `ejercicio-04.html`

**Objetivo:** Practicar la inserción de imágenes.

**Requisitos:**
- `<h1>` "Mi galería de fotos"
- 4 imágenes (pueden ser de internet)
- Cada imagen debe tener:
  - Atributo `alt` descriptivo
  - Atributo `title`
  - Un párrafo debajo describiendo la imagen

??? success "✅ Solución"
    ```
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Mi Galería</title>
    </head>
    <body>
        <h1>Mi galería de fotos</h1>
        
        <h2>Naturaleza</h2>
        <img src="https://picsum.photos/400/300?random=1" 
             alt="Paisaje de montaña" 
             title="Montañas al atardecer">
        <p>Esta imagen muestra un hermoso paisaje de montaña al atardecer, con colores cálidos en el cielo.</p>
        
        <h2>Ciudad</h2>
        <img src="https://picsum.photos/400/300?random=2" 
             alt="Edificios modernos" 
             title="Arquitectura urbana">
        <p>Rascacielos modernos que reflejan la luz del sol en una gran ciudad.</p>
        
        <h2>Playa</h2>
        <img src="https://picsum.photos/400/300?random=3" 
             alt="Costa tropical" 
             title="Playa paradisíaca">
        <p>Una playa de arena blanca con aguas cristalinas y palmeras.</p>
        
        <h2>Bosque</h2>
        <img src="https://picsum.photos/400/300?random=4" 
             alt="Camino forestal" 
             title="Sendero en el bosque">
        <p>Un sendero rodeado de árboles altos en un bosque frondoso.</p>
    </body>
    </html>
    ```

---

### Ejercicio 5: Página de enlaces

**Archivo:** `ejercicio-05.html`

**Objetivo:** Practicar enlaces internos y externos.

**Requisitos:**
- `<h1>` "Mis sitios web favoritos"
- `<h2>` "Educación"
- Lista con 3 enlaces a sitios educativos (que abran en nueva pestaña)
- `<h2>` "Entretenimiento"
- Lista con 3 enlaces a sitios de entretenimiento
- `<h2>` "Contacto"
- Un enlace de correo electrónico

??? success "✅ Solución"
    ```
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Mis Sitios Favoritos</title>
    </head>
    <body>
        <h1>Mis sitios web favoritos</h1>
        
        <h2>Educación</h2>
        <ul>
            <li><a href="https://www.khanacademy.org" target="_blank" rel="noopener noreferrer">Khan Academy</a></li>
            <li><a href="https://www.coursera.org" target="_blank" rel="noopener noreferrer">Coursera</a></li>
            <li><a href="https://developer.mozilla.org" target="_blank" rel="noopener noreferrer">MDN Web Docs</a></li>
        </ul>
        
        <h2>Entretenimiento</h2>
        <ul>
            <li><a href="https://www.youtube.com">YouTube</a></li>
            <li><a href="https://www.spotify.com">Spotify</a></li>
            <li><a href="https://www.netflix.com">Netflix</a></li>
        </ul>
        
        <h2>Contacto</h2>
        <p>Si quieres contactar conmigo, escríbeme a: <a href="mailto:miemailç@ejemplo.com">miemail@ejemplo.com</a></p>
    </body>
    </html>
    ```

---

## 🟡 Ejercicios Nivel Intermedio

### Ejercicio 6: Receta de cocina

**Archivo:** `ejercicio-06.html`

**Objetivo:** Combinar múltiples elementos HTML.

**Requisitos:**
- Estructura HTML5 completa
- `<h1>` con nombre de la receta
- Una imagen del plato
- `<h2>` "Información"
- Párrafo con: tiempo de preparación, dificultad, raciones
- `<h2>` "Ingredientes"
- Lista desordenada con ingredientes (mínimo 6)
- `<h2>` "Preparación"
- Lista ordenada con pasos (mínimo 5)
- `<h2>` "Consejos"
- 2 párrafos con consejos útiles

??? success "✅ Solución"
    ```
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Receta: Tortilla de Patatas</title>
    </head>
    <body>
        <h1>Tortilla de Patatas Española</h1>
        
        <img src="https://picsum.photos/500/300?random=10" alt="Tortilla de patatas" title="Tortilla española">
        
        <h2>Información</h2>
        <p><strong>Tiempo de preparación:</strong> 45 minutos</p>
        <p><strong>Dificultad:</strong> Media</p>
        <p><strong>Raciones:</strong> 4 personas</p>
        
        <h2>Ingredientes</h2>
        <ul>
            <li>4 patatas medianas</li>
            <li>6 huevos</li>
            <li>1 cebolla grande (opcional)</li>
            <li>Aceite de oliva virgen extra</li>
            <li>Sal al gusto</li>
            <li>Pimienta negra (opcional)</li>
        </ul>
        
        <h2>Preparación</h2>
        <ol>
            <li>Pelar y cortar las patatas en láminas finas</li>
            <li>Freír las patatas en abundante aceite a fuego medio durante 20 minutos</li>
            <li>Escurrir el aceite y mezclar las patatas con los huevos batidos</li>
            <li>Calentar un poco de aceite en una sartén y verter la mezcla</li>
            <li>Cocinar 3-4 minutos por cada lado hasta que cuaje</li>
            <li>Dar la vuelta con cuidado usando un plato</li>
        </ol>
        
        <h2>Consejos</h2>
        <p>Para que la tortilla quede más jugosa, no dejes que las patatas se doren demasiado al freírlas. El secreto está en freírlas lentamente a temperatura media.</p>
        <p>Si prefieres una tortilla más cuajada, déjala más tiempo en la sartén. Si te gusta más jugosa, reduce el tiempo de cocción.</p>
    </body>
    </html>
    ```

### Ejercicio 07: Página con estructura semántica

**Archivo:** `ejercicio-07.html`

**Objetivo:** Usar etiquetas semánticas HTML5.

??? success "✅ Solución"
    ```
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8" />
        <title>Mi sitio web</title>
    </head>
    <body>
        <header>
            <img src="logo.png" alt="Logo" />
            <nav>
                <ul>
                    <li><a href="#sobre">Sobre mí</a></li>
                    <li><a href="#habilidades">Habilidades</a></li>
                    <li><a href="#proyectos">Proyectos</a></li>
                    <li><a href="#contacto">Contacto</a></li>
                </ul>
            </nav>
        </header>
        <main>
            <article>
                <h2 id="sobre">Sobre mí</h2>
                <p>Soy estudiante y me gusta programar.</p>
                <p>Tengo 17 años y estudio en el instituto.</p>
                <p>Me interesa el desarrollo web y crear páginas atractivas.</p>
            </article>
            <aside>
                <h3>Artículos relacionados</h3>
                <ul>
                    <li><a href="#">HTML avanzado</a></li>
                    <li><a href="#">CSS para principiantes</a></li>
                    <li><a href="#">JavaScript básico</a></li>
                </ul>
            </aside>
            <section id="habilidades">
                <h2>Habilidades</h2>
                <ul>
                    <li>HTML5 &amp; CSS3</li>
                    <li>Javascript básico</li>
                    <li>Diseño responsivo</li>
                </ul>
            </section>
            <section id="proyectos">
                <h2>Mis proyectos</h2>
                <p>Proyecto 1: Página personal</p>
                <p>Proyecto 2: Tienda online</p>
            </section>
            <section id="contacto">
                <h2>Contacto</h2>
                <p>Correo: <a href="mailto:miemail@ejemplo.com">miemail@ejemplo.com</a></p>
            </section>
        </main>
        <footer>
            <p>&copy; 2025 Mi Página Web</p>
        </footer>
    </body>
    </html>
    ```

---

### Ejercicio 08: Portfolio personal

**Archivo:** `ejercicio-08.html`

**Objetivo:** Crear una página completa con varias secciones.

??? success "✅ Solución"
    ```
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8" />
      <title>Mi Portfolio</title>
    </head>
    <body>
      <header>
        <h1>Mi Portfolio</h1>
        <nav>
          <ul>
            <li><a href="#sobre">Sobre mí</a></li>
            <li><a href="#habilidades">Habilidades</a></li>
            <li><a href="#proyectos">Proyectos</a></li>
            <li><a href="#contacto">Contacto</a></li>
          </ul>
        </nav>
      </header>
      <section id="sobre">
        <h2>Sobre mí</h2>
        <img src="foto.jpg" alt="Foto mía" style="width:200px;">
        <p>Soy estudiante de 2º de Bachillerato, apasionado por la programación y el diseño web.</p>
        <p>Me gusta aprender nuevas tecnologías y crear proyectos interesantes.</p>
      </section>
      <section id="habilidades">
        <h2>Habilidades técnicas</h2>
        <ul>
          <li>HTML5 y CSS3</li>
          <li>JavaScript básico</li>
          <li>Responsive Design</li>
        </ul>
        <h2>Habilidades personales</h2>
        <ul>
          <li>Trabajo en equipo</li>
          <li>Creatividad</li>
          <li>Organización</li>
        </ul>
      </section>
      <section id="proyectos">
        <h2>Proyectos</h2>
        <article>
          <h3>Proyecto A</h3>
          <img src="proyecto1.jpg" alt="Proyecto 1" style="width:200px;">
          <p>Una página web personal con efectos CSS y responsive.</p>
        </article>
        <article>
          <h3>Proyecto B</h3>
          <img src="proyecto2.jpg" alt="Proyecto 2" style="width:200px;">
          <p>Una tienda online con carrito y validaciones.</p>
        </article>
        <article>
          <h3>Proyecto C</h3>
          <img src="proyecto3.jpg" alt="Proyecto 3" style="width:200px;">
          <p>Un blog para publicar artículos tecnológicos.</p>
        </article>
      </section>
      <section id="contacto">
        <h2>Contacto</h2>
        <p>Email: <a href="mailto:miemail@ejemplo.com">miemail@ejemplo.com</a></p>
        <p>Teléfono: +34 612345678</p>
      </section>
      <footer>
        <p>&copy; 2025 Mi Portfolio Personal</p>
      </footer>
    </body>
    </html>
    ```

---

### Ejercicio 09: Artículo de blog

**Archivo:** `ejercicio-09.html`

**Objetivo:** Crear contenido con estructura avanzada.

??? success "✅ Solución"
    ```
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8" />
      <title>Mi Primer Post</title>
    </head>
    <body>
      <article>
        <header>
          <h1>Mi aventura en la programación web</h1>
          <p>Por Juan García | 27 octubre 2025</p>
        </header>
        <img src="blog1.jpg" alt="Pantalla de código" style="width:100%;">
        <section>
          <h2>Introducción</h2>
          <p>Comencé hace unos meses y ha sido un camino lleno de aprendizaje y desafíos.</p>
        </section>
        <section>
          <h2>Mi experiencia</h2>
          <p>Al principio costó entender cómo funcionaba todo, pero con práctica diaria ahora puedo crear páginas sencillas.</p>
        </section>
        <section>
          <h3>Lo más difícil</h3>
          <p>Resolver errores en el código y entender el layout responsive.</p>
        </section>
        <section>
          <h2>Consejos</h2>
          <ul>
            <li>Practica todos los días</li>
            <li>Pide ayuda cuando te atasques</li>
            <li>Estudia código de otros</li>
          </ul>
        </section>
        <section>
          <h2>Conclusión</h2>
          <p>La programación web es divertida y útil. ¡Sigue practicando!</p>
        </section>
        <footer>
          <p>Lectura recomendada: <a href="#">Curso completo de HTML y CSS</a></p>
        </footer>
      </article>
    </body>
    </html>
    ```

---

### Ejercicio 10: Página con anclas

**Archivo:** `ejercicio-10.html`

**Objetivo:** Navegación interna con enlaces a secciones.

??? success "✅ Solución"
    ```
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8" />
      <title>Mi Página con Anclas</title>
    </head>
    <body>
      <h1>Índice</h1>
      <ul>
        <li><a href="#seccion1">Sección 1</a></li>
        <li><a href="#seccion2">Sección 2</a></li>
        <li><a href="#seccion3">Sección 3</a></li>
        <li><a href="#seccion4">Sección 4</a></li>
        <li><a href="#seccion5">Sección 5</a></li>
      </ul>
      
      <hr>
      <section id="seccion1">
        <h2>Sección 1</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
        <p>Vestibulum auctor dapibus neque.</p>
        <p>Donec tellus quam, tristique sed, vulputate nec, mattis id, orci.</p>
        <a href="#top">Volver al índice</a>
      </section>
      <section id="seccion2">
        <h2>Sección 2</h2>
        <p>Nulla facilisi. Sed cursus orci nec augue commodo.</p>
        <p>Donec dui libero, accumsan nec, vulputate ut, vulputate sed, nisl.</p>
        <p>Curabitur ligula sapien, tincidunt non, euismod vitae, posuere imperdiet, leo.</p>
        <a href="#top">Volver al índice</a>
      </section>
      <section id="seccion3">
        <h2>Sección 3</h2>
        <p>Nam fermentum, ligula non tempus aliquam, nunc turpis ullamcorper nibh.</p>
        <p>Proin libero augue, porta ac, volutpat ac, bibendum in, nisi.</p>
        <p>Nam fermentum, ligula non tempus aliquam.</p>
        <a href="#top">Volver al índice</a>
      </section>
      <section id="seccion4">
        <h2>Sección 4</h2>
        <p>Sed ut perspiciatis unde omnis iste natus error sit voluptatem.</p>
        <p>Sit voluptatem accusantium doloremque laudantium, totam rem aperiam.</p>
        <p>Eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.</p>
        <a href="#top">Volver al índice</a>
      </section>
      <section id="seccion5">
        <h2>Sección 5</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
        <p>Vestibulum auctor dapibus neque.</p>
        <p>Donec tellus quam, tristique sed, vulputate nec, mattis id, orci.</p>
        <a href="#top">Volver al índice</a>
      </section>
      
    </body>
    </html>
    ```

---

## 🔴 Ejercicios Nivel Avanzado

### Ejercicio 11: Sitio multi-página

**Archivos:** `index.html`, `sobre-mi.html`, `proyectos.html`, `contacto.html`

**Objetivo:** Crear un sitio con múltiples páginas conectadas.

**Requisitos:**
- 4 páginas HTML interconectadas
- Navegación consistente en todas
- Header y footer compartidos

??? success "✅ Solución - index.html"
    ```
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Inicio - Mi Sitio Web</title>
    </head>
    <body>
        <header>
            <h1>Mi Sitio Web Personal</h1>
            <nav>
                <a href="index.html">Inicio</a> |
                <a href="sobre-mi.html">Sobre mí</a> |
                <a href="proyectos.html">Proyectos</a> |
                <a href="contacto.html">Contacto</a>
            </nav>
        </header>
        
        <main>
            <h2>Bienvenido a mi sitio web</h2>
            <p>Aquí encontrarás información sobre mí, mis proyectos y cómo contactarme.</p>
            <p>Explora las diferentes secciones usando el menú de navegación.</p>
        </main>
        
        <footer>
            <p>&copy; 2025 - Todos los derechos reservados</p>
        </footer>
    </body>
    </html>
    ```

??? success "✅ Solución - sobre-mi.html"
    ```
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Sobre mí - Mi Sitio Web</title>
    </head>
    <body>
        <header>
            <h1>Mi Sitio Web Personal</h1>
            <nav>
                <a href="index.html">Inicio</a> |
                <a href="sobre-mi.html">Sobre mí</a> |
                <a href="proyectos.html">Proyectos</a> |
                <a href="contacto.html">Contacto</a>
            </nav>
        </header>
        
        <main>
            <h2>Sobre mí</h2>
            <img src="https://via.placeholder.com/200" alt="Mi foto">
            <p>Soy estudiante de 2º de Bachillerato interesado en el desarrollo web y la programación.</p>
            <p>Me gusta aprender nuevas tecnologías y crear proyectos que mejoren la vida de las personas.</p>
        </main>
        
        <footer>
            <p>&copy; 2025 - Todos los derechos reservados</p>
        </footer>
    </body>
    </html>
    ```

---

### Ejercicio 12: Documentación técnica

**Archivo:** `documentacion.html`

**Objetivo:** Crear una página tipo documentación.

**Requisitos:**
- Barra lateral con índice (lista de enlaces internos)
- Mínimo 6 secciones documentando conceptos HTML
- Cada sección con: título, explicación (2-3 párrafos), ejemplos de código, notas
- Navegación "Anterior" y "Siguiente" al final de cada sección

??? success "✅ Solución"
    ```
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Documentación HTML</title>
        <style>
            body { display: flex; }
            aside { width: 250px; padding: 20px; background: #f5f5f5; }
            main { flex: 1; padding: 20px; }
            nav a { display: block; margin: 5px 0; }
        </style>
    </head>
    <body>
        <aside>
            <h2>Contenidos</h2>
            <nav>
                <a href="#intro">1. Introducción</a>
                <a href="#etiquetas">2. Etiquetas básicas</a>
                <a href="#atributos">3. Atributos</a>
                <a href="#listas">4. Listas</a>
                <a href="#enlaces">5. Enlaces</a>
                <a href="#imagenes">6. Imágenes</a>
            </nav>
        </aside>
        
        <main>
            <h1>Documentación HTML - Guía Completa</h1>
            
            <section id="intro">
                <h2>1. Introducción a HTML</h2>
                <p>HTML (HyperText Markup Language) es el lenguaje estándar para crear páginas web. Define la estructura del contenido mediante un sistema de etiquetas.</p>
                <p>Cada etiqueta HTML tiene un propósito específico y ayuda a los navegadores a interpretar y mostrar el contenido correctamente.</p>
                <p>HTML no es un lenguaje de programación, sino un lenguaje de marcado que estructura documentos.</p>
                
                <h3>Ejemplo básico:</h3>
                <pre><code>&lt;!DOCTYPE html&gt;
&lt;html lang="es"&gt;
&lt;head&gt;
    &lt;title&gt;Mi Página&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;h1&gt;Hola Mundo&lt;/h1&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
                
                <p><strong>Nota:</strong> Siempre incluye la declaración DOCTYPE al inicio del documento.</p>
                <p><a href="#etiquetas">Siguiente: Etiquetas básicas →</a></p>
            </section>
            
            <hr>
            
            <section id="etiquetas">
                <h2>2. Etiquetas básicas</h2>
                <p>Las etiquetas más comunes incluyen encabezados, párrafos y elementos de formato.</p>
                <p>Los encabezados van de <code>&lt;h1&gt;</code> a <code>&lt;h6&gt;</code>, siendo h1 el más importante.</p>
                <p>Los párrafos se definen con <code>&lt;p&gt;</code> y separan bloques de texto.</p>
                
                <h3>Ejemplo:</h3>
                <pre><code>&lt;h1&gt;Título principal&lt;/h1&gt;
&lt;h2&gt;Subtítulo&lt;/h2&gt;
&lt;p&gt;Este es un párrafo con &lt;strong&gt;texto en negrita&lt;/strong&gt;.&lt;/p&gt;</code></pre>
                
                <p><strong>Advertencia:</strong> Usa solo un <code>&lt;h1&gt;</code> por página para mejor SEO.</p>
                <p><a href="#intro">← Anterior: Introducción</a> | <a href="#atributos">Siguiente: Atributos →</a></p>
            </section>
            
            <hr>
            
            <section id="atributos">
                <h2>3. Atributos HTML</h2>
                <p>Los atributos proporcionan información adicional sobre los elementos HTML.</p>
                <p>Se escriben dentro de la etiqueta de apertura y tienen formato nombre="valor".</p>
                <p>Algunos atributos son universales (id, class), otros son específicos de ciertas etiquetas.</p>
                
                <h3>Ejemplo:</h3>
                <pre><code>&lt;p id="intro" class="destacado"&gt;Párrafo con atributos&lt;/p&gt;
&lt;img src="foto.jpg" alt="Descripción"&gt;
&lt;a href="pagina.html" target="_blank"&gt;Enlace&lt;/a&gt;</code></pre>
                
                <p><strong>Nota:</strong> El atributo <code>alt</code> es obligatorio en imágenes para accesibilidad.</p>
                <p><a href="#etiquetas">← Anterior: Etiquetas básicas</a> | <a href="#listas">Siguiente: Listas →</a></p>
            </section>
            
            <hr>
            
            <section id="listas">
                <h2>4. Listas en HTML</h2>
                <p>HTML soporta tres tipos de listas: ordenadas, desordenadas y de definición.</p>
                <p>Las listas ordenadas (<code>&lt;ol&gt;</code>) muestran números, las desordenadas (<code>&lt;ul&gt;</code>) muestran viñetas.</p>
                <p>Cada elemento de lista se define con <code>&lt;li&gt;</code>.</p>
                
                <h3>Ejemplo:</h3>
                <pre><code>&lt;ul&gt;
    &lt;li&gt;Item 1&lt;/li&gt;
    &lt;li&gt;Item 2&lt;/li&gt;
&lt;/ul&gt;

&lt;ol&gt;
    &lt;li&gt;Primer paso&lt;/li&gt;
    &lt;li&gt;Segundo paso&lt;/li&gt;
&lt;/ol&gt;</code></pre>
                
                <p><strong>Tip:</strong> Puedes anidar listas dentro de otras listas.</p>
                <p><a href="#atributos">← Anterior: Atributos</a> | <a href="#enlaces">Siguiente: Enlaces →</a></p>
            </section>
            
            <hr>
            
            <section id="enlaces">
                <h2>5. Enlaces</h2>
                <p>Los enlaces permiten la navegación entre páginas. Se crean con la etiqueta <code>&lt;a&gt;</code>.</p>
                <p>El atributo <code>href</code> especifica el destino del enlace.</p>
                <p>Pueden ser absolutos (URL completa) o relativos (ruta local).</p>
                
                <h3>Ejemplo:</h3>
                <pre>odede>&lt;a href="https://ejemplo.com"&gt;Enlace externo&lt;/a&gt;
&lt;a href="pagina.html"&gt;Enlace interno&lt;/a&gt;
&lt;a href="#seccion"&gt;Ancla&lt;/a&gt;
&lt;a href="mailto:email@ejemplo.com"&gt;Email&lt;/a&gt;</code></pre>
                
                <p><strong>Seguridad:</strong> Usa <code>rel="noopener noreferrer"</code> con <code>target="_blank"</code>.</p>
                <p><a href="#listas">← Anterior: Listas</a> | <a href="#imagenes">Siguiente: Imágenes →</a></p>
            </section>
            
            <hr>
            
            <section id="imagenes">
                <h2>6. Imágenes</h2>
                <p>Las imágenes se insertan con la etiqueta <code>&lt;img&gt;</code>.</p>
                <p>Los atributos <code>src</code> (fuente) y <code>alt</code> (texto alternativo) son obligatorios.</p>
                <p>Puedes especificar dimensiones con <code>width</code> y <code>height</code>.</p>
                
                <h3>Ejemplo:</h3>
                <pre><code>&lt;img src="foto.jpg" 
     alt="Descripción de la imagen" 
     width="400" 
     height="300"&gt;</code></pre>
                
                <p><strong>Importante:</strong> Optimiza las imágenes antes de subirlas para mejor rendimiento.</p>
                <p><a href="#enlaces">← Anterior: Enlaces</a></p>
            </section>
        </main>
    </body>
    </html>
    ```

---

### Ejercicio 13: Landing page

**Archivo:** `landing.html`

**Objetivo:** Crear una página de aterrizaje profesional.

**Requisitos:**
- Hero section con título, subtítulo, imagen de fondo, llamada a la acción
- Sección "Características" con 4 puntos destacados
- Sección "Cómo funciona" con pasos numerados
- Sección "Testimonios" con 3 citas
- Sección "FAQ" con preguntas frecuentes
- Footer completo

??? success "✅ Solución"
    ```
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>MiApp - La mejor solución</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { font-family: Arial, sans-serif; }
            .hero { 
                background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), 
                            url('https://picsum.photos/1920/800') center/cover;
                color: white; text-align: center; padding: 150px 20px;
            }
            section { padding: 60px 20px; }
            .caracteristicas { background: #f5f5f5; }
            footer { background: #333; color: white; padding: 40px 20px; text-align: center; }
        </style>
    </head>
    <body>
        <!-- Hero Section -->
        <section class="hero">
            <h1>Transforma tu negocio con MiApp</h1>
            <p>La solución definitiva para gestionar tu empresa de forma eficiente</p>
            <br>
            <a href="#contacto" style="background: #007bff; color: white; padding: 15px 40px; 
                                        text-decoration: none; border-radius: 5px; font-size: 18px;">
                Prueba gratis 30 días
            </a>
        </section>
        
        <!-- Características -->
        <section class="caracteristicas">
            <h2 style="text-align: center; margin-bottom: 40px;">¿Por qué elegir MiApp?</h2>
            
            <article style="max-width: 1200px; margin: 0 auto;">
                <div style="display: inline-block; width: 45%; padding: 20px; vertical-align: top;">
                    <h3>⚡ Rápido y eficiente</h3>
                    <p>Procesa miles de transacciones por segundo sin ralentizar tu negocio.</p>
                </div>
                
                <div style="display: inline-block; width: 45%; padding: 20px; vertical-align: top;">
                    <h3>🔒 Seguro y confiable</h3>
                    <p>Encriptación de nivel bancario para proteger tus datos más sensibles.</p>
                </div>
                
                <div style="display: inline-block; width: 45%; padding: 20px; vertical-align: top;">
                    <h3>📱 Multiplataforma</h3>
                    <p>Accede desde web, móvil o tablet. Siempre sincronizado en tiempo real.</p>
                </div>
                
                <div style="display: inline-block; width: 45%; padding: 20px; vertical-align: top;">
                    <h3>💬 Soporte 24/7</h3>
                    <p>Nuestro equipo está disponible las 24 horas para ayudarte cuando lo necesites.</p>
                </div>
            </article>
        </section>
        
        <!-- Cómo funciona -->
        <section>
            <h2 style="text-align: center; margin-bottom: 40px;">Cómo funciona</h2>
            <ol style="max-width: 800px; margin: 0 auto; font-size: 18px; line-height: 2;">
                <li><strong>Regístrate</strong> en menos de 2 minutos con tu email</li>
                <li><strong>Configura</strong> tu espacio de trabajo según tus necesidades</li>
                <li><strong>Invita</strong> a tu equipo y comienza a colaborar</li>
                <li><strong>Disfruta</strong> de una gestión más eficiente desde el primer día</li>
            </ol>
        </section>
        
        <!-- Testimonios -->
        <section style="background: #f9f9f9;">
            <h2 style="text-align: center; margin-bottom: 40px;">Lo que dicen nuestros clientes</h2>
            
            <div style="max-width: 1200px; margin: 0 auto;">
                <blockquote style="border-left: 4px solid #007bff; padding-left: 20px; margin: 30px;">
                    <p style="font-style: italic; font-size: 18px;">
                        "MiApp ha revolucionado la forma en que gestionamos proyectos. 
                        Ahora somos un 40% más productivos."
                    </p>
                    <footer>— María González, CEO de TechStart</footer>
                </blockquote>
                
                <blockquote style="border-left: 4px solid #007bff; padding-left: 20px; margin: 30px;">
                    <p style="font-style: italic; font-size: 18px;">
                        "La mejor inversión que hemos hecho. El ROI fue positivo en el primer mes."
                    </p>
                    <footer>— Carlos Pérez, Director de Operaciones</footer>
                </blockquote>
                
                <blockquote style="border-left: 4px solid #007bff; padding-left: 20px; margin: 30px;">
                    <p style="font-style: italic; font-size: 18px;">
                        "Interfaz intuitiva y soporte excepcional. No podríamos estar más contentos."
                    </p>
                    <footer>— Ana Martínez, Freelance Designer</footer>
                </blockquote>
            </div>
        </section>
        
        <!-- FAQ -->
        <section>
            <h2 style="text-align: center; margin-bottom: 40px;">Preguntas frecuentes</h2>
            <div style="max-width: 800px; margin: 0 auto;">
                <details style="margin: 20px 0; padding: 15px; border: 1px solid #ddd;">
                    <summary style="font-weight: bold; cursor: pointer;">¿Cuánto cuesta MiApp?</summary>
                    <p style="margin-top: 10px;">
                        Ofrecemos planes desde 9€/mes. Prueba gratuita de 30 días sin tarjeta de crédito.
                    </p>
                </details>
                
                <details style="margin: 20px 0; padding: 15px; border: 1px solid #ddd;">
                    <summary style="font-weight: bold; cursor: pointer;">¿Puedo cancelar en cualquier momento?</summary>
                    <p style="margin-top: 10px;">
                        Sí, puedes cancelar tu suscripción cuando quieras sin penalizaciones.
                    </p>
                </details>
                
                <details style="margin: 20px 0; padding: 15px; border: 1px solid #ddd;">
                    <summary style="font-weight: bold; cursor: pointer;">¿Mis datos están seguros?</summary>
                    <p style="margin-top: 10px;">
                        Absolutamente. Usamos encriptación SSL y cumplimos con RGPD.
                    </p>
                </details>
                
                <details style="margin: 20px 0; padding: 15px; border: 1px solid #ddd;">
                    <summary style="font-weight: bold; cursor: pointer;">¿Ofrecen formación?</summary>
                    <p style="margin-top: 10px;">
                        Sí, incluimos videotutoriales, documentación completa y webinars mensuales.
                    </p>
                </details>
            </div>
        </section>
        
        <!-- Footer -->
        <footer id="contacto">
            <h3>¿Listo para empezar?</h3>
            <p>Únete a más de 10,000 empresas que ya confían en MiApp</p>
            <br>
            <p>Email: contacto@miapp.com | Tel: +34 900 123 456</p>
            <p style="margin-top: 20px;">
                <a href="#" style="color: white; margin: 0 10px;">Facebook</a> |
                <a href="#" style="color: white; margin: 0 10px;">Twitter</a> |
                <a href="#" style="color: white; margin: 0 10px;">LinkedIn</a>
            </p>
            <p style="margin-top: 30px; font-size: 14px;">&copy; 2025 MiApp. Todos los derechos reservados.</p>
        </footer>
    </body>
    </html>
    ```
```

***

---

## ✅ Criterios de evaluación

Tu código será evaluado según:

- ✅ **Validez HTML**: Sin errores en validator.w3.org
- ✅ **Tablas correctas**: Uso apropiado de `<thead>`, `<tbody>`, `<th>`, `<td>`
- ✅ **Formularios funcionales**: Labels correctos, validaciones, campos apropiados
- ✅ **Multimedia operativa**: Audio y vídeo que funcionan correctamente
- ✅ **Accesibilidad**: `alt` en imágenes, `label` en formularios, estructura semántica
- ✅ **Organización**: Código limpio, indentado y comentado

---

## 💡 Consejos

!!! tip "Tablas"
    - No uses tablas para maquetar, solo para datos tabulares
    - Siempre incluye `<thead>` y `<tbody>` para mejor semántica
    - Usa `scope="col"` o `scope="row"` en `<th>` para accesibilidad

!!! tip "Formularios"
    - Siempre conecta `<label>` con el campo usando `for` e `id`
    - Usa el tipo de `input` más apropiado (email, number, date, etc.)
    - Aprovecha las validaciones HTML5 (`required`, `min`, `max`, `pattern`)
    - Agrupa campos relacionados con `<fieldset>` y `<legend>`

!!! tip "Multimedia"
    - Siempre incluye el atributo `controls` en audio y vídeo
    - Proporciona múltiples formatos (`<source>`) para compatibilidad
    - Añade texto alternativo para navegadores que no soporten multimedia
    - Optimiza el tamaño de archivos multimedia antes de subirlos

---

## 📚 Recursos adicionales

- [MDN - Tablas HTML](https://developer.mozilla.org/es/docs/Learn/HTML/Tables)
- [MDN - Formularios HTML](https://developer.mozilla.org/es/docs/Learn/Forms)
- [MDN - Audio y Vídeo](https://developer.mozilla.org/es/docs/Web/HTML/Elemento/audio)
- [HTML Validator](https://validator.w3.org/)

---

## ⬅️ Volver

Volver a [Apuntes HTML Avanzado](../apuntes/03-html-avanzado.md)
