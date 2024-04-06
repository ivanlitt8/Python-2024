# Escribe un programa que tome una lista de números enteros como entrada del usuario.
# Luego, convierte cada número en la lista a string y únelos en una sola cadena,
# separados por guiones ('-'). Sin embargo, excluye cualquier número que sea múltiplo
# de 3 de la cadena final.


entrada = input("Por favor, ingresa una lista de números separados por espacios: ")

numeros_str = entrada.split()
excluidos_mult_3 = []

for numero_str in numeros_str:
    numero = int(numero_str)
    if numero % 3 != 0:
        excluidos_mult_3.append(numero_str)

numeros_sin_mult_3_str = [str(numero) for numero in excluidos_mult_3]

resultado = '-'.join(numeros_sin_mult_3_str)

print("La cadena sin múltiplos de 3 es:", resultado)

print("La cadena resultante sin múltiplos de 3 es:", resultado)



# Consultar este ejercicio. Cadena es necesariamente un string ? 
# se puede hacer una cadena de string en un vector en este caso?