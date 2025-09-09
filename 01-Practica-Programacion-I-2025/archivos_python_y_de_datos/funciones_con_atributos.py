# Funciones con atributos

# class Persona:
#     edad = 27
#     nombre = 'Victor'
#     pais = 'Brazil'

# doctor = Persona()
# print('la edad es: ', doctor.edad)
# print('la edad es: ', getattr(doctor, 'edad')) #usamos la palabra reservada getattr() para obtener el atributo


# #funcion para saber si un atributo existe o no
# print('el doctor tiene una edad?', hasattr(doctor,'edad'))
# print('el doctor tiene una edad?', hasattr(doctor,'apellido'))
# #función que permite cambiar el valor de un atributo
# print('antes era:', doctor.nombre)
# setattr(doctor,'nombre', 'Hector')
# print('ahora se llama: ',doctor.nombre)
# #función para eliminar un atibuto
# delattr(Persona, 'pais') #delattr funciona con el nombre de la clase
# print(doctor.pais) #error ya que no existe mas


# en OO sirve para inicializar variables
# class Persona:

#     def __init__(self, nombre ,año):
#         self.nombre = nombre
#         self.año = año

#     def descripcion(self):
#         return '{} tiene {} años'.format(self.nombre, self.año)
    
#     def comentario(self, frase):
#         return '{} dice: {}'.format(self.nombre, frase)

# doctor = Persona('Gerardo', 20)
# print(doctor.nombre)
# print(doctor.descripcion())
# print(doctor.comentario('esta es la frace que yo dije'))

# #Modificar un atributo

# class Email:
#     def __init__(self):
#         self.enviado = False

#     def enviar_correo(self):
#         self.enviado = True

# mi_correo = Email()
# print(mi_correo.enviado)
# mi_correo.enviar_correo()
# print(mi_correo.enviado)

# class Pokemon: 
#     pass
#     def __init__(self, nombre, tipo):
#         self.nombre = nombre
#         self.tipo = tipo

#     def descripcion(self):
#         return "{} es un pokemon de tipo: {}".format(self.nombre, self.tipo)
    
# class Pikachu(Pokemon): 
#     def ataque(self, tipoataque):
#         return "{} tipo de ataque: {}".format(self.nombre, tipoataque)
    
# class Charmander(Pokemon):
#     def ataque(self, tipoataque):
#         return "{} tipo de ataque: {}".format(self.nombre, self.tipoataque)
    
# nuevo_pokemon = Pikachu("body", "electrico")
# print(nuevo_pokemon.descripcion())
# print(nuevo_pokemon.ataque("Impacto trueno"))

