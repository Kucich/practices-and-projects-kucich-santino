/*
Clase 24 - Ejercicios: Condicionales
Vídeo: https://youtu.be/1glVfFxj8a4?t=8652
*/

// if/else/else if/ternaria

// 1. Imprime por consola tu nombre si una variable toma su valor

let nombre = "Santino"

if (nombre == "Santino") {
    console.log(nombre)
} else{
    console.log("El nombre no coincide")
}

// 2. Imprime por consola un mensaje si el usuario y contraseña concide con unos establecidos

let contraseña = "12345"

if (nombre == "Santino" && contraseña == "12345"){
    console.log("Usuario encontrado.")
} else {
    console.log("Usuario no encontrado.")
}

// 3. Verifica si un número es positivo, negativo o cero e imprime un mensaje

let numero = 5

if (numero > 0){
    console.log("El numero es positivo.")
} else if (numero < 0){
    console.log("El numero es negativo.")
} else{
    console.log("El numero es cero.")
}

// 4. Verifica si una persona puede votar o no (mayor o igual a 18) e indica cuántos años le faltan

let edad = 20

if (edad >= 18){
    console.log("Puede votar.")
} else{
    console.log("No puede votar. Le faltan años.")
}

// 5. Usa el operador ternario para asignar el valor "adulto" o "menor" a una variable
//    dependiendo de la edad 

let edad_de_persona = 17

const persona = edad_de_persona >= 18 ? "Es un adulto" : "Es menor."
console.log(persona)

// 6. Muestra en que estación del año nos encontramos dependiendo del valor de una variable "mes"

let mes = "febrero"

if (mes == "julio" || mes == "junio" || mes == "agosto"){
    console.log("Estamos en invierno.")
} else if (mes == "diciembre" || mes == "enero" || mes == "febrero"){
    console.log("Estamos en verano.")
} else if (mes == "septiembre" || mes == "octubre" || mes == "noviembre"){
    console.log("Estamos en primavera")
} else{
    console.log("Estamos en otoño.")
}

// 7. Muestra el número de días que tiene un mes dependiendo de la variable del ejercicio anterior

if (mes == "enero" || mes == "marzo" || mes == "mayo" || mes == "julio" || mes == "agosto" || mes == "octubre" || mes == "diciembre"){
    console.log("Este mes tiene 31 días.")
} else if (mes == "abril" || mes == "junio" || mes == "septiembre" || mes == "noviembre"){ 
    console.log("Este mes tiene 30 días.")
} else {
    console.log("Este mes tiene 28 días")
}

// switch

// 8. Usa un switch para imprimir un mensaje de saludo diferente dependiendo del idioma

let idioma = "aleman"

switch (idioma){
    case "español":
        console.log("Hola")
        break

    case "ingles":
        console.log("Hello")
        break

    case "frances":
        console.log("Bonjour")
        break

    default:
        console.log("Idioma no registrado, así que: hola, hello, bonjour")
}

// 9. Usa un switch para hacer de nuevo el ejercicio 6

mes = "mayo"

switch (mes){
    case "enero":
        console.log("Estamos en verano.")
        break
    case "julio":
        console.log("Estamos en invierno.")
        break
    case "mayo":
        console.log("Estamos en otoño.")
        break
}

// 10. Usa un switch para hacer de nuevo el ejercicio 7

mes = "abril"

switch (mes){
    case "enero":
        console.log("Tiene 31 días.")
        break
    case "febrero":
        console.log("Tiene 28 días.")
        break
    case "abril":
        console.log("Tiene 30 días.")
        break
}