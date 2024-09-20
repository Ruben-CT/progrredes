'''
Nombre: Rubén COlmenro Sánchez
Descripcion: Operadores y expreciones
Fecha: 19/09/2024
'''

hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# Escribe tu código aqui.
total =mins + dura
cociente = total // 60
residuo = total % 60
hour += cociente

print (f"{hour}:{residuo}")