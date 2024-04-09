def contar_caracteres(frase):
    # Inicializar contadores
    mayusculas = 0
    minusculas = 0
    no_letras = 0
    
    # Recorrer cada carácter en la frase
    for caracter in frase:
        # Contar mayúsculas
        if caracter.isupper():
            mayusculas += 1
        # Contar minúsculas
        elif caracter.islower():
            minusculas += 1
        # Contar caracteres no letras
        elif not caracter.isspace():
            no_letras += 1
    
    # Dividir la frase en palabras para contar su cantidad
    palabras = frase.split()
    cantidad_palabras = len(palabras)
    
    # Imprimir los resultados
    print("Mayúsculas:", mayusculas)
    print("Minúsculas:", minusculas)
    print("Caracteres no letras:", no_letras)
    print("Cantidad de palabras:", cantidad_palabras)

# Frase proporcionada
text = """ La brecha salarial alcanzó el 27,7%: las mujeres ocupadas
debieron trabajar 8 días y 10 horas más que los varones ocupados para
ganar lo mismo que ellos en un mes. """

# Llamar a la función para contar caracteres
contar_caracteres(text)
