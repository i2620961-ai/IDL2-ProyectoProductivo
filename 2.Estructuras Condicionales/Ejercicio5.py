# Declaración de variables
a: float = 0.0
b: float = 0.0
c: float = 0.0
perimetro: float = 0.0
s: float = 0.0
area: float = 0.0

import math

# Entrada de datos
a = float(input("Ingrese el lado a: "))
b = float(input("Ingrese el lado b: "))
c = float(input("Ingrese el lado c: "))

# Validación de los lados
if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
    print("Los lados ingresados no forman un triángulo.")

# Clasificación del triángulo
elif a == b and b == c:
    perimetro = a + b + c
    print(f"Es un triángulo Equilátero. Perímetro: {perimetro:.2f}")

elif a == b or b == c or a == c:
    print("Es un triángulo Isósceles.")

    if a == b:
        print("Los lados iguales son a y b.")
    if b == c:
        print("Los lados iguales son b y c.")
    if a == c:
        print("Los lados iguales son a y c.")

else:
    s = (a + b + c) / 2.0
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"Es un triángulo Escaleno. Área: {area:.2f}")