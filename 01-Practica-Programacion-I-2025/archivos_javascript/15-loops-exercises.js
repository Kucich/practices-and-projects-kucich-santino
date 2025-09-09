/*
Clase 30 - Ejercicios: Bucles
Vídeo: https://youtu.be/1glVfFxj8a4?t=12732
*/

// NOTA: Explora diferentes sintaxis de bucles para resolver los ejercicios

// 1. Crea un bucle que imprima los números del 1 al 20

for (let i = 1; i <= 20; i++) {
    console.log(i)
}

// 2. Crea un bucle que sume todos los números del 1 al 100 y muestre el resultado

console.log("\nEjercicio 2\n")
let contador = 0
let total = 0
while (contador != 100) {
    contador = contador + 1
    total = total + contador
    console.log(total)
    
    if (contador == 100) {
        console.log(`El total de la suma de los numeros es ${total}`)
        break
    }
}

// 3. Crea un bucle que imprima todos los números pares entre 1 y 50

console.log("\nEjercicio 3\n")
for (i = 1; i <= 50; i++) {
    if (i % 2 == 0) {
        console.log(i)
    }
}

// 4. Dado un array de nombres, usa un bucle para imprimir cada nombre en la consola

console.log("\nEjercicio 4\n")
let nombres = ["Santino", "Macarena", "Kucich", "Sosa"]

for (let nombre of nombres) {
    console.log(nombre)
}

// // 5. Escribe un bucle que cuente el número de vocales en una cadena de texto

console.log("\nEjercicio 5\n")
let texto = "Hola a todos, ¿como estan?. El otro dia hacia mucho frio."
let contador_vocal = 0

for (let vocal of texto.toLowerCase()){
    if (vocal == "a" || vocal == "e" || vocal == "i" || vocal == "o" || vocal == "u") {
        console.log(vocal)
        contador_vocal ++
    }
}
console.log(`El numero de vocales es ${contador_vocal}.`)

// 6. Dado un array de números, usa un bucle para multiplicar todos los números y mostrar el producto

console.log("\nEjercicio 6\n")
let numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
let producto = 1
let indice = 0
console.log("El producto del los diferentes elementos del array es: ")

for (i; i = numeros[indice]; indice ++) {
    producto = producto * i
    total = producto * i
    console.log(`${producto} * ${i} = ${total}`)
}

// La forma correcta es esta de abajo.

i = 0
producto = 1
for (i; i < numeros.length; i ++) {
    console.log(`${producto} * ${numeros[i]} = ${producto * numeros[i]}`);
    producto = producto * numeros[i];
}

console.log(`El producto de todos los números es: ${producto}`)


// 7. Escribe un bucle que imprima la tabla de multiplicar del 5

console.log("\nEjercicio 7\n")
producto = 0
for (i = 1; i <= 10; i ++) {
    producto = i * 5
    console.log(`5 x ${i} = ${producto}`)
}

// Tambien se puede hacer asi 

for (i = 1; i <= 10; i++) {
    console.log(`5 x ${i} = ${i * 5}`);
}

// 8. Usa un bucle para invertir una cadena de texto

console.log("\nEjercico 8\n")

let cadena = "ROMA"
let nueva_cadena = []
let cadena_definitiva = []
indice = 0
let ultima = 3

for (let letra of cadena) {
    nueva_cadena.push(letra)
}
nueva_cadena.reverse()
cadena = nueva_cadena.join("")
console.log(cadena)

// Otra forma, creo que la correcta, completar

for (i = cadena.length - 1; i < cadena.length; i --){}

// 9. Usa un bucle para generar los primeros 10 números de la secuencia de Fibonacci

console.log("\nEjercicio 9\n")
let f1 = 0
let f2 = 1
let f3 = 0
let f_contador = 0
// console.log(f1)
// console.log(f2)

while (f_contador < 10) {
    f3 = f1 + f2
    console.log(f3)
    f1 = f2 
    f2 = f3    
    f_contador ++
}

// 10. Dado un array de números, 
// usa un bucle para crear un nuevo array que contenga solo los números mayores a 10

console.log("\nEjercicio 10\n")
let lista_numeros = [23, 1, 2, 3 ,6, 9, 10, 12, 15, 25, 30, 35]
let nueva_lista_numeros = []
i = 0
for (i of lista_numeros) {
    if (i > 10) {
        nueva_lista_numeros.push(i)
    }
}

console.log(`La lista de numeros mayores a 10 es :\n${nueva_lista_numeros}`)