# Declaración de variables
v0: float = 0.0
aceleracion: float = 0.0
tiempo: float = 0.0
vf_m_s: float = 0.0
vf_km_h: float = 0.0

# Asignación de datos
v0 = 0.0
aceleracion = 0.8
tiempo = 30.0

# Proceso
vf_m_s = v0 + (aceleracion * tiempo)
vf_km_h = vf_m_s * 3.6

# Salida de resultados
print(f"La velocidad final es: {vf_m_s:.2f} m/s")
print(f"Equivalente a: {vf_km_h:.2f} km/h")