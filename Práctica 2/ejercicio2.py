# Importo Counter
from collections import Counter

# Importo variable de ejercicio1
from ejercicio1 import cadena_sin_numeros

# Paso la lista a minúsculas y la divido en palabras
palabras = cadena_sin_numeros.lower().split()

# Busco en la lista palabras con longitud mayor a 4
palabras_mas_de_4_caracteres = [palabra for palabra in palabras if len(palabra) > 4]
# Utilizo Counter
frecuencia_palabras = Counter(palabras_mas_de_4_caracteres)


# (1) Me devuelve una lista con la palabra más común y la frecuencia.
# 1er [0] Accedo al primer elemento (una tupla que tiene la palabra más común y su frecuencia)
# 2do [0] Accedo al primer elemento de la tupla (la palabra más común)
# [1] Accedo al segundo elemento de la tupla, (la frecuencia)

palabra_mas_comun = frecuencia_palabras.most_common(1)[0][0]
frecuencia_maxima = frecuencia_palabras.most_common(1)[0][1]
print(f"La palabra más común con más de 4 caracteres es '{palabra_mas_comun}' con una frecuencia de {frecuencia_maxima} veces.")