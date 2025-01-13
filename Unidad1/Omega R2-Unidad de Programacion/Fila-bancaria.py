# Nombre del problema: Fila Bancaria
# Rubén Colmenero Sánchez 
# 12/01/2025

# Lectura de entrada
n = int(input())  # Número de eventos
eventos = [input().strip() for _ in range(n)]  # Lista de eventos

# Inicializar la fila (cola)
fila = []

# Procesar los eventos
for evento in eventos:
    if evento == 'E':  # Evento E: llega una persona dispuesta a esperar
        fila.append(1)
    elif evento == 'N':  # Evento N: llega una persona impaciente
        if len(fila) > 4:
            print("no espera")  # Más de 4 personas en la fila
        else:
            print("espera")  # 4 o menos personas en la fila
            fila.append(1)
    elif evento == 'F':  # Evento F: alguien es atendido
        if fila:
            fila.pop(0)
