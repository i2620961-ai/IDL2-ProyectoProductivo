# Declaración de variables
edad: int = 0
ingresos: float = 0.0
monto: float = 0.0

# Entrada de datos
edad = int(input("Ingrese su edad: "))
ingresos = float(input("Ingrese sus ingresos mensuales (S/): "))

# Proceso y condición
if edad > 18 and ingresos >= 3000:
    monto = ingresos * 0.05
    print(f"Tiene que tributar. Monto a tributar: S/ {monto:.2f}")
else:
    print("No tiene que tributar.")