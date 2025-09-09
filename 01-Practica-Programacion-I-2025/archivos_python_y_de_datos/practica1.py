#Ejercicio 1: Crear una clase
#Consigna: Define una clase llamada Animal con un atributo nombre. 
# Luego, crea una instancia de la clase y muestra el nombre.

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

perro = Animal("Perro Juan")
print(perro.nombre)

#Ejercicio 2: Añadir un método
#Consigna: Añade un método llamado hacer_sonido a la clase Animal 
# que imprima un sonido.

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        print("Sonido de animal")

gato = Animal("Paco")
gato.hacer_sonido()

#Ejercicio 3: Atributos adicionales
#Consigna: Añade un atributo edad a la clase Animal y muestra tanto el nombre como la
#edad del animal.

class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        print("Sonido de animal")

pajaro = Animal("Alvaro", 87)
print(pajaro.nombre)
print(pajaro.edad)

#Ejercicio 4: Método que usa atributos
#Consigna: Añade un método llamado descripcion que devuelva una cadena con el
#nombre y la edad del animal.

class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        print("Sonido de animal")

    def descripcion(self):
        print("El animal se llama {} y su edad es {} años.".format(self.nombre, self.edad))

oso = Animal("Pardo", 40)
oso.descripcion()

#Ejercicio 5: Modificar atributos
#Consigna: Añade un método llamado cumplir_años que 
# incremente la edad del animal en 1.

class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        print("Sonido de animal")

    def descripcion(self):
        print("El animal se llama {} y su edad es {} años.".format(self.nombre, self.edad))

    def cumplir_años(self):
        self.edad = self.edad + 1
        print(self.edad)

cocodrilo = Animal("Dante", 50)
cocodrilo.cumplir_años()

#Ejercicio 6: Clase base y clase derivada
#Consigna: Crea una clase base Animal con un método hablar. Luego, crea una clase
#derivada Perro que herede de Animal y sobrescriba el método hablar.

class Animal:
    def hablar(self):
        print("Hola soy un animal")

class Perro(Animal):
    def hablar(self):
        print("Hola soy un perro, guau guau")

animal = Animal()
animal.hablar()

perro = Perro()
perro.hablar()

# Ejercicio 7: Herencia y atributos
# Consigna: Crea una clase base Vehiculo con un atributo marca. Luego, crea una clase
# derivada Coche que herede de Vehiculo y tenga un atributo adicional modelo.

class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

class Coche(Vehiculo):
    def __init__(self, marca, modelo):
        Vehiculo.__init__(self, marca)
        self.modelo = modelo

auto = Coche("Toyota", "Aurora")
print(auto.marca)
print(auto.modelo)

# Ejercicio 8: Métodos adicionales en la clase derivada
# Consigna: Crea una clase base Persona con un método saludar. Luego, crea una clase
# derivada Estudiante que herede de Persona y tenga un método adicional estudiar.

class Persona:
    def saludar(self):
        print("Hola estoy saludando.")

class Estudiante(Persona):
    def estudiar(self):
        print("Estudiando...")

alumno = Estudiante()
alumno.saludar()
alumno.estudiar()

# Ejercicio 9: Herencia y métodos sobrescritos
# Consigna: Crea una clase base Figura con un método area. Luego, crea una clase derivada
# Cuadrado que herede de Figura y sobrescriba el método area.

class Figura:
    def area(self):
        pass

class Cuadrado(Figura):
    def __init__(self, lado_uno, lado_dos):
        self.lado_uno = lado_uno
        self.lado_dos = lado_dos

    def area(self):
        area = self.lado_uno * self.lado_dos
        print("El area del cuadrado es {}".format(area))

cuadrado = Cuadrado(5, 5)
cuadrado.area()

# Ejercicio 10: Herencia y uso de super()
# Consigna: Crea una clase base Empleado con un método trabajar. Luego, crea una clase
# derivada Gerente que herede de Empleado y use super() para llamar al método trabajar.

class Empleado:
    def trabajar(self):
        print("Trabajando...")

class Gerenete(Empleado):
    def __init__(self):
        super().__init__()

        