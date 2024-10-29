lista = []
producto1 = {"Nombre":"Manzana","Stock":200,"Precio":12.90}
lista.append(producto1)
producto2 = {"Nombre":"Piña","Stock":100,"Precio":18.90}
lista.append(producto2)
producto3 = {"Nombre":"Fresa","Stock":150,"Precio":22.20}
lista.append(producto3) 
producto4 = {"Nombre":"Mango","Stock":80,"Precio":25.50}
lista.append(producto4)

print ("\nBienvenido a tu Sistema de Gestión de Tienda\n")
print ("\t.:Menu:.\n")
print ("1. Añadir producto")
print ("2. Ver productos")
print ("3. Realizar venta")
print ("4. Ver historial")
print ("5. Salir \n")
opcion = int(input("Por favor escoge una opción del menú -> "))

while opcion < 1 or opcion > 5:
    print("Error -> Por favor ingresa un número entre 1 y 5\n")
    opcion = int(input(f"Por favor escoge una opción del menú ->"))

if opcion ==1:
    nombre = str(input("Ingresa nombre del producto:"))
    for producto in lista:
        if producto["Nombre"] == nombre:
            print(f"Producto ingresado {nombre} ya existe")
    cantidad = int(input("Ingresa cantidad:"))
    precio = float(input("Ingresa precio:"))
    print(f"\nProducto ingresado es: {nombre}, Cantidad ingresada: {cantidad} Kgs, Precio ${precio: .2f}\nGracias")
    producto5 = {"Nombre":nombre, "Stock":cantidad, "Precio":precio}
    lista.append (producto5)
    print("\nLa lista actualizada de productos es:\n")
    for producto in lista:
        print(f"Nombre: {producto['Nombre']}, Stock {producto['Stock']} Kg, Precio ${producto['Precio']}" )

elif opcion ==2:
    if not lista:
        print("No existe producto")
    else:
        for producto in lista:
            print(f"Nombre: {producto['Nombre']}, Precio: $ {producto['Precio']: .2f}, Stock: {producto['Stock']}")

elif opcion == 3:
    print("Lista de productos disponibles")
    for i, producto in enumerate(lista):
        print(f"{i+1}. {producto['Nombre']}, {producto['Stock']}Kg, ${producto['Precio']}")
    while True:
        try:
            seleccion = int(input(f"\nSelecciona el número del producto que deseas comprar: "))
            if 1 <= seleccion <= len(lista):
                producto_comprado = lista[seleccion - 1]
                print(f"Has seleccionado {producto_comprado['Nombre']}")
                break
            else:
                print("Error: Selecciona un número válido en la lista.")
        except ValueError:
            print("Error: Debes ingresar un número")

    while True:
        try:
            cantidad = int(input(f"Ingresa cantidad de Kg que deseas comprar: "))
            if 0 < cantidad <= producto_comprado['Stock']:
                print(f"Has comprado {cantidad} Kgs del producto {producto_comprado['Nombre']}")
                total = cantidad * producto_comprado["Precio"]
                #print(f"Total a pagar es de: $ {total}")
                #break
                if total >= 200:
                    precio_descuento = total - (total * 0.10)
                    print(f"Feliciades, ganaste descuento del 10%, el total a pagar es: {precio_descuento}")
                else:
                    print(f"Total a pagar es de: $ {total}")
                break
            else:
                print(f"Error: la cantidad debe ser menor o igual a $ {producto_comprado['Stock']}")
        except ValueError:
            print("Error: Debes ingresar un número")



    

