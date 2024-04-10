def contar_caracteres(frase):
    # Contadores.
    mayusculas = 0
    minusculas = 0
    no_letras = 0
    
    # Recorro cada caracter en la frase.
    for caracter in frase:
        # Cuento mayusculas
        if caracter.isupper():
            mayusculas += 1
        # Cuento minusculas
        elif caracter.islower():
            minusculas += 1
        # Cuento caracteres de tipo no letras
        elif not caracter.isspace():
            no_letras += 1
    
    # Divido la frase en palabras para contar su cantidad
    palabras = frase.split()
    cantidad_palabras = len(palabras)
    
    # Impresion
    print("Mayúsculas:", mayusculas)
    print("Minúsculas:", minusculas)
    print("Caracteres no letras:", no_letras)
    print("Cantidad de palabras:", cantidad_palabras)

text = """ La brecha salarial alcanzó el 27,7%: las mujeres ocupadas
debieron trabajar 8 días y 10 horas más que los varones ocupados para
ganar lo mismo que ellos en un mes. """

contar_caracteres(text)
