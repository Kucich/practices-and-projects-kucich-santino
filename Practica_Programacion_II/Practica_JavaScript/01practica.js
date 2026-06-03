// Formas de escribir codigo js:
// En linea, Extenerno, Enbebido

// DOM : Documnet Object Mode

// El dom son objetos dentro de un documento(todo lo que esta dentro de la pagina es un objeto). Se pueden manipular todo lo que esta dentro del documento.


// Declaracion de variable
// var , let (Permite reasignar o asignar pero no puedo decalrarlas nuevamente), const

// Asignacion de variables
// x = 1 por ejemplo , una variable anteriormente declarada.

// Conceptos: 
// heritade : variable elevada, el navegador lee primero las variables var , solo las var. Esto es cuando se habla de variables elevadas.
// Scope : variables locales o globales, si estan dentro de una funcion o fuera de la funcion. Si una variable es global, y le asignas un valor dentro de una funcion, el valor sigue siendo global.




var txnombre; //declarada
txnombre = document.getElementById("campo"); //asignacion de valor del DOM, en este caso el input campo. En este caso la variable txnombre es un objetohtml , el valor del campo del formulario.

// alert(txnombre); Te muestra una pantalla en el sitio. Es lo mismo que el console.log, la diferencia es que el console.log aparece en la terminal y la ve el programador y el alert aparece en el sitio y lo ve el usuario.


// Funciones

function nombre () {
    txnombre.value = "hola mundo";

   
}

// function nombre () {
//     console.log("hola")
// }

// 

