
# Utilizando la información aportada en la siguiente tabla sobre las estaciones del año:
# |----------------------------------------------|-----------------------------------------------|-----------------------------------------|
# |               Periodo del año                |        Estación en el hemisferio norte        |     Estación en el hemisferio sur       |
# |----------------------------------------------|-----------------------------------------------|-----------------------------------------|
# |     Desde el 21 de diciembre hasta el        |                                               |                                         |
# |          20 de marzo (incluidos)             |                    Invierno                   |                Verano                   |                   |                                               |                                         |  
# |----------------------------------------------|-----------------------------------------------|-----------------------------------------|   
# |      Desde el 21 de marzo hasta el           |                                               |                                         |
# |          20 de junio (incluidos)             |                    Primavera                  |                 Otoño                   |
# |----------------------------------------------|-----------------------------------------------|-----------------------------------------|
# |      Desde el 21 de junio hasta el           |                                               |                                         | 
# |          20 deseptiembre (incluidos)         |                     Verano                    |                Invierno                 |
# |----------------------------------------------|-----------------------------------------------|-----------------------------------------|
# |     Desde el 21 de septiembre hasta el       |                                               |                                         |
# |          20 de  diciembre (incluidos)        |                     Otoño                     |               Primavera                 | 
# |----------------------------------------------|-----------------------------------------------|-----------------------------------------|
#
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. 
# El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.
                    
# Se le pide al usuario que ingrese el hemisferio
hemisferio = input("Ingrese el hemisferio. Escribir la letra N para Norte y S para Sur): ").upper()

# Se valida que el hemisferio ingresado sea válido, si no lo es, se imprime un mensaje de error
if hemisferio not in ["N", "S", "n", "s"]:
    print("Hemisferio no válido. Debe ingresar 'N' para el hemisferio norte o 'S' para el hemisferio sur.") 

# Se le pide al usuario que ingrese el mes
mes = int(input("Ingrese el mes (1-12): "))

#Se le pide al usuario que ingrese el día
dia = int(input("Ingrese el día (1-31): "))

# Se valida que el día sea válido para el mes ingresado, si no lo es, se imprime un mensaje de error
if mes < 1 or mes > 12:
    print("El mes ingresado no es válido. Debe ser un número entre 1 y 12.") # Se valida que el mes sea un número entre 1 y 12
elif mes == 2 and dia > 29:
    print("Febrero solo tiene 29 días en años bisiestos")# Febrero tiene 29 días en años bisiestos
elif mes == 2 and dia > 28:
    print("Febrero solo tiene 28 días en años no bisiestos") # Febrero tiene 28 días en años no bisiestos
elif mes in [4, 6, 9, 11] and dia > 30: #Se valida si el mes tiene 30 días en los meses de abril, junio, septiembre y noviembre
    print("El mes ingresado solo tiene 30 días")
else:
    if mes in [1, 3, 5, 7, 8, 10, 12] and dia > 31: # Se valida si el mes tiene 31 días en los meses de enero, marzo, mayo, julio, agosto, octubre y diciembre
        print("El mes ingresado solo tiene 31 días")
        
# Se determina la estación del año según el hemisferio y la fecha ingresada
# Se utiliza un condicional if para determinar la estación del año
if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes <= 3 and dia <= 20):
        estacion = "Invierno"
        print("Estación Invierno")
    elif (mes == 3 and dia >= 21) or (mes <= 6 and dia <= 20):
        estacion = "Primavera"
        print("Estación Primavera")
    elif (mes == 6 and dia >= 21) or (mes <= 9 and dia <= 20):
        estacion = "Verano"
        print("Estación Verano")
    else:
        estacion = "Otoño"
        print("Estación Otoño")
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes <= 3 and dia <= 20):
        estacion = "Verano"
        print("Estación Verano")
    elif (mes == 3 and dia >= 21) or (mes <= 6 and dia <= 20):
        estacion = "Otoño"
        print("Estación Otoño")
    elif (mes == 6 and dia >= 21) or (mes <= 9 and dia <= 20):
        estacion = "Invierno"
        print("Estación Invierno")
    else:
        estacion = "Primavera"
        print("Estación Primavera")