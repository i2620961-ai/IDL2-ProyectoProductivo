# DECLARACIÓN E INICIALIZACIÓN DE VARIABLES
monto_base: float = 0.0
porcentaje_desc: float = 0.0
efectivo_pagado: float = 0.0
monto_descuento: float = 0.0
precio_final: float = 0.0
vuelto: float = 0.0

# ENTRADA DE DATOS
monto_base = float(input("Ingrese el monto base de la compra (S/): "))
porcentaje_desc = float(input("Ingrese el porcentaje de descuento (%): "))
efectivo_pagado = float(input("Ingrese el efectivo entregado (S/): "))

# PROCESO
monto_descuento = monto_base * (porcentaje_desc / 100)
precio_final = monto_base - monto_descuento
vuelto = efectivo_pagado - precio_final

# SALIDA DE DATOS
print(f"Monto con descuento: S/ {precio_final:.2f}")
print(f"Cambio / Vuelto: S/ {vuelto:.2f}")