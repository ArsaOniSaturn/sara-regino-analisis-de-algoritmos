import random
from estructuras import ListaEnlazada, TablaHash


def probar_busqueda_basica():
    """Verifica búsqueda exitosa e infructuosa en ListaEnlazada y TablaHash."""
    lista = ListaEnlazada()
    tabla = TablaHash(7)

    lista.insertar(1000000001, "en bodega")
    tabla.insertar(1000000001, "en bodega")

    # Busqueda exitosa
    assert lista.buscar(1000000001) == "en bodega"
    assert tabla.buscar(1000000001) == "en bodega"

    # Busqueda infructuosa
    assert lista.buscar(9999999999) is None
    assert tabla.buscar(9999999999) is None


def probar_colision_forzada_y_factor_carga():
    """Verifica colision de guias 10, 24 y 17 en la casilla 3 de una tabla m=7."""
    tabla = TablaHash(7)
    guias_colision = (10, 24, 17)

    for g in guias_colision:
        assert tabla.hash(g) == 3
        tabla.insertar(g, "en bodega")

    # Verificar que las tres se encuentran
    for g in guias_colision:
        assert tabla.buscar(g) == "en bodega"

    # La casilla 3 debe ser una ListaEnlazada de tamano 3
    assert tabla.casillas[3].tamano == 3

    # Factor de carga = 3 / 7
    assert tabla.factor_carga() == 3 / 7


def probar_colecciones_aleatorias():
    """Verifica equivalencia de resultados en al menos 20 colecciones aleatorias."""
    estados_posibles = ["en bodega", "en reparto", "entregado", "cancelado"]

    for _ in range(25):  # 25 colecciones aleatorias
        m = random.randint(5, 50)
        n = random.randint(10, 100)

        lista = ListaEnlazada()
        tabla = TablaHash(m)

        # Generar guias unicas de 10 digitos
        guias = random.sample(range(1000000000, 2000000000), n)
        guias_dict = {}

        for g in guias:
            est = random.choice(estados_posibles)
            guias_dict[g] = est
            lista.insertar(g, est)
            tabla.insertar(g, est)

        # Pruebas con guias existentes
        for g in guias:
            res_l = lista.buscar(g)
            res_t = tabla.buscar(g)
            assert res_l == res_t == guias_dict[g]

        # Pruebas con guias inexistentes
        guias_inexistentes = random.sample(range(2000000000, 3000000000), 10)
        for g_inex in guias_inexistentes:
            assert lista.buscar(g_inex) is None
            assert tabla.buscar(g_inex) is None


if __name__ == "__main__":
    probar_busqueda_basica()
    probar_colision_forzada_y_factor_carga()
    probar_colecciones_aleatorias()
    print("Todas las pruebas pasaron")