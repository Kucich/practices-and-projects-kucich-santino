// let numero = 0

// if (numero > 0){
//     console.log("El numero es positivo.")
// } else if (numero < 0){
//     console.log("El numero es negativo.")
// } else{
//     console.log("El numero es cero.")
// }

// let contraseña = "12345"
// let nombre = "Santino"

// if (nombre == "Santino" && contraseña == "12345"){
//     console.log("Usuario encontrado.")
// } else {
//     console.log("Usuario no encontrado.")
// }



// if (nombre == "Santino") {
//     console.log(nombre)
// } else{
//     console.log("El nombre no coincide")
// }

// MODULO
// let letra
// let texto = "Hola a todos como estan"
// for (letra of texto) {
//     console.log(letra)
// }

// let numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
// let producto = 1
// let indice = 0
// let i = 0
// for (i; i = numeros[indice]; indice ++) {
//     console.log(i) 
// }

function factorial(n) {
    if (n === 0 || n === 1) {
        return 1
    }

    let resultado = 1
    for (let i = 2; i <= n; i++) {
        resultado *= i
        //console.log(i)
        console.log(resultado)
    }
    return resultado
}

console.log("\nEjercicio factorial\n")
let numero = 5
console.log(`El factorial de ${numero} es: ${factorial(numero)}`)
