#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

#Se solicita al usuario que ingrese un número entero positivo
numero = input("Introduce un número entero positivo: ")

#Se utiliza el bucle while para validar si el número es un entero positivo
while not numero.isdigit() or int(numero) <= 0: #Si no es un dígito o es menor o igual a 0 imprime el mensaje de error 
    print("Por favor ingresa un número entero positivo: ")
    numero = input("Introduce un número entero positivo: ")
#Se pasa el número a entero
numero = int(numero)
suma = 0 #Inicializa la variable suma en 0 para el acumulado

#Con el bucle for se itera desde el 1 hasta el número ingresado por el usuario
for i in range(1, numero + 1):
    suma += i

print(f"La suma de los números comprendidos entre 0 y {numero} es: {suma}")
