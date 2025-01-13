# Nombre del problema: Puntos Ordenados
# Rubén Colmenero Sánchez 
# 12/01/2025

# Leer el número de puntos
n = int(input())

# Leer los puntos y almacenarlos en una lista
puntos = [tuple(map(int, input().split())) for _ in range(n)]

# Ordenar los puntos según la coordenada x
puntos_ordenados = sorted(puntos, key=lambda p: p[0])

# Imprimir los puntos ordenados
for punto in puntos_ordenados:
    print(punto[0], punto[1])