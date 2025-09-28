# Clases

class Usuario:
    def __init__(self, documento, receta):
        self.documento = documento
        self.receta = receta

    def pedir_medicamento(self):
        pidiendo_medicamento(self.documento, self.receta)

class Farmaceutico:

    def pedir_dni(self, documento, receta):

        while True:
            if documento in usuarios:
                print("¡Usuario encontrado!")
                print("Verificando receta...")
                self.entregar_medicamento(receta)
                break

            elif documento not in usuarios:
                print("Usuario no existente...")
                print("Registrando nuevo usuario...")
                self.registrar_usuario(documento, receta)
                break

    def entregar_medicamento(self, receta):

        if receta in recetas:
            print("Receta encontrada!")
            print("Entregando medicamento...")
            print(f"Medicamento {receta} entregado con exito.")
        
        else:
            print("El medicamento de la receta ingresada no esta registrado.")
            print("No hay nada que hacer.")
            
    def registrar_usuario(self, documento, receta):
        
        if len(str(documento)) > 8 or len(str(documento)) < 8:
            print("¡Documento no valido! Intente nuevamente.")
        
        else:
            usuarios.add(documento)
            self.pedir_dni(documento, receta)
            
# Funciones

def pidiendo_medicamento(dni, receta):
    """Creamos los objetos y corroboramos el DNI 
    para entregar el medicamento o registrar el usuario."""

    farmacia = Farmaceutico()
    farmacia.pedir_dni(dni, receta)

def volver_a_utilizar():
    """Volver a utilizar todo el programa o finalizarlo."""

    global salir 

    while True:
        respuesta = input("¿Desea volver a utilizar el programa? SI/NO: ")

        if respuesta.lower() == "si":
            break

        elif respuesta.lower() == "no":
            print("¡Hasta pronto!")        
            salir = 1
            break

        else:
            print("Respuesta no valida, intente nuevamente.")

#Inicio

usuarios = set()
recetas = {"ibuprofeno", "amoxicilina", "paracetamol"} # Simulacion de base de datos
salir = 0
print("¡Bienvenido al sistema de entrega de medicamentos Farmacia!")

while True:
    if salir == 1:
        exit()

    print("1- Pedir medicamento.")
    print("2- Registrarse.")
    print("3- Salir.")
    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        while True:
            try:
                dni = int(input("Ingrese su documento: "))
                receta = input("Ingrese receta: ").lower()
                persona = Usuario(dni, receta)
                print(persona.documento)
                print(persona.receta)
                persona.pedir_medicamento()
                volver_a_utilizar()
                break

            except:
                print("Ingreso no valido. Solo deben ser numeros.")

    elif opcion == "2":
        while True:
            try:
                dni = int(input("Ingrese su documento: "))

                if len(str(dni)) == 8:
                    usuarios.add(dni)
                    print("¡Usuario registrado con exito!")
                    print("Volviendo al menu principal...")
                    break
                
                else:
                    print("Documento ingresado no valido, debe tener exactamente 8 digitos.")
                    pass

            except ValueError:
                print("Ingreso no valido. Solo debe ingresar numeros.")

    elif opcion == "3":
        print("¡Hasta pronto!")
        exit()

    else:
        print("Opcion ingresada no valida, intente nuevamente.")
        pass