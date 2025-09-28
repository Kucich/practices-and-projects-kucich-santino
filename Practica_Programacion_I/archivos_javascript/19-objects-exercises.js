/*
Clase 34 - Ejercicios: Objetos
Vídeo: https://youtu.be/1glVfFxj8a4?t=15675
*/

// 1. Crea un objeto con 3 propiedades

let objeto = {
    nombre: "Santino",
    edad: 21,
    email: "kucihs777@gmail.com",
    telefono: 3413245568
}

// 2. Accede y muestra su valor

console.log("\nEjercicio 2\n")
console.log(objeto.nombre)
console.log(objeto.edad)
console.log(objeto.email)
console.log(objeto.telefono)

// 3. Agrega una nueva propiedad

console.log("\nEjercicio 3\n")
objeto.dni = 45654548
console.log(objeto.dni)
console.log(objeto)

// 4. Elimina una de las 3 primeras propiedades

console.log("\nEjercicio 4\n")
delete objeto.telefono
console.log(objeto)

// 5. Agrega una función e invócala

console.log("\nEjercicio 5\n")
objeto.saludar = function () {
    console.log(`Hola mi nombre es ${this.nombre}`)
}

console.log(objeto)
objeto.saludar()

// 6. Itera las propiedades del objeto

console.log("\nEjercicio 6\n")
for (let key in objeto) {
    console.log(key + ": " + objeto[key])
}

// 7. Crea un objeto anidado

console.log("\nEjercicio 7\n")
objeto.objeto2 = {
    trabajo: "programador",
    experiencia: 2,
    empresa: "Tera"
}

console.log(objeto)
console.log(objeto.objeto2)


// 8. Accede y muestra el valor de las propiedades anidadas

console.log("\nEjercicio 8\n")
console.log(objeto.objeto2.trabajo)
console.log(objeto.objeto2.empresa)
console.log(objeto.objeto2.experiencia)

// 9. Comprueba si los dos objetos creados son iguales

console.log("\nEjercicio 9\n")
console.log(objeto == objeto.objeto2)
console.log(objeto === objeto.objeto2)

// 10. Comprueba si dos propiedades diferentes son iguales

console.log("\nEjercicio 10\n")
console.log(objeto.nombre == objeto.edad)
console.log(objeto.nombre === objeto.edad)

console.log(objeto.dni == objeto.edad)
console.log(objeto.dni === objeto.edad)

console.log(objeto == objeto)
console.log(objeto.nombre == objeto.nombre)
console.log(objeto.nombre === objeto.nombre)

