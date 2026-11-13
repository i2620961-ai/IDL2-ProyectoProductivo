import time

def iniciar_cronometro():
    print("=== CRONÓMETRO REFERENCIAL (hh:mm:ss) ===")
    print("Presiona Ctrl + C en la terminal si deseas detenerlo.\n")

    # 1. Declaración de variables
    horas: int = 0
    minutos: int = 0
    segundos: int = 0

    try:
        # Bucle infinito para simular el avance continuo del tiempo
        while True:
            # Mostramos el formato hh:mm:ss usando f-strings con ceros a la izquierda (:02d)
            print(f"\r{horas:02d}:{minutos:02d}:{segundos:02d}", end="", flush=True)

            # Pausamos la ejecución del programa durante 1 segundo referencial
            time.sleep(1)

            # Incrementamos los segundos
            segundos += 1

            # Lógica para cambiar de minuto
            if segundos == 60:
                segundos = 0
                minutos += 1

            # Lógica para cambiar de hora
            if minutos == 60:
                minutos = 0
                horas += 1

    except KeyboardInterrupt:
        # Esto permite que el usuario detenga el cronómetro limpiamente con el teclado
        print(f"\n\nCronómetro detenido. Tiempo final registrado: {horas:02d}:{minutos:02d}:{segundos:02d}")

if __name__ == "__main__":
    iniciar_cronometro()