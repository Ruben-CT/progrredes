'''
Nombre: Rubén COlmenro Sánchez
Descripcion: 
Fecha: 19/09/2024
'''
word_without_vowels = ""

# Indicar al usuario que ingrese una palabra
# y asignarla a la variable user_word.
user_word=input("Ingresa una palabra: ")
user_word = user_word.upper()
for letter in user_word:
    if letter == "A" or letter == "E" or letter == "I" or letter == "O":
        continue
    elif letter == "U":
        continue
    word_without_vowels=word_without_vowels+letter
    #Imprimir palabra
print(word_without_vowels)