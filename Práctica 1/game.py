import random

# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)

# Número máximo de intentos permitidos
max_attempts = 10
# Se cuentan los fallos dentro de una cantidad de intentos
fallos = 0

# Lista para almacenar las letras adivinadas
guessed_letters = []

print("¡Bienvenido al juego de adivinanzas!")
dificultad = input("Por favor seleccione su nivel: fácil, media, difícil: ")

# Mostrar la letras segun dificultad
if dificultad == "facil":
    # Mostrar todas las vocales considerando acentos
    vocales = "aáeéiíoóuú"
    word_displayed = ""
    for letra in secret_word:
        if letra in vocales:
            word_displayed += letra
        else:
            word_displayed += "_"
elif dificultad == "media":
    # Mostrar ultima y primer letra
    word_displayed = secret_word[0] + "_" * (len(secret_word)-2) + secret_word[-1]
elif dificultad == "dificil":
    # Original
    word_displayed = "_" * len(secret_word)
else:
    print("Nivel de dificultad no válido. Intente nuevamente.")
    exit()
    
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")

# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")

while fallos < max_attempts :
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()
    
    # Solucion bug de caracter vacio
    if letter == "":
        print("¡El espacio no es un caracter valido! Ingrese otro caracter")
        continue
 
    # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue
    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)
 
    # Verificar si la letra está en la palabra secreta
    if letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        print("Lo siento, la letra no está en la palabra.")
        # Se cuenta el fallo
        fallos+=1
 
    # Mostrar la palabra parcialmente adivinada
    letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")
    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")
    
     # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
else:
 print(f"¡Oh no! Has agotado tus {max_attempts} intentos.")
 print(f"La palabra secreta era: {secret_word}")
