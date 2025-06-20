
import random
import timeit
from ordenamientos import merge_sort, quick_sort, insertion_sort, bubble_sort
from busquedas import busqueda_lineal, busqueda_binaria

# Generar lista aleatoria
tamaño_lista = 10000 
list= random.sample(range(1, 100000), tamaño_lista)  # Lista de números únicos

# Copias para no modificar original
list1 = list.copy()
list2 = list.copy()
list3 = list.copy()
list4 = list.copy()

# Elegir un objetivo aleatorio
objetivo = random.choice(list)

# Medición quicksort
start_time = timeit.default_timer()
quick_sort(list1)
end_time = timeit.default_timer()
time_quick = end_time - start_time
print(f"[QUICKSORT] Tiempo para una lista grande: {time_quick:.4f} segundos")

# Medición MergeSort
start_time = timeit.default_timer()
merge_sort(list2)
end_time = timeit.default_timer()
time_merge = end_time - start_time
print(f"[MERGESORT]:Tiempo para una lista grande: {time_merge:.4f} segundos")

# Medición InsertionSort
start_time = timeit.default_timer()
insertion_sort(list1)
end_time = timeit.default_timer()
time_insertion = end_time - start_time
print(f"[INSERTIONSORT]:Tiempo para una lista grande: {time_insertion:.4f} segundos")

# Medición BubbleSort
start_time = timeit.default_timer()
bubble_sort(list1)
end_time = timeit.default_timer()
time_bubble = end_time - start_time
print(f"[BUBBLESORT]:Tiempo para una lista grande: {time_bubble:.4f} segundos")

# Medir tiempo de búsqueda lineal
start_time = timeit.default_timer()
resultado_lineal = busqueda_lineal(list, objetivo)
end_time = timeit.default_timer()
tiempo_lineal = end_time - start_time

#Búsqueda binaria
lista_ordenada = sorted(list)  
# Medir tiempo de búsqueda binaria
start_time = timeit.default_timer()
resultado_binaria = busqueda_binaria(lista_ordenada, objetivo)
end_time = timeit.default_timer()
tiempo_binaria = end_time - start_time

# Resultados
print(f"Búsqueda Lineal: Resultado = {resultado_lineal}, Tiempo = {tiempo_lineal:.6f} segundos")

print(f"Búsqueda Binaria: Resultado = {resultado_binaria}, Tiempo = {tiempo_binaria:.6f} segundos")


#Gráficos 
# Utilizamos el módulo matplotlib de la librería de Python para armar los gráficos
import matplotlib.pyplot as plt

# Listas con los valores para los ejes X e Y
algoritmos = ['Quick Sort', 'Merge Sort', 'Insertion Sort', 'Bubble Sort']
tiempos = [time_quick, time_merge, time_insertion, time_bubble]

# Creación de gráfico de barras con plt.bar
plt.bar(algoritmos, tiempos, color=['blue', 'green', 'orange', 'red'])
plt.ylabel('Tiempo (segundos)')
plt.title('Comparación de tiempos de ordenamiento')
plt.show()

import matplotlib.pyplot as plt

algoritmos = ['Búsqueda Lineal', 'Búsqueda Binaria']
tiempos = [tiempo_lineal, tiempo_binaria]

plt.bar(algoritmos, tiempos, color=['blue', 'green'])
plt.ylabel('Tiempo (segundos)')
plt.title('Comparación de tiempos de búsqueda')
plt.show()

