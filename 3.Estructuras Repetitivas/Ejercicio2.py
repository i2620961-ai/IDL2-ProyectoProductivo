def analizar_numeros():
    # DECLARACIÓN E INICIALIZACIÓN DE VARIABLES
    pares: int = 0
    impares: int = 0
    positivos: int = 0
    negativos: int = 0
    neutros: int = 0
    num: int = 0

    print("=== ANALIZADOR DE 10 NÚMEROS ===")

    # ESTRUCTURA REPETITIVA (BUCLE FOR QUE SE EJECUTA 10 VECES)
    for i in range(1, 11):
        # ENTRADA DE DATOS
        num = int(input(f"\n Ingresa el número {i} de 10: "))

        # EVALUAMOS SI ES PAR O IMPAR
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1

        # EVALUAMOS SI ES POSITIVO, NEGATIVO O NEUTRO
        if num > 0:
            positivos += 1
        elif num < 0:
            negativos += 1
        else:
            neutros += 1

    # SALIDA DE DATOS
    print("\n--- RESUMEN FINAL DE LOS 10 NÚMEROS ---")
    print(f"\n• Pares: {pares}")
    print(f"• Impares: {impares}")
    print(f"• Positivos: {positivos}")
    print(f"• Negativos: {negativos}")
    print(f"• Neutros (ceros): {neutros}")


# EJECUTAR EL PROGRAMA PRINCIPAL
if __name__ == "__main__":
    analizar_numeros()