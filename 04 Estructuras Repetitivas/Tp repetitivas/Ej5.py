#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

#Se inicia con import random que genera un número aleatorio entre 0 y 9
import random
numero_aleatorio = random.randint(0,9) #Variable que almacena el número aleatorio
contador = 0 #Contador de intentos
numero_adivinado = False #Variable que indica si el número fue adivinado

print("Juego adivina el número!")

#Se utiliza el bucle while not porque numero_adivinado es False 
while not numero_adivinado:
    numero_ingresado = input("Ingrese un número entre 0 y 9: ")
    if not numero_ingresado.isdigit() or not (0 <= int(numero_ingresado) <= 9): # Verificar que el numero ingresado sea un digito y este en el 
                                                                                #rango de 0 a 9
        print("Entrada no válida. Por favor, ingresa un número entre 0 y 9.") #Mensaje de error si el número no es válido
        continue # continuar con el bucle
    numero_ingresado = int(numero_ingresado) #Se convierte el número ingresado a entero
    contador +=1 
    if numero_ingresado == numero_aleatorio: #Verifica si el numero ingresado es igual al numero aleatorio
        print(f"Felicitaciones adivinaste, el número era el {numero_aleatorio}!")
        print(f"Te tomó {contador} intento/s adivinar el número.")
        break #Para salir del bucle
    else:
        print("No adivinaste, vuelve a intentarlo")