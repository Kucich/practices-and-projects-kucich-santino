/*
Clase 32 - Ejercicios: Funciones
Vídeo: https://youtu.be/1glVfFxj8a4?t=14146
*/

// NOTA: Explora diferentes sintaxis de funciones para resolver los ejercicios

// 1. Crea una función que reciba dos números y devuelva su suma

function suma (a, b) {
    return `El resultado de la suma es: ${a + b}`
}

let resultado_suma = suma(20, 40)
console.log(resultado_suma)

// 2. Crea una función que reciba un array de números y devuelva el mayor de ellos

console.log("\nEjercicio 2\n")
let lista_numeros = [23, 1, 2, 3 , 0, -15, 6, 9, 10, 12, 15, 25, 30, 35, 5, 17, 29, 33]
let numeros_negativos = [-5, -12, -3, -40, -7, -1, -25]

function mayorArray (lista) {
    let mayor = lista[0]
    for (let numero of lista) {
        if (numero > mayor) {
            mayor = numero
        }
    }
    return mayor
}

let numero_mayor = mayorArray(numeros_negativos)
console.log(numero_mayor)

// 3. Crea una función que reciba un string y devuelva el número de vocales que contiene

console.log("\nEjercicio 3\n")
function vocales (cadena) {
    let contador_vocal = 0
    for (let vocal of cadena.toLowerCase()) {
        if ("aeiou".includes(vocal))
            contador_vocal ++
    }
    return `El numero de vocales del string es ${contador_vocal}`
}

let cadena_texto = "Hola a todos"
console.log(vocales(cadena_texto))

// 4. Crea una función que reciba un array de strings
// y devuelva un nuevo array con las strings en mayúsculas

console.log("\nEjercicio 4\n")
function listaStrings (array_strings) {
    let nuevo_array_strings = []
    for (let cadena of array_strings) {
        nuevo_array_strings.push(cadena.toUpperCase())
    }
    return nuevo_array_strings
}   

let array_cadena = ["hola", "mI", "nomBRe", "ES", "santino"]
console.log(listaStrings(array_cadena))

// 5. Crea una función que reciba un número y devuelva true si es primo, y false en caso contrario

console.log("\nEjercicio 5\n")

function primos(numero) {
    if (numero <= 1) {
        console.log(`${numero} no es primo.`);
        return false;
    }

    for (let i = 2; i < numero; i++) {
        if (numero % i === 0) {
            console.log(`${numero} no es primo (divisible por ${i}).`);
            return false;
        }
    }

    console.log(`${numero} es primo.`);
    return true;
}

primos(9);   // no es primo
primos(17);  // es primo


// 6. Crea una función que reciba dos arrays 
// y devuelva un nuevo array que contenga los elementos comunes entre ambos

console.log("\nEjercicio 6\n")
function nombresRepetidos (array1, array2) {
    let array3 = []
    for (let nombre1 of array1) { 
        if (array2.includes(nombre1)) {
            array3.push(nombre1)
        }
    }
    return array3
}

let nombres = ["Santino", "Macarena", "Kucich", "Sosa", "Salvador", "Luz", "Bosk"]
let nombres2 = ["Santino", "Macarena", "Emanuel", "Nazira", "Salvador", "Luz", "Rut"]
let nombres3 = nombresRepetidos(nombres, nombres2)
console.log(nombres3)

// 7. Crea una función que reciba un array de números y devuelva la suma de todos los números pares

console.log("\nEjercicio 7\n")
function sumaDePares (lista_de_numeros) {
    let sumatoria = 0
    for (let numerito of lista_de_numeros) {
        if (numerito % 2 == 0) {
            sumatoria = numerito + sumatoria 
        }
    }
    console.log(`La sumatoria de los numeros pares del array es ${sumatoria}`)
}

let lista_numeros2 = [23, 1, 2, 3 , 0, -15, 6, 9, 10, 12, 15, 25, 30, 35, 5, 17, 29, 33]
sumaDePares(lista_numeros2)

// 8. Crea una función que reciba un array de números 
// y devuelva un nuevo array con cada número elevado al cuadrado

console.log("\nEjercicio 8\n")
function arrayCuadrado (elevar_array) {
    let cuadrados = []
    for (let cuadrado of elevar_array) {
        cuadrados.push(cuadrado**2)
    }
    return cuadrados
}

let array4 = [2, 4, 8, 10]
let array_con_cuadrados = arrayCuadrado(array4)
console.log(array_con_cuadrados)

// 9. Crea una función que reciba una cadena de texto 
// y devuelva la misma cadena con las palabras en orden inverso

// console.log("\nEjercicio 9\n")
// const invertir = (cadena) => {
//     let cadena_lista = []
//     let cadena_invertida = []
//     for (let letra of cadena) {
//         cadena_lista.push(letra)
//     }
//     console.log(cadena_lista)

//     for (i = cadena_lista.length - 1; i < cadena.length; i--){
//         cadena_invertida.push(cadena_lista[i])
//         console.log(cadena_invertida)
//     }
// }

// let texto = "Hola a todos"
// invertir(texto)

// 10. Crea una función que calcule el factorial de un número dado

console.log("\nEjercicio factorial\n")
function factorial(n) {
    if (n === 0 || n === 1) {
        return 1
    }

    let resultado = 1
    for (let i = 2; i <= n; i++) {
        resultado *= i
    }
    return resultado
}

let numero = 5
console.log(`El factorial de ${numero} es: ${factorial(numero)}`)



