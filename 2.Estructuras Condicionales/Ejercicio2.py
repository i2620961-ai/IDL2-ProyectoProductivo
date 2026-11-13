# Declaración de variables
num1: float = 0.0
num2: float = 0.0
num3: float = 0.0
mayor: float = 0.0
menor: float = 0.0

# Entrada de datos
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

# Proceso: encontrar el mayor
mayor = num1

if num2 > mayor:
    mayor = num2

if num3 > mayor:
    mayor = num3

# Proceso: encontrar el menor
menor = num1

if num2 < menor:
    menor = num2

if num3 < menor:
    menor = num3

# Salida de resultados
print(f"El mayor es: {mayor}")
print(f"El menor es: {menor}")