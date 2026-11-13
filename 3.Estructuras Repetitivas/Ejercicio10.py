def analizar_notas_curso():
    print("=== SISTEMA DE ANÁLISIS DE CALIFICACIONES ===")

    # 1. Declaración de variables
    n: int = 0
    notas: list[int] = []
    i: int = 0
    nota: int = 0
    mayor_nota: int = 0
    menor_nota: int = 0
    cant_mayor: int = 0
    cant_menor: int = 0
    promedio_salon: float = 0.0
    cant_pares: int = 0
    cant_impares: int = 0
    cant_aprobados: int = 0
    cant_desaprobados: int = 0
    porc_aprobados: float = 0.0
    porc_desaprobados: float = 0.0

    # 2. Validación de N (mínimo 5 y máximo 20 estudiantes)
    while True:
        try:
            n = int(input("\nIngrese la cantidad de estudiantes (entre 5 y 20): "))
            if 5 <= n <= 20:
                break
            print("Error: El número de estudiantes debe estar entre 5 y 20.")
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

    print(f"\nIngrese las notas de 0 a 20 para los {n} estudiantes:")

    # 3. Recolección y validación de las notas individuales
    for i in range(1, n + 1):
        while True:
            try:
                nota = int(input(f"Estudiante N° {i} - Nota: "))
                if 0 <= nota <= 20:
                    notas.append(nota)
                    break
                print("Error: La calificación debe ser un valor entre 0 y 20.")
            except ValueError:
                print("Error: Debe ingresar un número entero válido.")

    # 4. Procesamiento de estadísticas

    # a) Mayor nota y b) Menor nota
    mayor_nota = max(notas)
    menor_nota = min(notas)

    # c) Cantidad de alumnos que obtuvieron la mayor y menor nota
    cant_mayor = notas.count(mayor_nota)
    cant_menor = notas.count(menor_nota)

    # d) Promedio de notas del salón
    promedio_salon = sum(notas) / n

    # e) Cantidad de notas pares e impares
    cant_pares = sum(1 for nota in notas if nota % 2 == 0)
    cant_impares = sum(1 for nota in notas if nota % 2 != 0)

    # f) Aprobados (>= 13) y desaprobados (< 13)
    cant_aprobados = sum(1 for nota in notas if nota >= 13)
    cant_desaprobados = n - cant_aprobados

    # g) Porcentajes de aprobados y desaprobados
    porc_aprobados = (cant_aprobados / n) * 100
    porc_desaprobados = (cant_desaprobados / n) * 100

    # 5. Presentación de resultados
    print("\n" + "="*45)
    print("         REPORTE ACADÉMICO DEL CURSO")
    print("="*45)
    print(f"\n• Notas registradas: {notas}")
    print(f"\na) Mayor nota: {mayor_nota}")
    print(f"b) Menor nota: {menor_nota}")
    print(f"c) Alumnos con la mayor nota: {cant_mayor}")
    print(f"d) Alumnos con la menor nota: {cant_menor}")
    print(f"e) Promedio de notas del salón: {promedio_salon:.2f}")
    print(f"f) Cantidad de notas pares: {cant_pares}")
    print(f"g) Cantidad de notas impares: {cant_impares}")
    print(f"h) Cantidad de alumnos aprobados (>= 13): {cant_aprobados}")
    print(f"i) Cantidad de alumnos desaprobados (< 13): {cant_desaprobados}")
    print(f"j) Porcentaje de aprobados: {porc_aprobados:.1f}%")
    print(f"k) Porcentaje de desaprobados: {porc_desaprobados:.1f}%")
    print("="*45)


if __name__ == "__main__":
    analizar_notas_curso()