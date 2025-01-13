# Nombre del problema: El lado más corto
# Rubén Colmenero Sánchez 
# 12/01/2025

import math

# Leemos las coordenadas de los vértices
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
x3, y3 = map(float, input().split())
x4, y4 = map(float, input().split())

# Calculamos las longitudes de los lados
lado1 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  # Distancia entre (x1, y1) y (x2, y2)
lado2 = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)  # Distancia entre (x2, y2) y (x3, y3)
lado3 = math.sqrt((x4 - x3)**2 + (y4 - y3)**2)  # Distancia entre (x3, y3) y (x4, y4)
lado4 = math.sqrt((x1 - x4)**2 + (y1 - y4)**2)  # Distancia entre (x4, y4) y (x1, y1)

# Encontramos el lado más corto
lado_mas_corto = min(lado1, lado2, lado3, lado4)

# Imprimimos la longitud del lado más corto
print(f"{lado_mas_corto:.6f}")


