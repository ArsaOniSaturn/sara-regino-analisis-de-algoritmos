"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1."""
 
import matplotlib.pyplot as plt
 
def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.
 
    No modifica la lista recibida: trabaja sobre una copia.
 
    Args:
        datos: lista de indices de riesgo a ordenar.
 
    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """

    datos_copia = datos.copy()

    comparaciones = 0
    desplazamientos = 0
    n = len(datos_copia)

    for i in range(1, n):
        clave = datos_copia[i] #Elemento que se va a insertar
        j = i - 1

        while j >= 0:
            comparaciones += 1
            if datos_copia[j] <= clave:
                break
            datos_copia [j + 1] = datos_copia[j]
            desplazamientos += 1
            j -= 1
        datos_copia[j + 1] = clave
    return datos_copia, comparaciones










def grafica_comparaciones(resultados: dict):
    """
    Genera y guarda la gráfica de Comparaciones vs Tamaño de entrada
    """

    plt.figure(figsize=(10, 5))
    for escenario, datos in resultados.items():
        tamanios = [d["n"] for d in datos]
        comparaciones = [d["comparaciones"] for d in datos]
        plt.plot(tamanios, comparaciones, marker='o', label=escenario)

    plt.title('Comparaciones vs Tamaño de Entrada (n)')
    plt.xlabel('Tamaño de Entrada (n)')
    plt.ylabel('Número de Comparaciones')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig('laboratorios\lab1-fundamentos-complejidad-recurrencias\graficas\parte3_comparaciones.png')


def grafica_tiempo(resultados: dict):
    """
        Genera y guarda la gráfica de Tiempo vs Tamaño de entrada
    """

    plt.figure(figsize=(10, 5))
    for escenario, datos in resultados.items():
        tamanios = [d["n"] for d in datos]
        tiempos = [d["tiempo"] for d in datos]
        plt.plot(tamanios, tiempos, marker='s', label=escenario)

    plt.title('Tiempo de Ejecución vs Tamaño de Entrada (n)')
    plt.xlabel('Tamaño de Entrada (n)')
    plt.ylabel('Tiempo (segundos)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig('laboratorios\lab1-fundamentos-complejidad-recurrencias\graficas\parte3_tiempo.png')
