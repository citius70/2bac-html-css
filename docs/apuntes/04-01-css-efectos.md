# Animaciones y transiciones CSS

***

## ¿Qué son?

Las **transiciones** y **animaciones** en CSS permiten que los cambios de estilo ocurran de manera suave y visualmente atractiva, en vez de forma instantánea. Son ideales para mejorar la experiencia del usuario y hacer la página más profesional y dinámica.

***

## Transiciones CSS

**Las transiciones** hacen que los cambios entre dos estados (por ejemplo, al poner el mouse encima de un botón) sean graduales.

### Ejemplo básico
```css
.boton {
  background: #379;
  color: #fff;
  transition: background 0.3s, transform 0.2s;
}
.boton:hover {
  background: #fa7;
  transform: scale(1.1);
}
```
**¿Qué ocurre?** El fondo cambia de color y el botón se agranda de forma suave al pasar el mouse.

**Propiedades clave:**
- `transition-property`: Qué propiedad se anima
- `transition-duration`: Cuánto dura
- `transition-timing-function`: Velocidad/interpolación (ej. `ease`, `linear`)
- `transition-delay`: Espera antes de comenzar

***

## Animaciones CSS

**Las animaciones** permiten crear movimientos y efectos más complejos, controlando varios pasos y repeticiones.

### Ejemplo básico
```css
.cuadro {
  width: 100px;
  height: 100px;
  background: #5ac;
  animation: mover 2s infinite alternate;
}

@keyframes mover {
  from { transform: translateX(0); }
  to { transform: translateX(200px); }
}
```
**¿Qué ocurre?** El cuadro se mueve suavemente de izquierda a derecha y vuelve.

**Propiedades clave:**
- `animation-name`: Nombre de la animación (`@keyframes`)
- `animation-duration`: Duración
- `animation-timing-function`: Interpolación
- `animation-iteration-count`: Número de repeticiones
- `animation-delay`: Espera antes de empezar
- `animation-direction`: Sentido, normal o alternando

***

## ¿Por qué usar animaciones y transiciones?

- Mejoran la experiencia del usuario.
- Destacan acciones importantes (ej: notificaciones).
- Hacen la web más atractiva y profesional.

***

**Consejo:**  
No abuses de las animaciones. Úsalas para reforzar interactividad y claridad visual, no para distraer.