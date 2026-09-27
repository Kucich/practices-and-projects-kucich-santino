/* --------------------------------------------------
   Reglas básicas de la batalla naval:
    Cada jugador tiene una grilla 5x5.
    Coloca sus barcos en casilla 3 barcos por jugador).
    Los barcos ocupan una.
    Los jugadores se turnan para “tirar bombas” en coordenadas de la grilla del rival.
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
const prompt = require("prompt-sync")();

// 0 casilla vacia, 1 = barco, 2 = impacto, 3 = agua

// Creo grilla 5x5 inicializada con ceros
const tamaño = 5;
let grillaJugador = Array.from({ length: 5 }, () => Array(5).fill(0));
let grillaMaquina = Array.from({ length: 5 }, () => Array(5).fill(0));

const barcosDisponibles = 3;

// Math.random devuelve un número decimal entre 0 y 1 (ejemplo: 0.2345).
// Para obtener un número entero en un rango, combinás con Math.floor().
// let numero = Math.floor(Math.random() * 5); // entero entre 0 y 4

function ubicar_barco() {
    /* Se ingresan los datos de ubicación, se validan y se coloca en la grilla. 
       Se eligen posiciones al azar para ubicar en la grilla de la maquina */
    let contadorBarcosMaquina = 0

    for (let index = 0; index < barcosDisponibles; index++) {
        while(true) {
            const jugador = 0
            let filaSeleccionada = parseInt(prompt("Ingrese una fila del 0 al 4: "));
            let columnaSeleccionada = parseInt(prompt("Ingrese una columna del 0 al 4: "));
            if (validarFilaColumna(filaSeleccionada, columnaSeleccionada, jugador)) {
                grillaJugador[filaSeleccionada][columnaSeleccionada] = 1
                console.log(grillaJugador);
                break  
            };
        };
    };

    while(contadorBarcosMaquina < barcosDisponibles) {
        const maquina = 1
        let filaMaquina = Math.floor(Math.random() * 5); // entero entre 0 y 4
        let columnaMaquina = Math.floor(Math.random() * 5); // entero entre 0 y 4
        if (validarFilaColumna(filaMaquina, columnaMaquina, maquina)) {
            grillaMaquina[filaMaquina][columnaMaquina] = 1
            console.log(grillaMaquina);
            contadorBarcosMaquina += 1
        };
    };
};

function validarFilaColumna(fila, columna, grilla) {    
    /* Valido que fila y columna ingresados esten entre 0 y 4.
       Luego verifico que el lugar seleccionado no este ocupado. */
    if (fila < 0 || fila > 4 || columna < 0 || columna > 4) {
        console.log("El número debe ser mayor o igual a 0 y menor o igual a 4.");
        return false
    } else {
        if (grilla === 0 && grillaJugador[fila][columna] === 1) {
            console.log("Casilla ya ocupada por un barco. Intente con otra.")
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
};

function realizarDisparos() {
    /* Se realizan los disparos por turnos comenzando con el jugador
       El juego no termina hasta que todos los barcos de algun bando sean destruidos */
    while(contarBarcos(grillaJugador) > 0 && contarBarcos(grillaMaquina) > 0) {
        disparoJugador();
        disparoMaquina();
    };
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
}

ubicar_barco();
realizarDisparos();

if(contarBarcos(grillaJugador) === 0) {
        console.log("Todos las barcos del Jugador fueron destruidos. ¡La Maquina gana!");
    } else if(contarBarcos(grillaMaquina) === 0) {
        console.log("Todos las barcos de la Maquina fueron destruidos. ¡El Jugador gana!");
    } else{
        console.log("¡Los barcos de ambos bandos fueron destruidos! La guerra no tiene ganadores...")
    };