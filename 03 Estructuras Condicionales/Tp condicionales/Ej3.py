#Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.


# Se solicita al usuario que ingrese un número par"
num = int(input("ingrese un número par: "))

# Se utiliza el condicional if, si el módulo determinó que es par se imprime por pantalla y finaliza el programa
if num % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un númer par") #En caso contrario se imprime por pantalla el mensaje de error