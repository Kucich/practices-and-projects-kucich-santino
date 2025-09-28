# Sistema de gestión de zoológico

class Animal:
    def __init__(self, nombre, especie, edad, salud):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.salud = salud

    def mostrar_info(self):
        print("Propiedades del animal:")
        print(f"Nombre: {self.nombre}\nEspecie: {self.especie}\nEdad: {self.edad}\nSalud: {self.salud}")

    def actualizar_salud(self, nueva_salud):
        self.salud = nueva_salud
        print(f"La salud de {self.nombre} ahora es {self.salud}!")

class Zoologico:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.animales = []

    def agregar_animal(self, nuevo_animal):
        self.animales.append(nuevo_animal)
        print(f"Los animales del zoologico son {self.animales}!")

    def eliminar_animal(self, borrar_animal):
        for i in self.animales:
            if i.nombre == borrar_animal:
                self.animales.remove(i)
                print(f"Se borro el registro del animal {i.nombre} del Zoo.")
                print(f"Esta es la nueva lista de animales:\n{self.animales}")
                break

            else:
                print("No se encontro el animal ingresado...")

    def buscar_animal(self, nombre_animal):
        print("Buscando animal...")
        x = 0
        for i in self.animales:
            if i.nombre == nombre_animal: 
                print("Animal enonctrado!")
                print(f"El animal {i} se encuentra en el Zoo.")
                x=0
                break

            else:
                x=1
        
        if x == 1:
            print("No se encontro.")            
        

    def mostrar_animales(self):
        print(f"Los animales actuales en el zoologico {self.nombre} son:")
        print(self.animales)

class AnimalExotico(Animal):
    def __init__(self, nombre, especie, edad, salud, pais_origen, nivel_riesgo):
        super().__init__(nombre, especie, edad, salud)

        self.pais_origen = pais_origen
        self.nivel_riesgo = nivel_riesgo

    def mostrar_info_exotica(self):
        print(f"El animal {self.nombre} es de {self.pais_origen} y su especie tiene un riesgo {self.nivel_riesgo} de extinción!")

oso = AnimalExotico("Oso", "Polar", 34, "Media", "Artico polar", "Alto")

rinoceronte = AnimalExotico("Rino", "Duracel", 56, "Baja", "Africa", "Alto")

cebra = AnimalExotico("Bryan", "Cebra", 20, "Buena", "Africa", "Medio")

oso.mostrar_info()
oso.mostrar_info_exotica()
rinoceronte.mostrar_info()
rinoceronte.mostrar_info_exotica()
cebra.mostrar_info()
cebra.mostrar_info_exotica()
cebra.actualizar_salud("Media")

amazonas = Zoologico("Amazonas", "Argentina")
amazonas.mostrar_animales()
amazonas.agregar_animal(oso)
amazonas.agregar_animal(rinoceronte)
amazonas.agregar_animal(cebra)
amazonas.mostrar_animales()
amazonas.buscar_animal("Bryan")
amazonas.eliminar_animal("Bryan")
amazonas.buscar_animal("Bryan")