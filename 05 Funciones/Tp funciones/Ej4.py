#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
#   calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
#   Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

def calcular_area_circulo(radio):
    return 3.14159 * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * 3.14159 * radio

if __name__ == "__main__":
    # Solicitar el radio al usuario y calcular el área y el perímetro del círculo
    radio = float(input("Ingrese el radio: "))
    #Se llama a las funciones:
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    print (f"El área del círculo es: {area} y el perímetro es: {perimetro}")
