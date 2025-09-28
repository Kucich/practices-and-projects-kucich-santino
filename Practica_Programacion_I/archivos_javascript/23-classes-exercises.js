/*
Clase 39 - Ejercicios: Clases
Vídeo: https://youtu.be/1glVfFxj8a4?t=18630
*/

// 1. Crea una clase que reciba dos propiedades

class Estudiante {
    constructor (nombre, materia) {
        this.nombre = nombre
        this.materia = materia
    }

    propiedad () {
        console.log(`El estudiante se llama ${this.nombre} y esta estudaindo ${this.materia}`)
    }

    static recibir_nota (nombre, nota) {
        return `La nota del estudiante ${nombre} fue: ${nota}`
    }
}

// 2. Añade un método a la clase que utilice las propiedades

// 3. Muestra los valores de las propiedades e invoca a la función

// 4. Añade un método estático a la primera clase

// 5. Haz uso del método estático


let santino = new Estudiante ("Santino", "Programación")
santino.propiedad()
console.log(Estudiante.recibir_nota(santino.nombre, 10))


// 6. Crea una clase que haga uso de herencia

class Pasante extends Estudiante {
    constructor(origen) {
        super(this.nombre, this.materia)

        this.origen = origen
    }
}

// 7. Crea una clase que haga uso de getters y setters

// 8. Modifica la clase con getters y setters para que use propiedades privadas

// 9. Utiliza los get y set y muestra sus valores

class ObtenerEstablecer {
    #cuenta
    #contraseña
    constructor (cuenta, contraseña, usuario) {
        this.#cuenta = cuenta
        this.#contraseña = contraseña
        this.usuario = usuario
    }

    get cuenta () {
        return this.#cuenta
    }

    get contraseña () {
        return this.#contraseña
    }
    set contraseña(new_password) {
        this.#contraseña = new_password
    }

}

let usuario1 = new ObtenerEstablecer(2134, 2004, "Hallen")
console.log(usuario1.usuario)
console.log(usuario1.cuenta)

console.log(usuario1.contraseña)
usuario1.contraseña = "santi2004"
console.log(usuario1.contraseña)


// 10. Sobrescribe un método de una clase que utilice herencia 

class Alumno extends Estudiante {
    constructor (nombre, materia, numero) {
        super(nombre, materia)

        this.numero = numero
    }

    propiedad () {
        console.log("Los alumnos estudian " + this.materia)
    }


}

let macarena = new Estudiante("Macarena", "Estadistica")
macarena.propiedad()

let Santi = new Alumno("San", "Ing de Software",33)
Santi.propiedad()