# Consigna 2: Sistema de Gestión de Empleados
# Objetivo: Crear una clase base Empleado y una clase derivada Gerente. La clase Gerente debe utilizar
# super() para invocar el constructor de Empleado y extender sus funcionalidades.
# Detalles: • La clase Empleado debe tener atributos como nombre y salario. • 
# La clase Gerente debe agregar atributos específicos como departamento. 
# • Implementar métodos en Empleado para mostrar información básica y en Gerente para mostrar
# información extendida.

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar_informacion(self):
        print(f"Empleado : {self.nombre}")
        print(f"Salario de empleado : {self.salario}")

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)

        self.departamento = departamento

    def mostrar_informacion_adicional(self):
        print(f"El empleado {self.nombre} se encuentra en el departamento {self.departamento}.")

sujeto = Gerente("Santino", 3000000, "Gestion de proyectos")
sujeto.mostrar_informacion()
sujeto.mostrar_informacion_adicional()