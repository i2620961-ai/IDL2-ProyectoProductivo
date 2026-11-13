# DECLARACIÓN E INICIALIZACIÓN DE VARIABLES
edad: int = 0
meses: int = 0
semanas: int = 0
dias: int = 0
horas: int = 0

# ENTRADA DE DATOS
edad = int(input("Ingrese su edad en años: "))

# PROCESO
meses = edad * 12
semanas = edad * 52
dias = edad * 365
horas = dias * 24

# SALIDA DE DATOS
print(f"Meses aproximados: {meses}")
print(f"Semanas aproximadas: {semanas}")
print(f"Días aproximados: {dias}")
print(f"Horas aproximadas: {horas}")