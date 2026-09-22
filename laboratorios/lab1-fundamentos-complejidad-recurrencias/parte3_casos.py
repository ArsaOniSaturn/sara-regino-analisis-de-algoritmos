# Experimentos

from algoritmos import insertion_sort
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso, medir_algoritmo
from algoritmos import grafica_comparaciones, grafica_tiempo


def ejecutar_experimento():
    tamanios = [100, 200, 400, 800, 1600, 3200, 6400]
    escenarios = {
        "A - Aleatorio": generar_aleatorio,
        "B - Casi Ordenado": generar_casi_ordenado,
        "C - Inverso": generar_inverso,
    }

    resultados_grafica = {escenario: [] for escenario in escenarios}

    print(f"{'Escenario':<20} | {'N':<6} | {'Tiempo (s)':<12} | {'Comparaciones':<15}")
    print("-" * 60)

    for escenario, generador in escenarios.items():
        for n in tamanios:
            if escenario == "C - Inverso":
                datos = generador(n)
            else:
                datos = generador(n, semilla=42)

            tiempo_ejecucion, comparaciones = medir_algoritmo(insertion_sort, datos)

            #Gráficas
            resultados_grafica[escenario].append({
                "n": n,
                "tiempo": tiempo_ejecucion,
                "comparaciones": comparaciones
            })

            # Impresión de resultados organizados
            print(f"{escenario:<20} | {n:<6} | {tiempo_ejecucion:<12.6f} | {comparaciones:<15}")
        print("-" * 60)

    grafica_comparaciones(resultados_grafica)
    grafica_tiempo(resultados_grafica)

if __name__ == "__main__":
    ejecutar_experimento()
    