# Ejercicios de Flexbox

---

## 1. Centrar elementos horizontal y verticalmente

**Enunciado:**  
Crea un contenedor con tres cajas y usa flexbox para centrar todas las cajas en la pantalla (horizontal y vertical).

<details>
<summary>Solución</summary>

```
<style>
.contenedor {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 300px;
  background: #eee;
}
.caja {
  background: #379;
  color: #fff;
  width: 80px;
  height: 80px;
  margin: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-weight: bold;
}
</style>
<div class="contenedor">
  <div class="caja">A</div>
  <div class="caja">B</div>
  <div class="caja">C</div>
</div>
```
</details>

---

## 2. Repartir espacio entre elementos

**Enunciado:**  
Haz que tres botones se repartan todo el espacio horizontal disponible, ocupando el mismo ancho cada uno (responsive).

<details>
<summary>Solución</summary>

```
<style>
.barra {
  display: flex;
}
.boton {
  flex: 1;
  padding: 20px;
  background: #5ac;
  color: #fff;
  border: none;
  margin: 5px;
  font-size: 1em;
}
</style>
<div class="barra">
  <button class="boton">Inicio</button>
  <button class="boton">Servicios</button>
  <button class="boton">Contacto</button>
</div>
```
</details>

---

## 3. Cambiar dirección y orden de los elementos

**Enunciado:**  
Crea una lista vertical de cajas y haz que el tercer ítem se muestre en primer lugar utilizando la propiedad `order` de flexbox.

<details>
<summary>Solución</summary>

```
<style>
.lista {
  display: flex;
  flex-direction: column;
  gap: 10px;
  height: 220px;
}
.item {
  background: #fa7;
  color: #333;
  padding: 20px;
  font-weight: bold;
  border-radius: 7px;
}
.item.tercero {
  order: -1; /* Aparece primero */
}
</style>
<div class="lista">
  <div class="item">Primero</div>
  <div class="item">Segundo</div>
  <div class="item tercero">Tercero (ahora el primero visual)</div>
</div>
```
</details>