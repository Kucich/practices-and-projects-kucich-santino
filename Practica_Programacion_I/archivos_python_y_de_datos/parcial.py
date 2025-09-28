# Sistema gestión de inventario

class Producto:
    """Crear Productos los cuales que seran registrados y almacenados para su gestionar el inventario de una Tienda"""
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def registrar_producto(self, nuevo_producto):
        """Metodo que permite registrar los productos ingresados por el usuario"""
        lista_producto_objeto.append(nuevo_producto)
        print(f"Fueron agregados {nuevo_producto.cantidad} unidades del producto: {nuevo_producto.nombre} a la lista, con su precio de {nuevo_producto.precio} pesos.")

    def buscar_producto(self, producto):
        """Metodo que permite buscar los productos registrados en el almacen de la Tienda"""
        x = 0
        for i in lista_producto_objeto:
            if i.nombre == producto:
                print(f"Producto {i.nombre} encontrado. Cantidad en stock: {i.cantidad}. Precio registrado: {i.precio}")
                x = x + 1
                break
            else:
                x = 0
        if x == 0:
            print("El producto ingresado no se encuentra registrado.")

    def calcular_total(self):
        """Metodo que permite calcular el valor total del inventario teniendo en cuenta la cantidad y el precio de cada producto"""
        total = 0
        for i in lista_producto_objeto:
            primer_producto = i.cantidad * i.precio
            total = total + primer_producto 
        print(f"El valor total del inventario es de {total} pesos.")

    def listar_productos(self):
        """Metodo que lista todos los productos registrados en el almacen para visualización del usuario"""
        print("Esta es la lista de productos registrados:\n")
        for i in lista_producto_objeto:
            print(f"Producto: {i.nombre}, Cantidad: {i.cantidad}, Precio: {i.precio}")

def pidiendo_mensaje(mensaje):
    """Esta función se asegura de que en cada input del usuario se ingrese un valor y no un espacio vacio"""
    while True:
        ingreso = input(mensaje)
        if ingreso:
            return ingreso
        else:
            print("Debe ingresar una opción.\n")

lista_producto_objeto = []

# Cuerpo del programa

while True:
    print("\nMenú principal") # Menú de inicio
    print("1-Registrar producto\n2-Buscar producto por nombre\n3-Calcular valor total de inventario\n4-Mostrar productos registrados\n5-Salir")

    opcion = pidiendo_mensaje("Ingrese una opción: ")
    # Validación de opciones
    if opcion == "1": # La opción 1 permite registrar productos
        while True:
            if len(lista_producto_objeto) == 10:
                print("Cantidad maxima de productos ingresados alcanzada. Volviendo al menú principal...\n")
                break
            else:
                nombre_producto = pidiendo_mensaje("Ingrese el nombre del producto: ")
                cantidad_producto = int(pidiendo_mensaje("Ingrese la cantidad: "))
                if cantidad_producto < 0:
                    print("El valor de la cantidad no puede ser negativo. Intente nuevamente...")
                else:
                    precio_producto = float(pidiendo_mensaje("Ingrese precio del producto: "))
                    if precio_producto < 0:
                        print("El valor del precio no puede ser negativo. Intente nuevamente...")
                    else:
                        nuevo_producto = Producto(nombre_producto, cantidad_producto, precio_producto)
                        nuevo_producto.registrar_producto(nuevo_producto)
                        continuar = pidiendo_mensaje("¿Desea registrar otro producto? Si para continuar o cualquier tecla para volver al menú principal: ").lower()

                        if continuar == "si":
                            pass
                        else:
                            break

    elif opcion == "2": # La opción 2 permite buscar productos por su nombre
        if len(lista_producto_objeto) == 0:
            print("Todavía no se registraron productos. Volviendo al menú principal...")
        else:
            while True:
                producto = pidiendo_mensaje("Ingrese el nombre del producto que desea buscar: ")
                nuevo_producto.buscar_producto(producto)
                continuar = pidiendo_mensaje("¿Desea buscar otro producto? Si para continuar o cualquier tecla para volver al menú principal: ").lower()
                if continuar == "si":
                    pass
                else:
                    break

    elif opcion == "3": # La opción 3 calcula y devuelve el valor TOTAL del invetario
        if len(lista_producto_objeto) == 0:
            print("Todavía no se registraron productos. Volviendo al menú principal...")
        else:
            nuevo_producto.calcular_total()
            input("\nAprete ENTER para voler al menú principal: ")

    elif opcion == "4": # La opción 4 muestra el listado de productos registrados
        if len(lista_producto_objeto) == 0:
            print("Todavía no se registraron productos. Volviendo al menú principal...")
        else:
            nuevo_producto.listar_productos()
            input("\nAprete ENTER para voler al menú principal: ")

    elif opcion == "5": # La opción 5 permite al usuario salir del programa
        print("¡Hasta pronto!")
        exit()

    else: # En caso de que se ingrese una opción no esperada, se muestra este mensaje
        print("Opción ingresada no valida, intente nuevamente.")