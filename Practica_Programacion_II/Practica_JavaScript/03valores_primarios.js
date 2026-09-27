// undefined , no existe
// null , nulo, cuando tenes un espacio o sin valor "_"
// empty , vació, 
// NaN , Not a Number, estas comparando tipos de datos no numéricos

// Tipos de datos
// Int , Float , Bool , String

// Compraracion entre Js y Python

// Objetos Js 
// Arrays Js , Listas en Py

// Como crear un objeto

var objusuarios;


objusuarios = {
    nombre: "Santino",
    apellido: "Kucich",
    edad: 22,
    idiomas: ["Español", "Portugues", "Ingles", "Italiano"]
}

function imprimir () {

    document.getElementById("idiomas").innerText = objusuarios.idiomas;

}

// funcion anonima , metemos la funcion en una variable 
var saludo = function () { alert("hola mundo")}

// alert(saludo)
// alert(saludo())
// alert(typeof saludo)

let myfunction = function() {}
let myStang = "Hola mundo"
let myNumber = 21
let myDate = new Date()

console.log(typeof myNoexiste)

// alert emite un mensaje al usuario con un solo boton que es el de "ok"

// prompt le pide al usuario que ingrese alguna informacion
// ej: prompt("cual es tu nombre") y ahi aparece un cartel de cual es tu nombre, aparece un campo para ingresar texto y un boton de aceptar
// el prompt tiene que estar asignado a una variable para guardar el valor que ingrese

// confirm("Esta seguro que queres borarr?") le aparece al usuario una ventana con el mensaje y dos botones el de ok y el de cancelar
// tambien el confirm hay que guardarlo en una variable y es de tipo booleano

// if (!respuesta) significa si es false

// if (respuesta) significa que es true

