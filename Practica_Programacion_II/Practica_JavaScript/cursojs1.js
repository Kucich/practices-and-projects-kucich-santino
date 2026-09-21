// let numero_ingresado;
// let numero_ingresado2;
// let resultado_resta;

// numero_ingresado = prompt("Ingrese un número: ");
// numero_ingresado2 = prompt("Ingrese un segundo número: ");

// resultado_resta = numero_ingresado - numero_ingresado2

// if (resultado_resta > 0) {
//     console.log("Es mayor a 0")
//     if (resultado_resta % 2 == 0) {
//         console.log("Es par")
//     } else {
//         console.log("Es impar")
//     }

// } else {
//     console.log("Es menor o igual a 0")
// }

// Ejercicio 2

// for (let i = 10; i >= 0; i--) {
//     console.log(i);

//     if (i == 0) {
//         console.log("Feliz Año Nuevo");
//     }
// }


// Ejercicio 3

// let valor1 = window.prompt("Ingrese un valor númerico: ")
// let valor2 = window.prompt("Ingrese un segundo valor númerico: ")

// if (valor1 > valor2) {
//     alert("El primer valor es mayor: " + valor1)
// } else {
//     alert("El segundo valor es mayor: " + valor2)
// }


let fechaIngreso = prompt("Ingresa una fecha formato: mm/dd/yyyy");
alert(fechaIngreso)
let fecha = new Date(fechaIngreso);
let dia = fecha.getDay()
alert(fecha)
alert(dia)