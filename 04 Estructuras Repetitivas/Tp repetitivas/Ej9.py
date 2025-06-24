#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#   media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#   poder procesar 100 números cambiando solo un valor).

#Se inicializa la variable suma en 0 y el contador en 0
suma = 0 
contador = 0

# Se utiliza un blucle for para solicitar los numeros al usuario
for i in range(99):
    numero_ingresado = int(input("Ingrese un número entero: "))
    suma += numero_ingresado #Acumula la suma de los números ingresados
    contador += 1  # Aumentar el contador por cada número ingresado

# Calcular la media
media = suma / contador


print(f"La media de los números ingresados es: {media}")