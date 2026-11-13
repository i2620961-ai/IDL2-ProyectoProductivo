def analizar_asistentes_fiesta():
    print("=== REGISTRO Y ESTADÍSTICAS DE ASISTENTES A LA FIESTA ===")

    # 1. Declaración de variables
    total_asistentes: int = 0
    total_hombres: int = 0
    total_mujeres: int = 0

    suma_edades_hombres: int = 0
    suma_edades_mujeres: int = 0

    edad: int = 0
    edad_minima: int = 0
    edad_maxima: int = 0
    sexo: str = ""
    continuar: str = ""

    promedio_hombres: float = 0.0
    promedio_mujeres: float = 0.0

    while True:
        print(f"\n--- Registro de Asistente N° {total_asistentes + 1} ---")

        # 2. Ingreso y validación de la edad
        while True:
            try:
                edad = int(input("Ingrese la edad: "))
                if edad <= 0 or edad > 120:
                    print("Por favor, ingrese una edad válida (entre 1 y 120 años).")
                    continue
                break
            except ValueError:
                print("Error: Debe ingresar un número entero para la edad.")

        # 3. Ingreso y validación del sexo
        while True:
            sexo = input("Ingrese el sexo (M para Masculino / F para Femenino): ").strip().upper()
            if sexo in ['M', 'F']:
                break
            print("Opción inválida. Ingrese 'M' para hombre o 'F' para mujer.")

        # --- PROCESAMIENTO DE DATOS ---
        total_asistentes += 1

        # Control de Hombres y Mujeres, y suma de edades por sexo
        if sexo == 'M':
            total_hombres += 1
            suma_edades_hombres += edad
        else:
            total_mujeres += 1
            suma_edades_mujeres += edad

        # Control de la persona de menor y mayor edad
        if total_asistentes == 1 or edad < edad_minima:
            edad_minima = edad
        if total_asistentes == 1 or edad > edad_maxima:
            edad_maxima = edad

        # 4. Preguntar si desea registrar a otra persona
        continuar = input("\n¿Desea registrar a otra persona? (S/N): ").strip().lower()
        if continuar != 's':
            break

    # --- CÁLCULOS FINALES Y RESULTADOS ---
    print("\n" + "="*40)
    print("      REPORTE FINAL DE LA FIESTA")
    print("="*40)

    print(f"\n• Total de personas que asistieron: {total_asistentes}")
    print(f"• Total de hombres: {total_hombres}")
    print(f"• Total de mujeres: {total_mujeres}")

    # Promedio de edades por sexo
    if total_hombres > 0:
        promedio_hombres = suma_edades_hombres / total_hombres
        print(f"• Promedio de edades de hombres: {promedio_hombres:.1f} años")
    else:
        print("• Promedio de edades de hombres: No hay registros de hombres.")

    if total_mujeres > 0:
        promedio_mujeres = suma_edades_mujeres / total_mujeres
        print(f"• Promedio de edades de mujeres: {promedio_mujeres:.1f} años")
    else:
        print("• Promedio de edades de mujeres: No hay registros de mujeres.")

    print(f"• Edad del asistente con menor edad: {edad_minima} años")
    print(f"• Edad del asistente con mayor edad: {edad_maxima} años")
    print("="*40)


if __name__ == "__main__":
    analizar_asistentes_fiesta()