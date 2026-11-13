# Declaración de variables
nota1: float = 0.0
nota2: float = 0.0
nota3: float = 0.0
nota4: float = 0.0
promedio: float = 0.0

# Entrada de datos
nota1 = float(input("Ingrese la calificación del examen 1: "))
nota2 = float(input("Ingrese la calificación del examen 2: "))
nota3 = float(input("Ingrese la calificación del examen 3: "))
nota4 = float(input("Ingrese la calificación del examen 4: "))

# Proceso
promedio = (nota1 + nota2 + nota3 + nota4) / 4

# Salida de resultados
print(f"El promedio final de las 4 evaluaciones es: {promedio:.2f}")