def contar_ocurrencias(palabra):
    # Convierto la palabra a minusculas.
    palabra = palabra.lower()
    
    # Itero sobre las letra en la palabra
    for letra in palabra:
        # Cuento ocurrencias de la letra actual
        if(letra.isalpha()):
            cantidad = palabra.count(letra)
            # Si hay mas de una ocurrencia, "No"
            if cantidad > 1:
                return "No"
    # Si no hay mas de una ocurrencia, "Si"
    return "Sí"

palabra = input("Ingrese una palabra: ")
print(contar_ocurrencias(palabra))