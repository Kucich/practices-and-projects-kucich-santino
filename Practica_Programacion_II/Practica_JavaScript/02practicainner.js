let variable;
let contenedor2;

let nombre;
let apellido;
let opinion;
let selector;

nombre = document.getElementById("nombre");
apellido = document.getElementById("apellido");
opinion = document.getElementById("textoarea");
selector = document.getElementById("select")

let contenido_genero = document.getElementById("contenido-genero")

function validar_campos() {

    if (nombre.value != "") {
        alert("ok");
    } 
    
    else {
        alert("Completar con su nombre");
        nombre.focus();
        return false;
    }

    if (apellido.value != "") {
        alert("ok");
    } 
    
    else {
        alert("Completar con su apellido");
        apellido.focus();
        return false;
    }

    if (selector.value == "Masculino") {
        alert("Masculino")
    } 
    
    else if (selector.value == "Femenino") {
        alert("Femenino")
    }

    else {
        alert("Seleccione su genero");
        selector.focus();
        return false;
    }

}

function agregar_profesiones() {

    if (selector.value == "Masculino") {
        contenido_genero.innerHTML = `<label>Seleccione su profesión</label>
        <select>
            <option value="s" selected disabled>Seleccionar</option>
            <option value="h">Herrero</option>
            <option value="s">Soldador</option>
            <option value="c">Carpintero</option>
        </select>`
    } 
    
    else if (selector.value == "Femenino") {
        
        contenido_genero.innerHTML = `<label>Seleccione su profesión</label>
        <select>
            <option value="s" selected disabled>Seleccionar</option>
            <option value="h">Administrativa</option>
            <option value="s">Docente</option>
            <option value="c">Jardinera</option>
        </select>`
    }
}


variable = document.getElementById("contenedor");
contenedor2 = document.getElementById("contenedor2");

function apretar() {
    variable.innerText = "Lo que queiras";
}

function cambiar_texto() {
    contenedor2.innerHTML = "<b>Pepaso</b>"
}



