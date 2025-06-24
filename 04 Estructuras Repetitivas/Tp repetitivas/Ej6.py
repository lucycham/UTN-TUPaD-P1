#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

#Se utiliza un bucle for para usar el rango de 100 a 0

for i in range(100, -1, -1):
    if i%2 == 0: #Con módulo se verifica si el número es par
        print(i)