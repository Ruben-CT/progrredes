'''
Nombre: Rubén COlmenro Sánchez
Descripcion: 
Fecha: 19/09/2024
'''
import time
user_word=input("Ingresa tu nombre ")

for letter in user_word:
    
    if  not (letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U'):
        print (letter)
    time.sleep(1)    