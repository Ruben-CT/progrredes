# Nombre del problema: Suma de dados
# Rubén Colmenero Sánchez 
# 12/01/2025

# Lectura de entrada
n = int(input())  # Número de dados lanzados
dados = [int(input()) for _ in range(n)]  # Resultados de los dados

# Inicializar valores para las sumas mínima y máxima
min_suma = float('inf')
max_suma = float('-inf')

# Comparar todas las posibles parejas de dados
for i in range(n):
    for j in range(i + 1, n):
        suma = dados[i] + dados[j]
        min_suma = min(min_suma, suma)
        max_suma = max(max_suma, suma)

# Salida de las sumas mínima y máxima
print(min_suma)
print(max_suma)