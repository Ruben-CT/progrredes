import requests

url = 'https://www.swapi.tech/api/people'
# Esta Api consulta  informacion de 10 personajes de la saga Star Wars.
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    characters = data.get("results", [])
    
    print(f"Hay {len(characters)} personajes disponibles.")

    while True:
        user_input = input("Introduce el número del personaje que deseas conocer (1 al total disponible) o 'salir' para terminar: ")

        if user_input.lower() == 'salir':
            print("Saliendo del programa.")
            break 

        try:
            character_number = int(user_input) - 1
            
            if 0 <= character_number < len(characters):
                character = characters[character_number]

                character_url = character.get("url")
                character_response = requests.get(character_url)

                if character_response.status_code == 200:
                    character_data = character_response.json().get("result", {}).get("properties", {})
                    
                    print("Nombre:", character_data.get("name", "No disponible"))
                    print("Altura:", character_data.get("height", "No disponible"))
                    print("Género:", character_data.get("gender", "No disponible"))
                    print("Color de ojos:", character_data.get("eye_color", "No disponible"))
                    print("Color de piel:", character_data.get("skin_color", "No disponible"))
                    print("Año de nacimiento:", character_data.get("birth_year", "No disponible"))
                    print("-" * 30)
                else:
                    print("Error al obtener detalles adicionales del personaje.")
            else:
                print("Número de personaje fuera de rango.")
        
        except ValueError:
            print("Por favor, ingresa un número válido o 'salir' para terminar.")

else:
    print("Error en la solicitud:", response.status_code)