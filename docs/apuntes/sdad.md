<style>
.parent {
    display: grid;
    grid-template-columns: 2fr 1fr 4fr 1fr;
    grid-template-rows: 1fr 2fr 4fr 1fr;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    width: 600px;
    height: 450px;
    border: 2px solid #333;
}
.div1   { grid-area: 1 / 1 / 2 / 2; background: #ffadad; }
.div2   { grid-area: 1 / 2 / 2 / 3; background: #ffd6a5; }
.div3   { grid-area: 1 / 3 / 2 / 4; background: #fdffb6; }
.div4   { grid-area: 1 / 4 / 2 / 5; background: #caffbf; }
.div5   { grid-area: 2 / 1 / 3 / 2; background: #9bf6ff; }
.div6   { grid-area: 2 / 2 / 3 / 3; background: #a0c4ff; }
.div7   { grid-area: 2 / 3 / 3 / 4; background: #bdb2ff; }
.div8   { grid-area: 2 / 4 / 3 / 5; background: #ffc6ff; }
.div9   { grid-area: 3 / 1 / 4 / 2; background: #f1c6e7; }
.div10  { grid-area: 3 / 2 / 4 / 3; background: #c2f6c5; }
.div11  { grid-area: 3 / 3 / 4 / 4; background: #dad7cd; }
.div12  { grid-area: 3 / 4 / 4 / 5; background: #ffb4a2; }
.div13  { grid-area: 4 / 1 / 5 / 2; background: #b7e4c7; }
.div14  { grid-area: 4 / 2 / 5 / 3; background: #f7d6e0; }
.div15  { grid-area: 4 / 3 / 5 / 4; background: #b5ead7; }
.div16  { grid-area: 4 / 3 / 5 / 4; background: #cfbaf0; }
.div17  { grid-area: 4 / 4 / 5 / 5; background: #d0f4de; }
.div18  { grid-area: 4 / 4 / 5 / 5; background: #bdb2ff; }
.parent > div {
    border: 1px solid #444;
    /* display: flex; */
    align-items: center;
    justify-content: center;
    font-weight: bold;
    font-family: sans-serif;
    font-size: 1em;
    min-width: 0;
    min-height: 0;
}
</style>
<div class="parent">
    <div class="div1">1</div>
    <div class="div2">2</div>
    <div class="div3">3</div>
    <div class="div4">4</div>
    <div class="div5">5</div>
    <div class="div6">6</div>
    <div class="div7">7</div>
    <div class="div8">8</div>
    <div class="div9">9</div>
    <div class="div10">10</div>
    <div class="div11">11</div>
    <div class="div12">12</div>
    <div class="div13">13</div>
    <div class="div14">14</div>
    <div class="div15">15</div>
    <div class="div16">16</div>
    <div class="div17">17</div>
    <div class="div18">18</div>
</div>




