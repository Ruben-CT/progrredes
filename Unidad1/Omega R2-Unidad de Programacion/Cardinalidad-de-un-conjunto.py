# Nombre del problema: Cardinalidad de un conjunto
# Rubén Colmenero Sánchez 
# 12/01/2025

# Leemos los límites del conjunto (aunque no se utilizan directamente)
a, b = map(int, input().split())

# Inicializamos el conjunto vacío
conjunto = set()

# Procesamos los eventos
while True:
    try:
        evento = input().split()
        tipo_evento = evento[0]
        
        if tipo_evento == 'I':  # Inserción
            valor = int(evento[1])
            conjunto.add(valor)
        elif tipo_evento == 'E':  # Extracción
            valor = int(evento[1])
            conjunto.discard(valor)  # discard no lanza error si el valor no está
        elif tipo_evento == 'C':  # Consulta de cardinalidad
            print(len(conjunto))
    except EOFError:
        break


