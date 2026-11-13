def separar_y_calcular(n: int) -> None:
    # DECLARACIÓN DE VARIABLES
    pares: list[int] = []
    impares: list[int] = []
    suma_pares: int = 0
    suma_impares: int = 0
    prom_pares: float = 0.0
    prom_impares: float = 0.0

    # ESTRUCTURA REPETITIVA: RECORREMOS DESDE 1 HASTA N
    for i in range(1, n + 1):
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)

    # PROCESO: SUMAS
    suma_pares = sum(pares)
    suma_impares = sum(impares)

    # PROCESO: PROMEDIOS
    prom_pares = suma_pares / len(pares) if len(pares) > 0 else 0
    prom_impares = suma_impares / len(impares) if len(impares) > 0 else 0

    # SALIDA DE DATOS
    print(f"\n--- RESULTADOS PARA EL NÚMERO {n} ---")
    print(f"\nNúmeros Pares: {pares}")
    print(f"Suma de Pares: {suma_pares} | Promedio: {prom_pares:.2f}")

    print(f"\nNúmeros Impares: {impares}")
    print(f"Suma de Impares: {suma_impares} | Promedio: {prom_impares:.2f}")


# BLOQUE PRINCIPAL
limite_n: int = 0

limite_n = int(input("Ingresa el número límite hasta el cual deseas calcular la suma y el promedio: "))

separar_y_calcular(limite_n)