# Declaración de variables
clave: int = 0
minutos: int = 0
zona: str = ""
tarifa: float = 0.0
valido: bool = False
costo_total: float = 0.0

# Entrada de datos
clave = int(input("Ingrese la clave de la zona destino (10, 12, 20, 22, 30, 32): "))
minutos = int(input("Ingrese el número de minutos hablados: "))

# Identificación de zona y tarifa
if clave == 10:
    zona = "América del norte"
    tarifa = 2.2
    valido = True
elif clave == 12:
    zona = "América del centro"
    tarifa = 2.5
    valido = True
elif clave == 20:
    zona = "América del sur"
    tarifa = 1.2
    valido = True
elif clave == 22:
    zona = "Asia"
    tarifa = 3.5
    valido = True
elif clave == 30:
    zona = "Europa"
    tarifa = 3.0
    valido = True
elif clave == 32:
    zona = "África"
    tarifa = 3.2
    valido = True
else:
    zona = "Clave no registrada"
    tarifa = 0.0
    valido = False

# Cálculo y salida de resultados
if valido:
    costo_total = minutos * tarifa
    print(f"Zona destino: {zona}")
    print(f"Costo total de la llamada: S/ {costo_total:.2f}")
else:
    print("Error: La clave de la zona geográfica no es válida.")