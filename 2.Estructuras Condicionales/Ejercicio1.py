# Declaración de variables
cantidad: int = 0
precio: float = 0.0
total: float = 0.0

# Ingreso de datos
cantidad = int(input("Ingrese la cantidad de llantas a comprar: "))

# Proceso
if cantidad < 5:
    precio = 150.0
else:
    precio = 120.0

total = cantidad * precio

# Salida
print(f"Total a pagar: S/ {total:.2f}")