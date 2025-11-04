# Ejercicio evaluable : HTML básico

---

## 🎯 Objetivo

Crear una **página HTML única y completa** que integre todos los conceptos principales de HTML Básico: estructura, encabezados, párrafos, formato de texto, imágenes, enlaces, listas y etiquetas semánticas.

## Nombre archivo:

Entregar el archivo con el nombre `index.html`

## 📋 Requisitos del proyecto

### Estructura HTML5 Completa

Tu página debe tener una estructura HTML5 válida con:

- `<!DOCTYPE html>`
- `<html lang="es">`
- `<head>` con meta tags (charset, viewport)
- `<title>` descriptivo
- `<body>` con contenido organizado

**Por qué:** Una estructura correcta hace que el navegador interprete bien tu página y los buscadores la indexen correctamente.

---

### Encabezados y jerarquía

**Requisitos:**

- Un `<h1>` con tu nombre (debe ser el principal)
- Mínimo cuatro `<h2>` para cada sección
- Estructura jerárquica correcta (no saltar niveles)

**Secciones sugeridas:**

- Sobre mí
- Habilidades
- Intereses
- Enlaces de interés

**Ejemplo:**

```
<h1>Juan García López</h1>
<p>Desarrollador Web Junior</p>

<h2>Sobre mí</h2>
<p>Contenido...</p>

<h2>Habilidades</h2>
<p>Contenido...</p>
```

**Por qué:** Los encabezados organizan el contenido y ayudan a los motores de búsqueda a entender la estructura de tu página.

---

### Párrafos con Formato de Texto

**Requisitos:**

- Mínimo 4-5 párrafos en total
- Usa `<strong>` para palabras importante (se ve en negrita)
- Usa `<em>` para palabras énfasis (se ve en cursiva)
- Cada párrafo debe tener sentido completo

**Ejemplo:**

```
<p>
    Hola, mi nombre es <strong>Juan García</strong> y estudio
    <strong>2º de Bachillerato</strong>. Me apasiona la
    <em>tecnología</em> y quiero aprender a crear páginas web.
</p>
```

**Dónde usarlos:**

- `<strong>`: nombres, fechas, datos importantes
- `<em>`: énfasis, conceptos especiales, palabras en otro idioma

**Por qué:** Ayuda a los lectores a identificar rápidamente información importante.

---

### Imágenes

**Requisitos:**

- Mínimo 2-3 imágenes
- Cada imagen debe tener:
  - Atributo `src` (ruta de la imagen)
  - Atributo `alt` descriptivo (obligatorio para accesibilidad)
  - Atributo `title` (aparece al pasar el ratón)

**Ejemplo:**

```
<img
    src="https://via.placeholder.com/300"
    alt="Mi foto de perfil"
    title="Juan García - 2025"
>

<img
    src="mi-proyecto.jpg"
    alt="Captura de pantalla de mi primer proyecto web"
    title="Proyecto 1: Landing Page"
>
```

**Tipos de imágenes a incluir:**

- Tu foto de perfil
- Imágenes de proyectos o intereses
- Capturas de pantalla

**Por qué:** El `alt` es importante para personas con discapacidad visual que usan lectores de pantalla.

---

### Enlaces (Internos y Externos)
es Internos (Anclas)

Permiten navegar dentro de la misma página usando `#id`.

**Requisitos:**

- Crea una navegación con al menos 4 enlaces internos
- Cada enlace apunta a una sección con `id` correspondiente

**Ejemplo:**

```
<!-- Navegación -->
<nav>
    <ul>
        <li><a href="#sobre">Sobre mí</a></li>
        <li><a href="#habilidades">Habilidades</a></li>
        <li><a href="#intereses">Intereses</a></li>
        <li><a href="#enlaces">Enlaces</a></li>
    </ul>
</nav>

<!-- Secciones con id -->
<section id="sobre">
    <h2>Sobre mí</h2>
    <p>Contenido...</p>
</section>

<section id="habilidades">
    <h2>Habilidades</h2>
    <p>Contenido...</p>
</section>
```

#### Enlaces Externos

Apuntan a sitios web externos.

**Requisitos:**

- Mínimo 3-4 enlaces externos
- Usa `target="_blank"` para abrir en nueva pestaña
- Cada enlace debe ser relevante y funcionar

**Ejemplo:**

```
<section id="enlaces">
    <h2>Enlaces de Interés</h2>
    <ul>
        <li>
            <a href="https://developer.mozilla.org" target="_blank">
                MDN Web Docs
            </a>
        </li>
        <li>
            <a href="https://www.w3schools.com" target="_blank">
                W3Schools
            </a>
        </li>
        <li>
            <a href="https://github.com" target="_blank">
                GitHub
            </a>
        </li>
    </ul>
</section>
```

**Por qué:** Los enlaces son la esencia de la web y permiten navegación entre contenidos.

---

### Listas

#### Lista Desordenada

Se usa cuando el orden no importa. Los elementos aparecen con viñetas.

**Requisitos:**

- Una lista desordenada con mínimo 5 elementos
- Úsala para: habilidades, intereses, características

**Ejemplo:**

```
<h2>Habilidades</h2>
<ul>
    <li>HTML5 &amp; CSS3</li>
    <li>Diseño Responsivo</li>
    <li>JavaScript Básico</li>
    <li>Control de Versiones (Git)</li>
    <li>Comunicación Efectiva</li>
</ul>
```

#### Lista Ordenada

Se usa cuando el orden es importante. Los elementos aparecen numerados.

**Requisitos:**

- Una lista ordenada con mínimo 3-4 elementos
- Úsala para: ranking, pasos, procesos

**Ejemplo:**

```
<h2>Top 3 Intereses</h2>
<ol>
    <li>Desarrollo Web Frontend</li>
    <li>Diseño de Interfaces Modernas</li>
    <li>Nuevas Tecnologías</li>
</ol>
```

**Por qué:** Las listas organizan información de forma clara y legible.

---

### Etiquetas Semánticas

Las etiquetas semánticas dan significado al contenido, no solo presentación.

**Requisitos:**

- `<header>` para el encabezado de la página
- `<nav>` para la navegación
- `<section>` para agrupar contenido relacionado
- `<footer>` para el pie de página

**Ejemplo completo:**

```
<header>
    <h1>Tu Nombre</h1>
    <p>Tu especialidad</p>
</header>

<nav>
    <ul>
        <li><a href="#sobre">Sobre</a></li>
        <li><a href="#habilidades">Habilidades</a></li>
    </ul>
</nav>

<main>
    <section id="sobre">
        <h2>Sobre mí</h2>
        <p>Contenido...</p>
    </section>

    <section id="habilidades">
        <h2>Habilidades</h2>
        <p>Contenido...</p>
    </section>
</main>

<footer>
    <p>&copy; 2025 Tu Nombre</p>
</footer>
```

**Por qué:** Ayuda a los motores de búsqueda y lectores de pantalla a entender la estructura de tu página.

---

### Entidades HTML

Las entidades HTML representan caracteres especiales.

**Requisitos:**

- Usa al menos 3-4 entidades HTML diferentes

**Entidades comunes:**

```
&amp;    <!-- & (ampersand) -->
&copy;   <!-- © (copyright) -->
&lt;     <!-- < (menor que) -->
&gt;     <!-- > (mayor que) -->
&nbsp;   <!-- Espacio no rompible -->
&quot;   <!-- " (comillas) -->
```

**Ejemplo:**

```
<p>HTML &amp; CSS son complementarios</p>
<p>&copy; 2025 Tu Nombre. Todos los derechos reservados.</p>
<p>Tag HTML: &lt;p&gt;</p>
```

**Por qué:** Garantiza que caracteres especiales se muestren correctamente en todos los navegadores.

---

## 🔧 Estructura Recomendada

```
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Perfil - [Tu Nombre]</title>
</head>
<body>
    <!-- Header -->
    <header>
        <h1>Tu Nombre</h1>
        <p>Tu especialidad o profesión</p>
    </header>

    <!-- Navegación -->
    <nav>
        <ul>
            <li><a href="#sobre">Sobre mí</a></li>
            <li><a href="#habilidades">Habilidades</a></li>
            <li><a href="#intereses">Intereses</a></li>
            <li><a href="#enlaces">Enlaces</a></li>
        </ul>
    </nav>

    <!-- Contenido Principal -->
    <main>
        <section id="sobre">
            <h2>Sobre mí</h2>
            <img src="foto.jpg" alt="Mi foto de perfil" title="[Tu Nombre]">
            <p>Párrafo 1: Quién eres y qué estudias...</p>
            <p>Párrafo 2: Qué te apasiona...</p>
            <p>Párrafo 3: Tus metas...</p>
        </section>

        <section id="habilidades">
            <h2>Habilidades</h2>
            <ul>
                <li>HTML5 &amp; CSS3</li>
                <li>Diseño Web Responsivo</li>
                <li>JavaScript Básico</li>
                <li>Git &amp; GitHub</li>
                <li>Comunicación Efectiva</li>
            </ul>
        </section>

        <section id="intereses">
            <h2>Top 3 Intereses</h2>
            <ol>
                <li>Desarrollo Web</li>
                <li>Diseño de Interfaces</li>
                <li>Innovación Tecnológica</li>
            </ol>
        </section>

        <section id="enlaces">
            <h2>Enlaces de Interés</h2>
            <ul>
                <li>
                    <a href="https://developer.mozilla.org" target="_blank">
                        MDN Web Docs
                    </a>
                </li>
                <li>
                    <a href="https://www.w3schools.com" target="_blank">
                        W3Schools
                    </a>
                </li>
                <li>
                    <a href="https://github.com" target="_blank">
                        GitHub
                    </a>
                </li>
            </ul>
        </section>
    </main>

    <!-- Footer -->
    <footer>
        <p>&copy; 2025 [Tu Nombre]. Todos los derechos reservados.</p>
        <p>Email: <a href="mailto:tuemail@ejemplo.com">tuemail@ejemplo.com</a></p>
    </footer>
</body>
</html>
```

---

## ✅ Checklist de Validación

Antes de entregar, verifica que tu página incluya:

- [ ] Estructura HTML5 completa y válida
- [ ] 1 `<h1>` y mínimo 4 `<h2>` con jerarquía correcta
- [ ] 4-5 párrafos con `<strong>` y `<em>`
- [ ] 2-3 imágenes con `alt` y `title`
- [ ] Navegación con enlaces internos (#id)
- [ ] 3-4 enlaces externos con `target="_blank"`
- [ ] 1 lista desordenada (`<ul>`) con 5+ items
- [ ] 1 lista ordenada (`<ol>`) con 3+ items
- [ ] Etiquetas semánticas: `<header>`, `<nav>`, `<section>`, `<footer>`
- [ ] Mínimo 3-4 entidades HTML (`&amp;`, `&copy;`, etc.)
- [ ] Sin errores en [validator.w3.org](https://validator.w3.org/)
- [ ] Código bien indentado
- [ ] Comentarios en secciones importantes

---

## 📊 Rúbrica de Evaluación

| Criterio                                | Puntos     |
| --------------------------------------- | ---------- |
| Estructura HTML5 completa y válida      | 15 pts     |
| Encabezados con jerarquía correcta      | 10 pts     |
| Párrafos con `<strong>` y `<em>`        | 10 pts     |
| Imágenes con `alt` descriptivo          | 10 pts     |
| Enlaces internos y externos funcionales | 15 pts     |
| Listas desordenada y ordenada           | 15 pts     |
| Etiquetas semánticas                    | 15 pts     |
| Entidades HTML                          | 5 pts      |
| Validez W3C                             | 5 pts      |
| **TOTAL**                               | **100 pts** |

---

## 💡 Consejos Importantes

!!! warning "No olvides" 
    - Todos los `<img>` necesitan `alt` descriptivo - Los enlaces internos necesitan `#id` que coincida con el `id` de la sección - No olvides cerrar todas las etiquetas - La estructura debe ser jerárquica: `<h1>` → `<h2>` → `<h3>`

!!! tip "Para mejorar"
     - Usa nombres descriptivos para tus ids: `id="sobre-mi"` es mejor que `id="s1"` - Añade comentarios en tu HTML para explicar secciones - Usa imágenes de buena calidad (pero optimizadas) - Escribe contenido auténtico y personal

!!! error "Errores comunes"
     - ❌ Olvidar el `alt` en imágenes - ❌ No cerrar etiquetas correctamente - ❌ No usar jerarquía correcta de encabezados - ❌ Enlaces internos sin `#id` correspondiente - ❌ No validar en W3C

---

## 📚 Recursos

- [Validador W3C](https://validator.w3.org/)
- [MDN - HTML Básico](https://developer.mozilla.org/es/docs/Learn/HTML)
- [Imágenes placeholder](https://via.placeholder.com/)

---

¡Suerte creando tu página de perfil! 🚀
