
# Módulo 5.2: Position

!!!notion "Position"
    La propiedad `position` controla **cómo se posiciona un elemento en la página**.
    Es esencial para crear layouts complejos y efectos avanzados.

### Static (por defecto)

```
position: static;
```

El elemento sigue el flujo normal del documento. Las propiedades `top`, `right`, `bottom`, `left` no tienen efecto.

### Relative

```
.elemento {
    position: relative;
    top: 20px;    /* Se desplaza 20px hacia abajo */
    left: 30px;   /* Se desplaza 30px hacia la derecha */
}
```

El elemento se desplaza **desde su posición original**, pero el espacio original se mantiene reservado. Otros elementos no se mueven.

**Cuándo usarlo:**
- Para ajustes pequeños de posición
- Como referencia para elementos `absolute` dentro de él

### Absolute

```
.elemento {
    position: absolute;
    top: 0;
    right: 0;
}
```

El elemento se posiciona respecto al **ancestro más cercano con `position` distinto de `static`** (normalmente un padre con `position: relative`). Se saca del flujo normal: otros elementos lo ignoran.

**Ejemplo común:**
```
<div style="position: relative;">
    <div style="position: absolute; top: 10px; right: 10px;">
        Insignia
    </div>
</div>
```

**Cuándo usarlo:**
- Tooltips, insignias, overlays
- Elementos decorativos
- Posicionamiento preciso dentro de un contenedor

### Fixed

```
.header {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
}
```

El elemento se posiciona respecto a la **ventana del navegador** y permanece fijo al hacer scroll.

**Cuándo usarlo:**
- Headers o menús de navegación fijos
- Botones flotantes (volver arriba, chat)
- Barras de notificaciones

### Sticky

```
.menu {
    position: sticky;
    top: 0;
}
```

El elemento es `relative` hasta que alcanza cierta posición al hacer scroll, entonces se vuelve `fixed`. Cuando su contenedor sale de la vista, deja de ser fijo.

**Cuándo usarlo:**
- Headers que se fijan al hacer scroll
- Menús de navegación de secciones

---
