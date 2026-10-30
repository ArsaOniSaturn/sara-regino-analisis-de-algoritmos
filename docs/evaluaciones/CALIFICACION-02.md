# Retroalimentación — Laboratorio 02: Dividir y vencer

**Estudiante:** Sara Regino Ferraro · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `edf27e8`

Muy buen trabajo: el código es correcto y el informe responde todas las preguntas.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 18 / 20 |
| Calidad de la explicación teórica | 19 / 20 |
| Corrección de la implementación | 23 / 25 |
| Calidad del análisis de las gráficas | 20 / 25 |
| Documentación y organización del informe | 8 / 10 |
| **Total** | **88 / 100** |
| **Nota (0–5)** | **4.40** |

## 1. Corrección conceptual (18 / 20)
**Lo que hizo bien:**
- Identifica que desde n = 50 divide y vencerás empieza a ganar, con sus propios datos, y explica que en tamaños muy pequeños pesa el costo de las llamadas recursivas.
- En la comparación con hallar el máximo de un arreglo, plantea `T(n) = 2T(n/2) + Θ(1)` y concluye que dividir no mejora nada.
- Recomienda divide y vencerás y declara que las cifras a 1.000.000 de registros son estimaciones, sin usar regla de tres lineal.

**Lo que puede mejorar:**
- En la estimación, la cifra de 8000 registros sale de una captura de pantalla; conviene apoyarse también en una tabla dentro del informe y advertir que los tiempos reales pueden variar.

## 2. Calidad de la explicación teórica (19 / 20)
**Lo que hizo bien:**
- Explica de dónde sale cada término de `T(n) = 2T(n/2) + Θ(n)` y verifica el caso 2 del método maestro.
- Justifica el `Θ(n²)` de la fuerza bruta con la suma de iteraciones.

**Lo que puede mejorar:**
- Al resolver con el método maestro, diga explícitamente que se compara `f(n)` con `n^(log_b a)` y por qué eso corresponde al caso 2 (ya lo hace, pero de forma muy breve).

## 3. Corrección de la implementación (23 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en todos los casos pedidos y coinciden en miles de listas aleatorias.
- `subarreglo_maximo` resuelve los tres casos sin llamar a la fuerza bruta y ninguna función modifica la lista recibida.
- Las pruebas cubren todos los casos pedidos y 25 listas aleatorias.

**Lo que puede mejorar:**
- En `pruebas.py` falta una línea en blanco antes del bloque final (PEP 8 pide dos).
- El comentario del caso cruzado en `pruebas.py` no coincide con la serie usada (el mejor tramo suma 10, no 7).

## 4. Calidad del análisis de las gráficas (20 / 25)
**Lo que hizo bien:**
- La gráfica tiene título, ejes rotulados, leyenda y ambas curvas en los mismos ejes, con siete tamaños.
- Los valores que cita (8.13 s y 0.0355 s en n = 8000) coinciden con lo publicado, y calcula el factor al duplicar n para ambos algoritmos.

**Lo que puede mejorar:**
- Para la fuerza bruta obtuvo un factor de 2.97 y la teoría predice 4. Atribuirlo a "optimizaciones del entorno" no está respaldado; lo honesto es decir que no coincide del todo y proponer causas medibles (ruido de la máquina, falta de repeticiones).
- Para divide y vencerás obtuvo 1.61 contra 2.16 esperado, y dice que se ajusta "de forma muy precisa". Esa diferencia es grande y debía señalarse.
- No indica si repitió las mediciones; promediar varias corridas reduce estas diferencias.

## 5. Documentación y organización del informe (8 / 10)
**Lo que hizo bien:**
- La carpeta `laboratorios/lab2-divide-y-vencer/` está en una ubicación válida, con todos los archivos del entregable.
- El informe sigue el orden pedido, enlaza `subarreglo.py`, `pruebas.py` y `medicion.py`, y la gráfica se ve en el README.
- Hay varios commits con mensajes descriptivos.

**Lo que puede mejorar:**
- Las instrucciones de reproducción tienen fallos: el enlace del `git clone` va entre `<>`, y `pip install -r requirements.txt` se indica desde la carpeta del laboratorio, pero ese archivo está en la raíz del repositorio.
- Se publicó una captura extra (`resultados.png`) que no hacía parte del entregable; una tabla en el README sería más clara.

## ¿El código funciona?
Sí. Las pruebas pasan, ambos algoritmos coinciden con un resultado de referencia y el experimento corre completo y genera la gráfica.

## Para el próximo laboratorio
- Deje dos líneas en blanco entre funciones y antes del bloque final, y corrija los comentarios que no coincidan con el código.
- Cuando la medición no coincida con la teoría, dígalo con claridad y explique la causa probable, sin afirmar un ajuste que no existe.
- Repita cada medición varias veces y diga en el informe cuántas veces lo hizo.
- Revise las instrucciones de reproducción siguiéndolas desde cero en una carpeta limpia.
- Incluya una tabla con los tiempos medidos dentro del README.
