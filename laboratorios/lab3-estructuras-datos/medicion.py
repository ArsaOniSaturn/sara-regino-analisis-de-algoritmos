import os
import random
import time
import matplotlib.pyplot as plt
from estructuras import ListaEnlazada, TablaHash


# Obtiene la carpeta donde está este archivo
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CARPETA_GRAFICAS = os.path.join(BASE_DIR, "graficas")

# Crea la carpeta 'graficas' junto a este archivo si no existe
os.makedirs(CARPETA_GRAFICAS, exist_ok=True)


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: guias almacenadas en las estructuras.
        cantidad: cuantas guias inexistentes generar.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Una lista con `cantidad` guias que no pertenecen a `existentes`.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes


def generar_datos_prueba(
    n: int, semilla: int = 42
) -> tuple[list[tuple[int, str]], set[int]]:
    """Genera n guias unicas de diez digitos, cada una con un estado al azar.

    Args:
        n: cantidad de guias a generar.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Una tupla con la lista de pares (guia, estado) y el conjunto de
        las guias generadas.
    """
    azar = random.Random(semilla)
    estados = ["en bodega", "en reparto", "entregado", "cancelado"]

    # Generar guias unicas de 10 digitos
    guias_set = set()
    while len(guias_set) < n:
        guias_set.add(azar.randint(10**9, 10**10 - 1))

    guias_lista = list(guias_set)
    datos = [(g, azar.choice(estados)) for g in guias_lista]
    return datos, guias_set


def experimento_a() -> None:
    """Experimento A — Comparación de Lista vs Tabla Hash según n."""
    print("Ejecutando Experimento A: Lista vs Tabla Hash...")

    # Valores de n requeridos (dos menores a 1000 y uno de 20.000 o mas)
    valores_n = [100, 500, 1000, 5000, 20000, 40000]
    # Primos cercanos a n / 2 para garantizar alpha ≈ 2
    m_primos = [53, 251, 509, 2503, 10007, 20011]

    tiempos_lista_ms = []
    tiempos_tabla_ms = []

    for n, m in zip(valores_n, m_primos):
        datos, guias_set = generar_datos_prueba(n, semilla=42)
        inexistentes = generar_guias_inexistentes(
            guias_set, cantidad=200, semilla=7
        )

        # Poblar estructuras
        lista = ListaEnlazada()
        tabla = TablaHash(m)
        for guia, estado in datos:
            lista.insertar(guia, estado)
            tabla.insertar(guia, estado)

        # Verificación interna: ambas devuelven lo mismo para guias existentes
        muestra = datos[:10]
        for g, est in muestra:
            assert lista.buscar(g) == tabla.buscar(g) == est

        # Cronometraje ListaEnlazada (solo las búsquedas)
        t_inicio = time.perf_counter()
        for guia_inex in inexistentes:
            lista.buscar(guia_inex)
        t_fin = time.perf_counter()
        # Convertir tiempo total a tiempo medio por búsqueda en milisegundos (ms)
        tiempo_medio_lista = ((t_fin - t_inicio) / 200) * 1000
        tiempos_lista_ms.append(tiempo_medio_lista)

        # Cronometraje TablaHash (solo las búsquedas)
        t_inicio = time.perf_counter()
        for guia_inex in inexistentes:
            tabla.buscar(guia_inex)
        t_fin = time.perf_counter()
        tiempo_medio_tabla = ((t_fin - t_inicio) / 200) * 1000
        tiempos_tabla_ms.append(tiempo_medio_tabla)

        print(
            f"  n={n:5d} | Lista: {tiempo_medio_lista:.5f} ms | "
            f"Tabla (m={m}): {tiempo_medio_tabla:.5f} ms"
        )

    # Generar Gráfica Experimento A
    plt.figure(figsize=(9, 5))
    plt.plot(
        valores_n, tiempos_lista_ms, "o-r", linewidth=2, label="Lista Enlazada"
    )
    plt.plot(
        valores_n,
        tiempos_tabla_ms,
        "s-b",
        linewidth=2,
        label="Tabla Hash (α ≈ 2)",
    )
    plt.title("Tiempo Medio de Búsqueda de Guías Inexistentes vs. Número de Guías (n)")
    plt.xlabel("Número de guías activas (n) [unidades]")
    plt.ylabel("Tiempo medio por búsqueda [milisegundos]")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.tight_layout()
    ruta_grafica = os.path.join(CARPETA_GRAFICAS, "lista_vs_tabla.png")
    plt.savefig(ruta_grafica, dpi=300)
    plt.close()
    print("Gráfica 'lista_vs_tabla.png' guardada con éxito.\n")


def experimento_b() -> None:
    """Experimento B — Efecto del factor de carga (alpha) en la Tabla Hash."""
    print("Ejecutando Experimento B: Tiempo vs. Factor de Carga (alpha)...")

    n_fijo = 20000
    datos, guias_set = generar_datos_prueba(n_fijo, semilla=42)
    inexistentes = generar_guias_inexistentes(guias_set, cantidad=200, semilla=7)

    # Valores deseados de alpha entre 0.5 y 10 (con n = 20000)
    # m = n / alpha -> m primos aproximados: alpha = 0.5, 1, 4 y 10
    configuraciones_m = [40009, 20011, 5003, 2003]

    alphas_reales = []
    tiempos_tabla_ms = []

    for m in configuraciones_m:
        tabla = TablaHash(m)
        for guia, estado in datos:
            tabla.insertar(guia, estado)

        alpha_real = tabla.factor_carga()
        alphas_reales.append(alpha_real)

        # Cronometraje de búsquedas inexistentes
        t_inicio = time.perf_counter()
        for guia_inex in inexistentes:
            tabla.buscar(guia_inex)
        t_fin = time.perf_counter()

        tiempo_medio = ((t_fin - t_inicio) / 200) * 1000
        tiempos_tabla_ms.append(tiempo_medio)

        print(
            f"  m={m:5d} | alpha={alpha_real:.2f} | "
            f"Tiempo Hash: {tiempo_medio:.5f} ms"
        )

    # Generar Gráfica Experimento B
    plt.figure(figsize=(9, 5))
    plt.plot(
        alphas_reales,
        tiempos_tabla_ms,
        "d-g",
        linewidth=2,
        label="Tabla Hash (n = 20.000)",
    )
    plt.title("Tiempo Medio de Búsqueda de Guías Inexistentes vs. Factor de Carga (α)")
    plt.xlabel("Factor de carga (α = n / m)")
    plt.ylabel("Tiempo medio por búsqueda [milisegundos]")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.tight_layout()
    ruta_grafica = os.path.join(CARPETA_GRAFICAS, "tiempo_vs_alfa.png")
    plt.savefig(ruta_grafica, dpi=300)
    plt.close()
    print("Gráfica 'tiempo_vs_alfa.png' guardada con éxito.\n")


if __name__ == "__main__":
    experimento_a()
    experimento_b()
    print("Mediciones completadas y gráficas generadas satisfactoriamente.")
    