import requests
from datetime import datetime
import csv
import os

# Clases

# Funciones

def pidiendo_mensaje(mensaje):
    """Esta función se asegura de que en cada input del usuario se ingrese un valor y no un espacio vacio"""
    while True:
        ingreso = input(mensaje)
        if ingreso:
            return ingreso
        else:
            print("Debe ingresar una opción.\n")

# Cuerpo del Programa

diccionario_de_regiones = {} # Diccionario en el cual guardo las regiones donde buscar los hoteles
diccionario_de_hoteles = {} # Diccionario donde guardo los hoteles con sus caracteristicas


# Menu principal

while True:
    print("\n--- ¡Bienvenidos a la agencia de viajes! ---\n")
    print("1- Consultar viajes.\n2- Consultar hoteles.")

    opcion = pidiendo_mensaje("Ingrese una opcion: ")

    if opcion == "1":
        print("Viajes\n")

    elif opcion == "2":

        # Buscar país, provincia y ciudad. Ademas la fecha de inicio de reserva y de partida.
        
        pais = pidiendo_mensaje("Ingrese el país donde desea buscar un Hotel: ")
        provincia = pidiendo_mensaje("Ingrese el nombre de la provincia en la: ")
        ciudad = pidiendo_mensaje("Ingrese el nombre de la ciudad donde iniciar la busqueda: ")
        fecha_de_llegada = pidiendo_mensaje("¿En qué fecha iniciara la reserva del hotel? Complete con dd/mm/aaaa: ")
        fecha_de_partida = pidiendo_mensaje("¿Hasta qué fecha reservara en el hotel? Complete con dd/mm/aaaa: ")

        # 1. Convertir los strings a objetos de fecha
        fecha_llegada_obj = datetime.strptime(fecha_de_llegada, "%d/%m/%Y")
        fecha_partida_obj = datetime.strptime(fecha_de_partida, "%d/%m/%Y")

        # 2. Formatear los objetos de fecha al formato YYYY-MM-DD
        fecha_llegada_api = fecha_llegada_obj.strftime("%Y-%m-%d")
        fecha_partida_api = fecha_partida_obj.strftime("%Y-%m-%d")

        # Consulta a la API Serach Hotels Destination, 
        # para visualizar hoteles en la región ingresada por el usuario

        url_1 = "https://booking-com15.p.rapidapi.com/api/v1/hotels/searchDestination"

        querystring = {f"query":{ciudad + " " + provincia + " " + pais}}
        print(querystring)
        headers = {
            "x-rapidapi-key": "f981cd47b6mshcb3742cd4ee8522p1fdedbjsn49b886b5c874",
            "x-rapidapi-host": "booking-com15.p.rapidapi.com"
        }

        response = requests.get(url_1, headers=headers, params=querystring)
        data_hoteles = response.json()
        
        # A continuación uno de los algoritmos más importantes, el cual nos pone los hoteles enumerados
        # y nos permite seleccionar el hotel para obtener sus caracteristicas

        print("\n --- Regiones Encontradas --- \n")
        indice = 1
        for diccionarios in data_hoteles["data"]:
            if "name" in diccionarios: # Le borre esta condición: and diccionarios["search_type"] == "hotel"
                diccionario_de_regiones[indice] = [diccionarios['name'], diccionarios['dest_id'], diccionarios['search_type']]
                print(indice ,diccionario_de_regiones[indice][0])
                indice += 1
        print(diccionario_de_regiones)

        seleccionar_region = int(pidiendo_mensaje("\nSeleccione la región en la desea encontrar su hotel: "))

        # Consultamos a la API Serachs Hotels para mostrar los hoteles de la región
        # y para obtener y vizualizar los datos del hotel

        url_2 = "https://booking-com15.p.rapidapi.com/api/v1/hotels/searchHotels"

        querystring2 = {f"dest_id":{diccionario_de_regiones[seleccionar_region][1]},
                        "search_type":{diccionario_de_regiones[seleccionar_region][2]},
                        "arrival_date": {fecha_llegada_api}, "departure_date": {fecha_partida_api}, 
                        "units":"metric", "languagecode":"es-ar", 
                        "currency_code":"AED"}

        headers = {
          "x-rapidapi-key": "182a9fa00bmsh1f9c7a1a71822ecp1eddb8jsndb1db7264d06",
          "x-rapidapi-host": "booking-com15.p.rapidapi.com"
        }

        response = requests.get(url_2, headers=headers, params=querystring2)
        data_regiones_de_hoteles = response.json()

        while True:

            for i, hotel in enumerate(data_regiones_de_hoteles["data"]["hotels"], start=1):
                print(i, " - ", hotel["property"]["name"])

                lista_de_hoteles = [hotel["hotel_id"], hotel["property"]["name"], hotel["accessibilityLabel"], hotel["property"]["reviewScore"], hotel["property"]["reviewScoreWord"]]
                
                diccionario_de_hoteles[i] = lista_de_hoteles
            
            seleccionar_hotel = int(pidiendo_mensaje("\nSeleccione el hotel del que desea ver sus características: "))

            # Itera directamente sobre la lista de hoteles en el diccionario de datos.
            for hotel in data_regiones_de_hoteles["data"]["hotels"]:
                # Compara el valor de la clave 'hotel_id' con el ID que buscas.
                if hotel["hotel_id"] == int(diccionario_de_hoteles[seleccionar_hotel][0]):

                    hotel_seleccionado = diccionario_de_hoteles[seleccionar_hotel]
                    print(f"\nHotel : {diccionario_de_hoteles[seleccionar_hotel][1]}")
                    print(f"\nDescripción : {diccionario_de_hoteles[seleccionar_hotel][2]}")
                    print(f"\nReseñas : {diccionario_de_hoteles[seleccionar_hotel][3]}")
                    print(f"\nReseñas Globales : {diccionario_de_hoteles[seleccionar_hotel][4]}")
                    break  # Sal del bucle una vez que se encuentra el hotel.

            # if hotel["hotel_id"] == int(diccionario_de_hoteles[seleccionar_hotel][0]):
            #     # Este 'else' se ejecuta si el bucle termina sin encontrar el hotel.
            #     print(f"No se encontró ningún hotel con el ID: {int(diccionario_de_hoteles[seleccionar_hotel][0])}")
            print(hotel_seleccionado)
            seleccionar_opcion = pidiendo_mensaje("\n--- Menú de Opciones ---\n1- Realizar reserva en el Hotel\n2- Volver a mostrar lista de Hoteles\n3- Regresar al menú principal\nSeleccione una Opción: ")

            if seleccionar_opcion == "1":
                
                print(f"--- Reservación en {hotel_seleccionado[1]} ---")

                apellido_familiar = pidiendo_mensaje("\nIngrese su Apellido: ")
                numero_adultos = pidiendo_mensaje("¿Cúantos adultos van a ser? : ")
                numero_chicos = pidiendo_mensaje("¿Cúantos niños habra? : ")
                archivo = "reservas_de_hoteles.csv"
                reserva = [f"Familia: {apellido_familiar}", f"Total de adultos: {numero_adultos}", f"Total de chicos: {numero_chicos}", fecha_de_llegada, fecha_de_partida, f"Hotel: {hotel_seleccionado[1]}"]
                with open(archivo, "a", newline="") as file:
                    escritura = csv.writer(file, delimiter=",")

                    if os.stat(archivo).st_size == 0:
                        encabezado = ["FAMILIA", "Nº DE ADULTOS", "Nº DE NIÑOS", "FECHA DE LLEGADA", "FECHA DE SALIDA","NOMBRE DEL HOTEL"]
                        escritura.writerow(encabezado)
                    
                    escritura.writerows(reserva)
                print("--- ¡Reservación completada con exito!")
                print(f"Detalles de reserva: {reserva}")
                # Menú : para volver a hacer otra reserva mostrando hoteles, o volver al menú principal
                input("\nPuasa")

            elif seleccionar_opcion == "2":
                pass

            elif seleccionar_opcion == "3":
                break

            else:
                print("Opción no valida, intente nuevamente...\n")

    else:
        print("Opción no valida, intente nuevamente.")
        pass
