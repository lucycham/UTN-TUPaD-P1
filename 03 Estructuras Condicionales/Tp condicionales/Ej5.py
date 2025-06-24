#Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). 
#Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta";
#en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

#Se solicita al usuario que ingrese una contraseña
contraseña = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")

#Se utiliza el condicional if. Cuando la contraseña es correcta dará el mensaje de que la contraseña es correcta y finaliza el programa
if len(contraseña) >= 8 and len(contraseña) <=14: #Con la funcion len() se evalúa la cantidad de caracteres de la contraseña
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres") #En caso contrario se imprime por pantalla el mensaje de error
