#Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.

# Se solicita al usuario que ingrese su nombre
nombre = input("Ingrese su nombre: ")

#Se solicita al usuario que seleccione una opción
#Se muestra un menú con las opciones disponibles
print("Seleccione una opción:")
print("1. Nombre en mayúsculas")
print("2. Nombre en minúsculas")
print("3. Nombre con la primera letra mayúscula")
opcion = input("Ingrese el número de la opción deseada (1, 2 o 3): ")

if opcion == "1":
    print("Su nombre en mayúsculas es:", nombre.upper()) #Se utiliza upper() para convertir a mayúsculas
elif opcion == "2":
    print("Su nombre en minúsculas es:", nombre.lower()) #Se utiliza lower() para convertir a minúsculas
elif opcion == "3":
    print("Su nombre con la primera letra mayúscula es:", nombre.title()) #Se utiliza title() para convertir la primera letra a mayúscula
else:
    print("Opción no válida. Por favor, ingrese 1, 2 o 3.") # Se muestra un mensaje de error si la opción no es válida