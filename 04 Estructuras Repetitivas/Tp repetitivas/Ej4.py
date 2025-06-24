#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

#Se inicializa la variable suma en 0
suma = 0
# Se solicita al usuario que ingrese un número entero
numero = int(input("Ingrese un número entero (0 para terminar): "))
# Se utiliza un bucle while para seguir solicitando números hasta que el usuario ingrese 0
while numero != 0:
    suma += numero
    numero = int(input("Ingrese un número entero (0 para terminar): "))
print(f"Total suma acumulada: {suma}")