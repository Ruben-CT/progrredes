'''
Nombre: Rubén COlmenro Sánchez
Descripcion: 
Fecha: 19/09/2024
'''
bloques = int(input("Ingresa el número de bloques: "))

altura = 0
bloques_usados = 0

while bloques_usados <= bloques:
  altura += 1
  bloques_usados += altura
  if bloques_usados > bloques:
    altura -= 1
    break

print("La altura de la pirámide:", altura)