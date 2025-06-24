#5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad
#   de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    horas = segundos // 3600
    return f"La cantidad de segundos {segundos} equivale a {horas} horas"

if __name__ == "__main__":
    segundos = int(input("Ingrese los segundos: "))
    resultado = segundos_a_horas(segundos)
    print(resultado)