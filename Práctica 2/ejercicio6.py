def contar_palabras_con_string(frase, palabra):
    # Convertir la frase y la palabra a minúsculas para hacer la comparación sin distinguir entre mayúsculas y minúsculas
    frase = frase.lower()
    palabra = palabra.lower()
    
    # Dividir la frase en palabras
    palabras = frase.split()
    
    # Contar la cantidad de veces que aparece la palabra en la lista de palabras
    cantidad = palabras.count(palabra)
    
    # Imprimir el resultado
    print("Resultado:", cantidad)

# Ejemplos
frase = "Tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban trigo tres tristes tigres."
palabra = input("Palabra: ")
contar_palabras_con_string(frase, palabra)
