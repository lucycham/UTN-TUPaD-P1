# Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

stock_productos = {'Harina': 25, 'Fideos': 15, 'Arroz': 10}

producto = input("Ingrese el nombre del producto: ").capitalize()

if producto in stock_productos:
    print(f"Stock de {producto}: {stock_productos[producto]} unidades")

    agregar = input(f"Quiere agregar unidades al stock disponible de {producto}: (s/n)").lower()
    if agregar =="s":
        cantidad_unidades = int(input("Ingrese las unidades que desea agregar: "))
        stock_productos[producto] += cantidad_unidades
        print(f"Se agregaron {cantidad_unidades} unidades al producto {producto}")
    else:
        print("No se agregaron unidades al producto")
else:
    print(f"El producto no existe en el sistema")
    nuevo_producto = input("¿Desea agregar un nuevo producto?: (s/n)").lower()
    if nuevo_producto == 's':
        cantidad_unidades = int(input("Ingrese la unidades que desea agregar: "))
        stock_productos[producto] = cantidad_unidades
        print(f"Producto: {producto} agregado, contiene: {cantidad_unidades} unidades")
    else:
        print("No se agrega nuevo producto")

print(f"Stock actual:", stock_productos)

