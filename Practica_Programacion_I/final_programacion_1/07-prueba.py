dicc = {
    "status": True,
    "message": "Success",
    "timestamp": 1761774459999,
    "data": [
      {
        "id": "LIM.AIRPORT",
        "type": "AIRPORT",
        "name": "Jorge Chavez International Airport",
        "code": "LIM",
        "city": "LIM",
        "cityName": "Lima",
        "regionName": "Provincia de Lima",
        "country": "PE",
        "countryName": "Peru",
        "countryNameShort": "Peru",
        "photoUri": "https://q-xx.bstatic.com/xdata/images/city/square150/644697.jpg?k=996569f86e338238f8c0e768527219cedd1075493c7b5de56684e08f20bdb776&o=",
        "distanceToCity": {
          "value": 9.514313458983848,
          "unit": "km"
        },
        "parent": "LIM"
      }
    ]
}

import requests

# diccionario_aeropuertos_origen = {}
# diccionario_aeropuertos_destino = {}
origen = input("Ingrese el lugar origen de donde va a salir: ")
destino = input("Ingrese el lugar de destino donde va a llegar: ")


# url = "https://booking-com15.p.rapidapi.com/api/v1/flights/searchDestination"

# querystring = {f"query":{origen}}

# headers = {
# 	"x-rapidapi-key": "182a9fa00bmsh1f9c7a1a71822ecp1eddb8jsndb1db7264d06",
# 	"x-rapidapi-host": "booking-com15.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

def aero(origen, destino):
    diccionario_aeropuertos_origen = {}
    diccionario_aeropuertos_destino = {}
    url = "https://booking-com15.p.rapidapi.com/api/v1/flights/searchDestination"

    querystring_origen = {f"query":{origen}}
    querystring_destino = {f"query":{destino}}

    headers = {
        "x-rapidapi-key": "182a9fa00bmsh1f9c7a1a71822ecp1eddb8jsndb1db7264d06",
        "x-rapidapi-host": "booking-com15.p.rapidapi.com"
    }

    response_aero_origen = requests.get(url, headers=headers, params=querystring_origen)
    response_aero_destino = requests.get(url, headers=headers, params=querystring_destino)


    aeropuertos_origen = response_aero_origen.json()
    aeropuertos_destino = response_aero_destino.json()

    indice = 1
    for aeropuerto_origen in aeropuertos_origen["data"]:
        if aeropuerto_origen["type"].upper() == "AIRPORT":
            
            diccionario_aeropuertos_origen[indice] = [aeropuerto_origen["name"], aeropuerto_origen["id"], aeropuerto_origen["type"]]
            print(indice, " " ,aeropuerto_origen["name"])
            indice += 1

    print("\n")
    #print(diccionario_aeropuertos_origen)
    print("\n")

    indice = 1
    for aeropuerto_destino in aeropuertos_destino["data"]:
        if aeropuerto_destino["type"].upper() == "AIRPORT":
            
            diccionario_aeropuertos_destino[indice] = [aeropuerto_destino["name"], aeropuerto_destino["id"], aeropuerto_destino["type"]]
            print(indice, " " ,aeropuerto_destino["name"])
            indice += 1

    #print(diccionario_aeropuertos_destino)

    return diccionario_aeropuertos_origen, diccionario_aeropuertos_destino


aeropuertos = aero(origen, destino)

print(type(aeropuertos))
print(len(aeropuertos))
print("\n")    
print("\n")
print(aeropuertos)
print("\n")    
print("\n")
print(aeropuertos[0])
print("\n")    
print("\n") 
print("\n")
print(aeropuertos[1])
print("\n")    
print("\n")