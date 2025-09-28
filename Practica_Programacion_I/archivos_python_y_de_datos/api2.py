import requests

def buscar_universidades(pais):
    url = "http://universities.hipolabs.com/search"
    params = {"country": pais}
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        universidades = response.json()
        
        if not universidades:
            print(f"No se encontraron universidades para {pais}.")
            return
        
        print(f"Universidades en {pais}:")
        for uni in universidades[:10]:  # mostramos solo las primeras 10
            print(f"- {uni['name']} ({uni['web_pages'][0]})")
            
    except requests.RequestException as e:
        print("Error al consultar la API:", e)

# Ejemplo de uso
buscar_universidades("Argentina")

# def obtener_dolar_oficial():
#     url = "https://dolarapi.com/v1/dolares/oficial"
#     try:
#         datos = requests.get(url).json()
#         return datos
#     except requests.RequestException as e:
#         print("Error al consultar la API:", e)
#         return None

# def imprimir_oficial():
#     data = obtener_dolar_oficial()
#     if data:
#         print(f"Dólar Oficial — compra: {data['compra']}, venta: {data['venta']}, actualizado: {data['fechaActualizacion']}")


# imprimir_oficial()