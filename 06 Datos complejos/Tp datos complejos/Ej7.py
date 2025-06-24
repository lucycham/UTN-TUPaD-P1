# Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial_1 = {'Ana', 'David', 'Belén', 'Juan'}
parcial_2 = {'Leandro', 'Ana', 'Belén','Joaquín'}

ambos_aprobados = parcial_1 & parcial_2
print("Aprobaron ambos parciales:", ambos_aprobados)

uno_aprobado = parcial_1 ^ parcial_2
print("Aprobaron un solo parcial:", uno_aprobado)

lista_total_aprobados = parcial_1 | parcial_2
print("estudiantes que aprobaron al menos un parcial:", lista_total_aprobados) 