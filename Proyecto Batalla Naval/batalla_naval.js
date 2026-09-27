// Como se usa el appendChild();
// const div = document.getElementById("contenedor");
// const boton = document.createElement("button");
// boton.textContent = "Jugar";
// div.appendChild(boton);
// --------------------------------------------------

// Reglas básicas de la batalla naval
// Cada jugador tiene una grilla (ej: 5x5 o 10x10).

// Coloca sus barcos en casillas (vos querés 3 barcos por jugador).

// Los barcos ocupan una o varias casillas (podés simplificar y hacerlos de 1 casilla cada uno).

// Los jugadores se turnan para “tirar bombas” en coordenadas de la grilla del rival.

// Si aciertan, esa casilla se marca como “impacto”; si fallan, como “agua”.

// Gana quien destruye todos los barcos del otro.

// Paso a paso para diseñar tu juego

// Definir grilla

// Representala como un array bidimensional en JS.

// Colocar barcos

// Para el jugador: permitir elegir casillas.

// Para la máquina: ubicar barcos en posiciones random.

// Turnos

// Alternar entre jugador y máquina.

// Jugador: selecciona una casilla del rival.

// Máquina: elige una casilla random en tu grilla.

// Impactos y agua

// Si la casilla tiene barco → marcar impacto.

// Si no → marcar agua.

// Condición de victoria

// Revisar si todos los barcos de un jugador fueron destruidos.

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

// Crear grilla 5x5 inicializada con ceros
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

    while(contadorBarcosMaquina < 3) {
        const maquina = 1
        let filaMaquina = Math.floor(Math.random() * 5); // entero entre 0 y 4
        let columnaMaquina = Math.floor(Math.random() * 5); // entero entre 0 y 4
        if (validarFilaColumna(filaMaquina, columnaMaquina, maquina)) {
            grillaMaquina[filaMaquina][columnaMaquina] = 1
            console.log(grillaMaquina);
        };

        contadorBarcosMaquina += 1
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
    /* Seleccionamos la posición en la que realizamos el disparo.
       La maquina realiza sus disparos en posiciones selecciona sin repetir */
    let jugando = true
    let barcosJugador = 3
    let barcosMaquina = 3

    while(jugando) {
        let filaAtacada = parseInt(prompt("Ingrese una fila del 0 al 4 donde atacar: "));
        let columnaAtacada = parseInt(prompt("Ingrese una columna del 0 al 4 donde atacar: "));
        
        switch (grillaMaquina[filaAtacada][columnaAtacada]) {
            /*Verifico la posición a la que se disparo y ejecuto 
              una acción depende el valor de la posición*/
            case 0:
                console.log("¡AGUA! Disparo errado.");
                grillaMaquina[filaAtacada][columnaAtacada] = 3;
                break;

            case 1:
                console.log("¡EN EL BLANCO! Barco Destruido.");
                grillaMaquina[filaAtacada][columnaAtacada] = 2;
                break;

            case 2 || 3:
                console.log("Esta posición ya fue seleccionada. Perdiste el turno.");
                break;
            // Aca quede, tenemos que hacer que la maquina dispare a nuestra grilla y que sea por turnos.
        };

        console.log(grillaMaquina);
    };
};

ubicar_barco();
realizarDisparos();