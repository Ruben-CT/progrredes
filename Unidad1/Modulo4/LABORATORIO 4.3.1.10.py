'''
Nombre: Rubén Colmenro Sánchez
Fecha: 02/oct/2024
Descripción:Convirtiendo el consumo de combustible
'''

 #1 milla (mile) = 1609.3 metros(metres)
# 1 galón (gallon) = 3.785 litros(litres)
    
def liters_100km_to_miles_gallon(litros):
    galones = litros / 3.785
    millas = 100 * 1000 / 1609.3
    return millas / galones

def miles_gallon_to_liters_100km(millas):
    km100 = millas * 1609.344 / 1000 / 100
    litros = 3.785
    return litros / km100

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))