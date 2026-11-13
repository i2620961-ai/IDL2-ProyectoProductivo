def calcular_factorial_y_expansion(n: int):
    """Calcula el valor del factorial y genera la cadena de texto con la expansión (ej: 1x2x3...)."""

    # 1. Declaración de variables
    resultado: int = 1
    elementos: list[str] = []
    expansion: str = ""

    if n < 0:
        return None, "No existe factorial para números negativos"
    if n == 0:
        return 1, "1"

    for i in range(1, n + 1):
        resultado *= i
        elementos.append(str(i))

    expansion = " x ".join(elementos)
    return resultado, expansion


def comparar_factoriales():
    print("=== COMPARADOR Y CALCULADOR DE FACTORIALES ===")

    # 2. Declaración de variables
    num1: int = 0
    num2: int = 0
    val1: int = 0
    val2: int = 0
    exp1: str = ""
    exp2: str = ""
    limite_comun: int = 0

    try:
        num1 = int(input("\nIngrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))

        if num1 < 0 or num2 < 0:
            print("Por favor, ingrese números enteros mayores o iguales a 0.")
            return
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")
        return

    # 3. Sección de resultados del factorial
    print("\n--- RESULTADOS DEL FACTORIAL ---")
    val1, exp1 = calcular_factorial_y_expansion(num1)
    print(f"{num1}! = {exp1} = {val1}")

    val2, exp2 = calcular_factorial_y_expansion(num2)
    print(f"{num2}! = {exp2} = {val2}")

    # 4. Sección de comparación
    print("\n--- COMPARACIÓN ---")
    limite_comun = min(num1, num2)
    print(f"Son iguales hasta el múltiplo {limite_comun}")


if __name__ == "__main__":
    comparar_factoriales()