#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
#   respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
#   en los videos o bien investigar cómo funciona el indexing con números negativos!
#   animales = ["perro","gato","conejo","pez"]

animales = ["perro", "gato", "conejo", "pez"] #Lista dada
animales[1] = "loro" #Se reemplaza el 2do elemento de la lista
animales[-1] = "oso" #Se reemplaza el ultimo elemento de la lista con indexing negativo
print(animales)