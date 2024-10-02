'''
Nombre: Rubén COlmenro Sánchez
Descripcion: 
Fecha: 19/09/2024
'''
año = int(input("Introduce un año:"))

if año<=1582:
    print("No esta dentro del período del calendario Gregoriano")
elif año%4!=0:
    print("Año comun")
else:
    print("Año bisiesto")