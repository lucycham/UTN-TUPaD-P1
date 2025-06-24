#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga 
# “Es mayor de edad”.

# Se solicita al usuario que ingrese su edad
edad = input("Ingrese su edad: ")

# Se utiliza el bucle while para que siga solicitando que se ingrese el número con las condiciones correctas
# Se utiliza .isnumeric() con el not para que determine que si el número ingresado es solo número, incluye también (-)
# por lo que no incluirá a números negativos
while not edad.isnumeric():
    edad = input("Por favor ingresar un número entero y positivo para edad: ")

# Se pasa la variable edad a número entero para poder determinar si es mayor o menor
edad = int(edad)

# Se utiliza el condicional if y se imprime por pantalla el resultado finalizando el programa
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

