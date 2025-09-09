# class Auto:
#     marca = ""
#     modelo = 2004
#     placa = ""

# taxi = Auto()
# print(taxi.modelo)

# class Jugadores_A:
#     j1 = "messi"
#     j2 = "c.ronaldo"

# class Jugadores_B:
#     j3 = "marcelo"
#     j1 = "falcao"

# print(Jugadores_B.j1)
# print(Jugadores_A.j1)

# class Auto_taxi:
#     marca = "nissan"
#     modelo = 2004
#     placa = "123-ABC"

# class Auto_patrullero:
#     marca = "nissan"
#     modelo = 2017
#     placa = "789-XYZ"

# taxi = Auto_taxi()
# patrullero = Auto_patrullero()

# print(taxi)

# class Nombre:
#     pass

# victor = Nombre()
# maria = Nombre()

# victor.edad = 30
# victor.sexo = "Masculino"
# victor.pais = "Argentina"

# maria.edad = 25
# maria.sexo = "Femenino"
# maria.pais = "Brazil"

# print(victor.edad)
# print(maria.edad)

# class Auto:
#     pass

# taxi = Auto()
# patrullero = Auto()

# taxi.marca = "nissan"
# taxi.modelo = 2004
# taxi.placa = "123-ABC"

# patrullero.marca = "toyota"
# patrullero.modelo = 2017
# patrullero.placa = "789-XYZ"

# print(taxi.marca)
# print(patrullero.marca)

# class Matematica:
#     def suma(self):
#         self.n1 = 2
#         self.n2 = 3

# S = Matematica()

# S.suma()

# print(S.n1 + S.n2)

# class Auto:
#     def Caracteristicas(self):
#         self.marca = ""
#         self.modelo = 2004
#         self.placa = ""

# taxi = Auto()
# taxi.Caracteristicas()
# taxi.marca = "nissan"
# taxi.placa = "123-ABC"

# print("El modelo del auto es", taxi.modelo)
# print("La marca del auto es", taxi.marca)
# print("La placa del auto es", taxi.placa)

# class Ropa:
#     def __init__(self):
#         self.marca = "Willow"
#         self.talla = "M"
#         self.color = "rojo"

# camisa = Ropa()

# print(camisa.marca)
# print(camisa.talla)
# print(camisa.color)

# class Auto_taxi:
#     def __init__(self):
#         self.marca = "nissan"
#         self.modelo = 2004
#         self.placa = "123-ABC"

# taxi = Auto_taxi()

# print(taxi.marca)
# print(taxi.modelo)
# print(taxi.placa)

# class Auto:
#     def __init__(self, modelo, marca, placa):
#         self.modelo = modelo
#         self.marca = marca
#         self.placa = placa

#     def aclaracion_taxi(self):
#         print(f"Hola soy un taxi {self.modelo} marca {self.marca} y mi placa es {self.placa}")

#     def aclaracion_patrullero(self):
#         print(f"Hola soy un patrullero {self.modelo} marca {self.marca} y mi placa es {self.placa}")

#     def aclaracion_auto(self):
#         print(f"Hola soy un auto {self.modelo} marca {self.marca} y mi placa es {self.placa}")

# taxi = Auto("nissan", 2004, "123-ABC")
# patrullero = Auto("toyota", 2017, "789-XYZ")
# auto = Auto("Autasos", 2020, "567-TYO")

# taxi.aclaracion_taxi()
# patrullero.aclaracion_patrullero()
# auto.aclaracion_auto()