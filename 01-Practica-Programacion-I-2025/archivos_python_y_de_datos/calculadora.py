class Calculadora:
    def __init__(self, numero):
        self.numero = numero
        self.datos = [0 for i in range(numero)]

    def ingresardato(self):
        self.datos = [int(input("Ingresar dato" + str(i+1) + "=")) 
                      for i in range(self.numero)]
        
class Op_basicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 2)

    def suma(self):
        a, b = self.datos
        s = a + b
        print("El resultado es: ", s)

    def resta(self):
        a, b = self.datos
        s = a - b
        print("El resultado es: ", s)

class Raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 1)

    def cuadrada(self):
        import math

        a, = self.datos
        print("El resultado es: ", math.sqrt(a)) 

# ejemplo = Op_basicas()
# print(ejemplo.ingresardato())
# print(ejemplo.resta())

# ejemplo = Raiz()
# print(ejemplo.ingresardato())
# print(ejemplo.cuadrada())

print(issubclass(Op_basicas, Calculadora))
# print(issubclass(potencia, Calculadora)) Esta tira error, porque potencia no existe
print(issubclass(Raiz, Calculadora))
