# Retroalimentación — Laboratorio 01: Fundamentos, complejidad y recurrencias

**Estudiante:** Sara Regino Ferraro · **Laboratorio:** Fundamentos, complejidad y recurrencias (Plataforma Tamiza)

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 11 / 25 |
| Calidad de la explicación teórica | 17 / 25 |
| Corrección de la implementación | 14 / 20 |
| Calidad del análisis de las gráficas | 12 / 20 |
| Documentación y organización del informe | 6 / 10 |
| **Total** | **60 / 100** |
| **Nota (0–5)** | **3.00** |

## 1. Corrección conceptual (11 / 25)
**Lo que hizo bien:**
- Explica que el algoritmo servía para 20.000 registros y que el crecimiento del programa lo dejó corto.
- Relaciona la ejecución diaria durante años con consumo de energía y costos.
- Señala que una lista incompleta puede hacer que se llame primero a alguien de menor riesgo y se deje de lado a un paciente urgente.

**Lo que puede mejorar:**
- No distingue con claridad entre "da el resultado correcto" y "lo da dentro de la ventana de cuatro horas", ni nombra esa ventana como la restricción que se incumple.
- No explica por qué un servidor del doble de velocidad no arregla el problema de fondo (solo reduce el tiempo a la mitad, mientras el trabajo crece mucho más rápido).
- Falta el segundo ejemplo propio, distinto de Tamiza, con datos aproximados y la restricción incumplida.
- En la parte ética faltó decir explícitamente quién asume el costo de cada error (paciente, operador, Secretaría o equipo de desarrollo) y discutir la obligación adicional de que el orden decide a quién se llama primero.

## 2. Calidad de la explicación teórica (17 / 25)
**Lo que hizo bien:**
- Plantea bien la recurrencia de merge sort, explica cada término y la resuelve con el método maestro, verificando la condición del caso 2 hasta llegar a `Θ(n log n)`.
- El cálculo línea a línea de insertion sort está completo y llega a `Θ(n²)`.
- Incluye la tabla de complejidades y deja escrita la predicción antes del experimento.

**Lo que puede mejorar:**
- Las definiciones de mejor, peor y promedio no dicen sobre qué conjunto de entradas se toma el mínimo, el máximo o el promedio, y el mejor caso no es "una sola comparación".
- Para decidir si el algoritmo entra en producción, con una ventana estricta, lo correcto es el peor caso; usted eligió el caso promedio.

## 3. Corrección de la implementación (14 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien, no cambian la lista original, cuentan comparaciones entre elementos y no usan `sorted()` ni `sort()`. La mezcla de merge sort es propia y recursiva.
- Los generadores producen lotes del tamaño pedido, sin repetidos y con semilla.

**Lo que puede mejorar:**
- Hay varios incumplimientos de PEP 8: líneas demasiado largas, falta de líneas en blanco entre funciones y comentarios mal formados.
- La función interna `merge_recursivo` y `medir_algoritmo` no tienen docstring completo ni *type hints* en todos los parámetros.
- Las rutas para guardar las gráficas usan barras invertidas y la carpeta desde la raíz, por lo que fuera de Windows no se guardan en `graficas/`.
- Hay importaciones y una variable (`desplazamientos`) que no se usan.

## 4. Calidad del análisis de las gráficas (12 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, tienen título, ejes rotulados y leyenda, y se ven en el informe.
- Identifica correctamente A como promedio, B como mejor caso y C como peor caso, y concluye que merge sort conviene.
- Usa datos medidos (comparaciones en n = 3.200 y n = 6.400 del escenario C) para mostrar que el trabajo se cuadruplica.

**Lo que puede mejorar:**
- En la Parte 4.2 no contrasta la conclusión con las complejidades de 4.1 ni explica qué pasa con tamaños pequeños.
- La estimación para 1.200.000 registros no explica el razonamiento ni sus supuestos, y las cifras (360.000 s y 1,61 s) no se ven coherentes con lo que muestra la gráfica parte4_tiempo.png (insertion cerca de 4,5 s y merge cerca de 0,04 s en n = 6400).
- La respuesta al servidor del doble de velocidad no cita un dato de tiempo de la gráfica, y no discute memoria, estabilidad u otra consideración distinta del tiempo.

## 5. Documentación y organización del informe (6 / 10)
**Lo que hizo bien:**
- El laboratorio está en la ubicación acordada y tiene los archivos pedidos.
- El informe sigue el orden de las partes, enlaza el código de cada parte y las gráficas se ven.

**Lo que puede mejorar:**
- Las instrucciones de reproducción piden entrar a una carpeta del laboratorio justo después de clonar, que no existe con ese nombre en la raíz.
- Solo hay 3 commits del laboratorio; se pedían al menos cinco que mostraran el avance.

## ¿El código funciona?
Sí. Ambos scripts corren y generan las tablas de resultados; los dos algoritmos ordenan bien. Las gráficas no se guardarían en la carpeta correcta fuera de Windows.

## Para el próximo laboratorio
- Responda cada pregunta cubriendo todos los puntos pedidos (segundo ejemplo, quién asume el costo, obligación del orden).
- Defina los casos indicando sobre qué entradas se toma el máximo, mínimo o promedio.
- Explique su extrapolación paso a paso y declare que es una estimación.
- Revise PEP 8, docstrings y *type hints* en todas las funciones, y use rutas relativas con `os.path` o `pathlib`.
- Haga commits frecuentes (al menos cinco) durante el desarrollo.
