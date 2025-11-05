# Módulos y Librerias

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
            "x-rapidapi-key": "4c3e31a8c3msh13653f487510d5ep18801ejsn60c95ffe982b",
            "x-rapidapi-host": "booking-com15.p.rapidapi.com"
        }

        response = requests.get(url_1, headers=headers, params=querystring)
        print(response)
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
          "x-rapidapi-key": "4c3e31a8c3msh13653f487510d5ep18801ejsn60c95ffe982b",
          "x-rapidapi-host": "booking-com15.p.rapidapi.com"
        }

        response = requests.get(url_2, headers=headers, params=querystring2)
        data_regiones_de_hoteles = response.json()
        print(response)

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

class Aeropuerto:
    def __init__(self, origen, destino):
        self.origen = origen
        self.destino = destino

    def consultar_aeropuertos(self):
        """Consultamos los aeropuertos en los lugares seleccionados por el usuario,
           estos datos se buscan en Search Flight Location"""

        url = "https://booking-com15.p.rapidapi.com/api/v1/flights/searchDestination"

        querystring_origen = {f"query":{self.origen}}
        querystring_destino = {f"query":{self.destino}}

        headers = {
            "x-rapidapi-key": "4c3e31a8c3msh13653f487510d5ep18801ejsn60c95ffe982b",
            "x-rapidapi-host": "booking-com15.p.rapidapi.com"
        }

        response_aero_origen = requests.get(url, headers=headers, params=querystring_origen)
        response_aero_destino = requests.get(url, headers=headers, params=querystring_destino)
        print(response_aero_origen, response_aero_destino)
        data_aero_origen = response_aero_origen.json()
        data_aero_destino = response_aero_destino.json()

        return data_aero_origen, data_aero_destino

    def mostrar_aeropuertos_region_origen(self, aeropuertos_origen):
        
        indice = 1
        for aeropuerto_origen in aeropuertos_origen["data"]:
            if aeropuerto_origen["type"].upper() == "AIRPORT":
                
                diccionario_aeropuertos_origen[indice] = [aeropuerto_origen["name"], aeropuerto_origen["id"], aeropuerto_origen["type"]]
                print(indice, " " ,aeropuerto_origen["name"])
                indice += 1

        return diccionario_aeropuertos_origen

    def mostrar_aeropuertos_region_destino(self, aeropuertos_destino):

        indice = 1
        for aeropuerto_destino in aeropuertos_destino["data"]:
            if aeropuerto_destino["type"].upper() == "AIRPORT":
                
                diccionario_aeropuertos_destino[indice] = [aeropuerto_destino["name"], aeropuerto_destino["id"], aeropuerto_destino["type"]]
                print(indice, " " ,aeropuerto_destino["name"])
                indice += 1

        return diccionario_aeropuertos_destino

class Vuelo:
    def __init__(self, aeropuertos_de_origen, aeropuertos_de_destino, fecha_de_salida):
        self.aeropuertos_de_origen = aeropuertos_de_origen
        self.aeropuertos_de_destino = aeropuertos_de_destino
        self.fecha_de_salida = fecha_de_salida

    def consultar_vuelos(self, origen_seleccionado, destino_seleccionado):
        """Consultamos los vuelos disponibles entre los aeropuertos seleccionados, y mostramos sus datos."""

        url = "https://booking-com15.p.rapidapi.com/api/v1/flights/searchFlights"

        querystring = {"fromId":{self.aeropuertos_de_origen[origen_seleccionado][1]},"toId":{self.aeropuertos_de_destino[destino_seleccionado][1]}, "departDate":{self.fecha_de_salida},"stops":"none","pageNo":"1","adults":"1","children":"0,17","sort":"BEST","cabinClass":"ECONOMY","currency_code":"AED"}

        headers = {
            "x-rapidapi-key": "4c3e31a8c3msh13653f487510d5ep18801ejsn60c95ffe982b",
            "x-rapidapi-host": "booking-com15.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        print(response)
        vuelos_disponibles = response.json()

        return vuelos_disponibles

    def mostrar_vuelos(self, vuelos_encontrados, aero_origen_seleccionado, aero_destino_seleccionado):

        # Acceso directo al total de vuelos
        total_vuelos = vuelos_encontrados["data"]["aggregation"]["totalCount"]

        # Acceso a la lista de escalas
        lista_de_escalas = vuelos_encontrados["data"]["aggregation"]["stops"]

        print(f'\n--- ✈️ Total de Vuelos Encontrados: {total_vuelos} ---')
        print("--- Precios Mínimos por Opciones de Escala ---\n")

        for escala in lista_de_escalas:
            
            # --- 1. Cálculo del Precio Final ---
            
            # Acceder a los componentes del precio mínimo redondeado (minPriceRound)
            unidades = escala['minPriceRound']['units']
            nanos = escala['minPriceRound']['nanos']
            moneda = escala['minPriceRound']['currencyCode']
            
            # Combinar unidades y nanos (dividiendo nanos por 1,000,000,000 para obtener decimales)
            precio_final = unidades + (nanos / 1000000000)
            
            # --- 2. Extracción de Otros Datos ---
            
            vuelos_count = escala['count']
            num_escalas = escala['numberOfStops']
            aerolinea = escala['cheapestAirline']['name']
            
            # Formato de salida
            etiqueta_escala = "Vuelo Directo" if num_escalas == 0 else f"{num_escalas} Escala(s)"
            
            # --- 3. Imprimir el Resumen ---
            
            print(f"| {etiqueta_escala} ({vuelos_count} opciones)")
            print(f"|   Precio Mínimo: {precio_final:,.2f} {moneda}")
            print(f"|   Aerolínea más barata: {aerolinea}")
            print("-" * 30)

            while True:
                escala_seleccionada = pidiendo_mensaje("\nSeleccione el número de escala para reservar el vuelo: ")

                if escala_seleccionada == "0" or escala_seleccionada == "1" or escala_seleccionada == "2":
                    break

                else:
                    print("Escala seleccionada no valida... Intente nuevamente.\n")

            lista_de_valores_reserva = [self.aeropuertos_de_origen[aero_origen_seleccionado][0], self.aeropuertos_de_destino[aero_destino_seleccionado][0], 
                                        self.fecha_de_salida, aerolinea, precio_final, escala_seleccionada, moneda]
            
            return lista_de_valores_reserva

    def reservar_vuelo(self, vuelo_seleccionado):
        """Realiza la reserva de un vuelo con sus datos."""

        print(f"\n--- 🎫 Confirmación de Reserva de Vuelo ---")
        
        aerolinea = vuelo_seleccionado[3]
        precio = vuelo_seleccionado[4]
        escalas = vuelo_seleccionado[5]
        
        # 1. Solicitar datos personales para la reserva
        apellido_familiar = pidiendo_mensaje("Ingrese su Apellido: ")
        numero_adultos = pidiendo_mensaje_numerico("¿Cuántos adultos van a ser? : ")
        numero_chicos = pidiendo_mensaje_numerico("¿Cuántos niños habra? : ")

        # 2. Construir la lista de datos a guardar
        datos_reserva = [apellido_familiar, numero_adultos, numero_chicos, vuelo_seleccionado[0], 
                         vuelo_seleccionado[1], self.fecha_de_salida, aerolinea, escalas, precio]

        # 3. Abrir y escribir en el archivo CSV
        with open(archivo_vuelos, "a", newline="", encoding='utf-8') as file:
            escritura = csv.writer(file, delimiter=",")

            # Verifica si el archivo está vacío para escribir el encabezado
            if os.stat(archivo_vuelos).st_size == 0:
                encabezado = [
                    "FAMILIA", "Nº ADULTOS", "Nº NIÑOS", "ORIGEN", "DESTINO", 
                    "FECHA DE SALIDA", "AEROLÍNEA", "ESCALAS", "PRECIO FINAL"
                ]
                escritura.writerow(encabezado)
            
            # Escribe la nueva fila de reserva
            escritura.writerow(datos_reserva)

        # 4. Mensaje de confirmación
        print(f"\n--- ¡Reserva de vuelo completada con éxito! ---\n")
        print(f"Detalles:\nFamilia: {apellido_familiar}\nRuta: {vuelo_seleccionado[0]} -> {vuelo_seleccionado[1]}")
        print(f"Aerolínea: {aerolinea} ({escalas} escalas) | Precio: {precio} {vuelo_seleccionado[6]}")
        print(f"Fecha de ida: {self.fecha_de_salida}")


# Funciones

def pidiendo_mensaje(mensaje):
    """Esta función se asegura de que en cada input del usuario se ingrese un valor y no un espacio vacio"""
    while True:
        ingreso = input(mensaje)
        if ingreso:
            return ingreso
        else:
            print("Debe ingresar una opción.\n")

def pidiendo_mensaje_numerico(mensaje):
    """Verifica que se ingrese un dato y que sea un número entero mayor a cero."""

    while True:
        try:
            ingreso = int(input(mensaje))
            if ingreso and ingreso > 0:
                return ingreso
            
        except ValueError:
            print("El valor ingresado debe ser numérico y mayor a cero. Intente nuevamente...\n")

def cambiar_a_formato_fecha(fecha_de_llegada, fecha_de_partida=None):
    """Cambia el formato de las fechas ingresadas por el usuario a formato valido para consulta a la API"""

    if fecha_de_partida != None:
        # 1. Convertir los strings a objetos de fecha
        fecha_llegada_obj = datetime.strptime(fecha_de_llegada, "%d/%m/%Y")
        fecha_partida_obj = datetime.strptime(fecha_de_partida, "%d/%m/%Y")

        # 2. Formatear los objetos de fecha al formato YYYY-MM-DD
        fecha_llegada_api = fecha_llegada_obj.strftime("%Y-%m-%d")
        fecha_partida_api = fecha_partida_obj.strftime("%Y-%m-%d")

        return fecha_llegada_api, fecha_partida_api

    else:
        fecha_salida = fecha_de_llegada
        fecha_salida = datetime.strptime(fecha_de_llegada, "%d/%m/%Y")
        fecha_salida_api = fecha_salida.strftime("%Y-%m-%d")

        return fecha_salida_api

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
            limpiar_terminal()
            print(f"🎉 ¡Bienvenido, {nombre_ingresado}!\n")
            return True # ¡Éxito!
        else:
            limpiar_terminal()
            print("❌ Contraseña incorrecta.")
            print("Intente nuevamente...\n")
    else:
        limpiar_terminal()
        print("❌ Usuario no encontrado.")
        print("Debe registrarse o intentar nuevamente...\n")
        
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

def verificar_estado_respuesta(response, datos_json):
    """ Verifica el estado de la conexión HTTP y el estado interno 'status' del JSON. 
        Retorna True si la conexión es 200 y el estado interno es True.
        Retorna False en caso de errores HTTP, fallas de autenticación o errores en los datos."""

    # --- 1. VERIFICACIÓN DEL CÓDIGO DE ESTADO HTTP (Conexión) ---
    if response.status_code != 200:
        print(f"❌ Error HTTP {response.status_code}.")
        
        if response.status_code == 403:
            print("   Acceso Prohibido. Verifique su API Key.")
        elif response.status_code == 429:
            print("   Límite de solicitudes excedido. Intente en unos minutos.")
        else:
            print("   No se pudo realizar la solicitud. Código de error no manejado.")
        return False

    # Si la conexión es 200, ahora verificamos el JSON.

    # --- 2. VERIFICACIÓN DEL ESTADO INTERNO DEL JSON ('status' de la API) ---

    # Comprueba si la clave 'status' existe y si su valor es False
    if datos_json.get('status') is False:
        print("⚠️ La API reporta un error en los datos de la consulta.")
        
        # Muestra el mensaje de error específico si está disponible
        mensaje_error = datos_json.get('message', 'Error interno no especificado.')
        print(f"   Mensaje de la API: {mensaje_error}")
        return False

    # --- 3. VERIFICACIÓN DE DATOS VACÍOS (Aplica a Aeropuertos/Búsquedas) ---

    # Usa un chequeo más general si la clave 'data' está vacía o es nula
    if not datos_json.get('data'):
        # Esto ocurre cuando la búsqueda de aeropuertos o de vuelos no devuelve resultados
        print("🔍 Búsqueda sin resultados: La API no devolvió datos (posiblemente un resultado vacío).")
        return False
        
    # Si pasa todas las verificaciones
    return True

def limpiar_terminal():
    """Función que limpia la terminal cada vez que es llamada."""

    os.system("clear")


# Cuerpo del Programa

diccionario_de_regiones = {} # Diccionario en el cual guardo las regiones donde buscar los hoteles.
diccionario_de_hoteles = {} # Diccionario donde guardo los hoteles con sus caracteristicas.
diccionario_aeropuertos_origen = {} # Diccionario donde guardo los aeropuertos de origen con sus caracteristicas.
diccionario_aeropuertos_destino = {} # Diccionario donde guardo los aeropuertos de destino con sus caracteristicas.
archivo_hoteles = "reservas_de_hoteles.csv" # Archivo donde guardo las reservas realizadas por los usuarios.
archivo_usuarios = "reserva_de_usuarios.csv" # Archivo donde guardo los usuarios que se registran y sus contraseñas.
archivo_vuelos = "reserva_de_vuelos.csv" # Archivo donde guardo las reservas de vuelos ingresadas por los usuarios.

# Menu principal

while True:
    print("\n--- ¡Bienvenidos a la Agencia de Viajes y reserva de Hoteles! ---\n")
    print("1- Iniciar sesión.\n2- Registrarse.\n3- Salir.")

    opcion = pidiendo_mensaje("\nIngrese una opcion: ")

    if opcion == "1":
        limpiar_terminal()
        print("\n--- Iniciar Sesión ---\n")
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
                bandera_cero = True
                while bandera_cero:
                    limpiar_terminal()
                    print("\n--- Consultar Vuelos ---\n")
                    origen = pidiendo_mensaje("Ingrese el lugar de origen de donde partira: ")
                    destino = pidiendo_mensaje("Ingrese el lugar de destino a donde llegara: ")

                    aeropuertos = Aeropuerto(origen, destino)
                    aeropuertos_encontrados = aeropuertos.consultar_aeropuertos()
                    aeropuertos_origen_mostrados = aeropuertos.mostrar_aeropuertos_region_origen(aeropuertos_encontrados[0])
                    aeropuerto_origen_seleccionado = int(pidiendo_mensaje_numerico("\nSeleccione el Aeropuerto desde el que tomara el vuelo: "))

                    aeropuertos_destino_mostrados = aeropuertos.mostrar_aeropuertos_region_destino(aeropuertos_encontrados[1])
                    aeropuerto_destino_seleccionado = int(pidiendo_mensaje_numerico("\nSeleccione el Aeropuerto donde desea aterrizar: "))
                    
                    fecha_de_salida = pidiendo_mensaje("Ingrese la fecha en la que desea tomar el vuelo (en formato DD/MM/YYYY): ")
                    fecha_formateada = cambiar_a_formato_fecha(fecha_de_salida)
                    vuelos = Vuelo(aeropuertos_origen_mostrados, aeropuertos_destino_mostrados, fecha_formateada)
                    vuelos_disponibles = vuelos.consultar_vuelos(aeropuerto_origen_seleccionado, aeropuerto_destino_seleccionado)
                    vuelos_disponibles = vuelos.mostrar_vuelos(vuelos_disponibles, aeropuerto_origen_seleccionado, aeropuerto_destino_seleccionado)

                    while True:
                        print("\n--- Menú de Opciones ---\n1- Realizar reserva de vuelo.\n2- Consultar otros vuelos.\n3- Volver al menú principal.\n")
                        opcion_ingresada = pidiendo_mensaje("Ingrese una opción del menú: ")

                        if opcion_ingresada == "1":
                            reservar_vuelo = vuelos.reservar_vuelo(vuelos_disponibles)
                            input("\nPresione cualquier TECLA para volver al menú principal")
                            limpiar_terminal()
                            bandera_cero = False
                            break

                        elif opcion_ingresada == "2":
                            limpiar_terminal()
                            break

                        elif opcion_ingresada == "3":
                            limpiar_terminal()
                            bandera_cero = False
                            break
                            
                        else:
                            limpiar_terminal()
                            print("Opción ingresada no valida... Intente nuevamente.")    

            elif opcion_seleccionada == "2":
                print("\n--- Consultar Hoteles ---\n")
                # Buscar país, provincia y ciudad.
                
                pais = pidiendo_mensaje("Ingrese el país donde desea buscar un Hotel: ")
                provincia = pidiendo_mensaje("Ingrese el nombre de la provincia en la: ")
                ciudad = pidiendo_mensaje("Ingrese el nombre de la ciudad donde iniciar la busqueda: ")

                regiones = Region(pais, provincia, ciudad)
                regiones_encontradas = regiones.consultar_regiones()
                regiones_mostradas = regiones.mostrar_regiones(regiones_encontradas)

                seleccionar_region = int(pidiendo_mensaje_numerico("\nSeleccione la región en la desea encontrar su hotel: "))

                # Se ingresa la fecha de inicio de reserva y de partida y se convierten a formato de fecha.
                fecha_de_llegada = pidiendo_mensaje("¿En qué fecha iniciara la reserva del hotel? Complete con dd/mm/aaaa: ")
                fecha_de_partida = pidiendo_mensaje("¿Hasta qué fecha reservara en el hotel? Complete con dd/mm/aaaa: ")
                fechas_ingresadas = cambiar_a_formato_fecha(fecha_de_llegada, fecha_de_partida)

                hoteles = Hotel(regiones_mostradas, fechas_ingresadas[0], fechas_ingresadas[1])
                data_regiones_de_hoteles = hoteles.consultar_hoteles(seleccionar_region)
                bandera_uno = True

                while bandera_uno:
                    hoteles_mostrados = hoteles.mostar_hoteles(data_regiones_de_hoteles)

                    seleccionar_hotel = int(pidiendo_mensaje_numerico("\nSeleccione el hotel del que desea ver sus características: "))
                    
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