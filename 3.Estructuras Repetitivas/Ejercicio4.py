def encontrar_max_min():
    print("=== ENCONTRAR MÁXIMO Y MÍNIMO DE UNA LISTA ===")

    # 1. Declaración de variables
    n: int = 0
    numeros: list[float] = []
    num: float = 0.0
    maximo: float = 0.0
    minimo: float = 0.0

    # 2. Validación de la cantidad de números (N)
    try:
        n = int(input("Ingrese la cantidad total de números: "))
        if n <= 0:
            print("El número N debe ser mayor a 0.")
            return
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")
        return

    # 3. Recolección de datos en una lista (array)
    print(f"\nIngrese los {n} números:")
    for i in range(1, n + 1):
        num = float(input(f"Número {i}: "))
        numeros.append(num)

    # 4. Inicialización: asumimos temporalmente que el primer número es el mayor y el menor
    maximo = numeros[0]
    minimo = numeros[0]

    # 5. Proceso simultáneo: evaluamos cada número del array
    for num in numeros:
        if num > maximo:
            maximo = num  # Actualizamos el nuevo máximo si encontramos uno mayor
        if num < minimo:
            minimo = num  # Actualizamos el nuevo mínimo si encontramos uno menor

    # 6. Presentación ordenada de resultados
    print(f"\n=== RESULTADOS FINALES ===")
    print(f"• Lista de números ingresados: {numeros}")
    print(f"• El número máximo es: {maximo}")
    print(f"• El número mínimo es: {minimo}")

if __name__ == "__main__":
    encontrar_max_min()