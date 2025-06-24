# Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario

def factorial(x):
    return 1 if x == 0 else x * factorial (x-1)

num = int(input("Ingresa un número entero: "))

print(f"Factoriales del 1 al {num}: ")

for i in range(1, num + 1):
    print(f"{i}! = {factorial(i)}")