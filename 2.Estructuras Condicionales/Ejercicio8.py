# Declaración de variables
n1: int = 0
n2: int = 0
n3: int = 0
orden: str = ""
mayor: int = 0
medio: int = 0
menor: int = 0

# Entrada de datos
n1 = int(input("Ingrese primer número entero: "))
n2 = int(input("Ingrese segundo número entero: "))
n3 = int(input("Ingrese tercer número entero: "))
orden = input("¿Cómo desea ordenarlos? (ascendente/descendente): ").strip().lower()

# Validación y proceso
if n1 == n2 or n2 == n3 or n1 == n3:
    print("Error: Todos los números ingresados deben ser diferentes.")

else:
    # Identificar el número mayor, medio y menor
    if n1 > n2 and n1 > n3:
        mayor = n1

        if n2 > n3:
            medio, menor = n2, n3
        else:
            medio, menor = n3, n2

    elif n2 > n1 and n2 > n3:
        mayor = n2

        if n1 > n3:
            medio, menor = n1, n3
        else:
            medio, menor = n3, n1

    else:
        mayor = n3

        if n1 > n2:
            medio, menor = n1, n2
        else:
            medio, menor = n2, n1

    # Mostrar resultados según el orden elegido
    if orden == "ascendente":
        print(f"Resultado: {menor}, {medio}, {mayor}")
    else:
        print(f"Resultado: {mayor}, {medio}, {menor}")