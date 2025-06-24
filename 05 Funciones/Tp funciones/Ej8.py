#8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de
#   masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    return peso / (altura ** 2)  # Cálculo de IMC peso (kg)/altura(mt) al cuadrado
    
if __name__ == "__main__":
    peso = float(input("Ingrese su peso en kilogramo: "))
    altura = float(input("Ingrese su altura en metros: "))
    imc = calcular_imc(peso, altura)
    print(f"Su IMC es: {imc:.2f}") #Se utiliza :.2f para mostrar el resultado con dos decimales
