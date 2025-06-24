# Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.
# Ejemplos:
# contar_digito(12233421, 2) → 3
# contar_digito(5555, 5) → 4
# contar_digito(123456, 7) → 0

def contar_digito(numero, digito):
    if numero == 0:
        return 0 
    else:
        ultimo_digito = numero % 10 #Se comprueba si el último dígito es igual a dígito
        if ultimo_digito == digito:
            return 1 + contar_digito(numero // 10, digito ) #Se cuenta 1 y se sigue con el resto
        else:
            return contar_digito(numero // 10, digito) # Sino es igual se sigue con el resto sin contar
        

    
if __name__== "__main__":
    print(contar_digito(12333444567, 4))