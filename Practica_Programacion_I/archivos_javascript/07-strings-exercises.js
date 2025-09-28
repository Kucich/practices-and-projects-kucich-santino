/*
Clase 22 - Ejercicios: Strings
Vídeo: https://youtu.be/1glVfFxj8a4?t=7226
*/

// 1. Concatena dos cadenas de texto

let nombre = "Santino"
let apellido = "Kucich"
let instituto = "I.S.P.I 4038"

console.log("Hola mi nombre es " + nombre + " y mi apellido es " + apellido + " y curso en el instituto " + instituto)


// 2. Muestra la longitud de una cadena de texto

console.log(nombre.length)

// 3. Muestra el primer y último carácter de un string

console.log(nombre[0], nombre[6])

// 4. Convierte a mayúsculas y minúsculas un string

console.log(apellido.toUpperCase())
console.log(instituto.toLowerCase())

// 5. Crea una cadena de texto en varias líneas

let datos_personales = `DNI: 45652029
DIRECCIÓN: JUJUY 1132
CIUDAD: ROLDÁN`

console.log(datos_personales)

// 6. Interpola el valor de una variable en un string

let texto = `Hola, soy el agente ${apellido} y estos son mis datos personales:\n${datos_personales}`

console.log(texto)

// 7. Reemplaza todos los espacios en blanco de un string por guiones

console.log(texto.replaceAll(" ", "-")) /* Use replaceALL te rellena todos lo que le indiques del string
si pones replace solo, solo reemplaza la primera coincidencia, en este ejmplo un solo espacio. */

// 8. Comprueba si una cadena de texto contiene una palabra concreta

console.log(texto.indexOf("Kucich"))

// 9. Comprueba si dos strings son iguales

console.log(nombre == apellido)

// 10. Comprueba si dos strings tienen la misma longitud

console.log(nombre.length == apellido.length)