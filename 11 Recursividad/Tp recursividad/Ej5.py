# Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
# Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])
    

if __name__== "__main__":
    cadena_texto = input("Ingrese una cadena de texto sin espacios ni tildes: ")
    if es_palindromo(cadena_texto):
        print(f"{cadena_texto} es un palíndromo")
    else:
        print(f"{cadena_texto} no es un palíndromo")

