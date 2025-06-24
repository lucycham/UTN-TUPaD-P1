#6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese
#   número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    # range para iterar del 1 al 10
    for i in range(1, 11):
        resultado = numero * i  # Para la multiplicación
        print(f"{numero} x {i} = {resultado}")

if __name__ == "__main__":
    numero = int(input("Ingrese un número para multiplicar: "))
    tabla_multiplicar(numero) #Se llama a la función