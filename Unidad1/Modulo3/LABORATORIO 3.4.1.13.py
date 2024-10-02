'''
Nombre: Rubén COlmenro Sánchez
Descripcion: 
Fecha: 19/09/2024
'''
#parte 1
Beatles = []
print("Paso 1:", Beatles)

# parte 2
Beatles.append("John Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")
print("Paso 2:", Beatles)

# parte 3
nuevos_miembros = ["Stu Sutcliffe", "Pete Best"]
for miembro in nuevos_miembros:
    Beatles.append(miembro)
print("Paso 3:", Beatles)
# parte 4
a1 = Beatles.index("Stu Sutcliffe")
del Beatles[a1]

a2 = Beatles.index("Pete Best")
del Beatles[a2]
print("Paso 4:", Beatles)

# parte 5
Beatles.insert(0, "Ringo Starr")
print("Paso 5:", Beatles)

# probando la longitud de la lista
print("Los Fav", len(Beatles))