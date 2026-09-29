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

// Renderizado en HTML

// Usar innerHTML para crear la grilla inicial dentro del único <div>.

// Usar appendChild para botones, mensajes, etc.

// Estilos con CSS

// Diferenciar casillas: agua, barco, impacto.

// Darle aspecto de tablero de juego.
// --------------------------------------------------

// Importar prompt-sync , es como input en python
// const prompt = require("prompt-sync")();

// Funciones

function ubicarBarcosJugador(filaSeleccionada, columnaSeleccionada) {
    /* Se ingresan los datos de ubicación, se validan y se coloca en la grilla.  */
    const jugador = 0;

    if (validarFilaColumna(filaSeleccionada, columnaSeleccionada, jugador)) {
        grillaJugador[filaSeleccionada][columnaSeleccionada] = 1
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
        console.log("Casilla ya ocupada por un barco. Intente con otra.")
        barcosJugador -= 1
        return false

    } else if (grilla === 0){
        return true

    } else if (grilla === 1 && grillaMaquina[fila][columna] === 1) {
        console.log("La maquina intento una combinación ya utilizada.")
        return false

    } else if (grilla === 1) {
        return true
    };
};

function realizarDisparos() {
    /* Se realizan los disparos por turnos comenzando con el jugador
       El juego no termina hasta que todos los barcos de algun bando sean destruidos */
    while(contarBarcos(grillaJugador) > 0 && contarBarcos(grillaMaquina) > 0) {
        disparoJugador();
        disparoMaquina();
    };

    definirGanador();
};

function disparoJugador() {
    /*Seleccionamos la posición en la que realizamos el disparo.*/
    let filaAtacada = parseInt(prompt("Ingrese una fila del 0 al 4 donde atacar: "));
    let columnaAtacada = parseInt(prompt("Ingrese una columna del 0 al 4 donde atacar: "));

    switch (grillaMaquina[filaAtacada][columnaAtacada]) {
    /*Verifico la posición a la que se disparo y ejecuto 
      una acción depende el valor de la posición */
    case 0:
        console.log("¡AGUA! Disparo errado.");
        grillaMaquina[filaAtacada][columnaAtacada] = 3;
        break;

    case 1:
        console.log("¡EN EL BLANCO! Barco Destruido.");
        grillaMaquina[filaAtacada][columnaAtacada] = 2;
        break;

    default:
        console.log("Esta posición ya fue seleccionada. Perdiste el turno.");
        break;
    };
    console.log("GRILLA DE LA MAQUINA:")
    console.log(grillaMaquina);
    let cont = contarBarcos(grillaMaquina)
    console.log("Barcos de la Maquina: " + cont);
};

function disparoMaquina() {
    /*La maquina realiza sus disparos en las posiciones seleccionadas.*/
    let filaAtacada = Math.floor(Math.random() * 5); // entero entre 0 y 4
    let columnaAtacada = Math.floor(Math.random() * 5); // entero entre 0 y 4
    
    switch (grillaJugador[filaAtacada][columnaAtacada]) {
        /*Verifico la posición a la que se disparo y ejecuto 
            una acción depende el valor de la posición*/
        case 0:
            console.log("La Maquina dio en el AGUA.");
            grillaJugador[filaAtacada][columnaAtacada] = 3;
            break;

        case 1:
            console.log("¡LA MAQUINA DIO EN EL BLANCO! Barco Destruido.");
            grillaJugador[filaAtacada][columnaAtacada] = 2;
            break;

        default:
            console.log("La Maquina disparo en un lugar que ya habia elegido. Pierde el turno.");
            break;
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
    return grilla.flat().filter(c => c === 1).length;
};

function definirGanador() {
    /* Se evalua los barcos de cada jugador y se define el ganador o empate. */
    if(contarBarcos(grillaJugador) === 0) {
        console.log("Todos las barcos del Jugador fueron destruidos. ¡La Maquina gana!");
    } else if(contarBarcos(grillaMaquina) === 0) {
        console.log("Todos las barcos de la Maquina fueron destruidos. ¡El Jugador gana!");
    } else{
        console.log("¡Los barcos de ambos bandos fueron destruidos! La guerra no tiene ganadores...");
    };
};

function DOMcrearGrillas(idContenedor, titulo) {
    const espacio = document.getElementById(idContenedor);

    espacio.innerHTML = `
        <h2 class="titulo">${titulo}</h2>
        <table>
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

// Cuerpo del programa

// Creo grilla 5x5 inicializada con ceros
let grillaJugador = Array.from({ length: 5 }, () => Array(5).fill(0));
let grillaMaquina = Array.from({ length: 5 }, () => Array(5).fill(0));

const barcosDisponibles = 3;
let barcosJugador = 0;

// DOM

const contenedor = document.getElementById("contenedor-principal");
contenedor.innerHTML = `
  <div class="contenedor-titulo">
    <h1 class="titulo">BATALLA NAVAL</h1>
  </div>

  <div class="contenedor-grillas">
  <section class="secciones" id="grilla-jugador"></section>
  <section class="secciones" id="grilla-maquina"></section>
  </div>
`;

DOMcrearGrillas("grilla-jugador", "GRILLA DEL JUGADOR");
DOMcrearGrillas("grilla-maquina", "GRILLA DE LA MÁQUINA");

console.log("Posiciones de la Maquina:");
ubicarBarcosMaquina();

contenedor.addEventListener("click", (evento) => {
    if (!(evento.target instanceof Element)) return;

    const boton = evento.target.closest("button[data-fila][data-columna]");
    if (!boton) return;

    const fila = Number(boton.dataset.fila);
    const columna = Number(boton.dataset.columna);
    barcosJugador += 1
    // console.log(grillaJugador)
    if(barcosJugador <= 3) {
        console.log("Casilla elegida:", fila, columna);
        ubicarBarcosJugador(fila, columna);
    } else {console.log("Numero maximo de barcos desplegado.")};

});

// realizarDisparos();
