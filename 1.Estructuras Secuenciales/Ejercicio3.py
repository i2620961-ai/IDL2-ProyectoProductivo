# DECLARACIÓN E INICIALIZACIÓN DE VARIABLES
inv1: float = 0.0
inv2: float = 0.0
inv3: float = 0.0
total_invertido: float = 0.0
porcentaje1: float = 0.0
porcentaje2: float = 0.0
porcentaje3: float = 0.0

# ENTRADA DE DATOS
inv1 = float(input("Monto invertido por el Socio 1 (S/): "))
inv2 = float(input("Monto invertido por el Socio 2 (S/): "))
inv3 = float(input("Monto invertido por el Socio 3 (S/): "))

# PROCESO
total_invertido = inv1 + inv2 + inv3

porcentaje1 = (inv1 / total_invertido) * 100
porcentaje2 = (inv2 / total_invertido) * 100
porcentaje3 = (inv3 / total_invertido) * 100

# SALIDA DE DATOS
print(f"Inversión Total: S/ {total_invertido:.2f}")
print(f"Socio 1: {porcentaje1:.2f}%")
print(f"Socio 2: {porcentaje2:.2f}%")
print(f"Socio 3: {porcentaje3:.2f}%")