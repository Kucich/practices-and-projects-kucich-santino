let variable = document.getElementById("superparrafo")

function desaparece() {

    if (variable.style.display == "none") {
        
        variable.style.display = "block"

    } else {
        variable.style.display = "none"
    }
}

// Ejercicio 2

let body = document.getElementById("cuerpo")
let color = document.getElementById("colores")

function color_fondo() {
    body.style.backgroundColor = color.value
}