/*
Clase 36 - Ejercicios: Desestructuración y propagación
Vídeo: https://youtu.be/1glVfFxj8a4?t=16802
*/

let lista = ["perro", "gato", "cebra", "cocodrilo", "panda"]

let conjunto = new Set(["Harry", "Margen", "Hechos", "Mateo", "Genesis"])

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

// 1. Usa desestructuración para extraer los dos primeros elementos de un array 

let [valor1, valor2] = lista
console.log(valor1, valor2)

// 2. Usa desestructuración en un array y asigna un valor predeterminado a una variable

console.log("\nEjercicio 2\n")
let [valor3, valor4, valor5, valor6, valor7, valor8 = 0] = lista

console.log(valor3)
console.log(valor4)
console.log(valor5)
console.log(valor6)
console.log(valor7)
console.log(valor8)


// 3. Usa desestructuración para extraer dos propiedades de un objeto

console.log("\nEjercicio 3\n")

let objeto = {
    nombre: "Santino",
    edad: 21,
    email: "kucihs777@gmail.com",
    telefono: 3413245568
}

let { nombre, edad } = objeto
console.log(nombre)
console.log(edad)


// 4. Usa desestructuración para extraer dos propiedades de un objeto y asígnalas
//    a nuevas variables con nombres diferentes

console.log("\nEjercicio 4\n")
let {nombre: value1, edad: value2, email: value3} = objeto
console.log(value1)
console.log(value2)
console.log(value3)

// 5. Usa desestructuración para extraer dos propiedades de un objeto anidado

console.log("\nEjercicio 5\n")

let objeto2 = {
    nombre: "Santino",
    edad: 21,
    email: "kucihs777@gmail.com",
    telefono: 3413245568,
    objeto3: {
        trabajo: "programador",
        experiencia: 2,
        empresa: "Tera"
    }
}

let {objeto3: {empresa: nombre_empresa}, objeto3: {trabajo: job}} = objeto2

console.log(nombre_empresa, job)


// 6. Usa propagación para combinar dos arrays en uno nuevo

console.log("\nEjercicio 6\n")
let array1 = [1, 2, 3]
let array2 = [4, 5 ,6]
let array3 = [...array1, ...array2]
console.log(array3)

// 7. Usa propagación para crear una copia de un array

console.log("\nEjercicio 7\n")
let array4 = [...array3]
console.log(array4)

// 8. Usa propagación para combinar dos objetos en uno nuevo

console.log("\nEjercicio 8\n")
let object1 = {
    name: "Santi",
    age: 21,
    job: "Profesor"
}

let object2 = {
    carrera: "Programador",
    institucion: "ISPI 4038"
}

let object3 = {...object1, ...object2}
console.log(object3)

// 9. Usa propagación para crear una copia de un objeto

let object4 = {...object1}
console.log(object4)

// 10. Combina desestructuración y propagación

console.log("\nEjercicio 10\n")

objeto2 = {
    nombre: "Santino",
    edad: 21,
    email: "kucihs777@gmail.com",
    telefono: 3413245568,
    objeto3: {
        trabajo: "programador",
        experiencia: 2,
        empresa: "Tera"
    }
}

let {nombre: name1, objeto3: {trabajo: trabajo1}} = objeto2

let objeto4 = {name1, trabajo1}
console.log(objeto4)

let objeto5 = {...objeto4, fecha: "10/07/2025", año: 2025}
console.log(objeto5)
