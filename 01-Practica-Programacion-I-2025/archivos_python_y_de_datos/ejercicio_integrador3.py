# Consigna:
# Desarrolla un programa en Python que gestione el 
# control de stock en una empresa de caramelos. 
# El programa debe permitir agregar, 
# buscar y listar productos.
# Cada producto tendrá un nombre, una cantidad en stock y un precio. 
# Además, se debe implementar una clase derivada para productos perecederos
# que incluya la fecha de vencimiento.

# Uso de listas: Utiliza listas para almacenar los productos ingresados.
# Clases y métodos: Implementa al menos dos clases (una base y una derivada) 
# con sus respectivos métodos.

# Permitir el ingreso de productos. Valide el ingreso de 10 
# productos como máximo sin repetirse con su respectivo stock.
# Permitir buscar un producto por código Permitir consultar el 
# total de stock por productos


class Producto:
    def __init__(self, nombre, cantidad, precio, codigo):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.codigo = codigo

    def agregar_producto(self):
            stock_productos.add(self.nombre)
            productos_ingresados.append(self.nombre)
            productos_ingresados.append(self.cantidad)
            productos_ingresados.append(self.precio)
            productos_ingresados.append(self.codigo)
            print(f"Prodcutos ingresados: {productos_ingresados}")
            print(f"\nProductos en stock: {stock_productos}")

    def buscar_producto(self, codigo_ingresado):
        if self.codigo == codigo_ingresado:
            print(f"Este es el producto correspondiente al codigo {self.nombre}.")
        else:
            print("El codigo ingresado no existe.")

    def listar_productos(self):
        if len(stock_productos) != 0:
            print(f"El listado de productos es: {stock_productos}")

        else:
            print("Todavia no se ingreso ningun producto.")

class Producto_perecedero(Producto):
    def __init__(self, nombre, cantidad, precio, codigo, vencimiento):
        super().__init__(nombre, cantidad, precio, codigo)
    
        self.vencimiento = vencimiento


productos_ingresados = []
stock_productos = set()
nuevo_producto = Producto("default", "default", "default", "default")
contador = 0

while True:
    opcion = int(input("¿Utilizar programa de gestión de stock? Presione 1 para SI o 2 para NO: "))

    if opcion == 1:
        print("1- Ver lista de productos.")
        print("2- Agregar nuevos productos.")
        print("3- Buscar producto por su codigo.")
        opcion2 = int(input("\nSeleccione una opción: "))

        if opcion2 == 2:
            while True:
                nombre = input("Ingrese nombre del producto: ")
                precio = input("Ingrese precio del producto: ")
                cantidad = input("Ingrese cantidad del producto: ")
                codigo = input("Ingrese codigo del producto: ")
                nuevo_producto = Producto(nombre, cantidad, precio, codigo)
                nuevo_producto.agregar_producto()
                seguir = int(input("¿Ingresar otro producto? Presionar 1 para salir o 2 para continuar: "))

                contador += 1
                if contador == 10:
                    break

                if seguir == 1:
                    break

                elif seguir == 2:
                    pass

                else:
                    print("Opción no valida")
                    break
            
        elif opcion2 == 1:
            nuevo_producto.listar_productos()

        elif opcion2 == 3:
            codigo_ingresado = input("Ingrese el codigo del producto: ")
            nuevo_producto.buscar_producto(codigo_ingresado)


    elif opcion == 2:
        print("¡Hasta pronto!")
        exit()

    else:
        print("Opción no valida, intente nuevamente.")