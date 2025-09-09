# Control de stock en una empresa de caramelos

class Producto:
    def __init__(self, nombre, cantidad, precio, codigo):
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio
        self.__codigo = codigo
        
    def agregar_producto(self, producto_objeto):
        productos.append(producto_objeto)
        print(f"Producto {producto_objeto.__nombre} agregado al stock.")
    
    def buscar_producto(self, codigo_producto):
        x = 0
        for i in productos:
            if i.__codigo == codigo_producto:
                print(f"Producto encontrado, codigo correspondiente a  {i.__nombre} . Se encuentra en stock.")
                x = 0
                break

            else:
                x = x + 1

        if x == 1:
            print("Codigo de producto no encontrado.")

    def lista_de_productos(self):
        print("Esta es la lista de productos registrados:")
        for i in productos:
            print(i.__nombre)

    def consultar_stock(self, nombre_producto):
        x = 0
        for i in productos:
            if i.__nombre == nombre_producto:
                print(f"La cantidad de {i.__nombre} es de {i.__cantidad}")
                x = 0
                break

            else:
                x = x + 1
        
        if x == 1:
            print("Nombre de producto no encontrado.")

class Productos_perecederos(Producto):
    def __init__(self, nombre, cantidad, precio, codigo, vencimiento):
        super().__init__(nombre, cantidad, precio, codigo)

        self.__vencimiento = vencimiento

    def agregar_producto(self, producto_objeto):
        return super().agregar_producto(producto_objeto)

def pidiendo_entrada(mensaje):
    while True:
        ingreso = input(mensaje).strip()
        if ingreso:
            return ingreso

productos = []
stock = []

while True:
    print("\nBienvenido")
    print("Estas son las opciones del programa:\n")
    print("1- Ingresar producto\n2- Buscar producto\n3- Listar prodcutos\n4- Consultar stock de producto\n5- Salir")

    opcion = pidiendo_entrada("Ingrese una opción: ")

    if opcion == "1":
        for i in range(1, 11):
            nombre = pidiendo_entrada("\nIngrese nombre del producto: ")
            if nombre in stock:
                print(f"El producto {nombre} ya esta registrado y no puede repetirse.")
        
            elif nombre not in stock:
                stock.append(nombre)
                cantidad = pidiendo_entrada("Ingrese cantidad ded producto: ")
                precio = pidiendo_entrada("Ingrese precio del producto: ")
                codigo = pidiendo_entrada("Ingrese codigo del producto: ")
                nuevo_producto = Producto(nombre, cantidad, precio, codigo)
                nuevo_producto.agregar_producto(nuevo_producto)

            if i == 10:
                print("\nProductos maximos ingresados.\n")
                break 

            continuar = pidiendo_entrada("¿Ingresar otro producto? SI/NO: ").lower()
            if continuar == "si":
                pass

            else:
                break

    elif opcion == "2":
        if len(productos) == 0:
            print("\nNo se registraron productos todavia.\n")
        
        else:
            while True:
                codigo_de_prodcuto = pidiendo_entrada("Ingrese el codigo del producto que desea buscar: ")
                nuevo_producto.buscar_producto(codigo_de_prodcuto)
                continuar = pidiendo_entrada("¿Buscar otro producto por codigo? SI/NO: ").lower()
                if continuar == "si":
                    pass

                else:
                    break

    elif opcion == "3":
        if len(productos) == 0:
            print("\nNo se registraron productos todavia.\n")

        else:
            nuevo_producto.lista_de_productos()
            input("Presione ENTER para voler al menu principal: ")

    elif opcion == "4":
        if len(productos) == 0:
            print("\nNo se registraron productos todavia.\n")

        else:
            producto_ingresado = pidiendo_entrada("Ingrese el nombre del producto del que desea saber su cantidad en stock: ")
            nuevo_producto.consultar_stock(producto_ingresado)
            input("Presione ENTER para voler al menu principal: ")

    elif opcion == "5":
        print("Hasta luego.")
        break