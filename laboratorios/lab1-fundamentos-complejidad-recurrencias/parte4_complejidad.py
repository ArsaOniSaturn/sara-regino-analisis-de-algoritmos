# Experimentos

from datos import medir_algoritmo, generar_aleatorio
from algoritmos import insertion_sort, merge_sort, graficar_comparacion_tiempos


def ejecutar_experimento_parte4():
    tamanios = [100, 200, 400, 800, 1600, 3200, 6400]
    tiempos_insertion = []
    tiempos_merge = []

    print(f"{'N':<8} | {'Tiempo Insertion (s)':<22} | {'Tiempo Merge (s)':<20}")
    print("-" * 56)

    for n in tamanios:
        datos = generar_aleatorio(n, semilla=42)

        t_insertion, _ = medir_algoritmo(insertion_sort, datos)
        t_merge, _ = medir_algoritmo(merge_sort, datos)

        tiempos_insertion.append(t_insertion)
        tiempos_merge.append(t_merge)

        print(f"{n:<8} | {t_insertion:<22.6f} | {t_merge:<20.6f}")

    graficar_comparacion_tiempos(tamanios, tiempos_insertion, tiempos_merge)


if __name__ == "__main__":
    ejecutar_experimento_parte4()