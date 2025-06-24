# Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique.

from Ej2 import fibonacci

num = int(input("Ingrese un valor: "))

print(f"Serie de Fibonacci hasta {num}")

for i in range(num + 1):
    print(f"{i} = {fibonacci(i)}")

