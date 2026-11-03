// Crea las líneas de escribir de cada <div class="espacio" style="--lineas:n"></div> (n líneas vectoriales).
document.querySelectorAll('.espacio').forEach(function (e) {
  var n = parseInt(e.style.getPropertyValue('--lineas')) || 4;
  for (var i = 0; i < n; i++) { var d = document.createElement('div'); d.className = 'linea'; e.appendChild(d); }
});
