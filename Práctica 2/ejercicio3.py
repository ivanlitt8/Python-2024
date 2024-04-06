# Importo el módulo.
import string
# Variable string.
jupyter_info = """JupyterLab is a web-based interactive development
environment for Jupyter notebooks, code, and data. JupyterLab is
flexible: configure and arrange the user interface to support a wide
range of workflows in data science, scientific computing, and machine
learning. JupyterLab is extensible and modular: write plugins that add
new components and integrate with existing ones."""

# Ingreso.
letra = input("Ingrese una letra: ")

# Verifico que el ingreso es una letra.
if len(letra) == 1 and letra in string.ascii_letters:
    
    # Convierto a minúsculas.
    letra = letra.lower()
    
    # Divido con split el texto en palabras.
    palabras = jupyter_info.split()
    
    # Filtro palabras que contengan la letra.
    # strip(string.punctuation) elimina signos de puntuación.
    palabras_filtradas = [palabras.strip(string.punctuation) for palabras in palabras if letra in palabras.lower()]
    
    # Si palabras_filtradas no es vacio muestro el contenido
    if palabras_filtradas:
        print(f"Palabras que contienen la letra '{letra}':")
        for word in palabras_filtradas:
            print(word)
    else:
        print("No se encontraron palabras que contengan la letra '{letra}'.")
else:
    print("Error: Debe ingresar una única letra.")