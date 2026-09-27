# class Contador():
#     def __init__(self, valor = 0):
#         self.valor_original = valor
#         self.valor = valor

#     def incrementar(self, cantidad = 1):
#         self.valor += cantidad
#         print(f"El valor interno es {self.valor}")
#         return self.valor
    
#     def decrementar(self, cantidad = 1):
#         self.valor -= cantidad
#         print(f"El valor interno es {self.valor}")
#         return self.valor
    
#     def reiniciar(self):
#         self.valor = self.valor_original
#         print(self.valor)
#         return self.valor
    
#     def valor(self):
#         print(f"self.valor")
#         return self.valor
    
# cuenta = Contador(10)

# cuenta.incrementar(10)

# cuenta.reiniciar()



# EJERCICIO 2

# from math import ceil

# class Pocion():
#     def __init__(self, color, volumen):
#         self.color= color
#         self.volumen = volumen

#     def get_color(self):
#         print(self.color)
#         return self.color
    
#     def get_volumen(self):
#         print(self.volumen)
#         return self.volumen

#     def mezclar(self, other):
#         print(other.volumen)
#         x = self.volumen + other.volumen
#         c1 = ceil((self.color[0] * self.volumen + other.color[0] * other.volumen) / x)
#         c2 = ceil((self.color[1] * self.volumen + other.color[1] * other.volumen) / x)
#         c3 = ceil((self.color[2] * self.volumen + other.color[2] * other.volumen) / x)
#         pocion_nuevo = Pocion([c1, c2, c3], x)
#         return pocion_nuevo


        # (c1 * v1) + (c2 * v2)
        # ---------------------
        #       v1 + v2


        # RGB = Valor1 , valor2 , valor3
        # RGB = 222 , 222 , 222
 
# 255, 255, 255

# nueva_pocion = Pocion([255, 255, 255], 7)
# otra_pocion = Pocion([51,102,51], 12)

# nueva_nueva_pocion = nueva_pocion.mezclar(otra_pocion)
# print(nueva_nueva_pocion)
# print(nueva_nueva_pocion.volumen)
# print(nueva_nueva_pocion.color)


# mezcla_pocion = nueva_pocion.mezclar(otra_pocion)

# mezclar_pocion.color
# mezclar_pocion.volumen

# EJERCICIO 3

class Cifrado():
    def __init__(self, alfabeto, alfabeto_mezclado):
        self.alfabeto = alfabeto
        self.alfabeto_mezclado = alfabeto_mezclado

    def codificar(self, texto):
        cont = 0
        lista = []
        for i in self.alfabeto:
            if i in texto:
                lista.append(self.alfabeto_mezclado[cont])
            else:
                pass
            cont += 1
        resultado = "".join(lista)
        return resultado

    def decodificar(self, texto):
        cont = 0
        lista = []
        for i in self.alfabeto_mezclado:
            if i in texto:
                lista.append(self.alfabeto[cont])
            else:
                pass
            cont += 1
        resultado = "".join(lista)
        return resultado
            
alfabeto = "abcdefghijklmnopqrstuvwxyz"
alfabeto_mezclado = "etaoinshrdlucmfwypvbgkjqxz"

mi_cifrado = Cifrado(alfabeto, alfabeto_mezclado)

print(mi_cifrado.decodificar("eta"))

print(mi_cifrado.codificar("abc")    )# => "eta"
print(mi_cifrado.codificar("xyz")    )# => "qxz"
print(mi_cifrado.codificar("aeiou")  )# => "eirfg"

print(mi_cifrado.decodificar("eta")  )  # => "abc"
print(mi_cifrado.decodificar("qxz")  )  # => "xyz"
print(mi_cifrado.decodificar("eirfg"))  # => "aeiou"
# frase = Cifrado()