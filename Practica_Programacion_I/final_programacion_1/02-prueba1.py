import requests

print("¡Bienvenidos a la agencia de viajes!")

# Menu principal

while True:

    print("1- Consultar viajes.\n2- Consultar hoteles.")

    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        print("Viajes\n")

    elif opcion == "2":

        # Buscar país, provincia y ciudad
        
        pais = input("Ingrese el país donde desea buscar un Hotel: ")

        provincia = input("Ingrese el nombre de la provincia en se ubicara: ")

        ciudad = input("Ingrese el nombre de la ciudad donde iniciar la busqueda: ")

        # Consulta a la API

        url_1 = "https://booking-com15.p.rapidapi.com/api/v1/hotels/searchDestination"

        # querystring = {"query": ciudad + " " + provincia + " " + pais}
        querystring = {"query": pais}
        print(querystring)

        headers = {
            "x-rapidapi-key": "182a9fa00bmsh1f9c7a1a71822ecp1eddb8jsndb1db7264d06",
            "x-rapidapi-host": "booking-com15.p.rapidapi.com"
        }

        response = requests.get(url_1, headers=headers, params=querystring)
        data = response.json()
        
        if "data" in data:
            for diccionarios in data["data"]:
                if "name" in diccionarios:
                    print(diccionarios["name"])