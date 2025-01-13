# Nombre del problema: Los Ultimos Seran Los Primeros
# Rubén Colmenero Sánchez 
# 12/01/2025

# Lista para almacenar los nombres de los concursantes
concursantes = []

# Leer los nombres hasta encontrar el string "#"
while True:
    nombre = input()
    if nombre == "#":
        break
    concursantes.append(nombre)

# Imprimir los nombres en orden inverso
for nombre in reversed(concursantes):
    print(nombre)