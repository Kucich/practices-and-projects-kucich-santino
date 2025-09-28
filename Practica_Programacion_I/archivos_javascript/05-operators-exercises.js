/*
Clase 20 - Ejercicios: Operadores
Vídeo: https://youtu.be/1glVfFxj8a4?t=6458
*/

// 1. Crea una variable para cada operación aritmética

let a = 5
let b = 10

console.log(a + b)
console.log(a - b)
console.log(a * b)
console.log(a / b)
console.log(a ** b)

// 2. Crea una variable para cada tipo de operación de asignación,
//    que haga uso de las variables utilizadas para las operaciones aritméticas

let variable = 10
console.log(variable)
variable += 1
console.log(variable)
variable -= 1
console.log(variable)
variable *= 2
console.log(variable)
variable /= 2
console.log(variable)
variable **= 2
console.log(variable)
variable %= 2
console.log(variable)

// 3. Imprime 5 comparaciones verdaderas con diferentes operadores de comparación
// 4. Imprime 5 comparaciones falsas con diferentes operadores de comparación

// 5. Utiliza el operador lógico and

console.log(a != b && b == a)

// 6. Utiliza el operador lógico or
// 7. Combina ambos operadores lógicos

console.log(a != b && a == a || a != b || b == b)


// 8. Añade alguna negación

console.log(!(a))

// 9. Utiliza el operador ternario

let lluvia = false

lluvia ? console.log("Esta lloviendo"): console.log("No esta lloviendo") 

// 10. Combina operadores aritméticos, de comparáción y lógicas