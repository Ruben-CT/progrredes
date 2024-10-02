'''
Nombre: Rubén COlmenro Sánchez
Descripcion: 
Fecha: 19/09/2024
'''
mi_lista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

aux = set()
lista = []
for num in mi_lista:
    if num not in aux:
        aux.add(num)
        lista.append(num)
        
print("La lista con elementos únicos:")
print(lista)