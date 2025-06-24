# Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

contacto = {}

print("Ingrese 5 contactos: ")
for i in range(2):
    nombre = input(f"Ingresar el nombre del contacto: {i+1}: ")
    tel = input(f"Ingresar el teléfono del contacto: {nombre}: ")
    contacto[nombre] = tel

buscar = input("Ingrese el nombre del contacto buscado: ")

if buscar in contacto:
    print(f"El número de {buscar} es: {contacto[buscar]}")
else:
    print("El contacto no existe")