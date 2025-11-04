```markdown
# Ejercicios de CSS Grid

---

## 1. Centrar elementos en una cuadrícula

**Enunciado:**  
Crea un contenedor cuadrado con CSS Grid, inserta tres cajas y centra cada una en una celda diferente usando `place-items: center;`.

<details>
<summary>Solución</summary>

```
<style>
.grid-center {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-template-rows: 150px;
  gap: 20px;
  width: 80%;
  margin: auto;
  background: #f0f0f0;
  place-items: center;
}
.celda {
  background: #4fa;
  color: #123;
  font-weight: bold;
  width: 80px;
  height: 80px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 9px;
}
</style>
<div class="grid-center">
  <div class="celda">A</div>
  <div class="celda">B</div>
  <div class="celda">C</div>
</div>
```
</details>

---

## 2. Repartir espacio entre elementos en filas y columnas

**Enunciado:**  
Crea una cuadrícula de 1 fila y 3 columnas. Reparte tres botones ocupando el 100% de cada celda, en toda la pantalla, usando CSS Grid.

<details>
<summary>Solución</summary>

```
<style>
.grid-barra {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 10px;
  width: 100%;
}
.boton-grid {
  padding: 20px;
  background: #69c;
  color: #fff;
  border: none;
  font-size: 1em;
  border-radius: 7px;
  font-weight: bold;
  width: 100%;
}
</style>
<div class="grid-barra">
  <button class="boton-grid">Inicio</button>
  <button class="boton-grid">Servicios</button>
  <button class="boton-grid">Contacto</button>
</div>
```
</details>

---

## 3. Colocar un elemento en cualquier celda usando grid-area

**Enunciado:**  
Usa CSS Grid para hacer una cuadrícula 3x3 y coloca un ítem destacado exactamente en la posición de la tercera fila y segunda columna.

<details>
<summary>Solución</summary>

```
<style>
.panel {
  display: grid;
  grid-template-columns: repeat(3, 100px);
  grid-template-rows: repeat(3, 100px);
  gap: 12px;
  background: #fff4a3;
}
.item-panel {
  background: #8e44ad;
  color: #fff;
  border-radius: 8px;
  font-size: 1.2em;
  display: flex;
  align-items: center;
  justify-content: center;
}
.destacado {
  grid-area: 3 / 2 / 4 / 3; /* Fila inicial / columna inicial / fila final / columna final */
  background: #f33;
}
</style>
<div class="panel">
  <div class="item-panel">1</div>
  <div class="item-panel">2</div>
  <div class="item-panel">3</div>
  <div class="item-panel">4</div>
  <div class="item-panel">5</div>
  <div class="item-panel">6</div>
  <div class="item-panel"></div>
  <div class="item-panel destacado">¡Aquí!</div>
  <div class="item-panel"></div>
</div>
```
</details>
```