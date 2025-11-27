# Por Brando Matute

from allpairspy import AllPairs


# Devuelve un diccionario con los factores y sus niveles
def obtener_factores():
    # Factores del experimento DOE para el checkout de e-commerce
    factores = {
        "Tipo de usuario": [
            "Invitado",
            "Registrado",
            "Administrador",
        ],
        "Navegador": [
            "Chrome",
            "Firefox",
            "Edge",
            "Safari",
            "Opera",
        ],
        "Idioma": [
            "Español",
            "Inglés",
            "Francés",
            "Portugués",
            "Alemán",
        ],
        "Método de pago": [
            "Tarjeta de crédito",
            "Tarjeta de débito",
            "PayPal",
            "Transferencia bancaria",
            "Pago contra entrega",
        ],
        "Tipo de envío": [
            "Estándar",
            "Express",
            "Internacional",
            "Recolección en tienda",
        ],
    }
    return factores


# Genera las combinaciones pairwise usando allpairspy
def generar_combinaciones_pairwise():
    factores = obtener_factores()
    niveles_por_factor = list(factores.values())
    return list(AllPairs(niveles_por_factor))


# Imprime la matriz pairwise en consola en formato de tabla
def imprimir_matriz_pairwise():
    factores = obtener_factores()
    nombres_factores = list(factores.keys())
    combinaciones_pairwise = generar_combinaciones_pairwise()

    print("MATRIZ DE PRUEBAS (PAIRWISE) PARA EL CHECKOUT DE E-COMMERCE")
    print("-" * 90)
    print(f"Número de factores: {len(nombres_factores)}")
    print(f"Número de casos de prueba generados: {len(combinaciones_pairwise)}\n")

    # Encabezado
    encabezado = "ID".ljust(4)
    for nombre in nombres_factores:
        encabezado += nombre.ljust(25)
    print(encabezado)
    print("-" * len(encabezado))

    # Filas de la matriz
    for indice, combinacion in enumerate(combinaciones_pairwise, start=1):
        fila = str(indice).ljust(4)
        for valor in combinacion:
            fila += str(valor).ljust(25)
        print(fila)


# Guarda la matriz en un archivo CSV
def guardar_matriz_csv(nombre_archivo="matriz_pairwise_ecommerce.csv"):
    import csv

    factores = obtener_factores()
    nombres_factores = list(factores.keys())
    combinaciones_pairwise = generar_combinaciones_pairwise()

    with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo, delimiter=";")
        escritor.writerow(["ID"] + nombres_factores)
        for indice, combinacion in enumerate(combinaciones_pairwise, start=1):
            escritor.writerow([indice] + list(combinacion))

    print(f"\nArchivo '{nombre_archivo}' generado correctamente.")


# Si ejecutas este archivo directamente, imprime y genera el CSV
if __name__ == "__main__":
    imprimir_matriz_pairwise()
    generar_csv = True
    if generar_csv:
        guardar_matriz_csv()
