# Consigna 1: Sistema de Gestión de Vehículos
# Objetivo: Crear una clase base Vehiculo y una clase derivada Automovil. La clase Automovil debe
# utilizar super() para invocar el constructor de Vehiculo y extender sus funcionalidades.
# Detalles:
# •La clase Vehiculo debe tener atributos como marca y modelo. •La clase Automovil debe agregar atributos
#  específicos como numero_de_puertas. •Implementar métodos en Vehiculo para mostrar información básica y en Automovil para mostrar
# información extendida.

class Vehiculo:
    def __init__(self, modelo, marca):
        self.__modelo = modelo 
        self.__marca = marca

    def mostrar_informacion(self):
        print(f"El modelo es : {self.__modelo}")
        print(f"Y su marca {self.__marca}")

class Automovil(Vehiculo):
    def __init__(self, modelo, marca, numero_de_puertas):
        super().__init__(modelo, marca)

        self.__numero_de_puertas = numero_de_puertas

    def mostrar_informacion_extendida(self):
        print(f"El numero de puertas de este auto es : {self.__numero_de_puertas}")

auto = Automovil("Focus", "Ford", 4)
auto.mostrar_informacion()
auto.mostrar_informacion_extendida()