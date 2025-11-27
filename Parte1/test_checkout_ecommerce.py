# Por Brando Matute

import pytest
from pairwise_ecommerce import generar_combinaciones_pairwise

def simular_checkout(tipo_usuario, navegador, idioma, metodo_pago, tipo_envio):
    return {
        "exito": True,
        "mensaje": "Compra simulada correctamente.",
        "tipo_usuario": tipo_usuario,
        "navegador": navegador,
        "idioma": idioma,
        "metodo_pago": metodo_pago,
        "tipo_envio": tipo_envio,
    }

# Se preparan las combinaciones para parametrizar el test
parametros = [tuple(combo) for combo in generar_combinaciones_pairwise()]

@pytest.mark.parametrize(
    "tipo_usuario, navegador, idioma, metodo_pago, tipo_envio",
    parametros,
)
def test_checkout_pairwise(tipo_usuario, navegador, idioma, metodo_pago, tipo_envio):
    resultado = simular_checkout(
        tipo_usuario, navegador, idioma, metodo_pago, tipo_envio
    )

    assert resultado["exito"] is True
