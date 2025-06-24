#Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.


# Se solicita al usuario que ingrese una frase o palabra
frase = input("Ingrese una frase o palabra: ")

# Se utiliza el condicional if para verificar si la última letra de la frase es una vocal
# Se utiliza el .lower() para convertir la última letra a minúscula y evitar problemas de mayúsculas
# Se utiliza frase[-1] para obtener la última letra de la frase
if frase[-1].lower() in "aeiou":
    frase += "!" # Se utiliza el += para concatenar el signo de exclamación al final de la frase
    print(frase) # Se imprime la frase con el signo de exclamación
else:
    print(frase) # Se imprime la frase original sin modificaciones