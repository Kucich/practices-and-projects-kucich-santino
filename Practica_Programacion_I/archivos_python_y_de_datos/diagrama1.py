# Reserva de hotel

class Usuario:
    def __init__(self, nombre, apellido, dni, celular, email):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.celular = celular
        self.email = email

    def buscar_habitacion(self):
        print("Buscando...")

    def seleccionar_habitacion(self):
        try:
            while True:
                seleccionar = int(input("Seleccione que habitacion prefiere."))

                if seleccionar > 0 and seleccionar < 100:
                    print("¡Habitacion seleccionada con exito!")
                    break
            
        except ValueError:
            print("Opcion no valida, intente nuevamente.")

class Habitacion:
    def __init__(self, numero_habitacion, cantidad_camas, tipo):
        self.numero_habitacion = numero_habitacion
        self.cantidad_camas = cantidad_camas
        self.tipo = tipo

    def mostrar_habitaciones(self):
        print("Estas son las habitaciones disponibles: ")
        print("Habitacion Simple Nº8")
        print("Habitacion Doble Nº13")
        print("Habitacion Doble Nº15")
        print("Habitacion Matrimonial Nº20")

    def enviar_confirmacion(self, email):
        print("Confirmacion enviada al mail {}".format(email))
        print("Gracias por elegir este Hotel.")

class Reserva(Usuario, Habitacion):
    def __init__(self, nombre, apellido, dni, celular, email, numero_habitacion, cantidad_camas, tipo):
        super().__init__(nombre, apellido, dni, celular, email, numero_habitacion, cantidad_camas, tipo)

    def comenzar_reserva(self):
        self.buscar_habitacion()
        self.seleccionar_habitacion()

    def completar_reserva(self, email):
        self.enviar_confirmacion(email)

mostrar = Habitacion(1, 1 ,1)

nombre = input("Ingrese se nombre: ")
apellido = input("Ingrese su apellido: ")
dni = input("Ingrese su DNI: ")
celular = input("Ingrese su celular: ")
email = input("Ingrese su email: ")
mostrar.mostrar_habitaciones()
numero_habitacion = input("\nIngrese numero de habitacion: ")
cantidad_camas = input("Ingrese cantidad de camas: ")
tipo_habitacion = input("Ingrese tipo de habitacion: ")
persona = Reserva(nombre, apellido, dni, celular, email, numero_habitacion, cantidad_camas, tipo_habitacion)

persona.comenzar_reserva()
persona.completar_reserva(email)
