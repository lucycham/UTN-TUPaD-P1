# Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

#Se solicita al usuario que ingrese dos número enteros
num1 = int(input("Ingrese un número entero: "))
num2 = int(input("Ingrese otro número entero: "))

contador = 0 # Se inicializa el contador en 0

#Utilizo el bucle for para iterar entre los número comprendidos entre num1 y num2
for i in range(num1 + 1, num2): 
    contador += i
for i in range(num2 + 1, num1):
    contador += i
print(f"La suma de los números enteros comprendidos entre {num1} y {num2} es: {contador}")