
# CÓDIGO ANTES

# def CalcularPromedio(Lista):
#     s=0
#     for x in Lista:
#      s=s+x
#     return s/len(Lista)
 
# l=[1,2,3,4,5]
# print(CalcularPromedio(l))



# CÓDIGO DESPUÉS

from typing import List

def calcular_promedio(numeros: List[float]) -> float:

    """
    Calcula el promedio aritmético de una lista de números.

    Args:
        numeros (List[float]): Lista de números a promediar.

    Returns:
        float: El promedio de los números.
    """
    s = 0
    for x in numeros:
     s = s + x
    return s / len(numeros)


def main() -> None:
    """Punto de entrada del script."""
    lista = [1, 2, 3, 4, 5]
    print(calcular_promedio(lista))
    

if __name__ == "__main__":
    main()