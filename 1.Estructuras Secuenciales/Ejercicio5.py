# DECLARACIÓN E INICIALIZACIÓN DE VARIABLES
capital: float = 0.0
ganancia_anual: float = 0.0
monto_total: float = 0.0

# ENTRADA DE DATOS
capital = float(input("Ingrese el capital a invertir (S/): "))

# PROCESO
ganancia_anual = capital * 0.02 * 12
monto_total = capital + ganancia_anual

# SALIDA DE DATOS
print(f"Ganancia pura generada: S/ {ganancia_anual:.2f}")
print(f"Monto total acumulado: S/ {monto_total:.2f}")