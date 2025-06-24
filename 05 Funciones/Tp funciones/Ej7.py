#7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resulta-
#   do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:   #Condición para evitar división por cero
        division = a / b 
    else:
        division = "Error, no se puede dividir por cero"
    return (suma, resta, multiplicacion, division) #tupla con los resultados

if __name__ == "__main__":
    a = float(input("Ingrese un número: "))
    b = float(input("Ingrese otro número: "))
    resultado = operaciones_basicas(a, b)
print(f"Resultados:\nLa suma es: {resultado[0]} \nLa resta es: {resultado[1]} \nLa multiplicación es: {resultado[2]} \nLa división es: {resultado[3]}")
