   

# Ingreso.
word = input("Ingresá una palabra: ")
# si tiene "a" y "n".
if "a" in word and "n" in word:
    print("La palabra contiene 'a' y 'n'.")
    # si solamente tiene "a".
elif "a" in word:
    print("La palabra solo contiene la letra 'a'.")
    # si solamente tiene "n".
elif "n" in word:
    print("La palabra solo contiene la letra 'n'.")
    # si no tiene ni "a" ni "n".
else:
    print("La palabra no contiene ni la letra 'a' ni la letra 'n'.")
