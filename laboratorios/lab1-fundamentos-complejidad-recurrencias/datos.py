"""Generadores de lotes de registros para los escenarios de Tamiza."""
 
import random
import time
from algoritmos import insertion_sort
 
def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote de n registros en orden aleatorio (escenario A).
 
    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio, para que el
            experimento sea reproducible.
 
    Returns:
        Lista de n indices de riesgo enteros distintos, desordenada.
    """
    random.seed(semilla)

    datos = list(range(1, n + 1))
    random.shuffle(datos)
    return datos
 
 
def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote casi ordenado: 98% ordenado y 2% al final (escenario B).
 
    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio.
 
    Returns:
        Lista de n indices de riesgo enteros distintos, con el primer
        98% en el orden que el algoritmo produce y el 2% restante
        desordenado al final.
    """
    random.seed(semilla)
    
    casi_todos = int(n * 0.98)
    ordenados = list(range(1, casi_todos + 1))
    restantes = list(range(casi_todos + 1, n + 1))
    random.shuffle(restantes)
    return ordenados + restantes
 
 
def generar_inverso(n: int) -> list[int]:
    """Genera un lote en el orden exactamente contrario (escenario C).
 
    Args:
        n: cantidad de registros del lote.
 
    Returns:
        Lista de n indices de riesgo enteros distintos, en el orden
        inverso al que el algoritmo debe producir.
    """
    return list(range(n, 0, -1))



def medir_algoritmo(datos: list[int]) -> tuple[float, int]:
    """
    Cronometra un algoritmo de ordenamiento y retorna tiempo y comparaciones.

    Args:
        datos: lista de enteros desordenada.

    Returns:
        Una tupla con el tiempo observado en segundos y el número de comparaciones.
    """

    inicio = time.perf_counter()
    _, comparaciones = insertion_sort(datos)
    fin = time.perf_counter()
    tiempo_ejecucion = fin - inicio

    return tiempo_ejecucion, comparaciones
