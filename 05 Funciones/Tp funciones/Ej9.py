#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en
#   Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

def celsius_a_fahrenheit(celsius):
    grados_f = (celsius * 9/5) + 32 #Calculo de grados Celsius a Farenheit
    return f"{celsius}°C equivale/n a {grados_f}°F"

if __name__ == "__main__":
    grados_c = float(input("Ingrese la temperatura en grados Celcius (°C): "))
    resultado = celsius_a_fahrenheit(grados_c) #Se llama a la función
    print(resultado)
