# Gestión de Inscripciones a un Curso Online

class Estudiante:
    def __init__(self, nombre, email, edad):
        self.__nombre = nombre
        self.__email = email
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre
    
    def get_email(self):
        return self.__email
    
    def get_edad(self):
        return self.__edad
    
    def agregar_estudiante(self, nuevo_estudiante):
        lista_inscriptos.append(nuevo_estudiante)
        print(f"Estudiante {nuevo_estudiante.__nombre} agregado con exito")

    def buscar_estudiante(self, email):
        x = 0
        for i in lista_inscriptos:
            if i.__email == email:
                print(f"Estudainte encontrado. Es {i.__nombre} de {i.__edad} años.")
                x = x + 1
                break
            else:
                x = 0
        if x == 0:
            print("El email de estudiante ingresado no exitste.")
    
    def listar_estudiantes(self):
        print("Esta es la lista de estudiantes inscriptos:\n")
        for i in lista_inscriptos:
            print(f"Estudiante {i.__nombre}. Email {i.__email}. Edad {i.__edad}.")

    def promedio_edades(self):
        promedio = 0
        edades = 0
        for i in lista_inscriptos:
            edades = edades + i.__edad
            promedio = promedio + 1
        promedio = edades / promedio
        print(f"El promedio de edades de los estudiantes inscriptos es de {promedio}")

class EstudianteBecado(Estudiante):
    def __init__(self, nombre, email, edad, porcentaje_beca):
        super().__init__(nombre, email, edad)

        self.__porcentaje_beca = porcentaje_beca

    def get_nombre(self):
        return super().get_nombre()
    
    def get_procentaje_beca(self):
        return self.__porcentaje_beca
    
    def agregar_estudiante(self, nuevo_estudiante):
        return super().agregar_estudiante(nuevo_estudiante)

def pidiendo_mensaje(mensaje):
    while True:
        ingreso = input(mensaje)
        if ingreso:
            return ingreso
        else:
            print("Debe ingresar alguna opción")

def lista_vacia():
    if len(lista_inscriptos) == 0:
        print("No se registraron estudiantes todavía. Volviendo al menú principal...\n")
    else:
        global paso
        paso = True
        return paso

lista_emails = []
lista_inscriptos = []
paso = False

while True:
    print("Sistema gestor de estudiantes inscriptos")
    print("Menu principal\n")
    print("1-Agregar estudiante\n2-Buscar estudiante por email\n3-Listar todos los estudiantes\n4-Mostrar el promedio de edad\n5-Salir")

    opcion = pidiendo_mensaje("Seleccione una opción: ")

    if opcion == "1":
        while True:
            if len(lista_inscriptos) == 15:
                print("Limite de registros de estudianes alcanzado... volviendo al menú principal.\n")
                break
            else:
                email = pidiendo_mensaje("Ingrese email de estudiante: ")
                if "@" in email and email not in lista_emails:
                    lista_emails.append(email)
                    nombre = pidiendo_mensaje("Ingrese el nombre de estudiante: ")
                    while True:
                        edad = pidiendo_mensaje(f"Ingrese la edad de {nombre}: ")
                        edad = int(edad)
                        if edad > 0:
                            break
                        else:
                            print("La edad no puede ser negativa. Intente nuevamente...\n")
                    nuevo_estudiante = Estudiante(nombre, email, edad)
                    nuevo_estudiante.agregar_estudiante(nuevo_estudiante)
                    continuar = pidiendo_mensaje("¿Quiere agregar otro estudiante? SI o cualquier tecla para volver al menu principal: ").lower()
                    if continuar == "si":
                        pass
                    else:
                        break
                else: 
                    print("El email debe contener @ o ya se encuentra registrado...")

    elif opcion == "2":
        lista_vacia()

        if paso is True:
            while True:
                email = pidiendo_mensaje("Ingrese el email del estudiante: ")
                nuevo_estudiante.buscar_estudiante(email)
                continuar = pidiendo_mensaje("¿Quiere buscar otro estudiante por email? Si o cualquier tecla para no: ").lower()
                if continuar == "si":
                    pass
                else:
                    print("Volviendo al menú principal...\n")
                    break

    elif opcion == "3":
        lista_vacia()

        if paso is True:
            nuevo_estudiante.listar_estudiantes()
            input("Presione ENTER para volver al menú: ")

    elif opcion == "4":
        if len(lista_inscriptos) >= 2:
           nuevo_estudiante.promedio_edades()
           input("Presione ENTER para volver al menú: ")
        else:
            print("No se registraron más de dos alumnos todavia.")

    elif opcion == "5":
        print("¡Hasta pronto!")
        exit()

    else:
        print("Opción ingresada no valida.\n")
# <
# >