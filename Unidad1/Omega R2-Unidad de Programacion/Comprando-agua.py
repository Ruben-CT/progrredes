# Nombre del problema: Comprando agua
# Rubén Colmenero Sánchez 
# 12/01/2025

# Leemos la entrada
n = int(input())  # número de marcas disponibles
precios = list(map(int, input().split()))  # precios de las marcas

# Encontramos el precio mínimo
precio_minimo = min(precios)

# Imprimimos el precio mínimo
print(precio_minimo)