## 5.2. Position

!!!notion "Position"
    La propiedad `position` controla **cómo se posiciona un elemento en la página**.
    Es esencial para crear layouts complejos y efectos avanzados.

***

### Static (por defecto)

```css
position: static;
```

**Qué hace:** El elemento sigue el **flujo normal** del documento, colocándose uno tras otro según el orden del HTML.

**Comportamiento:**
- ❌ Las propiedades `top`, `right`, `bottom`, `left` **no tienen efecto**  
  - Estas propiedades desplazarían el elemnto de su posición original 
- ✅ Los márgenes y padding funcionan normalmente
- ✅ Es el comportamiento **por defecto** de todos los elementos (no necesitas escribirlo)   
- ✅ Los elementos se colocan **uno tras otro** en el flujo normal


**Sintaxis:**
```css
.elemento1 {position: static;}
.elemento2 {position: static;}
.elemento3 {position: static;}
/* ↓ Todos siguen el flujo natural */
```

**Ejemplo:**

=== "Código"
    ```html linenums="1" hl_lines="6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30"
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Ejemplo position: static</title>
        <style>
            .caja {
                width: 200px;
                height: 80px;
                margin: 10px;
                padding: 10px;
                border: 2px solid navy;
                text-align: center;
                line-height: 80px;
                font-weight: bold;
            }
            
            .caja2 {
                background-color: lightblue;
                position: static;  /* Por defecto (innecesario escribirlo) */
            }
            
            .caja2 {
                background-color: lightgreen;
                position: static;
            }
            
            .caja3 {
                background-color: lightyellow;
                position: static;
            }
            
            .intento {
                position: static;
                top: 50px;      /* ❌ NO TIENE EFECTO */
                left: 50px;     /* ❌ NO TIENE EFECTO */
                background-color: lightsalmon;
            }
        </style>
    </head>
    <body>
        <h2>position: static (Por defecto)</h2>
        
        <p>Los elementos siguen el flujo normal del documento, uno tras otro.</p>
        
        <div class="caja caja1">Caja 1 ✅</div>
        <div class="caja caja2">Caja 2 ✅</div>
        <div class="caja caja3">Caja 3 ✅</div>
        
        <h2>Intentando usar top y left con static</h2>
        <p>Las propiedades top y left NO tienen ningún efecto:</p>
        
        <div class="caja intento">Caja 4 </div>
        
        <!-- ✅ Los elementos siguen el flujo normal -->
    </body>
    </html>
    ```

=== "Resultado visual"
<div style= "background-color: #f5f5f5">
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Ejemplo position: static</title>
        <style>
            .caja {
                width: 200px;
                height: 80px;
                margin: 10px;
                padding: 10px;
                border: 2px solid navy;
                text-align: center;
                line-height: 80px;
                font-weight: bold;
            }
            
            .caja1 {
                background-color: lightblue;
                position: static;  /* Por defecto (innecesario escribirlo) */
            }
            
            .caja2 {
                background-color: lightgreen;
                position: static;
            }
            
            .caja3 {
                background-color: lightyellow;
                position: static;
            }
            
            .intento {
                position: static;
                top: 50px;      /* ❌ NO TIENE EFECTO */
                left: 50px;     /* ❌ NO TIENE EFECTO */
                background-color: lightsalmon;
            }
        </style>
</head>
<body>
    <h2>position: static (Por defecto)</h2>
    
    <p>Los elementos siguen el flujo normal del documento, uno tras otro.</p>
    
    <div class="caja caja1">Caja 1 ✅</div>
    <div class="caja caja2">Caja 2 ✅</div>
    <div class="caja caja3">Caja 3 ✅</div>
    
    <h2>Intentando usar top y left con static</h2>
    <p>Las propiedades top y left NO tienen ningún efecto:</p>
    
    <div class="caja intento">Caja 4 ❌</div>
    
    <!-- ✅ Los elementos siguen el flujo normal -->
</body>
</html>
</div>

**Puntos clave:**
- ✅ Los elementos se colocan **uno tras otro** en el flujo normal
- ❌ Las propiedades `top`, `right`, `bottom`, `left` **no funcionan** con `static`
- ✅ Es el comportamiento **por defecto** (no necesitas escribirlo)
- ✅ Los márgenes y padding funcionan normalmente





***

### Relative

```css
.elemento {
    position: relative;
    top: 20px;    /* Se desplaza 20px hacia abajo desde su posición original */
    left: 30px;   /* Se desplaza 30px hacia la derecha desde su posición original */
}
```

**Qué hace:** El elemento se desplaza **desde su posición original**, pero **el espacio original se mantiene reservado**.

**Comportamiento:**
- ✅ Se desplaza respecto a donde **debería estar normalmente**
- ✅ El espacio original sigue ocupado (otros elementos no se mueven)
- ✅ Usa `top`, `right`, `bottom`, `left` para desplazarlo
- ✅ Sirve como **referencia** para hijos con `position: absolute`

**Ejemplo visual:**
```
Elemento 1
[Espacio reservado]  ← Aquí debería estar el Elemento 2
Elemento 3

        Elemento 2 ← Desplazado 20px abajo, 30px derecha
```

**Cuándo usarlo:**
- Para ajustes pequeños de posición sin afectar otros elementos
- Como **contenedor de referencia** para elementos `absolute` dentro de él
- Para crear efectos hover con desplazamiento

***

### Absolute

```css
.elemento {
    position: absolute;
    top: 0;
    right: 0;
}
```

**Qué hace:** El elemento se posiciona respecto al **ancestro más cercano con `position` distinto de `static`** (normalmente un padre con `position: relative`). Se **saca del flujo normal**: otros elementos lo ignoran.

**Comportamiento:**
- 🚀 Se **sale del flujo normal** (otros elementos ocupan su espacio)
- ✅ Se posiciona respecto al **padre con position** (o `<body>` si no hay)
- ✅ Usa `top`, `right`, `bottom`, `left` para colocarlo exactamente
- ⚠️ Los demás elementos actúan como si no existiera

**Ejemplo visual:**
```
Contenedor (position: relative)
┌─────────────────────────────────┐
│                        [Insignia]│ ← absolute (top:10px, right:10px)
│                                  │
│  Elemento 1                      │
│  Elemento 2                      │
│  Elemento 3                      │
└──────────────────────────────────┘
```

**Ejemplo común:**
```html
<div style="position: relative; width: 300px; height: 200px; background: lightblue;">
    <div style="position: absolute; top: 10px; right: 10px; background: red; padding: 5px;">
        Insignia
    </div>
    Contenido principal...
</div>
```

**Cuándo usarlo:**
- Tooltips, insignias, overlays
- Elementos decorativos que flotan sobre el contenido
- Posicionamiento preciso dentro de un contenedor
- Menús desplegables 

***

### Resumen de diferencias

| Tipo | ¿Sale del flujo? | ¿Respecto a qué se posiciona? | Espacio reservado |
|------|------------------|-------------------------------|-------------------|
| **static** | ❌ No | Flujo normal | ✅ Sí |
| **relative** | ❌ No | Su posición original | ✅ Sí (mantiene su espacio) |
| **absolute** | ✅ Sí | Ancestro con position o `<body>` | ❌ No (otros elementos lo ignoran) |