# Declaración de variables
materias: int = 0
promedio: float = 0.0
costo_base: float = 0.0
descuento: float = 0.0
pago_final: float = 0.0

# Entrada de datos
materias = int(input("Ingrese el número de materias cursadas: "))
promedio = float(input("Ingrese el promedio obtenido: "))

# Proceso
costo_base = materias * 100.0

if promedio >= 18.0:
    descuento = (materias / 2.0) * 100.0 * 0.50
else:
    descuento = 0.0

pago_final = costo_base - descuento

# Salida de resultados
print(f"Total a pagar: S/ {pago_final:.2f}")
print(f"Descuento aplicado: S/ {descuento:.2f}")