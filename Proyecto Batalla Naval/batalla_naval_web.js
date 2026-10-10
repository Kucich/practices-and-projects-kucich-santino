/* --------------------------------------------------
   Reglas básicas de la batalla naval:
    Cada jugador tiene una grilla 5x5.
    Coloca sus barcos en casilla 3 barcos por jugador).
    Los barcos ocupan una.
    Los jugadores se turnan para “tirar bombas” en coordenadas de la grilla del rival.
    En la grilla: 0 casilla vacia, 1 = barco, 2 = impacto, 3 = agua
    Si aciertan, esa casilla se marca como “impacto”; si fallan, como “agua”.
    Gana quien destruye todos los barcos del otro. 
    --------------------------------------------------
*/ 

// Funciones

function ubicarBarcosJugador(filaSeleccionada, columnaSeleccionada, boton) {
    /* Se ingresan los datos de ubicación, se validan y se coloca en la grilla.  */
    const jugador = 0;

    if (validarFilaColumna(filaSeleccionada, columnaSeleccionada, jugador)) {
        grillaJugador[filaSeleccionada][columnaSeleccionada] = 1
        boton.style.backgroundColor = "rgb(8, 111, 3)"
        console.log(grillaJugador);
    };
};

function ubicarBarcosMaquina() {
    /* Se eligen posiciones al azar para ubicar en la grilla de la maquina */
    const maquina = 1
    let contadorBarcosMaquina = 0

    while(contadorBarcosMaquina < barcosDisponibles) {
        /* Math.random devuelve un número decimal entre 0 y 1 (ejemplo: 0.2345).
           Para obtener un número entero en un rango, combinás con Math.floor(). */
        let filaMaquina = Math.floor(Math.random() * 5); // entero entre 0 y 4
        let columnaMaquina = Math.floor(Math.random() * 5); // entero entre 0 y 4
        if (validarFilaColumna(filaMaquina, columnaMaquina, maquina)) {
            grillaMaquina[filaMaquina][columnaMaquina] = 1
            contadorBarcosMaquina += 1
        };
    };
    console.log(grillaMaquina);
};

function validarFilaColumna(fila, columna, grilla) {    
    /* Valido que fila y columna ingresados esten entre 0 y 4.
       Luego verifico que el lugar seleccionado no este ocupado. */

    if (grilla === 0 && grillaJugador[fila][columna] === 1) {
        informacionDinamica.textContent = "Casilla ya ocupada por un barco. Intente con otra.";
        barcosJugador -= 1
        return false

    } else if (grilla === 0){
        return true

    } else if (grilla === 1 && grillaMaquina[fila][columna] === 1) {
        informacionDinamica.textContent = "La maquina intento una combinación ya utilizada.";
        return false

    } else if (grilla === 1) {
        return true
    };
};

function disparoJugador(filaAtacada, columnaAtacada, boton) {
    /*Seleccionamos la posición en la que realizamos el disparo.*/
    tituloGanador.textContent = "Turno de la Máquina";
    tituloGanador.style.color = "rgb(209, 2, 2)";
    switch (grillaMaquina[filaAtacada][columnaAtacada]) {
    /*Verifico la posición a la que se disparo y ejecuto 
      una acción depende el valor de la posición */
    case 0:
        informacionDinamica.textContent = "¡AGUA! Disparo errado.";
        informacionDinamica.style.color = "rgb(0, 189, 195)";
        grillaMaquina[filaAtacada][columnaAtacada] = 3;
        boton.style.backgroundColor = "rgb(0, 0, 48)";
        break;

    case 1:
        informacionDinamica.textContent = "¡EN EL BLANCO! Barco Destruido.";
        informacionDinamica.style.color = "rgb(16, 230, 30)";
        grillaMaquina[filaAtacada][columnaAtacada] = 2;
        boton.style.backgroundColor = "rgb(55, 2, 2)";
        contadorBarcosMaquina -= 1;
        actualizarInformacion();
        break;

    default:
        informacionDinamica.textContent = "¡Ya disparaste a esta posición! Perdiste el turno.";
        informacionDinamica.style.color = "rgb(240, 84, 22)";
        break;
    };
    console.log("GRILLA DE LA MÁQUINA:")
    console.log(grillaMaquina);
    let cont = contarBarcos(grillaMaquina)
    console.log("Barcos de la Máquina: " + cont);
};

function disparoMaquina() {
    /*La máquina realiza sus disparos en las posiciones seleccionadas.*/
    let filaAtacada = Math.floor(Math.random() * 5); // entero entre 0 y 4
    let columnaAtacada = Math.floor(Math.random() * 5); // entero entre 0 y 4
    tituloGanador.textContent = "Turno del Jugador";
    tituloGanador.style.color = "rgb(16, 230, 30)";
    let botonJugador = tablaJugador.querySelector(
        `[data-fila="${filaAtacada}"][data-columna="${columnaAtacada}"]`
        );
    switch (grillaJugador[filaAtacada][columnaAtacada]) {
        /*Verifico la posición a la que se disparo y ejecuto 
            una acción depende el valor de la posición*/
        case 0:
            informacionDinamica.textContent = "La Máquina dio en el AGUA.";
            informacionDinamica.style.color = "rgb(0, 189, 195)";
            grillaJugador[filaAtacada][columnaAtacada] = 3;
            botonJugador.style.backgroundColor = "rgb(0, 0, 48)";
            break;

        case 1:
            informacionDinamica.textContent = "¡LA MÁQUINA DIO EN EL BLANCO! Barco Destruido.";
            informacionDinamica.style.color = "rgb(209, 2, 2)";
            grillaJugador[filaAtacada][columnaAtacada] = 2;
            botonJugador.style.backgroundColor = "rgb(55, 2, 2)";
            contadorBarcosJugador -= 1;
            actualizarInformacion();
            break;

        default:
            informacionDinamica.textContent = "La Máquina disparo en un lugar que ya habia elegido. Dispara de nuevo.";
            informacionDinamica.style.color = "rgb(232, 200, 17)";
            disparoMaquina();
    };
    console.log("GRILLA DEL JUGADOR:")
    console.log(grillaJugador);
    let cont = contarBarcos(grillaJugador)
    console.log("Barcos del Jugador: " + cont);
};

function contarBarcos(grilla) {
    /*flat() aplana la grilla 5x5 en un solo array.
    filter(c => c === 1) se queda solo con barcos.
    .length te da la cantidad.*/
    return grilla.flat().filter(contador => contador === 1).length;
};

function definirGanador() {
    /* Se evalua los barcos de cada jugador y se define el ganador o empate. */
    if(contarBarcos(grillaJugador) === 0 || contarBarcos(grillaMaquina) === 0) {

        if(contarBarcos(grillaJugador) === 0 && contarBarcos(grillaMaquina) === 0) {
            tituloGanador.style.color = "rgb(214, 224, 16)"
            tituloGanador.textContent = "¡Los barcos de ambos bandos fueron destruidos! La guerra no tiene ganadores...";

        } else if(contarBarcos(grillaJugador === 0)){
            tituloGanador.style.color = "rgb(186, 3, 3)"
            tituloGanador.textContent = "Todos las barcos del Jugador fueron destruidos. ¡La Maquina gana!";

        } else if(contarBarcos(grillaMaquina) === 0) {
            tituloGanador.style.color = "rgb(9, 196, 9)"
            tituloGanador.textContent = "Todos las barcos de la Maquina fueron destruidos. ¡El Jugador gana!";
        };
    };
};

function DOMcrearGrillas(idContenedor, titulo, id) {
    const espacio = document.getElementById(idContenedor);

    espacio.innerHTML = `
        <h2 class="titulo">${titulo}</h2>
        <table id="${id}">
            <tr>
                <td><button class="casillas" data-fila="0" data-columna="0"></button></td>
                <td><button class="casillas" data-fila="0" data-columna="1"></button></td>
                <td><button class="casillas" data-fila="0" data-columna="2"></button></td>
                <td><button class="casillas" data-fila="0" data-columna="3"></button></td>
                <td><button class="casillas" data-fila="0" data-columna="4"></button></td>
            </tr>
            <tr>
                <td><button class="casillas" data-fila="1" data-columna="0"></button></td>
                <td><button class="casillas" data-fila="1" data-columna="1"></button></td>
                <td><button class="casillas" data-fila="1" data-columna="2"></button></td>
                <td><button class="casillas" data-fila="1" data-columna="3"></button></td>
                <td><button class="casillas" data-fila="1" data-columna="4"></button></td>
            </tr>
            <tr>
                <td><button class="casillas" data-fila="2" data-columna="0"></button></td>
                <td><button class="casillas" data-fila="2" data-columna="1"></button></td>
                <td><button class="casillas" data-fila="2" data-columna="2"></button></td>
                <td><button class="casillas" data-fila="2" data-columna="3"></button></td>
                <td><button class="casillas" data-fila="2" data-columna="4"></button></td>
            </tr>
            <tr>
                <td><button class="casillas" data-fila="3" data-columna="0"></button></td>
                <td><button class="casillas" data-fila="3" data-columna="1"></button></td>
                <td><button class="casillas" data-fila="3" data-columna="2"></button></td>
                <td><button class="casillas" data-fila="3" data-columna="3"></button></td>
                <td><button class="casillas" data-fila="3" data-columna="4"></button></td>
            </tr>
            <tr>
                <td><button class="casillas" data-fila="4" data-columna="0"></button></td>
                <td><button class="casillas" data-fila="4" data-columna="1"></button></td>
                <td><button class="casillas" data-fila="4" data-columna="2"></button></td>
                <td><button class="casillas" data-fila="4" data-columna="3"></button></td>
                <td><button class="casillas" data-fila="4" data-columna="4"></button></td>
            </tr>
        </table>
`;
};

function actualizarInformacion() {
    barcosDisponiblesJugador.textContent = `Barcos del Jugador: ${contadorBarcosJugador}`;
    barcosDisponiblesMaquina.textContent = `Barcos de la Máquina: ${contadorBarcosMaquina}`;
};

// Cuerpo del programa

// Creo grilla 5x5 inicializada con ceros
let grillaJugador = Array.from({ length: 5 }, () => Array(5).fill(0));
let grillaMaquina = Array.from({ length: 5 }, () => Array(5).fill(0));

const barcosDisponibles = 3;
let barcosJugador = 0;
let contadorBarcosJugador = 3;
let contadorBarcosMaquina = 3;
let turnoJugador = true;

// DOM

const contenedor = document.getElementById("contenedor-principal");
contenedor.innerHTML = `
  <div class="contenedor-titulo" id="contenedor-titulo">
    <h1 class="titulo">BATALLA NAVAL</h1>

  </div>

  <div class="contenedor-grillas">
  <section class="secciones" id="grilla-jugador"></section>
  <section class="secciones" id="grilla-maquina"></section>
  </div>
`;

DOMcrearGrillas("grilla-jugador", "GRILLA DEL JUGADOR");
DOMcrearGrillas("grilla-maquina", "GRILLA DE LA MÁQUINA");

console.log("Posiciones de la Máquina:");
ubicarBarcosMaquina();

const botonesMaquina = document.querySelectorAll("#grilla-maquina button");
const botonesJugador = document.querySelectorAll("#grilla-jugador button");
const tablaJugador = document.getElementById("grilla-jugador");

const barcosDisponiblesJugador = document.createElement("p");
barcosDisponiblesJugador.className = "barcos";
const barcosDisponiblesMaquina = document.createElement("p");
barcosDisponiblesMaquina.className = "barcos";

barcosDisponiblesJugador.textContent = "Coloque sus 3 barcos";
barcosDisponiblesMaquina.textContent = `Barcos de la Máquina: ${contadorBarcosMaquina}`

const seccionJugador = document.getElementById("grilla-jugador");
seccionJugador.appendChild(barcosDisponiblesJugador);
const seccionMaquina = document.getElementById("grilla-maquina");
seccionMaquina.appendChild(barcosDisponiblesMaquina);

const informacionDinamica = document.createElement("p");
informacionDinamica.id = "infodinamica";
contenedor.appendChild(informacionDinamica);

const contenedorTitulo = document.getElementById("contenedor-titulo")
const tituloGanador = document.createElement("h1");
tituloGanador.id = "tituloGanador";
tituloGanador.textContent = "Seleccione donde posicionar sus barcos.";
contenedorTitulo.appendChild(tituloGanador);

contenedor.addEventListener("click", (evento) => {
    if (!(evento.target instanceof Element)) return;
    
    const boton = evento.target.closest("button[data-fila][data-columna]");
    if (!boton) return;
    
    const fila = Number(boton.dataset.fila);
    const columna = Number(boton.dataset.columna);

    if(barcosJugador <= 2) {
        console.log("Casilla elegida:", fila, columna);
        ubicarBarcosJugador(fila, columna, boton);
        barcosJugador += 1;
        if(barcosJugador === 3){
            console.log("Numero maximo de barcos desplegado.");
            actualizarInformacion();
            tituloGanador.textContent = "¡Comienza la Batalla! Turno del Jugador";
            tituloGanador.style.color = "rgb(16, 230, 30)";
            botonesMaquina.forEach(boton => {boton.style.pointerEvents = "auto";});
            botonesJugador.forEach(boton => {boton.style.pointerEvents = "none";});
        };
    } else{
        if(contarBarcos(grillaJugador) > 0 && contarBarcos(grillaMaquina) > 0) {
             /* Se realizan los disparos por turnos comenzando con el jugador
                El juego no termina hasta que todos los barcos de algun bando sean destruidos */
            informacionDinamica.style.backgroundColor = "rgb(0, 0, 0)"
            if (!turnoJugador) return;
            turnoJugador = false;
            disparoJugador(fila, columna, boton);

            /* Este setTimeout hace que la Máquina tarde 3 segundos en disparar. */
            setTimeout(() => {
                disparoMaquina();
                turnoJugador = true;
            }, 3000);

            definirGanador();
        };
    }; 
});