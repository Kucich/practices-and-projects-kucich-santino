import requests
from datetime import datetime
import csv
import os

# Clases

class Region:
    def __init__(self, pais, provincia, ciudad):
        self.pais = pais
        self.provincia = provincia
        self.ciudad = ciudad

    def consultar_regiones(self):
        """Consulta a la API Serach Hotels Destination, 
           para visualizar las regiones localizadas en la ubicación ingresada por el usuario"""

        url_1 = "https://booking-com15.p.rapidapi.com/api/v1/hotels/searchDestination"

        querystring = {f"query":{self.ciudad + " " + self.provincia + " " + self.pais}}

        headers = {
            "x-rapidapi-key": "e9aeb9743fmsh7ee6828ce199259p1b282djsn80f01a3a77c0",
            "x-rapidapi-host": "booking-com15.p.rapidapi.com"
        }

        response = requests.get(url_1, headers=headers, params=querystring)
        data_hoteles = response.json()

        return data_hoteles
    
    def mostrar_regiones(self, data_hoteles):
        """Muestra regiones enumeradas"""

        print("\n --- Regiones Encontradas --- \n")
        indice = 1
        for diccionarios in data_hoteles["data"]:
            if "name" in diccionarios: # Le borre esta condición: and diccionarios["search_type"] == "hotel"
                diccionario_de_regiones[indice] = [diccionarios['name'], diccionarios['dest_id'], diccionarios['search_type']]
                print(indice ,diccionario_de_regiones[indice][0])
                indice += 1

        return diccionario_de_regiones
    
class Hotel:
    def __init__(self, hoteles_en_region, fecha_de_llegada, fecha_de_partida ):
        self.hoteles_en_region = hoteles_en_region
        self.fecha_de_llegada = fecha_de_llegada
        self.fecha_de_partida = fecha_de_partida

    def consultar_hoteles(self, seleccionar_region):
        """Consultamos a la API Serachs Hotels para mostrar los hoteles de la región
           y para obtener y vizualizar los datos del hotel"""

        url_2 = "https://booking-com15.p.rapidapi.com/api/v1/hotels/searchHotels"

        querystring2 = {f"dest_id":{self.hoteles_en_region[seleccionar_region][1]},
                        "search_type":{self.hoteles_en_region[seleccionar_region][2]},
                        "arrival_date": {self.fecha_de_llegada}, "departure_date": {self.fecha_de_partida}, 
                        "units":"metric", "languagecode":"es-ar", 
                        "currency_code":"AED"}

        headers = {
          "x-rapidapi-key": "e9aeb9743fmsh7ee6828ce199259p1b282djsn80f01a3a77c0",
          "x-rapidapi-host": "booking-com15.p.rapidapi.com"
        }

        response = requests.get(url_2, headers=headers, params=querystring2)
        data_regiones_de_hoteles = response.json()

        return data_regiones_de_hoteles
    
    def mostar_hoteles(self, hoteles):
        """Muestra todos los hoteles encontrados en la región seleccionada"""

        print("\n--- Hoteles Encontrados ---\n")

        for i, hotel in enumerate(hoteles["data"]["hotels"], start=1):
            print(i, " - ", hotel["property"]["name"])

            lista_de_hoteles = [hotel["hotel_id"], hotel["property"]["name"], hotel["accessibilityLabel"], hotel["property"]["reviewScore"], hotel["property"]["reviewScoreWord"]]
                
            diccionario_de_hoteles[i] = lista_de_hoteles

        return diccionario_de_hoteles

    def mostrar_caracteristicas(self, hotel_seleccionado):
        """Muestra las características del hotel seleccionado"""

        # Itera directamente sobre la lista de hoteles en el diccionario de datos.
        for hotel in data_regiones_de_hoteles["data"]["hotels"]:
            # Compara el valor de la clave 'hotel_id' con el ID que buscas.
            if hotel["hotel_id"] == int(diccionario_de_hoteles[seleccionar_hotel][0]):

                hotel_seleccionado = diccionario_de_hoteles[seleccionar_hotel]
                print(f"\nHotel : {diccionario_de_hoteles[seleccionar_hotel][1]}")
                print(f"\nDescripción : {diccionario_de_hoteles[seleccionar_hotel][2]}")
                print(f"\nReseñas : {diccionario_de_hoteles[seleccionar_hotel][3]}")
                print(f"\nReseñas Globales : {diccionario_de_hoteles[seleccionar_hotel][4]}")
                return hotel_seleccionado  # Devuelve las características del hotel seleccionado y sale del bucle una vez que se encuentra el hotel.
        
    def realizar_reserva(self, hotel_seleccionado):
        """Se piden los datos para realizar reservación en el hotel y se guardan los datos en un archivo csv"""
    
        print(f"\n--- Reservación en {hotel_seleccionado[1]} ---\n")

        apellido_familiar = pidiendo_mensaje("\nIngrese su Apellido: ")
        numero_adultos = pidiendo_mensaje("¿Cúantos adultos van a ser? : ")
        numero_chicos = pidiendo_mensaje("¿Cúantos niños habra? : ")
        reserva = [apellido_familiar, numero_adultos, numero_chicos, fecha_de_llegada, fecha_de_partida, hotel_seleccionado[1]]

        with open(archivo_hoteles, "a", newline="") as file:
            escritura = csv.writer(file, delimiter=",")

            if os.stat(archivo_hoteles).st_size == 0:
                encabezado = ["FAMILIA", "Nº DE ADULTOS", "Nº DE NIÑOS", "FECHA DE LLEGADA", "FECHA DE SALIDA","NOMBRE DEL HOTEL"]
                escritura.writerow(encabezado)
            
            escritura.writerow(reserva)
        print(f"\n--- ¡Reservación en {hotel_seleccionado[1]} completada con exito! ---\n")
        print(f"Detalles de reserva:\nFamilia: {reserva[0]}\nTotal de adultos: {reserva[1]}\nTotal de chicos: {reserva[2]}\nDesde: {reserva[3]} - Hasta: {reserva[4]}")


# Funciones

def pidiendo_mensaje(mensaje):
    """Esta función se asegura de que en cada input del usuario se ingrese un valor y no un espacio vacio"""
    while True:
        ingreso = input(mensaje)
        if ingreso:
            return ingreso
        else:
            print("Debe ingresar una opción.\n")

def cambiar_a_formato_fecha(fecha_de_llegada, fecha_de_partida):
    """Cambia el formato de las fechas ingresadas por el usuario a formato valido para consulta a la API"""

    # 1. Convertir los strings a objetos de fecha
    fecha_llegada_obj = datetime.strptime(fecha_de_llegada, "%d/%m/%Y")
    fecha_partida_obj = datetime.strptime(fecha_de_partida, "%d/%m/%Y")

    # 2. Formatear los objetos de fecha al formato YYYY-MM-DD
    fecha_llegada_api = fecha_llegada_obj.strftime("%Y-%m-%d")
    fecha_partida_api = fecha_partida_obj.strftime("%Y-%m-%d")

    return fecha_llegada_api, fecha_partida_api

def obtener_usuarios():
    """Lee el archivo CSV y devuelve un diccionario {nombre: clave}."""
    usuarios = {}

    if not os.path.exists(archivo_usuarios) or os.stat(archivo_usuarios).st_size == 0:
        return usuarios 

    # Modo 'r' (read) para lectura
    with open(archivo_usuarios, "r", newline="") as file:
        lector = csv.DictReader(file, delimiter=",") 
        
        for fila in lector:
            # Asume que los encabezados son 'NOMBRE DE USUARIO' y 'CONTRASEÑA'
            usuarios[fila["NOMBRE DE USUARIO"]] = fila["CONTRASEÑA"]
            
    return usuarios

def iniciar_sesion(nombre_ingresado, contrasena_ingresada):
    """Verifica las credenciales del usuario."""
    
    # 1. Cargar todos los usuarios
    usuarios_registrados = obtener_usuarios()
    
    if not usuarios_registrados:
        print("⚠️ No hay usuarios registrados. Regístrese primero.")
        return False # Fallo al no haber usuarios
        
    # 2. Verificar existencia del nombre
    if nombre_ingresado in usuarios_registrados:
        
        # 3. Si el usuario existe, verificar la contraseña guardada
        clave_guardada = usuarios_registrados[nombre_ingresado]
        
        if contrasena_ingresada == clave_guardada:
            print(f"🎉 ¡Bienvenido, {nombre_ingresado}!")
            return True # ¡Éxito!
        else:
            print("❌ Contraseña incorrecta.")
    else:
        print("❌ Usuario no encontrado.")
        
    return False # Fallo en el inicio de sesión

def registrar_usuario(nombre, contrasena):
    """Guarda un nuevo usuario en el archivo CSV."""

    # La lista de datos del nuevo usuario
    nuevo_usuario = [nombre, contrasena]

    # Modo 'a' (append) para añadir al final del archivo
    with open(archivo_usuarios, "a", newline="") as file:
        escritura = csv.writer(file, delimiter=",")

        # Verifica si el archivo está vacío para escribir el encabezado
        if os.stat(archivo_usuarios).st_size == 0:
            encabezado = ["NOMBRE DE USUARIO", "CONTRASEÑA"]
            escritura.writerow(encabezado)

        # Usa writerow para escribir la fila de datos
        escritura.writerow(nuevo_usuario)
        
    print(f"✅ Usuario {nombre} registrado exitosamente.")
    return True


# Cuerpo del Programa

diccionario_de_regiones = {} # Diccionario en el cual guardo las regiones donde buscar los hoteles
diccionario_de_hoteles = {} # Diccionario donde guardo los hoteles con sus caracteristicas
archivo_hoteles = "reservas_de_hoteles.csv" # Archivo donde guardo las reservas realizadas por los usuarios
archivo_usuarios = "reserva_de_usuarios.csv" # Archivo donde guardo los usuarios que se registran y sus contraseñas

# Menu principal

while True:
    print("\n--- ¡Bienvenidos a la Agencia de Viajes y reserva de Hoteles! ---\n")
    print("1- Iniciar sesión.\n2- Registrarse.\n3- Salir.")

    opcion = pidiendo_mensaje("\nIngrese una opcion: ")

    if opcion == "1":
        usuario = pidiendo_mensaje("Ingrese su nombre de usuario: ")
        contrasena_usuario = pidiendo_mensaje("Ingrese su contraseña: ")

        inicio = iniciar_sesion(usuario, contrasena_usuario)
        
        if inicio is True:
            pass

        else:
            continue

        while True:

            print("\n--- Menú de consulta de Viajes y Hoteles ---\n")
            print("1- Consultar Viajes en Avión.\n2- Consultar Hoteles por Región.\n3- Cerrar sesión.\n4- Salir del programa.\n")
            
            opcion_seleccionada = pidiendo_mensaje("Ingrese una opción: ")

            if opcion_seleccionada == "1":
                pass


            elif opcion_seleccionada == "2":
                
                # Buscar país, provincia y ciudad.
                
                pais = pidiendo_mensaje("Ingrese el país donde desea buscar un Hotel: ")
                provincia = pidiendo_mensaje("Ingrese el nombre de la provincia en la: ")
                ciudad = pidiendo_mensaje("Ingrese el nombre de la ciudad donde iniciar la busqueda: ")

                regiones = Region(pais, provincia, ciudad)
                regiones_encontradas = regiones.consultar_regiones()
                regiones_mostradas = regiones.mostrar_regiones(regiones_encontradas)

                seleccionar_region = int(pidiendo_mensaje("\nSeleccione la región en la desea encontrar su hotel: "))

                # Se ingresa la fecha de inicio de reserva y de partida y se convierten a formato de fecha.
                fecha_de_llegada = pidiendo_mensaje("¿En qué fecha iniciara la reserva del hotel? Complete con dd/mm/aaaa: ")
                fecha_de_partida = pidiendo_mensaje("¿Hasta qué fecha reservara en el hotel? Complete con dd/mm/aaaa: ")
                fechas_ingresadas = cambiar_a_formato_fecha(fecha_de_llegada, fecha_de_partida)

                hoteles = Hotel(regiones_mostradas, fechas_ingresadas[0], fechas_ingresadas[1])
                data_regiones_de_hoteles = hoteles.consultar_hoteles(seleccionar_region)
                bandera_uno = True

                while bandera_uno:
                    hoteles_mostrados = hoteles.mostar_hoteles(data_regiones_de_hoteles)

                    seleccionar_hotel = int(pidiendo_mensaje("\nSeleccione el hotel del que desea ver sus características: "))
                    
                    hotel_seleccionado = hoteles.mostrar_caracteristicas(seleccionar_hotel)
                    bandera_dos = True

                    while bandera_dos:
                        seleccionar_opcion = pidiendo_mensaje("\n--- Menú de Reservas de Hoteles ---\n\n1- Realizar reserva en el Hotel seleccionado\n2- Volver a mostrar lista de Hoteles\n3- Regresar al menú de Consultas de Viajes y Hoteles\n\nSeleccione una Opción: ")

                        if seleccionar_opcion == "1":
                            hoteles.realizar_reserva(hotel_seleccionado)

                            while True:
                                reservar_nuevamente = pidiendo_mensaje("\nPara volver al menú de Reservas de Hoteles, presione: S\nPara volver al menú de Consultas de Viajes y Hoteles, presione: N\nIngrese alguna opción mostrada: ").lower()

                                if reservar_nuevamente == "s":
                                    break

                                elif reservar_nuevamente == "n":
                                    bandera_uno = False
                                    bandera_dos = False
                                    break

                                else:
                                    print("Opción no valida, Intente nuevamente...\n")

                        elif seleccionar_opcion == "2":
                            bandera_dos = False
                            
                        elif seleccionar_opcion == "3":
                            bandera_uno = False
                            bandera_dos = False

                        else:
                            print("Opción no valida, Intente nuevamente...\n")

            elif opcion_seleccionada == "3":
                break

            elif opcion_seleccionada == "4":
                print("¡Hasta luego!")
                exit()

            else:
                print("Opción ingresada no valida... Intente nuevamente")    

    elif opcion == "2":
        nuevo_usuario = pidiendo_mensaje("Ingrese su nombre de usuario: ")
        nueva_contrasena = pidiendo_mensaje("Ingrese su contraseña: ")

        registrar_usuario(nuevo_usuario, nueva_contrasena)

    elif opcion == "3":
        print("¡Hasta pronto!")
        exit()

    else:
        print("Opción no valida, Intente nuevamente.")
        pass