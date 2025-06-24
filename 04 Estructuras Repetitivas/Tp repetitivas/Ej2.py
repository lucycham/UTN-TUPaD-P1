#Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.


num = int(input("Ingrese un número entero: "))

digito = len(str(abs(num)))

digito = str(digito)

print(f"El número tiene {digito} dígitos")





