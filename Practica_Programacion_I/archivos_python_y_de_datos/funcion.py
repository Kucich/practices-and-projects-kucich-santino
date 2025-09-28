def pidiendo_ingreso(mensaje):
    while True:
        ingreso = input(mensaje)
        if ingreso:
            return ingreso

        else:
            print("Debe ingresar una opción. Intente nuevamente...\n")

def pidiendo_ingreso_numerico(mensaje):
    while True:
        try:
            ingreso = int(input(mensaje))
            if ingreso and ingreso > 0:
                return ingreso
            
        except ValueError:
            print("El valor ingresado debe ser numérico y mayor a cero. Intente nuevamente...\n")

nombre = pidiendo_ingreso("Ingrese su nombre: ")
edad = pidiendo_ingreso_numerico("Ingrese su edad: ")
