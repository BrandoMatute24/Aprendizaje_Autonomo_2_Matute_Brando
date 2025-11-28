# Por Brando Matute

def busqueda_binaria(lista, objetivo):
    """
    Realiza una búsqueda binaria en una lista ordenada.
    """

    izquierda = 0
    derecha = len(lista) - 1

    # ANOMALÍA 1: Variable definida pero nunca utilizada
    valor_innecesario = "no se usa"

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        # ANOMALÍA 2: Uso de variable antes de ser inicializada
        if variable_sin_inicializar > 0:
            izquierda = medio + 1

        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1
