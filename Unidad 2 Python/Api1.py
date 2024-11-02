import requests

# Esta API da imágenes de la NASA
url = "https://api.nasa.gov/EPIC/api/natural/images?api_key=DEMO_KEY"

while True:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        images_to_show = data[:10]

        print("Imágenes disponibles:")
        for index, image in enumerate(images_to_show):
            print(f"{index + 1}. Identificador: {image['identifier']}")

        while True:
            user_choice = input("\n¿De qué imagen quieres ver los datos? (1-10) o 'salir' para terminar: ").strip()

            if user_choice.lower() == 'salir':
                print("Saliendo del programa.")
                exit() 

            user_choice = int(user_choice)  
            choice_index = user_choice - 1  

            if 0 <= choice_index < len(images_to_show):
                selected_image = images_to_show[choice_index]
                
                print("\nDatos de la imagen seleccionada:")
                print("Identificador:", selected_image["identifier"])
                print("Descripción:", selected_image["caption"])
                print("Fecha:", selected_image["date"])
                print("Posición del sol:", selected_image["sun_j2000_position"])
                print("Cuaterniones de actitud:", selected_image["attitude_quaternions"])

                continue_choice = input("\n¿Quieres ver otra imagen? (sí/no): ").strip().lower()
                if continue_choice != 'sí':
                    print("Saliendo del programa.")
                    exit()  

            else:
                print("Por favor, elige un número entre 1 y 10.")

    else:
        print("Error en la solicitud:", response.status_code)
        break