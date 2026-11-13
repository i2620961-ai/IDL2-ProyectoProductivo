# DECLARACIÓN E INICIALIZACIÓN DE VARIABLES
A: float = 0.0
B: float = 0.0
C: float = 0.0
area_rectangulo: float = 0.0
area_triangulo: float = 0.0
area_total: float = 0.0

# ENTRADA DE DATOS
A = float(input("Ingrese la altura máxima izquierda (Lado A): "))
B = float(input("Ingrese el ancho de la base (Lado B): "))
C = float(input("Ingrese la altura de la sección derecha (Lado C): "))

# PROCESO
area_rectangulo = B * C
area_triangulo = (B * (A - C)) / 2
area_total = area_rectangulo + area_triangulo

# SALIDA DE DATOS
print(f"Área rectangular base: {area_rectangulo:.2f} m²")
print(f"Área triangular superior: {area_triangulo:.2f} m²")
print(f"ÁREA TOTAL DEL TERRENO: {area_total:.2f} m²")