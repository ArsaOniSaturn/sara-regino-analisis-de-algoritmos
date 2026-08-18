
"""
Clasificador de años bisiestos.

"""


def es_bisiesto(anio: int) -> bool:
    """Determina si un año es bisiesto.

    Un año es bisiesto si es divisible por 4, excepto los años
    divisibles por 100 que no lo sean también por 400.

    Args:
        anio: año a evaluar (número entero).

    Returns:
        True si el año es bisiesto, False en caso contrario.
    """
    if anio % 400 == 0:
        return True
    elif anio % 100 == 0:
        return False
    elif anio % 4 == 0:
        return True
    else:
        return False


def leer_anios() -> list[int]:
    """Solicita al usuario una lista de años separados por comas.

    Debe reintentar mientras la entrada no se pueda convertir a enteros
    (se usó try / except para capturar entradas inválidas).

    Returns:
        Lista de años como enteros.
    """
    while True:
        entrada = input("Ingrese años separados por comas (ej. 1900, 2000, 2024): ")
        partes = entrada.split(",")
        try:
            anios = [int(p.strip()) for p in partes if p.strip() != ""]
            if not anios:
                print("Error: Debe ingresar al menos un número. Intente nuevamente.\n")
                continue

            if any(a < 0 for a in anios):
                raise ValueError("No se permiten años negativos.")
            return anios
        
        except ValueError as e:
            if "negativos" in str(e):
                print("Error: Los años deben ser números positivos. Intente nuevamente.\n")
            else:
                print("Error: Ingrese únicamente números enteros válidos separados por comas.\n")


def main() -> None:
    """Punto de entrada del script."""
    anios = leer_anios()
    bisiestos = [a for a in anios if es_bisiesto(a)]
    
    decadas_unicas = sorted(set((a // 10) * 10 for a in anios))
    anios_por_decada = {
        decada: [a for a in anios if (a // 10) * 10 == decada]
        for decada in decadas_unicas
    }

    print("\n--- Resumen de Años Bisiestos ---")
    print(f"Años ingresados: {anios}")
    print(f"Años bisiestos encontrados: {bisiestos}")
    print(f"Total de años bisiestos: {len(bisiestos)}")
    print(f"Años agrupados por década: {anios_por_decada}")


if __name__ == "__main__":
    main()