let a = 7;
let b = 2;
let c = 5;

//  = document.getElementById("campo");

function cual_es_mayor() {
    
    if (a > b) {
        if (a > c) {
            console.log("La mayor es " + a)
        } else {
            console.log("La mayor es " + c)
        }
    } else {
        if (b > c) {
            console.log("La mayor es " + b)
        } else {
            console.log("La mayor es " + c)
        }
    }
}

// Switch


let now = new Date();
let NowDay = now.getDay();
function dia_de_semana() {
    switch (NowDay) {
        case 6:
            console.log("Sabado")
            break
        case 0:
            console.log("domingo")
            break

        default:
            console.log("Otro dia")
            break
    }
}

// dia_de_semana()

// Calculadora

let num1 = 5
let num2 = 10
let operador = "+"

function calculadora(num1, num2, operador) {
    
    switch (operador) {
        case "+":
            console.log(num1 + num2)
            break

        case "-":
            console.log(num1 - num2)
            break
        
        case "*":
            console.log(num1 * num2)
            break

        case "/":
            console.log(num1 / num2)
            break

        default:
            console.log("Esta calculadora no puede hacer esa operación")
    
    }

}

// calculadora(num1, num2, operador)

// Operador ternario
// Hace lo mismo que el if pero se puede escribir en una linea 
// Ternario =) Condicion | True | False

let compra = 10500

let resultado = compra > 10000 ? (compra * 20) / 100 : console.log("No se aplica descuento")
console.log(resultado)

// Ejercicios:
// Par o impar, Es mayor de edad?, Numero positivo o negativo

// Valores falsos
// False, Undfinded, Null, 0(cero), NaN, cadena vacia "" 