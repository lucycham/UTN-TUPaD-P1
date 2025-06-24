#Ej 2 bis
##Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

numero = input("Introduce un número entero: ")

while not numero.startswith('-') : 
    print("Entrada no válida. Por favor, introduce un número entero.")
    numero = input("Introduce un número entero: ")

cantidad_digitos = len(numero)
print(f"El número {numero} tiene {cantidad_digitos} dígitos.")
# Este código solicita al usuario un número entero y verifica que la entrada sea válida.
# Si la entrada no es un número entero, solicita al usuario que vuelva a introducir un número.
# Luego, calcula la cantidad de dígitos del número y lo imprime.

