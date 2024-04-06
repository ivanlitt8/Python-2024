# Implementa un programa que solicite al usuario que ingrese una lista de números.
# Luego, imprime la lista pero detén la impresión si encuentras un número negativo.
# Nota: utilice la sentencia break cuando haga falta.

# Solicitar al usuario que ingrese una lista de números separados por espacios
entrada = input("Por favor, ingresa una lista de números separados por espacios: ")
numeros_str = entrada.split(" ")
numeros = []
for num in numeros_str:
    numeros.append(int(num))
print("Lista de números ingresada:", numeros)

for numero in numeros:
    if numero >= 0 :
        print(numero)
    else:
        break