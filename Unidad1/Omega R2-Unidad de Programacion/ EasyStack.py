# Nombre del problema: EasyStack
# Rubén Colmenero Sánchez 
# 12/01/2025

# Inicializamos la pila vacía
pila = []

# Leer el número de instrucciones
T = int(input())

# Procesar cada instrucción
for _ in range(T):
    # Leer la instrucción
    instruccion = input().split()
    
    if instruccion[0] == '1':  # Push
        # Insertar el número en la pila
        pila.append(int(instruccion[1]))
        
    elif instruccion[0] == '2':  # Pop
        if pila:  # Si la pila no está vacía
            pila.pop()
    
    elif instruccion[0] == '3':  # Top
        if pila:
            print(pila[-1])  # Imprimir el número en la parte superior de la pila
        else:
            print("Empty!")  # Si la pila está vacía, imprimir "Empty!"
