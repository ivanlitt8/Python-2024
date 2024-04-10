def contar_palabras_con_string(frase, palabra):
    # Convierto la frase y la palabra a minusculas .
    frase = frase.lower()
    palabra = palabra.lower()
    
    # Divido la frase en palabras.
    palabras = frase.split()
    
    # Cuento la cantidad de veces que aparece la palabra en la lista de palabras.
    cantidad = palabras.count(palabra)
    
    # Imprimo resultado.
    print("Resultado:", cantidad)

# Ejemplos
frase = "Tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban trigo tres tristes tigres."
palabra = input("Palabra: ")
contar_palabras_con_string(frase, palabra)
