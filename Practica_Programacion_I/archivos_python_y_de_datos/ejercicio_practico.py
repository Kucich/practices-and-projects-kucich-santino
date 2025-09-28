# Sistema de Gestión de Vehículos de una Empresa de Transporte

class Vehiculo:
    def __init__(self, patente, marca, carga):
        self.__patente = patente
        self.__marca = marca
        self.__carga = carga

    def agregar_vehiculo(self, nuevo_vehiculo):
        lista_vehiculos.append(nuevo_vehiculo)
        print("Vehiculo registrado con exito.")

    def buscar_vehiculo(self, patente):
        x = 0
        for i in lista_vehiculos:
            if i.__patente == patente:
                print(f"Vehiculo encontrado, es un {i.__marca}")
                x = 0
                break

            else:
                x = x + 1

        if x == 1:
            print("Patente ingresada no registrada.")

    def listar_vehiculos(self):
        print("La lista de vehiculos registrados es la siguiente:\n")
        for i in lista_vehiculos:
            print(i.__patente)

    def consultar_carga(self):
        y = 0
        for i in lista_vehiculos:
            y = y + i.__carga

        print(f"El total de carga de todos los vehiculos registrados es de {y} kg")

class VehiculoRefrigerado(Vehiculo):
    def __init__(self, patente, marca, carga, temperatura_minuma):
        super().__init__(patente, marca, carga)

        self.temperatura_minima = temperatura_minuma

    def agregar_vehiculo(self, nuevo_vehiculo):
        return super().agregar_vehiculo(nuevo_vehiculo)

def pidiendo_mensaje(mensaje):
    while True:
        ingreso = input(mensaje)
        if ingreso:
            return ingreso
        else:
            print("Debe ingresar una opción.")


lista_vehiculos = []
lista_patentes = []
condicion = False
while True:

    print("\nMenu principal")
    print("1-Agregar vehiculo\n2-Buscar vehiculo por patente\n3-Listar todos los vehiculos\n4-Mostrar capacidad de carga\n5-Salir")

    opcion = pidiendo_mensaje("Ingrese una opción: ")

    if opcion == "1":
        while True:
            if len(lista_vehiculos) == 10:
                print("Limite de vehiculos registrados alcanzado...")
                break
            else:
                patente = pidiendo_mensaje("Ingrese patente del vehiculo: ")
                if patente in lista_patentes:
                    print("Vehiculo ya registrado, no puede repetirse la patente.")
                else:
                    lista_patentes.append(patente)
                    marca = pidiendo_mensaje("Ingrese marca del vehiculo: ")
                    peso = pidiendo_mensaje("Ingrese capacidad de carga del vehiculo: ")
                    vehiculo = Vehiculo(patente, marca, peso)
                    vehiculo.agregar_vehiculo(vehiculo)
                continuar = pidiendo_mensaje("\n¿Desea ingresar otro vehiculo? Si para continuar o cualquier tecla para volver al menu: ").lower()
                if continuar == "si":
                    pass
                else:
                    break

    elif opcion == "2":
        if len(lista_vehiculos) == 0:
            print("No se registraron vehiculos todavia.")
        else:
            ingrese_patente = pidiendo_mensaje("Ingrese la patente del vehiculo que desea buscar: ")
            vehiculo.buscar_vehiculo(ingrese_patente)

    elif opcion == "3":
        if len(lista_vehiculos) == 0:
            print("No se registraron vehiculos todavia.")
        else:
            vehiculo.listar_vehiculos()

    elif opcion == "4":
        if len(lista_vehiculos) == 0:
            print("No se registraron vehiculos todavia.")
        else:
            vehiculo.consultar_carga()

    elif opcion == "5":
        exit()