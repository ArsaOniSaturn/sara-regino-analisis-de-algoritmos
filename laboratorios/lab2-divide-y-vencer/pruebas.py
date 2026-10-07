import random
from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def ejecutar_pruebas():
    # 1. Serie de ocho días de la situación problema (Suma esperada: 17)
    serie_problema = [-3, 5, -2, 8, -6, 3, 9, -4]
    fuerza_bruta_prueba = subarreglo_fuerza_bruta(serie_problema)
    div_vencer_prueba = subarreglo_maximo(serie_problema, 0, len(serie_problema) - 1)
    assert fuerza_bruta_prueba[2] == 17, f"Fuerza bruta falló en serie problema: {fuerza_bruta_prueba[2]}"
    assert div_vencer_prueba[2] == 17, f"Divide y vencerás falló en serie problema: {div_vencer_prueba[2]}"

    # 2. Serie de un solo elemento
    serie_un_elemento = [42.0]
    fuerza_bruta_prueba = subarreglo_fuerza_bruta(serie_un_elemento)
    div_vencer_prueba = subarreglo_maximo(serie_un_elemento, 0, len(serie_un_elemento) - 1)
    assert fuerza_bruta_prueba[2] == 42.0
    assert div_vencer_prueba[2] == 42.0

    # 3. Serie con todos los valores negativos
    serie_negativos = [-8.5, -3.0, -12.1, -1.5, -5.0]
    fuerza_bruta_prueba = subarreglo_fuerza_bruta(serie_negativos)
    div_vencer_prueba = subarreglo_maximo(serie_negativos, 0, len(serie_negativos) - 1)
    assert fuerza_bruta_prueba[2] == -1.5
    assert div_vencer_prueba[2] == -1.5

    # 4. Serie con todos los valores positivos
    serie_positivos = [10.0, 5.5, 3.2, 8.0]
    fuerza_bruta_prueba = subarreglo_fuerza_bruta(serie_positivos)
    div_vencer_prueba = subarreglo_maximo(serie_positivos, 0, len(serie_positivos) - 1)
    assert fuerza_bruta_prueba[2] == 26.7
    assert div_vencer_prueba[2] == 26.7

    # 5. Caso donde el mejor tramo cruza el punto medio explícitamente
    # Mitad izq: [2, 3], Mitad der: [4, 1], Tramo cruzado óptimo: [3, 4] suma 7
    serie_cruzada = [-5, 2, 3, 4, 1, -6]
    fuerza_bruta_prueba = subarreglo_fuerza_bruta(serie_cruzada)
    div_vencer_prueba = subarreglo_maximo(serie_cruzada, 0, len(serie_cruzada) - 1)
    assert fuerza_bruta_prueba[2] == 10.0
    assert div_vencer_prueba[2] == 10.0

    # 6. Al menos veinte listas aleatorias en las que ambas funciones deben dar la misma suma.
    random.seed(42)
    for i in range(25):
        tamanio = random.randint(5, 50)
        lista_aleatoria = [round(random.uniform(-50.0, 50.0), 2) for _ in range(tamanio)]

        suma_fuerza_bruta = subarreglo_fuerza_bruta(lista_aleatoria)[2]
        suma_div_vencer = subarreglo_maximo(lista_aleatoria, 0, len(lista_aleatoria) - 1)[2]

        assert abs(suma_fuerza_bruta - suma_div_vencer) < 1e-9, (
            f"Diferencia en iteración {i + 1}:\n"
            f"Fuerza Bruta: {suma_fuerza_bruta}, Divide y Vencerás: {suma_div_vencer}\n"
            f"Lista: {lista_aleatoria}"
        )

    print("¡TODAS LAS PRUEBAS PASARON!.")

if __name__ == "__main__":
    ejecutar_pruebas()