# Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. 
# Permití consultar qué actividad hay en cierto día y hora.

agenda = {
    ('lunes', '10:00'): 'Reunión',
    ('martes', '11:15'): 'Clase de inglés',
    ('jueves', '9:30'): 'Presentación'
}

dia = input("Ingrese el día que quiere consultar: ").lower()
hora = input("Ingrese la hora (formato HH:MM): ")

# Buscar el evento con la tupla (día, hora)
if (dia, hora) in agenda:
    print(f"El {dia} a las {hora} tiene: {agenda[(dia, hora)]}")
else:
    print("Sin actividad.")