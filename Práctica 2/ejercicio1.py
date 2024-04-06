# Texto en una variable 

text = """<h1 align="center">
<img src="https://raw.githubusercontent.com/numpy/numpy/main/branding/logo/primary/numpylogo.svg" width="300">
</h1><br>

[![Powered by NumFOCUS](https://img.shields.io/badge/powered%20by-NumFOCUS-orange.svg?style=flat&colorA=E1523D&colorB=007D8A)](https://numfocus.org)
[![PyPI Downloads](https://img.shields.io/pypi/dm/numpy.svg?label=PyPI%20downloads)](https://pypi.org/project/numpy/)
[![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/numpy.svg?label=Conda%20downloads)](https://anaconda.org/conda-forge/numpy)
[![Stack Overflow](https://img.shields.io/badge/stackoverflow-Ask%20questions-blue.svg)](https://stackoverflow.com/questions/tagged/numpy)
[![Nature Paper](https://img.shields.io/badge/DOI-10.1038%2Fs41586--020--2649--2-blue)](https://doi.org/10.1038/s41586-020-2649-2)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/numpy/numpy/badge)](https://securityscorecards.dev/viewer/?uri=github.com/numpy/numpy)

NumPy is the fundamental package for scientific computing with Python.

- **Website:** https://www.numpy.org
- **Documentation:** https://numpy.org/doc
- **Mailing list:** https://mail.python.org/mailman/listinfo/numpy-discussion
- **Source code:** https://github.com/numpy/numpy
- **Contributing:** https://www.numpy.org/devdocs/dev/index.html
- **Bug reports:** https://github.com/numpy/numpy/issues
- **Report a security vulnerability:** https://tidelift.com/docs/security

It provides:

- a powerful N-dimensional array object
- sophisticated (broadcasting) functions
- tools for integrating C/C++ and Fortran code
- useful linear algebra, Fourier transform, and random number capabilities

Testing:

NumPy requires `pytest` and `hypothesis`.  Tests can then be run after installation with:

    python -c "import numpy, sys; sys.exit(numpy.test() is False)"

Code of Conduct
----------------------

NumPy is a community-driven open source project developed by a diverse group of
[contributors](https://numpy.org/teams/). The NumPy leadership has made a strong
commitment to creating an open, inclusive, and positive community. Please read the
[NumPy Code of Conduct](https://numpy.org/code-of-conduct/) for guidance on how to interact
with others in a way that makes our community thrive.

Call for Contributions
----------------------

The NumPy project welcomes your expertise and enthusiasm!

Small improvements or fixes are always appreciated. If you are considering larger contributions
to the source code, please contact us through the [mailing
list](https://mail.python.org/mailman/listinfo/numpy-discussion) first.

Writing code isn’t the only way to contribute to NumPy. You can also:
- review pull requests
- help us stay on top of new and old issues
- develop tutorials, presentations, and other educational materials
- maintain and improve [our website](https://github.com/numpy/numpy.org)
- develop graphic design for our brand assets and promotional materials
- translate website content
- help with outreach and onboard new contributors
- write grant proposals and help with other fundraising efforts

For more information about the ways you can contribute to NumPy, visit [our website](https://numpy.org/contribute/). 
If you’re unsure where to start or how your skills fit in, reach out! You can
ask on the mailing list or here, on GitHub, by opening a new issue or leaving a
comment on a relevant issue that is already open.

Our preferred channels of communication are all public, but if you’d like to
speak to us in private first, contact our community coordinators at
numpy-team@googlegroups.com or on Slack (write numpy-team@googlegroups.com for
an invitation).

We also have a biweekly community call, details of which are announced on the
mailing list. You are very welcome to join.

If you are new to contributing to open source, [this
guide](https://opensource.guide/how-to-contribute/) helps explain why, what,
and how to successfully get involved."""

# Elimino todo lo que no sea letras o números
nueva_cadena = text.replace(","," ").replace("’"," ").replace("+"," ").replace("&"," ").replace("@"," ").replace("<"," ").replace("="," ").replace("."," ").replace(">"," ").replace(":"," ").replace("/"," ").replace("-"," ").replace("*"," ").replace("["," ").replace("]"," ").replace("("," ").replace(")"," ").replace("?"," ").replace("!"," ").replace("`"," ").replace("%"," ").replace('"','')
# Elimino numeros
cadena_sin_numeros = nueva_cadena.replace("0"," ").replace("1"," ").replace("2"," ").replace("3"," ").replace("4"," ").replace("5"," ").replace("6"," ").replace("7"," ").replace("8"," ").replace("9"," ")

# Divido con split el texto según sus saltos de línea.
lineas = cadena_sin_numeros.split("\n")

# Elimino los espacios adicionales en cada línea.
lineas_sin_espacios = [' '.join(linea.strip().split()) for linea in lineas]

# Elimino los elementos de la lista vacios, usando if linea devuelve true
# si tiene al menos un char, false si esta vacío.
lineas_sin_espacios = [linea for linea in lineas_sin_espacios if linea]

vocales = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

for linea in lineas_sin_espacios:
    # Divido con split la línea en palabras.
    palabras = linea.split()
    
    # Verificacion de al menos dos palabras por linea.
    if len(palabras) >= 2:
        # Verifico si la segunda palabra de la linea empieza con vocal.
        segunda_palabra = palabras[1]
        if segunda_palabra[0] in vocales:
            print(linea)
            
# Decidi usar todo el texto, incluidas el codigo HTML por gusto, pero eliminandolo
# se debería obtener el mismo resultado.