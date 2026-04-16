#------------------------------------------------------------------------
#  TRABAJO PRÁCTICO 
#------------------------------------------------------------------------
# CONSIGNA:
# Implementar dos clases:
# - Series → representa una columna de datos.
# - DataFrame → representa una tabla (con varias Series).
#
# Objetivo: crear una mini-versión de pandas para manejar datos.
#------------------------------------------------------------------------

######################################################################################

#------------------------------------------------------------------------
# TRABAJO PRÁCTICO FINAL
#------------------------------------------------------------------------
# Clase: Series
#------------------------------------------------------------------------
# Objetivo:
# Implementar una versión básica de la estructura Series (similar a pandas.Series)
#------------------------------------------------------------------------
from statistics import mean, pstdev as std, pvariance as var
from math import prod as product


class Series:
    def __init__(self, lista, name=" ", dtype=None):
        # Validar que name sea cadena de texto
        if not isinstance(name, str):
            raise TypeError("El parámetro (name) debe ser una cadena de texto (str)")

        # Determinar tipo si no se pasa dtype
        if dtype is None:

            # Chequea que toda la lista tenga solo un tipo de dato o valores nulos

            if all(isinstance(x, bool) or x is None for x in lista):
                dtype = bool
            
            elif all(isinstance(x, int) or x is None for x in lista):
                dtype = int

            elif all(isinstance(x, float) or x is None for x in lista):
                dtype = float

            elif all(isinstance(x, str) or x is None for x in lista):
                dtype = str

            else:
                raise TypeError("Los elementos deben ser del mismo tipo")
            
        else:
            tipos_validos = [int, float, str, bool]
            if dtype not in tipos_validos:
                raise ValueError(f"dtype inválido. Debe ser uno de {tipos_validos}")

        # Si dtype es float, convertir ints a float
        if dtype == float:
            try:
                lista = [float(x) if x is not None else None for x in lista]

            except ValueError:
                print(("Los elementos deben ser del mismo tipo"))

        # Atributos de Series
        self.lista = lista
        self.len = len(lista)
        self.dtype = dtype
        self.name = name

    # Metodos de Series

    def clone(self):
        pass

    def head(self, n=5):

        contador = 0
        valores = []

        for i in self.lista: 
            if contador == n:
                break

            valores.append(i)
            contador += 1

        return self.__str__(valores)

    def tail(self, n=5):
        
        contador = 0
        valores = []

        for i in self.lista[::-1]: 
            if contador == n:
                break

            valores.append(i)
            contador += 1

        return self.__str__(valores)

    def append(self, x):

        if type(x) != self.dtype:
            print(f"No se pueden agregar datos diferentes de dtype({self.dtype})...")
        
        else:
            self.lista.append(x)
            return self.__str__()

    def extend(self, s):

        for elem in s:
        
            # Permitir None siempre
            if elem is None:
                continue
            
            # Si no es del tipo correcto → error
            if not isinstance(elem, self.dtype):
                print(f"No se puede extender: '{elem}' no coincide con dtype {self.dtype.__name__}.")
                return
    
        # Si pasaron todas las validaciones
        self.lista.extend(s)
        return self.__str__()

    def filter(self, f):
        
        nueva_lista = []
        for i in self.lista:
            if i is None:
                continue   # Permitir los valores == None

            if f(i):
                nueva_lista.append(i)

        return self.__str__(nueva_lista)

    def where(self, f):
        pass

    def is_null(self):
        pass

    def is_not_null(self):
        pass

    def fill_null(self, x):
        pass

    def rename(self, name):
        pass

    def sort(self, descending=False):
        pass

    def argsort(self, descending=False):
        pass


    # Representación textual

    def __str__(self, valores=None): # mas amigable

        if valores is None:
            valores = self.lista
            
        if len(valores) <= 10:
            cuerpo = "\n".join([f"    {x}" for x in valores])

        else:
            cuerpo = "\n".join([f"    {x}" for x in valores[:5]]) + "\n    ...\n" + "\n".join([f"    {x}" for x in valores[-5:]])
        
        return (f"# Series: '{self.name}'\n"
                f"# len: {self.len}\n"
                f"# dtype: {self.dtype}\n"
                f"# [\n{cuerpo}\n# ]")

    def __repr__(self): # Técnico 
        valores = self.lista
        cuerpo = "\n".join([f"    {x}" for x in valores])

        return(f"Series: '{self.name}'\n"
                f"len: {self.len}\n"
                f"dtype: {self.dtype}\n" 
                f"[\n{cuerpo}\n]")
    
    def espacio(): # Meti todas las funciones aca para que no molesten, 
                   # despues hay que borrar def espacio() y desidentar todos los metodos de Series.
        # ---------------------------------------------------------
        # Acceso e iteración
        # ---------------------------------------------------------
        def __len__(self):  # Longitud de la serie
            return self.len

        def __contains__(self, item):  # Determina si item se encuentra en la serie
            return item in self.lista

        def __getitem__(self, index):  # __getitem__(self, index)
            return self.lista[index]

        def __iter__(self):  # __iter__(self)
            return iter(self.lista)

        # ---------------------------------------------------------
        # Comparaciones
        # ---------------------------------------------------------
        def __eq__(self, other):
            if isinstance(other, Series):
                if self.len != other.len:
                    raise ValueError("Las Series deben tener la misma longitud")
                result = [x == y for x, y in zip(self.lista, other.lista)]
            else:
                result = [x == other for x in self.lista]
            return Series(result, name=self.name, dtype="bool")

        def __gt__(self, other):
            if isinstance(other, Series):
                if self.len != other.len:
                    raise ValueError("Las Series deben tener la misma longitud")
                result = [x > y for x, y in zip(self.lista, other.lista)]
            else:
                result = [x > other for x in self.lista]
            return Series(result, name=self.name, dtype="bool")

        def __ge__(self, other):
            if isinstance(other, Series):
                if self.len != other.len:
                    raise ValueError("Las Series deben tener la misma longitud")
                result = [x >= y for x, y in zip(self.lista, other.lista)]
            else:
                result = [x >= other for x in self.lista]
            return Series(result, name=self.name, dtype="bool")

        # ---------------------------------------------------------
        # Operaciones aritméticas
        # ---------------------------------------------------------
        def __add__(self, other):
            if isinstance(other, Series):
                result = [x + y for x, y in zip(self.lista, other.lista)]
            else:
                result = [x + other for x in self.lista]
            return Series(result, name=self.name, dtype="float" if self.dtype == "float" or isinstance(other, float) else self.dtype)

        def __sub__(self, other):
            if isinstance(other, Series):
                result = [x - y for x, y in zip(self.lista, other.lista)]
            else:
                result = [x - other for x in self.lista]
            return Series(result, name=self.name, dtype="float")

        def __mul__(self, other):
            if isinstance(other, Series):
                result = [x * y for x, y in zip(self.lista, other.lista)]
            else:
                result = [x * other for x in self.lista]
            return Series(result, name=self.name, dtype="float")

        def __truediv__(self, other):
            if isinstance(other, Series):
                result = [x / y for x, y in zip(self.lista, other.lista)]
            else:
                result = [x / other for x in self.lista]
            return Series(result, name=self.name, dtype="float")

        def __pow__(self, other):
            if isinstance(other, Series):
                result = [x ** y for x, y in zip(self.lista, other.lista)]
            else:
                result = [x ** other for x in self.lista]
            return Series(result, name=self.name, dtype="float")
        #	El valor más pequeño.
        def min(self):
            return min(self.lista)
        #  El valor mas grande
        def max(self):
            return max(self.lista)
        # La suma de los elementos.
        def sum (self):
            return sum(self.lista)
        # El promedio de los elementos.
        def mean (self):
            return mean(self.lista)
        # El producto de los elementos.
        def product(self):
            return product(self.lista)
        # El desvío estandar
        def std (self):
            return std(self.lista)
        # La varianza
        def var (self):
            return var (self.lista)


s1 = Series([1, 4, 5, 2, 10, 7, 400], "Números", int)
s2 = Series([True, True, False, True])
s3 = Series([500,600,700], "cientos", int)
s4 = Series(["hola", "adios", "chau", "buenas tardes"])
print("\n")

# print(s1.dtype)
# print(s2.dtype)
# print(s3.dtype)
# print(s4.dtype)



#print(s1.filter(lambda x: x > 5))
#print(s1.append(1000))
# print(s1.lista)
# print(s1.lista)
# print(s1.extend(s3.lista))
# print(s1.lista)

#print(s3)
#s1.head()
#print(s1.tail(3))
# print(s1.lista)
# print(s1.append(1000))
# print(s1.lista)

# c = 50





# s1.min()     # 1
# s1.max()     # 9
# s1.sum()     # 55
# s1.mean()    # 5.5
# s1.product() # 3628800
# s1.std()     # 2.87228
# s1.var()     # 8.25

# # s= Series([1, 4, 5, 2, 10, 6, 3, 7, "hola", 9], "robin", "float")
# # s

# # Ejemplo 1
# serie = Series([1, 2, 3, 4])
# serie

# Series: ''
# len: 4
# dtype: int
# [
#     1
#     2
#     3
#     4
# ]