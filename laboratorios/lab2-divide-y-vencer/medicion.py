"""Experimento de tiempos: fuerza bruta vs. divide y vencerás.

Mide el tiempo de 'subarreglo_fuerza_bruta' y 'subarreglo_maximo' para
distintos tamaños de entrada y guarda la gráfica en 'graficas/'.
"""

import os
import random
import time
import matplotlib.pyplot as plt
from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def ejecutar_experimento() -> None:

    """Mide los tiempos de ambos algoritmos y genera la gráfica.

    Para cada tamaño de entrada genera datos aleatorios, mide el tiempo
    de 'subarreglo_fuerza_bruta' y de 'subarreglo_maximo', verifica
    que ambos devuelvan la misma suma y guarda la gráfica
    'tiempo vs. tamaño de entrada' en 'graficas/tiempo_vs_n.png'.
    """

    random.seed(42)

    # Tamaños de entrada
    tamanios = [10, 50, 100, 500, 1000, 4000, 8000]

    tiempo_fuerza_bruta = []
    tiempo_div_vencer = []

    encabezado = (
        f"{'n':<8}{'Fuerza Bruta (s)':<20}"
        f"{'Divide y Vencerás (s)':<22}{'FB = DV?'}"
    )
    print(encabezado)
    print("-" * len(encabezado))

    for n in tamanios:

        # Generar datos con enteros entre -100 y 100
        valores = [random.randint(-100, 100) for _ in range(n)]

        # 1. Medición Fuerza Bruta
        t_inicio = time.perf_counter()
        fuerza_bruta = subarreglo_fuerza_bruta(valores)
        t_fin = time.perf_counter()
        tiempo_fb = t_fin - t_inicio
        tiempo_fuerza_bruta.append(tiempo_fb)

        # 2. Medición Divide y Vencerás
        t_inicio = time.perf_counter()
        div_vencer = subarreglo_maximo(valores, 0, n - 1)
        t_fin = time.perf_counter()
        tiempo_dv = t_fin - t_inicio
        tiempo_div_vencer.append(tiempo_dv)

        # 3. Verificación de que ambos devuelven la misma suma
        suma_fb = fuerza_bruta[2]
        suma_dv = div_vencer[2]
        assert (
            abs(suma_fb - suma_dv) < 1e-9
        ), f"Error de coincidencia en N={n}: FB={suma_fb}, DV={suma_dv}"

        print(
            f"{n:<8}{tiempo_fb:<20.6f}{tiempo_dv:<22.6f}"
            f"Sí -> {suma_fb} = {suma_dv}"
        )

    # Asegurar que el directorio de destino exista
    os.makedirs("graficas", exist_ok=True)

    # Configuración de la gráfica
    plt.figure(figsize=(9, 6))
    plt.plot(
        tamanios,
        tiempo_fuerza_bruta,
        marker="o",
        linewidth=2,
        color="#D32F2F",
        label="Fuerza Bruta $\Theta(n^2)$",
    )
    plt.plot(
        tamanios,
        tiempo_div_vencer,
        marker="s",
        linewidth=2,
        color="#1976D2",
        label="Divide y Vencerás $O(n \log n)$",
    )

    # Etiquetas
    plt.title(
        "Tiempo de Ejecución vs. Tamaño de Entrada (n)", fontsize=14, pad=12
    )
    plt.xlabel("Tamaño de la entrada n (número de días)", fontsize=12)
    plt.ylabel("Tiempo de ejecución (segundos)", fontsize=12)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend(fontsize=11)
    plt.tight_layout()

    # Guardar gráfica
    ruta_grafica = os.path.join("graficas", "tiempo_vs_n.png")
    plt.savefig(ruta_grafica, dpi=300)
    plt.close()

    print("\nEl experimento se realizó con éxito.")


if __name__ == "__main__":
    ejecutar_experimento()