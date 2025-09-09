/*
Clase 28 - Ejercicios: Estructuras
Vídeo: https://youtu.be/1glVfFxj8a4?t=11451
*/

// 1. Crea un array que almacene cinco animales

let lista = ["perro", "gato", "cebra", "cocodrilo", "panda"]
console.log(lista)

// 2. Añade dos más. Uno al principio y otro al final

lista.push("elefante")
console.log(lista)

lista.unshift("mono")
console.log(lista)

lista.pop()
lista.shift()
console.log(lista)

// 3. Elimina el que se encuentra en tercera posición


lista.splice(2, 1)
console.log(lista)

// 4. Crea un set que almacene cinco libros

let conjunto = new Set(["Harry", "Margen", "Hechos", "Mateo", "Genesis"])
console.log(conjunto)
console.log(typeof conjunto)

// 5. Añade dos más. Uno de ellos repetido

conjunto.add("Judas")
console.log(conjunto)

conjunto.add("Marcos")
console.log(conjunto)

conjunto.add("Marcos")
console.log(conjunto)

// 6. Elimina uno concreto a tu elección

conjunto.delete("Margen")
console.log(conjunto)

// 7. Crea un mapa que asocie el número del mes a su nombre

let mapa = new Map([ 
    [1, "enero"],
    [2, "febrero"],
    [3, "marzo"],
    [4, "abril"],
    [5, "mayo"],
    [6, "junio"],
    [7, "julio"],
    [8, "agosto"],
    [9, "septiembre"],
    [10, "octubre"],
    [11, "noviembre"],
    [12, "diciembre"]]
)
console.log(mapa)

// 8. Comprueba si el mes número 5 existe en el map e imprime su valor

console.log(mapa.has(5))
console.log(mapa.get(5))

// 9. Añade al mapa una clave con un array que almacene los meses de verano

mapa.set(13, ["enero", "febrero", "diciembre"])
console.log(mapa)

// 10. Crea un Array, transfórmalo a un Set y almacénalo en un Map

let lista2 = ["Santino", "Macarena", "Kucich", "Sosa"]

conjunto2 = new Set(lista2)
console.log(conjunto2)

mapa.set(14, conjunto2)
console.log(mapa)