def calcular_ahorro_anual():
    print("=== CALCULADORA DE AHORRO ANUAL ===")

    # 1. Declaración de variables
    total_ahorrado: float = 0.0  # Variable acumuladora para el total
    mes: int = 0
    deposito: float = 0.0

    print("Ingrese las cantidades depositadas al finalizar cada mes:\n")

    # Bucle que recorre los 12 meses del año
    for mes in range(1, 13):
        while True:
            try:
                # Pedimos el monto variable del mes
                deposito = float(input(f"Mes {mes} - Monto depositado: S/. "))
                if deposito < 0:
                    print("El monto no puede ser negativo. Intente de nuevo.")
                    continue
                break
            except ValueError:
                print("Error: Por favor, ingrese un valor numérico válido.")

        # Acumulamos el depósito al total general
        total_ahorrado += deposito

        # Mostramos cuánto lleva ahorrado en cada paso (requisito del problema)
        print(f"   -> [Progreso] Acumulado hasta el mes {mes}: S/. {total_ahorrado:.2f}\n")

    # Mostrar el resultado final al cabo de los 12 meses
    print("==================================================")
    print(f"  AHORRO FINAL DESPUÉS DE 12 MESES: S/. {total_ahorrado:.2f}")
    print("==================================================")

if __name__ == "__main__":
    calcular_ahorro_anual()