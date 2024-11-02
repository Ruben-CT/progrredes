import requests
# Esta api da inpormacion de los paises
url = 'https://restcountries.com/v3.1/all'

while True:
    country_name = input("¿Qué país deseas conocer? (o escribe 'salir' para terminar): ").strip()

   
    if country_name.lower() == 'salir':
        print("Saliendo del programa.")
        break  

    response = requests.get(url)

    if response.status_code == 200:
        countries = response.json()
        
        index = 0
        found = False  
        
        while index < len(countries):
            country = countries[index]
            
            if country.get("name", {}).get("common", "").lower() == country_name.lower():
                print("Nombre:", country.get("name", {}).get("common", "No disponible"))
                print("Capital:", country.get("capital", ["No disponible"])[0])
                print("Región:", country.get("region", "No disponible"))
                print("Población:", country.get("population", "No disponible"))
                print("Área (km²):", country.get("area", "No disponible"))
                print("Continente:", country.get("continents", ["No disponible"])[0])
                found = True  
                break  

            index += 1
        
        if not found:  
            print(f"No se encontraron datos para el país: {country_name}")

    else:
        print("Error en la solicitud:", response.status_code)