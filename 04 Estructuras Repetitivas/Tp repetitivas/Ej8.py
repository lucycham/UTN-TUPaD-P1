#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#   programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#   negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#   menor, pero debe estar preparado para procesar 100 números con un solo cambio).

#Se solicita al 
numero_ingresado = input("Ingrese un número entero entre -100 y 100:")

pares = 0
impares = 0
negativos = 0
positivos = 0

for i in range(99):  # Cambia 100 por la cantidad de números que quieras procesar
    if numero_ingresado.isalpha() or int(numero_ingresado)<= -100 or int(numero_ingresado)>= 100:
        print("Entrada no válida. Por favor, ingrese un número entero entre -100 y 100.")
        numero_ingresado = input("Ingrese un número entero entre -100 y 100:")
        continue
    numero_ingresado = int(numero_ingresado)
    if numero_ingresado % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero_ingresado < 0:
        negativos += 1
    elif numero_ingresado > 0:
        positivos += 1
    else:
        print("Ingrese un número diferente de cero.")
    numero_ingresado = input("Ingrese un número entero entre -100 y 100: ")

print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números negativos: {negativos}")
print(f"Números positivos: {positivos}")