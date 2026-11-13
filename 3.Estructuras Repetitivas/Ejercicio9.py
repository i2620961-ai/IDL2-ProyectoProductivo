def calcular_producto_secuencia():
    print("=== PRODUCTO DE SECUENCIA DESCENDENTE CON ARRAYS ===")

    # 1. Declaración de variables
    secuencia: list[int] = []
    producto: int = 1
    num: int = 0

    # 2. Generar el array con los números desde 100 hasta 2
    secuencia = list(range(100, 0, -2))

    # 3. Inicializar el acumulador en 1
    producto = 1

    # 4. Recorrer el array para multiplicar
    for num in secuencia:
        producto *= num

    # 5. MOSTRAR TODOS LOS ELEMENTOS DEL ARRAY
    print(f"\nArray completo generado:\n{secuencia}")
    print(f"\nCantidad total de números: {len(secuencia)}")
    print(f"El producto total es: {producto}")

if __name__ == "__main__":
    calcular_producto_secuencia()