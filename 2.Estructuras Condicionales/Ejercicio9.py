# Declaración de variables
n: int = 0
precio_unitario: float = 0.0
subtotal: float = 0.0
pct: float = 0.0
descuento: float = 0.0
total: float = 0.0

# Entrada de datos
n = int(input("Ingrese la cantidad de camisas compradas: "))
precio_unitario = float(input("Ingrese el precio unitario de la camisa (S/): "))

# Cálculo del subtotal
subtotal = n * precio_unitario

# Determinar porcentaje de descuento
if n >= 1 and n <= 4:
    pct = 0.125
elif n >= 5 and n <= 8:
    pct = 0.20
else:
    pct = 0.315

# Cálculo del descuento y total
descuento = subtotal * pct
total = subtotal - descuento

# Salida de resultados
print(f"Compra final sin descuento: S/ {subtotal:.2f}")
print(f"Monto del descuento: S/ {descuento:.2f}")
print(f"Compra final con descuento: S/ {total:.2f}")