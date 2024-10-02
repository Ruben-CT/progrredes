'''
Nombre: Rubén COlmenro Sánchez
Descripcion: 
Fecha: 19/09/2024
'''
num = int(input("Ingrese un número entero positivo: "))
pasos = 0

while num != 1:
    pasos += 1  
    if num % 2 == 0:  
        num = num // 2
        print(num)
    else:  
        num = 3 * num + 1
        print(num)

print("pasos =", pasos)