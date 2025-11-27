# Por Brando Matute

import pytest
from busqueda_binaria import busqueda_binaria

@pytest.mark.parametrize(
    "lista, objetivo, esperado",
    [
        # Caso estándar con números decimales: valor presente en la lista
        ([5.0, 10.0, 15.0, 20.0], 15.0, 2),
        # Caso de búsqueda fallida con números decimales: valor no presente
        ([5.0, 10.0, 15.0, 20.0], 17.5, -1),
        # Caso mixto: lista centrada en cero — valor objetivo igual a cero
        ([-5, -3, -1, 0, 2, 4, 6], 0, 3),
        # Caso de rango amplio: lista de números impares — valor presente al inicio tras varias iteraciones
        (list(range(1, 50, 2)), 1, 0),
        # Caso de rango amplio: lista de números impares — valor presente al final de la lista
        (list(range(1, 50, 2)), 49, 24),
        # Caso con valores grandes: búsqueda de un número entero de gran magnitud
        ([1_000_000, 2_000_000, 3_000_000, 4_000_000], 3_000_000, 2),
        # Caso especial: lista con elementos repetidos — objetivo no presente en ningún elemento
        ([2, 2, 2, 2], 3, -1),
        # Caso especial: lista con todos los elementos iguales — objetivo presente
        ([7, 7, 7, 7, 7], 7, 2),
        # Caso de estrés: lista grande donde el objetivo está presente en el centro
        (list(range(1000)), 500, 500),
        # Caso de estrés: lista grande donde el objetivo no está — valor menor que el mínimo
        (list(range(1000)), -1, -1),
    ]
)
def test_busqueda_binaria(lista, objetivo, esperado):
    resultado = busqueda_binaria(lista, objetivo)
    assert resultado == esperado