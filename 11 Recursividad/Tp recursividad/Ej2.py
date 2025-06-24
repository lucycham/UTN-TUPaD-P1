# Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique.

def fibonacci(posicion):
    if posicion == 0:
        return 0 
    elif posicion == 1:
        return 1
    else:
        return fibonacci(posicion-1)+fibonacci(posicion-2)
    

if __name__ == "__main__":
    print(fibonacci(6))
