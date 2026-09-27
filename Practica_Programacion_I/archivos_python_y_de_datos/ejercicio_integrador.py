# EJERCICIO INTEGRADOR

# ● Sistema de Gestión de Biblioteca


# Descripción:
# Desarrolla un sistema de gestión de biblioteca utilizando programación orientada a objetos en Python. 
# El sistema debe permitir
# gestionar libros, revistas y periódicos. Cada uno de estos elementos debe ser representado
#  como una clase con sus respectivas
# propiedades y métodos. Además, se deben implementar las siguientes funcionalidades:

# Clases y Objetos:
# Crea una clase base Publicacion con atributos comunes como titulo, autor, y anio_publicacion.
# Crea clases derivadas Libro, Revista y Periodico que hereden de Publicacion.

# Métodos y Funciones:
# Implementa métodos en cada clase para mostrar información detallada de la publicación.
# Implementa un método en la clase Libro para indicar si el libro está disponible para préstamo.

# Herencia:
# Utiliza herencia para que Libro, Revista y Periodico hereden de Publicacion.
# Polimorfismo:
# Implementa polimorfismo mediante un método común en la clase base que sea sobrescrito en 
# las clases derivadas.

# Encapsulamiento:
# Utiliza atributos privados y métodos getter y setter para acceder y modificar 
# los atributos de las publicaciones.
# Uso de super():
# Utiliza super() en las clases derivadas para llamar al constructor de la clase base.

# class Publicacion:
#     def __init__(self, titulo, autor, anio_publicacion):
#         self.__titulo = titulo
#         self.__autor = autor
#         self.__anio_publicacion = anio_publicacion

#     def mostrar_informacion(self):
#         pass

#     def modificar_informacion(self):
#         pass

# class Libro(Publicacion):
#     def __init__(self, titulo, autor, anio_publicacion, estado, genero):
#         super().__init__(titulo, autor, anio_publicacion)

#         self.__estado = estado
#         self.__genero = genero

#     def mostrar_informacion(self):
#         print(f"La los datos de publicación son:\n1- {self._Publicacion__titulo}\n2- En el año {self._Publicacion__anio_publicacion}\n3- Por el autor {self._Publicacion__autor}")
#         print(f"4- Género {self.__genero}\n5- {self.__estado}")

#     def modificar_informacion(self, nuevo_genero, nuevo_titulo):
#         self.__genero = nuevo_genero
#         self.__titulo = nuevo_titulo
        
#         if self.__estado == True:
#             print(f"El libro {self.__titulo} del genero {self.__genero} se encuentra disponible.")

#         else:
#             print(f"El libro {self.__titulo} del genero {self.__genero} no se encuentra disponible.")

#     def estado_de_libro(self):
#         if self.__estado == True:
#             print(f"El libro {self.__titulo} se encuentra disponible.")

#         else:
#             print(f"El libro {self.__titulo} no se encuentra disponible.")

# class Revista(Publicacion):
#     def __init__(self, titulo, autor, anio_publicacion, catalogo, orientacion):
#         super().__init__(titulo, autor, anio_publicacion)

#         self.__catalogo = catalogo
#         self.__orientacion = orientacion

#     def mostrar_informacion(self):
#         print(f"La información de esta Revista es la siguiente:\n1- {self._Publicacion__titulo}\n2- {self.__catalogo}\n3- Orientación {self.__orientacion}")

#     def modificar_informacion(self, nueva_orientacion):
#         self.__orientacion = nueva_orientacion

#         print(f"La revista {self._Publicacion__titulo} cambio su orientación, ahora es orientada a {self.__orientacion}.\n")

# class Periodico(Publicacion):
#     def __init__(self, titulo, autor, anio_publicacion, editorial):
#         super().__init__(titulo, autor, anio_publicacion)

#         self.__editorial = editorial

#     def mostrar_informacion(self):
#         print(f"Este diario es de la {self.__editorial}\nCon {self._Publicacion__titulo} como titulo\nPublicado en {self._Publicacion__anio_publicacion}")

#     def modificar_informacion(self, nueva_editorial):
#         self.__editorial = nueva_editorial
    
#         print(f"El dueño de este dairio cambio, ahora es de la editorial {self.__editorial}.\n")


# diario = Periodico("Electrodomesticos", "Gaston", "14/05/2004", "Clarin")
# diario.mostrar_informacion()
# diario.modificar_informacion("La Nación")

# revista = Revista("Recetas de comida", "Santino Kucich", "21/05/2004", "Ingredientes", "Alimentos")
# revista.mostrar_informacion()
# revista.modificar_informacion("Comidas alemanas")

# libro = Libro("Percy Jackson", "Joan Jackson", "15/05/2004", False, "Aventura")
# libro.mostrar_informacion()
# libro.modificar_informacion("Ana Jackson", "Terror")
# libro.estado_de_libro()


class Padre():
    def __init__(self, nombre):
        
        self.nombre = nombre

    def mostrar_nombre(self):
        print("Mi nombre de papa es: " + self.nombre)


class Hijo(Padre):
    def __init__(self, nombre, edad):
        super().__init__(nombre)

        self.edad = edad

    def mostrar_nombre(self):
        print(f"Mi nombre de hijo es: {self.nombre}")


papa_juan = Padre("Juan")
papa_pedro = Padre("Pedro")
print(papa_juan)

hijo_jose = Hijo("Jose", 19)
hijo_jose.mostrar_nombre()