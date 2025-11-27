# Por Brando Matute

from allpairspy import AllPairs
import csv

# Factores del experimento para el checkout de e-commerce
FACTORES = {
    "Tipo de usuario": ["Invitado", "Registrado", "Administrador"],
    "Navegador": ["Chrome", "Firefox", "Edge", "Safari", "Opera"],
    "Idioma": ["Español", "Inglés", "Francés", "Portugués", "Alemán"],
    "Método de pago": ["Tarjeta de crédito", "Tarjeta de débito", "PayPal", "Transferencia bancaria", "Pago contra entrega",],
    "Tipo de envío": ["Estándar", "Express", "Internacional", "Recolección en tienda"],
}

def generar_combinaciones_pairwise():
    niveles = list(FACTORES.values())
    return list(AllPairs(niveles))

def imprimir_matriz_pairwise():
    nombres = list(FACTORES.keys())
    combinaciones = generar_combinaciones_pairwise()

    print("MATRIZ DE PRUEBAS (PAIRWISE) PARA EL CHECKOUT DE E-COMMERCE")
    print("-" * 90)
    print(f"Número de factores: {len(nombres)}")
    print(f"Número de casos de prueba generados: {len(combinaciones)}\n")

    encabezado = "ID".ljust(4) + "".join(nombre.ljust(25) for nombre in nombres)
    print(encabezado)
    print("-" * len(encabezado))

    for i, combo in enumerate(combinaciones, start=1):
        fila = str(i).ljust(4) + "".join(str(v).ljust(25) for v in combo)
        print(fila)

def guardar_matriz_csv(nombre_archivo="Parte1/matriz_pairwise_ecommerce.csv"):
    
    nombres = list(FACTORES.keys())
    combinaciones = generar_combinaciones_pairwise()

    with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo, delimiter=";")
        escritor.writerow(["ID"] + nombres)
        for i, combo in enumerate(combinaciones, start=1):
            escritor.writerow([i] + list(combo))
    print(f"\nArchivo '{nombre_archivo}' generado correctamente.")

if __name__ == "__main__":
    imprimir_matriz_pairwise()
    guardar_matriz_csv()
