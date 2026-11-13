# DECLARACIÓN E INICIALIZACIÓN DE VARIABLES
monto: int = 0
b200: int = 0
b100: int = 0
b50: int = 0
b20: int = 0
b10: int = 0
m5: int = 0
m1: int = 0

# ENTRADA DE DATOS
monto = int(input("Ingrese la cantidad entera a retirar (S/): "))

# PROCESO
b200 = monto // 200
monto %= 200

b100 = monto // 100
monto %= 100

b50 = monto // 50
monto %= 50

b20 = monto // 20
monto %= 20

b10 = monto // 10
monto %= 10

m5 = monto // 5
monto %= 5

m1 = monto // 1

# SALIDA DE DATOS
print(f"Billetes de S/ 200: {b200}")
print(f"Billetes de S/ 100: {b100}")
print(f"Billetes de S/ 50 : {b50}")
print(f"Billetes de S/ 20 : {b20}")
print(f"Billetes de S/ 10 : {b10}")
print(f"Monedas de S/ 5   : {m5}")
print(f"Monedas de S/ 1   : {m1}")