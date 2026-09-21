// Ejercicio 1
let nombre = document.getElementById("nombre");

// console.log(nombre.value)
function boton_nombre() {
    if (nombre.value) {
        console.log("Nombre registrado")
    } else {
        console.log("Debe ingresarse un valor.")
    }
}

// Ejercicio 2

let parrafo_mostrado = document.getElementById("parrafo_mostrado");

function ocultar_mostrar() {
    if (parrafo_mostrado.style.display == "block") {
        parrafo_mostrado.style.display = "none"
    } else {
        parrafo_mostrado.style.display = "block"
    }
}

// Ejercicio 3

let color_fondo = document.getElementById("color_fondo");

let cuerpo = document.getElementById("cuerpo")

function cambiar_color() {
    let color = color_fondo.value
    console.log(color)
    cuerpo.style.background = color
}

// Ejercicio 4

let incremento = 0

function incrementador() {
    incremento++; 
    document.getElementById("contador").textContent = incremento;
}

// Ejercicio 6

let parrafo_nuevo = document.getElementById("texto_ingresado");

function cambiar_parrafo() {
    document.getElementById("cambiado").textContent = parrafo_nuevo.value; 
}

// Ejercicio 7