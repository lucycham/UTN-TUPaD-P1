#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.

numeros_saltos = list(range(10, 31, 5)) #Se utiliza range para crear la lista
print(numeros_saltos[:2]) # Se utiliza slicing para mostrar los dos primeros elementos de la lista
