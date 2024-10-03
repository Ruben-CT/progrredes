'''
Nombre: Rubén COlmenro Sánchez
Descripcion: Un año bisiesto
Fecha: 19/09/2024
'''
def is_year_leap(year):

# Escribe tu código aquí.
 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")