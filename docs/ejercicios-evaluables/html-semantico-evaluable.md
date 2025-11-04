# Ejercicio evaluable: HTML Semántico (50 minutos máximo)

***

## Objetivo

Crear la estructura de una página web personal simple utilizando las etiquetas semánticas principales de HTML5.

***

## Instrucciones

1. **Crea un archivo llamado `index.html` con estructura HTML5 válida.**
2. **La página debe incluir:**

   - Una cabecera `<header>` con tu nombre y una breve presentación.  
   - Un menú de navegación `<nav>` con enlaces internos a tres secciones (usa `#id`).
   - Un contenido principal `<main>` con:
      - Sección `<section id="sobre-mi">` con dos párrafos sobre ti usando `<strong>` y `<em>`.
      - Sección `<section id="aficiones">` con una lista desordenada de al menos tres hobbies.
      - Un `<article>` titulado "Mi experiencia", con al menos cinco líneas relatando una anécdota real o imaginaria.
   - Una sección `<section id="enlaces">` con tres enlaces externos relevantes, usando `target="_blank"`.
   - Un pie de página `<footer>` con derechos de autor y un enlace de correo (`mailto:`).

3. **Incluye al menos una imagen tuya o de tus intereses con los atributos `alt` y `title`.**

4. **Usa mínimo tres entidades HTML (`&amp;`, `&copy;`, `&lt;`, etc).**

***

## Criterios de evaluación

| Criterio                                   | Pts |
|---------------------------------------------|-----|
| Estructura HTML5 y etiquetas semánticas     | 15  |
| Menú de navegación, enlaces internos/externos| 15  |
| Texto con formato `<strong>`, `<em>`        | 10  |
| Imágenes con `alt` y `title`                | 10  |
| Lista desordenada (hobbies/aficiones)       | 10  |
| `<article>` relato completo                 | 10  |
| Pie de página `<footer>` con entidad y correo| 10  |
| Entidades HTML                             | 10   |
| Código válido y bien indentado              | 10   |
| **TOTAL**                                  | **100** |

***

## Estructura recomendada

![html semántico](./img/html-semantico-resultado.png)

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Mi Perfil - [Tu nombre]</title>
</head>
<body>
  <header>
    <h1>[Tu Nombre]</h1>
    <p><em>Estudiante de Desarrollo Web</em></p>
  </header>

  <nav>
    <ul>
      <li><a href="#sobre-mi">Sobre mí</a></li>
      <li><a href="#aficiones">Aficiones</a></li>
      <li><a href="#enlaces">Enlaces</a></li>
    </ul>
  </nav>

  <main>
    <section id="sobre-mi">
      <h2>Sobre mí</h2>
      <p>Mi nombre es <strong>[Tu nombre]</strong> y estudio <strong>HTML &amp; CSS</strong> porque me interesa la tecnología.</p>
      <p><em>Uno de mis objetivos</em> es aprender desarrollo web &lt;de verdad&gt;.</p>
      <img src="https://via.placeholder.com/200" alt="Foto de perfil" title="[Tu Nombre]">
    </section>

    <section id="aficiones">
      <h2>Mis aficiones</h2>
      <ul>
        <li>Leer sobre ciencia</li>
        <li>Practicar deportes</li>
        <li>Navegar por internet</li>
      </ul>
    </section>

    <article>
      <h2>Mi experiencia</h2>
      <p>Recuerdo la primera vez que escribí código en <strong>HTML</strong>. Fue emocionante ver el resultado en pantalla.</p>
      <p>Cometí errores y aprendí a usar entidades como &amp; y &copy;. Me gusta mejorar cada día.</p>
      <p><em>No hay límites para aprender cosas nuevas.</em></p>
      <p>La programación une creatividad y lógica &lt;¡es divertido!&gt;.</p>
      <p>Mi meta es desarrollar sitios accesibles para todos &copy; 2025.</p>
    </article>

    <section id="enlaces">
      <h2>Enlaces de interés</h2>
      <ul>
        <li><a href="https://developer.mozilla.org" target="_blank">MDN Web Docs</a></li>
        <li><a href="https://w3schools.com" target="_blank">W3Schools</a></li>
        <li><a href="https://github.com" target="_blank">GitHub</a></li>
      </ul>
    </section>
  </main>

  <footer>
    <p>&copy; 2025 [Tu Nombre]. Contacto: <a href="mailto:tucorreo@ejemplo.com">tucorreo@ejemplo.com</a></p>
  </footer>
</body>
</html>
```

***

**Checklist antes de entregar:**

- [ ] Estructura semántica completa y válida
- [ ] Enlaces internos y externos con ids y target correcto
- [ ] Uso de `<strong>`, `<em>`, imágenes con `alt`/`title`
- [ ] Lista de aficiones (mínimo tres items)
- [ ] `<article>` con relato real o imaginario
- [ ] Pie de página `<footer>` con entidad y correo
- [ ] Incluye mínimo tres entidades HTML
- [ ] Código limpio y bien indentado

***

¡Dedica los primeros minutos a planificar la estructura y luego completa cada apartado!