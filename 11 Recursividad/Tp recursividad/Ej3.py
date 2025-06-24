# Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1)
# Prueba esta función en un algoritmo general.

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia ( base, exponente -1)
    
if __name__== "__main__":
    base = int(input("Ingrese la base: "))
    exponente = int(input("Ingrese el exponente: "))

    resultado = potencia(base, exponente)
    print(f"{base}^{exponente} = {resultado}")