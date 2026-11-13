# Declaración de variables
minutos: int = 0
dia: str = ""
turno: str = ""
costo_base: float = 0.0
pct_imp: float = 0.0
impuesto: float = 0.0
total: float = 0.0

# Entrada de datos
minutos = int(input("Ingrese los minutos de duración: "))
dia = input("Ingrese el día (domingo/otro): ").strip().lower()
turno = input("Ingrese el turno (nocturno/otro): ").strip().lower()

# Cálculo del costo base
if minutos <= 5:
    costo_base = minutos * 1.00
elif minutos <= 8:
    costo_base = (5 * 1.00) + ((minutos - 5) * 0.80)
elif minutos <= 10:
    costo_base = (5 * 1.00) + (3 * 0.80) + ((minutos - 8) * 0.70)
else:
    costo_base = (5 * 1.00) + (3 * 0.80) + (2 * 0.70) + ((minutos - 10) * 0.50)

# Determinar porcentaje de impuesto
if dia == "domingo":
    if turno == "nocturno":
        pct_imp = 0.05
    else:
        pct_imp = 0.03
else:
    pct_imp = 0.00

# Cálculo del impuesto y total
impuesto = costo_base * pct_imp
total = costo_base + impuesto

# Salida de resultados
print(f"Costo base: S/ {costo_base:.2f}")
print(f"Impuesto aplicado: S/ {impuesto:.2f}")
print(f"Total a pagar: S/ {total:.2f}")