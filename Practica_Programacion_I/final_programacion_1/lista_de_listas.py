dicc = {
  "status": True,
  "message": "Success",
  "timestamp": 1757105850165,
  "data": [
    {
      "dest_id": "-989774",
      "search_type": "city",
      "nr_hotels": 34,
      "country": "Argentina",
      "city_ufi": None,
      "roundtrip": "GhBhY2MyOTM1ZDIwYmQwZmYyIAAoATICZW46GEZ1bmVzIFNhbnRhIEZlIEFyZ2VudGluYUAASgBQAA==",
      "type": "ci",
      "longitude": -60.81049,
      "label": "Funes, Santa Fe Province, Argentina",
      "latitude": -32.91683,
      "hotels": 34,
      "lc": "en",
      "city_name": "Funes",
      "dest_type": "city",
      "name": "Funes",
      "cc1": "ar",
      "region": "Santa Fe Province"
    },
    {
      "dest_id": "4389634",
      "search_type": "hotel",
      "nr_hotels": 1,
      "country": "Argentina",
      "city_ufi": -989774,
      "type": "ho",
      "roundtrip": "GhBhY2MyOTM1ZDIwYmQwZmYyIAEoATICZW46GEZ1bmVzIFNhbnRhIEZlIEFyZ2VudGluYUAASgBQAA==",
      "latitude": -32.90892,
      "hotels": 1,
      "longitude": -60.866375,
      "label": "CASA FUNES, Funes, Santa Fe Province, Argentina",
      "lc": "en",
      "city_name": "Funes",
      "dest_type": "hotel",
      "name": "CASA FUNES",
      "image_url": "https://cf.bstatic.com/xdata/images/hotel/150x150/289981683.jpg?k=923dfb6e7b99ef67ee17e69b849c2df4019fdd0a6b1dc60247b90b90b71643c6&o=",
      "region": "Santa Fe Province",
      "cc1": "ar"
    },
    {
      "dest_id": "13017831",
      "search_type": "hotel",
      "image_url": "https://cf.bstatic.com/xdata/images/hotel/150x150/608618665.jpg?k=ddffa5dfe0350c2954dda1e7170ad71fc53bd3cbb58fdfbb90910a74f1f9fcb1&o=",
      "region": "Santa Fe Province",
      "cc1": "ar",
      "name": "Funes casa",
      "dest_type": "hotel",
      "lc": "en",
      "city_name": "Funes",
      "latitude": -32.9089,
      "hotels": 1,
      "longitude": -60.801968,
      "label": "Funes casa, Funes, Santa Fe Province, Argentina",
      "type": "ho",
      "roundtrip": "GhBhY2MyOTM1ZDIwYmQwZmYyIAIoATICZW46GEZ1bmVzIFNhbnRhIEZlIEFyZ2VudGluYUAASgBQAA==",
      "nr_hotels": 1,
      "city_ufi": -989774,
      "country": "Argentina"
    },
    {
      "dest_id": "13384012",
      "search_type": "hotel",
      "dest_type": "hotel",
      "city_name": "Funes",
      "lc": "en",
      "image_url": "https://cf.bstatic.com/xdata/images/hotel/150x150/700373663.jpg?k=31219374d740d154b44a1937b8a608ea878490f7d33976cadebe2036c375bf09&o=",
      "region": "Santa Fe Province",
      "cc1": "ar",
      "name": "Funes Inn",
      "country": "Argentina",
      "city_ufi": -989774,
      "nr_hotels": 1,
      "hotels": 1,
      "latitude": -32.91446,
      "label": "Funes Inn, Funes, Santa Fe Province, Argentina",
      "longitude": -60.7917,
      "type": "ho",
      "roundtrip": "GhBhY2MyOTM1ZDIwYmQwZmYyIAMoATICZW46GEZ1bmVzIFNhbnRhIEZlIEFyZ2VudGluYUAASgBQAA=="
    },
    {
      "dest_id": "14744412",
      "search_type": "hotel",
      "dest_type": "hotel",
      "lc": "en",
      "city_name": "Funes",
      "image_url": "https://cf.bstatic.com/xdata/images/hotel/150x150/729568562.jpg?k=92e1de0d12b95b7e66f39d579f10d9b2fd0b3486ab6baf158af2fa19a3d4a9b2&o=",
      "region": "Santa Fe Province",
      "cc1": "ar",
      "name": "Casa Funes Town",
      "nr_hotels": 1,
      "country": "Argentina",
      "city_ufi": -989774,
      "latitude": -32.90259,
      "hotels": 1,
      "longitude": -60.86029,
      "label": "Casa Funes Town, Funes, Santa Fe Province, Argentina",
      "type": "ho",
      "roundtrip": "GhBhY2MyOTM1ZDIwYmQwZmYyIAQoATICZW46GEZ1bmVzIFNhbnRhIEZlIEFyZ2VudGluYUAASgBQAA=="
    }
  ]
}

#print(f"{indice}- {diccionarios['name']}")
diccionario = {}
indice = 1

for diccionarios in dicc["data"]:
    if "name" in diccionarios and diccionarios["search_type"] == "hotel":
      diccionario[indice] = [diccionarios['name'], diccionarios['dest_id'], diccionarios['search_type']]
      print(indice ,diccionario[indice][0])
      indice += 1

print(diccionario)
seleccion = int(input("Seleccione el Hotel que desea para ver sus caracteristicas: "))
print(f"Hotel: {diccionario[seleccion][0]}")
print(f"Su ID es: {diccionario[seleccion][1]}")       
print(f"Tipo o Ubicación: {diccionario[seleccion][2]}") 


# print("\n --- Hoteles Disponibles --- \n")
        # for indice, diccionarios in enumerate(data["data"], start=1):
        #     if "name" in diccionarios and diccionarios["search_type"] == "hotel":
        #         indice -= 1
        #         diccionario_de_hoteles[indice] = [diccionarios['name'], diccionarios['dest_id'], diccionarios['search_type']]
        #         print(indice ,diccionario_de_hoteles[indice][0])
        # print(diccionario_de_hoteles)
        
        # seleccion = int(input("Seleccione el Hotel que desea para ver sus caracteristicas: "))
        # print(f"Hotel: {diccionario_de_hoteles[seleccion][0]}")
        # print(f"Su ID es: {diccionario_de_hoteles[seleccion][1]}")       
        # print(f"Tipo o Ubicación: {diccionario_de_hoteles[seleccion][2]}") 