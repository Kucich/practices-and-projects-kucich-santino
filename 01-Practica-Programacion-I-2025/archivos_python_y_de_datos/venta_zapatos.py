
class Producto:
    def __init__(self, precio, marca, calzado, color):
        
        self.precio = precio
        self.marca = marca
        self.calzado = calzado
        self.color = color
        
    def confirmar_compra(self):

        while True:
            print("¿Confirma la compra del producto?\n")
            print(f"Calzado {self.marca}\n {self.color}\n {self.calzado} \n por el precio de {self.precio} pesos.")

            confirmado = int(input("1 para SI, 2 para NO: "))

            if confirmado == 1:
                print("Redireccionando a Elegir metodo de pago...")
                pago()
                break

            elif confirmado == 2:
                print("Pago anulado. Gracias por utilizar el programa.")
                exit()

            else:
                print("Opcion invalida, intente nuevamente")

    def obtener_precio(self):
        print("El precio es {}".format(self.precio))

class Metodo_de_pago:
    def __init__(self, forma, cuotas):

        self.forma = forma
        self.cuotas = cuotas

    def descripcion_de_pago(self):
        print("Seleccion:")
        print("La forma de pago seleccionada es {} en {} cuota/s".format(self.forma, self.cuotas))

    def procesar_pago(self):
        print("Procesando pago... Espere...")
        print("¡Pago realizado con exito! Muchas gracias por su compra.")

class Zapato(Producto):
    def __init__(self, precio, marca, calzado, color, tipo):
        super().__init__(precio, marca, calzado, color)

        self.tipo = tipo

    def definir_caracteristicas(self, opcion):
        if opcion == 3:
            zapato.precio = 500000
            zapato.marca = "Puma"
            zapato.calzado = input("\nIngrese el numero de talle: ")
            zapato.color = "Marron"
            zapato.tipo = "Elegante"
            return zapato.precio, zapato.marca, zapato.calzado, zapato.color, zapato.tipo

        elif opcion == 4:
            zapato.precio = 400000
            zapato.marca = "Topper"
            zapato.calzado = input("\nIngrese el numero de talle: ")
            zapato.color = "Blanco"
            zapato.tipo = "Informal"
            return zapato.precio, zapato.marca, zapato.calzado, zapato.color, zapato.tipo

    def obtener_caracteristicas(self):
        print("Caracteristicas:")
        print(f"Marca: {self.marca}, Color: {self.color}, Tipo: {self.tipo}")
        input("\nEnter para continuar:")

class Zapatilla(Producto):
    def __init__(self, precio, marca, calzado, color, tipo):
        super().__init__(precio, marca, calzado, color)

        self.tipo = tipo

    def definir_caracteristicas(self, opcion):
        if opcion == 1:
            zapatilla.precio = 300000
            zapatilla.marca = "Nike"
            zapatilla.calzado = input("\nIngrese el numero de talle: ")
            zapatilla.color = "Rojo"
            zapatilla.tipo = "Running"
            return zapatilla.precio, zapatilla.marca, zapatilla.calzado, zapatilla.color, zapatilla.tipo

        elif opcion == 2:
            zapatilla.precio = 200000
            zapatilla.marca = "Addidas"
            zapatilla.calzado = input("\nIngrese el numero de talle: ")
            zapatilla.color = "Azul"
            zapatilla.tipo = "Running"
            return zapatilla.precio, zapatilla.marca, zapatilla.calzado, zapatilla.color, zapatilla.tipo
        
    def obtener_caracteristicas(self):
        print("Caracteristicas:")
        print(f"Marca: {self.marca}, Color: {self.color}, Tipo: {self.tipo}")
        input("\nEnter para continuar: ")

def pago():
    
    print("\nSeleccione metodo de pago.")
    metodo = int(input("Presione 1 para transferiencia, 2 para tarjeta o 3 para efectivo : "))
    print("\nSeleccione cantidad de cuotas.")
    cuotas = int(input("Presione 1 para 3 cuotas, 2 para 6 cuotas, 3 para 12 cuotas: "))

    if metodo == 1:
        metodo = "Transferencia"

    elif metodo == 2:
        metodo = "Tarjeta"

    elif metodo == 3:
        metodo = "Efectivo"
    
    if cuotas == 1:
        cuotas = 3
    
    elif cuotas == 2:
        cuotas = 6

    elif cuotas == 3:
        cuotas = 12

    pago = Metodo_de_pago(metodo, cuotas)
    pago.descripcion_de_pago()
    pago.procesar_pago()

lista_de_opciones = [1, 2, 3, 4, 5]

print("Catalogo de zapatos y zapatillas.\n")
print("1- Zapatilla Nike")
print("2- Zapatilla Addidas")
print("3- Zapato Puma")
print("4- Zapato Topper")
print("\nPresione 5 para salir.")
opcion = int(input("\nIngrese una opcion del catalogo o presione 5 para salir: "))

if opcion in lista_de_opciones:
    if opcion == 3 or opcion == 4:
        zapato = Zapato("Default", "Default", "Default", "Default", "Default")
        zapato.definir_caracteristicas(opcion)
        zapato.obtener_caracteristicas()
        zapato.obtener_precio()
        zapato.confirmar_compra()

    else:
        zapatilla = Zapatilla("Default", "Default", "Default", "Default", "Default")
        zapatilla.definir_caracteristicas(opcion)
        zapatilla.obtener_caracteristicas()
        zapatilla.obtener_precio()
        zapatilla.confirmar_compra()

elif opcion == 5:
            print("Adios")
            exit()

else:
    pass
