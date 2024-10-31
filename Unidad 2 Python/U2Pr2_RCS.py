import requests


url = "https://openlibrary.org/search.json?title=the+lord+of+the+rings"

response = requests.get(url)
print (url)
def linea(simbolo, longitud):
    for linea in range(longitud):
        print(simbolo, end="")


linea("*", 40 )
while True:
    if response.status_code == 200:
        date = response.json
        print("Titulo: The lord of the rings ")  
        print("Autor:  ")  
        print("Año de publicacion:" first_publish_year, ['first_publish_year'] )
        print("Más Informacion en: ")
    else:
        print(": Error en la solicitud")
    