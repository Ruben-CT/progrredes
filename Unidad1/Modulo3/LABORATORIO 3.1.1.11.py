'''
Nombre: Rubén COlmenro Sánchez
Descripcion: is y else
Fecha: 19/09/2024
'''
income = float(input("Introduce el ingreso anual:"))

if income <85528:
    tax = income*0.18-556.2
else:
    tax = income-85528
    tax = tax*0.32+14839
    
tax = round(tax, 0)
if tax<=0:
    tax = 0.0    
print("El impuesto es: ", tax, "pesos")