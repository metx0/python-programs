""" 
    # Bucle que se ejecuta hasta que escribas la palabra secreta
    while True:
    user_word = input("Escriba la palabra secreta para salir del bucle: ")
    
    if user_word == "chupacabras":
        print("Has dejado el bucle con éxito")
        break
"""

# Devorador de vocales, versión 1
"""
user_word = input("Ingrese una palabra: ")
user_word = user_word.upper() # La convertimos a mayúsculas y la almacenamos en la misma variable

for letter in user_word: # El bucle se ejecuta por cada letra de user_word
    if letter == "A": # Si la letra es A, saltamos la iteración actual y vamos a la siguiente
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else: # Si las condiciones de arriba no se cumplen, significa que la letra actual no es una vocal, y procedemos a imprimirla
        print(letter)
"""

# Devorador de vocales, versión 2

word_without_vowels = "" # Cadena vacía que usaremos después para concatenar las letras que no sean vocales
user_word = input("Ingrese una palabra: ") 
user_word = user_word.upper() # La convertimos a mayúsculas y la almacenamos en la misma variable

for letter in user_word: # El bucle se ejecuta por cada letra de user_word
    if letter == "A": # Si la letra es A, saltamos la iteración actual y vamos a la siguiente; lo mismo con las demás 
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else: # Si las condiciones de arriba no se cumplen, significa que la letra actual no es una vocal, y la concatenamos a word_without_vowels
        word_without_vowels += letter # word_without_vowels = word_without_vowels + letter

print(word_without_vowels)



