# lista = [1,2,3,4,5,6,7,8,9,10]

# if 11 not in lista:
#     print("verdadero")

class Persona:
    def  __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        print(self.__nombre)
    
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
        return self.__nombre
    
    def set_edad(self, nueva_edad):
        self.__edad = nueva_edad
        return self.__edad

san = Persona("Santino", "21")
san.get_nombre()

san.set_nombre("Santi")
san.get_nombre()
