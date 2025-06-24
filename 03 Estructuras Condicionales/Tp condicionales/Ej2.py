#Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.

# Se solicita al usuario que ingrese la nota
nota = float(input("Ingrese su nota: "))

#Se utiliza el condicional if y se imprime por pantalla el resultado aprobado o desaprobado finalizando el programa
if nota >= 6:
    print("Aprobado")
elif nota >= 0 and nota < 6:
    print("Desaprobado")
else:
    print("Error, ingresar nota válida")



   