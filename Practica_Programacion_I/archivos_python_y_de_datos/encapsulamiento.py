# Sistema de Gestión de Estudiantes

class Estudiante:
    def __init__(self, nombre, edad, calificaciones):
        self.__nombre = nombre
        self.__edad = edad
        self.__calificaciones = calificaciones

    def obtener_datos(self):
        print(f"Nombre: {self.__nombre}, Edad: {self.__edad}")
    
    def modificar_datos(self, nuevo_nombre, nueva_edad):
        self.__nombre = nuevo_nombre
        self.__edad = nueva_edad

    def agregar_calificacion(self, nueva_calificacion):
        self.__calificaciones.append(nueva_calificacion)

    def promedio_de_calificaciones(self):
        promedio = sum(self.__calificaciones) / len(self.__calificaciones)
        print(f"El promedio de calificaciones es {promedio}")

calificaciones = []
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
for i in range(0, 3):
    calificaciones.append(int(input("Ingrese la calificación: ")))

print(calificaciones)
san = Estudiante(nombre, edad, calificaciones)
san.obtener_datos()
san.modificar_datos("Santino", 21)
san.obtener_datos()
san.agregar_calificacion(6)
san.promedio_de_calificaciones()