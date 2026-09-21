let lista_tareas = new Array()

function agregar_tarea() {
  let tarea_agregada = document.getElementById("tarea").value;
  lista_tareas.push(tarea_agregada);
  console.log(lista_tareas.length)
  let lista_html = document.getElementById("lista_tareas")
  
  lista_html.innerHTML += `<li>${tarea_agregada}</li>` + `<button onclick="eliminar_tarea(${tarea_agregada})">Elminar ítem</button>`;
}

