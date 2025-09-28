/*
Clase 18 - Ejercicios: primeros pasos
Vídeo: https://youtu.be/1glVfFxj8a4?t=4733
*/

// 1. Escribe un comentario en una línea

// Mi primer comentario en js

// 2. Escribe un comentario en varias líneas

/* Comentando
en varias
líneas
*/

// 3. Declara variables con valores asociados a todos los datos de tipo primitivos

let cadena = "Santi esta aprendiendo js."

let numero = 30
let numero2 = 1.50

let booleanoV = true
let booleanoF = false

let indefinido

let nulo = null

let simbolo = Symbol("Este es un simbolo.")

let gran_entero = BigInt(100000000000000000000000)

// 4. Imprime por consola el valor de todas las variables

console.log(cadena)
console.log(numero)
console.log(numero2)
console.log(booleanoV)
console.log(booleanoF)
console.log(indefinido)
console.log(nulo)
console.log(simbolo)
console.log(gran_entero)

// 5. Imprime por consola el tipo de todas las variables

console.log(typeof cadena)
console.log(typeof numero)
console.log(typeof numero2)
console.log(typeof booleanoV)
console.log(typeof booleanoF)
console.log(typeof indefinido)
console.log(typeof nulo)
console.log(typeof simbolo)
console.log(typeof gran_entero)

// 6. A continuación, modifica los valores de las variables por otros del mismo tipo


cadena = "Santi esta aprendiendo js. Desde 0"

numero = 3000

// 7. A continuación, modifica los valores de las variables por otros de distinto tipo

cadena = 250

numero = "Papas con pure."

// 8. Declara constantes con valores asociados a todos los tipos de datos primitivos

const cadena3 = "Hola a todos, ¿comó estan?"

const numero3 = 560

// 9. A continuación, modifica los valores de las constantes

// cadena3 = 300

// numero3 = "Hola y adios" No se pueden modificar constantes...

// 10. Comenta las líneas que produzcan algún tipo de error al ejecutarse

console.log(cadena)
console.log(numero)
