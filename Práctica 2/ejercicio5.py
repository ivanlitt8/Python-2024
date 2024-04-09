def analizar_articulo(article):
    # Separar el título y el resumen
    titulo, resumen = article.split("resumen:")
    
    # Verificar el título
    titulo_palabras = len(titulo.split())
    if titulo_palabras > 10:
        print("Título: not ok")
    else:
        print("Título: ok")
    
    # Analizar el resumen
    oraciones = resumen.split(".")
    faciles = 0
    aceptables = 0
    dificiles = 0
    muy_dificiles = 0
    
    for oracion in oraciones:
        palabras = len(oracion.split()) # Contar palabras en la oración
        # Clasificar la oración según el número de palabras
        if palabras <= 12:
            faciles += 1
        elif palabras <= 17:
            aceptables += 1
        elif palabras <= 25:
            dificiles += 1
        else:
            muy_dificiles += 1
    
    # Imprimir los resultados
    print("Cantidad de oraciones fáciles de leer:", faciles)
    print("Cantidad de oraciones aceptables para leer:", aceptables)
    print("Cantidad de oraciones difíciles de leer:", dificiles)
    print("Cantidad de oraciones muy difíciles de leer:", muy_dificiles)

# El artículo proporcionado
article = """título: Experiences in Developing a Distributed Agent-based Modeling Toolkit with Python Version 3
    resumen: Distributed agent-based modeling (ABM) on high-performance
    computing resources provides the promise of capturing unprecedented
    details of large-scale complex systems. However, the specialized
    knowledge required for developing such ABMs creates barriers to wider
    adoption and utilization. Here we present our experiences in
    developing an initial implementation of Repast4Py, a Python-based
    distributed ABM toolkit. We build on our experiences in developing ABM
    toolkits, including Repast for High Performance Computing (Repast
    HPC), to identify the key elements of a useful distributed ABM
    toolkit. We leverage the Numba, NumPy, and PyTorch packages and the
    En este ejemplo se debe informar:
    Python C-API to create a scalable modeling system that can exploit the
    largest HPC resources and emerging computing architectures. """
# Llamar a la función para analizar el artículo
analizar_articulo(article)
