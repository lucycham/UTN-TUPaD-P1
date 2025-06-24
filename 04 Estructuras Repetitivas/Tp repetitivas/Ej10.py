#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#    usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = input("Ingresa un número entero: ")

# Se verifica que el número ingresado es un dígito
if numero.isdigit():
    numero_invertido = ""  # Variable para almacenar el número invertido
    
    # Bucle para recorrer el número a la inversa
    for digito in numero:
        numero_invertido = digito + numero_invertido  # Agrega el dígito al inicio
    
    print(f"El número invertido es: {numero_invertido}")
else:
    print("Por favor, ingresa un número válido.")