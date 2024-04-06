# Modifique el ejercicio 4 para que dada la lista de número genere dos nuevas listas, una
# con los número pares y otras con los que son impares. Imprima las listas al terminar de
# procesarlas.


numeros = [-5, -62, -3, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = []
numeros_impares = []

for numero in numeros:
    if numero % 2 != 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)
        
print(numeros_pares)
print(numeros_impares)