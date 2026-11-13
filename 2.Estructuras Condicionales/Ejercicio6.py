# Declaración de variables
h: int = 0
m: int = 0
s: int = 0
n: int = 0

# Entrada de datos
h = int(input("Ingrese horas (HH): "))
m = int(input("Ingrese minutos (MM): "))
s = int(input("Ingrese segundos (SS): "))
n = int(input("Ingrese la cantidad de segundos a agregar (N): "))

# Proceso
s += n
m += s // 60
s = s % 60

h += m // 60
m = m % 60

h = h % 24

# Salida de resultados
print(f"Nueva hora: {h:02d}:{m:02d}:{s:02d}")