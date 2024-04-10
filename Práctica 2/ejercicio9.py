def calcular_valor_palabra(palabra):
    # Diccionario de valores .
    valores_letras = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1,
        'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
    }
    
    # Convierto la palabra a mayusculas .
    palabra = palabra.upper()
    
    # Inicializo en cero
    valor_total = 0
    
    # Calculo el valor de la palabra sumando cada letra
    for letra in palabra:
        valor_total += valores_letras.get(letra, 0)
    
    return valor_total

# Ejemplo
palabra = "queso"
valor = calcular_valor_palabra(palabra)
print(f"El valor de la palabra '{palabra}' es: {valor}")