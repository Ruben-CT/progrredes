# Nombre del problema: Máximo Elemento en la Pila
# Rubén Colmenero Sánchez 
# 12/01/2025

# Pila principal para almacenar los elementos
pila = []
# Pila auxiliar para almacenar el máximo de cada estado de la pila
max_stack = []

# Leer el número de operaciones
N = int(input())

# Procesar las operaciones
for _ in range(N):
    # Leer la instrucción
    operacion = input().split()
    
    if operacion[0] == '1':  # Push
        x = int(operacion[1])
        pila.append(x)
        # Si max_stack está vacío o el nuevo elemento es mayor que el actual máximo, lo agregamos
        if not max_stack or x >= max_stack[-1]:
            max_stack.append(x)
        else:
            # Si no, repetimos el máximo anterior
            max_stack.append(max_stack[-1])
    
    elif operacion[0] == '2':  # Pop
        if pila:
            pila.pop()
            max_stack.pop()
    
    elif operacion[0] == '3':  # Top (imprimir el máximo)
        print(max_stack[-1])