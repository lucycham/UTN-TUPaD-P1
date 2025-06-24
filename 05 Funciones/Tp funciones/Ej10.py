#10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
#   Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a, b, c):
    return (a + b + c) / 3  #Cálculo del promedio

if __name__ == "__main__":
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    c = float(input("Ingresa el tercer número: "))
    promedio = calcular_promedio(a, b, c) #Se llama a la función
    print(f"El promedio de de los valores ingresados es: {promedio:.2f}")