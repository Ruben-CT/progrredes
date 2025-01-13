# Nombre del problema: Ordenando en cubetas
# Rubén Colmenero Sánchez 
# 12/01/2025

# Lectura de entrada
n, k = map(int, input().split())  # n = cantidad de pelotas, k = mayor número posible de color
pelotas = list(map(int, input().split()))  # Lista de pelotas

# Inicializar un arreglo para contar las pelotas
conteo = [0] * (k + 1)

# Contar las pelotas por color
for pelota in pelotas:
    conteo[pelota] += 1

# Imprimir la cantidad de pelotas de cada color en el formato solicitado
for i in range(1, k + 1):
    print(f"{i}: {conteo[i]}")