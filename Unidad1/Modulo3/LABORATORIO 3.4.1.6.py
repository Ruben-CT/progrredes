'''
Nombre: Rubén COlmenro Sánchez
Descripcion: 
Fecha: 19/09/2024
'''
sombrero_lista = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.

# Paso 1: escribe una línea de código que solicite al usuario
# reemplazar el número de en medio con un número entero ingresado por el usuario.
numero = int(input("Ingrese un nuevo número: "))
sombrero_lista[2] = numero

# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
sombrero_lista.pop()

# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
print("La longitud de la lista es:", len(sombrero_lista))

print(sombrero_lista)