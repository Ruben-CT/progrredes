# Nombre del problema: El tablero de Bety
# Rubén Colmenero Sánchez 
# 12/01/2025

# Leemos las dimensiones y el número de operaciones
m, n, k = map(int, input().split())

# Leemos las operaciones
operaciones = [int(input()) for _ in range(k)]

# Leemos el tablero
tablero = [list(map(int, input().split())) for _ in range(m)]

# Contadores de desplazamiento para filas y columnas
desplazamiento_filas = 0
desplazamiento_columnas = 0

# Aplicamos las operaciones de forma optimizada
for op in operaciones:
    if op == 1:  # Up
        desplazamiento_filas += 1
    elif op == 2:  # Down
        desplazamiento_filas -= 1
    elif op == 3:  # Left
        desplazamiento_columnas += 1
    elif op == 4:  # Right
        desplazamiento_columnas -= 1

# Normalizamos los desplazamientos para que estén dentro de los límites
desplazamiento_filas %= m
desplazamiento_columnas %= n

# Imprimimos el tablero con los índices lógicos de fila y columna
for i in range(m):
    fila_logica = tablero[(i + desplazamiento_filas) % m]
    # Aplicamos el desplazamiento de columnas
    fila_resultante = [fila_logica[(j + desplazamiento_columnas) % n] for j in range(n)]
    print(" ".join(map(str, fila_resultante)))