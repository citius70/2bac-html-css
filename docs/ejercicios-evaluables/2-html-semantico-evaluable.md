# Ejercicio evaluable: HTML semántico

## 🎯 Objetivo

T**ransformar la página creada en el ejercicio anterior para que use etiquetas semánticas de HTML5**, mejorando la estructura y accesibilidad del contenido.

## Nombre archivo:

Entregar el archivo actualizado con el nombre `index.html`.

## 📋 Requisitos del proyecto

### Uso de etiquetas semánticas

- Reemplazar todas las etiquetas genéricas (`<div>`, `<section>`, `<article>`) por las adecuadas:
  - `<header>` para cabecera
  - `<nav>` para navegación
  - `<main>` para contenido principal
  - `<section>` para dividir contenido en bloques temáticos
  - `<article>` para bloques de contenido independientes (si aplica)
  - `<footer>` para pie de página

### Estructura y jerarquía

- Mantener la estructura jerárquica de encabezados `<h1>`, `<h2>`, `<h3>`.
- Añadir `aria` y atributos de accesibilidad si fuera necesario para mejorar el lector de pantalla.

### Contenido

- **Mantener todo el contenido** del ejercicio previo.
- **Incorporar los cambios** en las etiquetas para aprovechar las etiquetas semánticas y mejorar la accesibilidad y el significado del documento.

### Comentarios

- Añadir comentarios en el código HTML que expliquen cada sección semántica.

***

# Recomendaciones

- Reemplaza los `<div>` por `<header>`, `<nav>`, `<section>`, `<footer>`, etc.
- Organiza correctamente la jerarquía de los encabezados.
- Mantén la estructura intacta, solo cambia las etiquetas para hacerla más semántica.
- Valida tu página en [validator.w3.org](https://validator.w3.org/) para corregir errores y asegurar compatibilidad.

***

Aquí tienes un ejemplo simple para empezar, basándote en el esquema del ejercicio anterior:

```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Mi Perfil - [Tu Nombre]</title>
</head>
<body>

<header>
  <h1>[Tu Nombre]</h1>
  <p>[Tu especialidad]</p>
</header>

<nav>
  <ul>
    <li><a href="#sobre-mi">Sobre mí</a></li>
    <li><a href="#habilidades">Habilidades</a></li>
    <li><a href="#intereses">Intereses</a></li>
    <li><a href="#enlaces">Enlaces</a></li>
  </ul>
</nav>

<main>
  <section id="sobre-mi">
    <h2>Sobre mí</h2>
    <!-- Contenido -->
  </section>
  <section id="habilidades">
    <h2>Habilidades</h2>
    <!-- Contenido -->
  </section>
  <section id="intereses">
    <h2>Intereses</h2>
    <!-- Contenido -->
  </section>
  <section id="enlaces">
    <h2>Enlaces de interés</h2>
    <!-- Contenido -->
  </section>
</main>

<footer>
  <p>&copy; 2025 [Tu Nombre]. Todos los derechos reservados.</p>
</footer>

</body>
</html>
```

***

