
# while True:

#     print("¡Bienvenidos a la agencia de viajes!")
#     print("1- Consultar viajes.\n2- Consultar hoteles.")

#     opcion = input("Ingrese una opcion: ")

#     if opcion == "1":
#         print("Viajes\n")

#     elif opcion == "2":
#         print("Hoteles\n")

#     else:
#         print("Opción no valida, intente nuevamente.")
#         pass

# import requests

# url = "https://booking-com15.p.rapidapi.com/api/v1/hotels/searchDestination"

# querystring = {"query": "Buenos Aires"}

# headers = {
#     "x-rapidapi-key": "182a9fa00bmsh1f9c7a1a71822ecp1eddb8jsndb1db7264d06",
#     "x-rapidapi-host": "booking-com15.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)
# print(response.json())

import requests
from datetime import date, timedelta
import json



# Fechas de ejemplo: hoy y mañana
checkin = date.today()
checkout = checkin + timedelta(days=1)

# Paso 1: Buscar ID del destino
def obtener_dest_id(ciudad):
    url = "https://booking-com15.p.rapidapi.com/api/v1/hotels/searchDestination"
    querystring = {"query": ciudad}
    headers = {
        "x-rapidapi-key": "182a9fa00bmsh1f9c7a1a71822ecp1eddb8jsndb1db7264d06",
        "x-rapidapi-host": "booking-com15.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    if "data" in data and len(data["data"]) > 0:
        return data["data"][0]["dest_id"]
    else:
        return None

# Paso 2: Buscar hoteles con arrival_date y departure_date
def buscar_hoteles(dest_id):
    url = "https://booking-com15.p.rapidapi.com/api/v1/hotels/searchHotels"
    querystring = {
        "dest_id": dest_id,
        "search_type": "CITY",
        "adults": "2",
        "room_qty": "1",
        "page_number": "1",
        "units": "metric",
        "languagecode": "es-ar",
        "currency_code": "ARS",
        "arrival_date": checkin.strftime("%Y-%m-%d"),     # 👈 Cambio aquí
        "departure_date": checkout.strftime("%Y-%m-%d")   # 👈 Cambio aquí
    }

    headers = {
        "x-rapidapi-key": "182a9fa00bmsh1f9c7a1a71822ecp1eddb8jsndb1db7264d06",
        "x-rapidapi-host": "booking-com15.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    return response.json()

# Ejecución
ciudad = input("Ingrese la ciudad (ej. Buenos Aires): ")
dest_id = obtener_dest_id(ciudad)

if dest_id:
    print(f"✅ ID encontrado para {ciudad}: {dest_id}")
    hoteles = buscar_hoteles(dest_id)
    
    print(json.dumps(hoteles, indent=4, ensure_ascii=False))

    print("🔍 Respuesta hoteles:", hoteles)  # Debug completo

    if "data" in hoteles and "hotels" in hoteles["data"] and len(hoteles["data"]["hotels"]) > 0:
        print("\n🏨 Hoteles encontrados:")
        for hotel in hoteles["data"]["hotels"][:5]:
            nombre = hotel.get("hotel_name", "Sin nombre")
            precio = hotel.get("price", {}).get("total", "Sin precio")
            puntuacion = hotel.get("review_score_word", "Sin puntuación")
            print(f"- {nombre} | Precio: {precio} ARS | Puntuación: {puntuacion}")
    else:
        print("⚠ No se encontraron hoteles en esta ciudad.")
else:
    print("⚠ No se encontró la ciudad en la base de datos.")