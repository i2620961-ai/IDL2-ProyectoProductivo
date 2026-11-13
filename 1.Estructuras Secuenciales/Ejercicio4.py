# DECLARACIÓN E INICIALIZACIÓN DE VARIABLES
sueldo_base: float = 0.0
venta1: float = 0.0
venta2: float = 0.0
venta3: float = 0.0
total_ventas: float = 0.0
comision: float = 0.0
total_mes: float = 0.0

# ENTRADA DE DATOS
sueldo_base = float(input("Ingrese el sueldo base (S/): "))
venta1 = float(input("Ingrese la venta 1 (S/): "))
venta2 = float(input("Ingrese la venta 2 (S/): "))
venta3 = float(input("Ingrese la venta 3 (S/): "))

# PROCESO
total_ventas = venta1 + venta2 + venta3
comision = total_ventas * 0.25
total_mes = sueldo_base + comision

# SALIDA DE DATOS
print(f"Monto por comisiones (25%): S/ {comision:.2f}")
print(f"Sueldo total a percibir: S/ {total_mes:.2f}")