#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.

autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["mercedes", "ferrari"] #Se utiliza slicing para reemplazar los valores en los índices 1 y 2
print(autos)