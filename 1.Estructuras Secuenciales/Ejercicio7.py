# DECLARACIÓN E INICIALIZACIÓN DE VARIABLES
horas: int = 0
minutos: int = 0
costo_horas: float = 0.0
costo_minutos: float = 0.0
total_pago: float = 0.0

# ENTRADA DE DATOS
horas = int(input("Ingrese las horas completas de uso: "))
minutos = int(input("Ingrese los minutos restantes: "))

# PROCESO
costo_horas = horas * 5.00
costo_minutos = minutos * 0.10
total_pago = costo_horas + costo_minutos

# SALIDA DE DATOS
print(f"Costo por horas: S/ {costo_horas:.2f}")
print(f"Costo por minutos: S/ {costo_minutos:.2f}")
print(f"TOTAL A PAGAR: S/ {total_pago:.2f}")