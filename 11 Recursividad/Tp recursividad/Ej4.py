# Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario (n // 2) + str(n % 2)
    
if __name__== "__main__":    
    
    num = int(input("Ingrese un número entero: "))
 
    print(f"El número {num} es {decimal_a_binario(num)} en binario")
    print(type(decimal_a_binario(num)))