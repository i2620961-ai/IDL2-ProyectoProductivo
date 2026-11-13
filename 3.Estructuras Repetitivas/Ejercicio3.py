def analizar_conjunto_numeros():
    print("=== ANALIZADOR DE CONJUNTO DE NÚMEROS ===")

    # 1. Declaración de variables
    n: int = 0
    x: float = 0.0
    numeros: list[float] = []
    num: float = 0.0
    menores: int = 0
    mayores: int = 0
    iguales: int = 0
    entre_1_y_x: int = 0
    ninguna: int = 0
    limite_inferior: float = 0.0
    limite_superior: float = 0.0
    porc_menores: float = 0.0
    porc_mayores: float = 0.0
    porc_iguales: float = 0.0
    porc_entre: float = 0.0
    porc_ninguna: float = 0.0

    # 2. Validación y lectura de datos iniciales
    try:
        n = int(input("\nIngrese la cantidad total de números a analizar: "))
        if n <= 0:
            print("El número debe ser mayor a 0.")
            return
        x = float(input("Ingrese el número de referencia para comparar (X) : "))
    except ValueError:
        print("Error: Debe ingresar números válidos.")
        return

    # 3. Recolección de datos usando un array (lista)
    print(f"\nIngrese los {n} números:")
    for i in range(1, n + 1):
        num = float(input(f"Número {i}: "))
        numeros.append(num)

    # 4. Estructura repetitiva para evaluar cada número del array
    for num in numeros:
        if num < x:
            menores += 1
        if num > x:
            mayores += 1
        if num == x:
            iguales += 1

        # Definimos los límites dinámicos para el rango entre 1 y X
        limite_inferior = min(1.0, x)
        limite_superior = max(1.0, x)
        if limite_inferior <= num <= limite_superior:
            entre_1_y_x += 1

        # Control para los que no cumplen ninguna de las condiciones anteriores
        if not (num < x or num > x or num == x or (limite_inferior <= num <= limite_superior)):
            ninguna += 1

    # 5. Cálculo de porcentajes (Regla de tres: (cantidad / N) * 100)
    porc_menores = (menores / n) * 100
    porc_mayores = (mayores / n) * 100
    porc_iguales = (iguales / n) * 100
    porc_entre = (entre_1_y_x / n) * 100
    porc_ninguna = (ninguna / n) * 100

    # 6. Presentación ordenada de resultados
    print(f"\n=== RESULTADOS FINALES (Total: {n}, X = {x}) ===")
    print(f"\n• Menores que {x}: {porc_menores:.2f}% ({menores} números)")
    print(f"• Mayores que {x}: {porc_mayores:.2f}% ({mayores} números)")
    print(f"• Iguales a {x}: {porc_iguales:.2f}% ({iguales} números)")
    print(f"• Entre 1 y {x}: {porc_entre:.2f}% ({entre_1_y_x} números)")
    print(f"• Sin condición: {porc_ninguna:.2f}% ({ninguna} números)")


if __name__ == "__main__":
    analizar_conjunto_numeros()