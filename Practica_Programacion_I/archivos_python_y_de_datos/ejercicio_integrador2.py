# 1.Biblioteca:
# •Atributos: catalogo (lista de libros), usuarios (lista de usuarios)
# •Métodos: agregar_libro(libro), prestar_libro(libro, usuario), devolver_libro(libro, usuario), consultar_catalogo()
# 2.Libro:
# •Atributos: titulo (privado), autor (privado), disponible (privado)
# •Métodos: __init__(titulo, autor), get_titulo(), get_autor(), is_disponible(), prestar(), devolver()

# TEMA: SISTEMA DE GESTIÓN DE BIBLIOTECA
# 3.Usuario:
# •Atributos: nombre (privado), libros_prestados (lista de libros)
# •Métodos: __init__(nombre), get_nombre(), prestar_libro(libro), devolver_libro(libro)
# 4.Empleado (hereda de Usuario):
# •Métodos: agregar_libro(libro)

class Biblioteca:
    def __init__(self):
        self.catalogo = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.catalogo.append(libro)
        print(self.catalogo)

    def prestar_libro(self, libro, usuario):
        print(f"El libro {libro} fue prestado a {usuario}.")
        self.usuarios.append(usuario)

    def devolver_libro(self, libro, usuario):
        print(f"El usuario {usuario} devolvio el libro {libro}.")

    def consultar_catalogo(self):
        print(f"El catalogo disponible es el siguiente:\n{self.catalogo}")

class Libro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor
        self.estado = True

    def get_titulo(self):
        print(f"El titulo de este libro es {self.__titulo}.")

    def get_autor(self):
        print(f"El autor de este libro es {self.__autor}.")

    def is_disponible(self):
        if self.estado == True:
            print(f"El libro esta disponible.")
        else:
            print("El libro no esta disponible.")

    def prestar(self):
        self.estado = False

    def devolver(self):
        self.estado = True

class Usuario:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.libros_prestados = []

    def get_nombre(self):
        print(f"Nombre de usuario: {self.__nombre}.")

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)
        print(self.libros_prestados)

    def devolver_libro(self, libro):
        self.libros_prestados.remove(libro)
        print(self.libros_prestados)

class Empleado(Usuario):
    def __init__(self, nombre):
        super().__init__(nombre)
        
        self.nuevos_libros = []

    def agregar_libro(self, libro):
        self.nuevos_libros.append(libro)
        print(self.nuevos_libros)
  
biblioteca = Biblioteca()
biblioteca.agregar_libro("Blanca Nieves")
biblioteca.prestar_libro("Tortugas Ninja", "Arthur")
biblioteca.devolver_libro("Cocinas espectaculares", "Fausto")
biblioteca.consultar_catalogo()

libro = Libro("Ancianas en bikini", "Norma")
libro.get_titulo()
libro.get_autor()
libro.prestar()
libro.is_disponible()
libro.devolver()
libro.is_disponible()

user = Usuario("Santino")
user.get_nombre()
user.prestar_libro("Superman")
user.devolver_libro("Superman")

empleado = Empleado("Jazmin")
empleado.agregar_libro("Ratatouile")