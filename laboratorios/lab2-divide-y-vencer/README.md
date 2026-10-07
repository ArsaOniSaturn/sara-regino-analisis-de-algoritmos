# LABORATORIO 02 - DIVIDIR Y VENCER

Nombre Estudiante: Sara Regino Ferraro

## Instrucciones para reproducir el experimento

### 1. Clonar el repositorio y acceder a la carpeta

```bash
git clone <https://github.com/ArsaOniSaturn/sara-regino-analisis-de-algoritmos.git>
cd lab2-divide-y-vencer
``` 

### 2. Creación e instalación del entorno virtual
En Windows:

```
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
.\venv\Scripts\activate

# Instalar dependencias desde el archivo de requirements.txt
pip install -r requirements.txt
```

En Linux / macOS:

```
# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate

# Instalar dependencias desde el archivo de requirements.txt
pip install -r requirements.txt
```

### 3. Ejecución de los Experimentos
Asegúrese de tener activo el entorno virtual antes de ejecutar cualquiera de los módulos.

#### Parte 1: 


#### Parte 2: 



## Situación Problema a Resolver

**Cooperativa de tiendas de barrio.**

Una cooperativa agrupa 1.500 tiendas de barrio. Cada tienda registra, al cierre de cada día, su variación de caja: lo que ganó o perdió ese día respecto al día anterior, en miles de pesos (puede ser negativa). La gerente financiera quiere saber, para cada tienda, cuál fue su mejor racha: el tramo de días consecutivos cuya variación acumulada es la mayor de todo el historial. Esa racha le sirve para entender qué promoción o temporada le funcionó mejor a cada tienda.

Una serie de ejemplo, de ocho días:

```
día:        1    2    3    4    5    6    7    8
variación: -3   +5   -2   +8   -6   +3   +9   -4
```

La mejor racha va del día 2 al día 7 y suma +17; es más que la suma de toda la serie (+10).

El historial de una tienda tiene unos 2.000 días, pero el equipo de datos planea analizar también series de sensores con cientos de miles de registros. Por eso la gerente pide un concepto técnico: ¿qué algoritmo debe usarse para encontrar la mejor racha, y por qué?

### Análisis

#### Pregunta 1

- Recurrencia. Plantee la recurrencia de su subarreglo_maximo explicando de dónde sale cada término (cuántos subproblemas, de qué tamaño, qué cuesta el caso cruzado) y resuélvala con el método maestro, verificando la condición del caso que aplica. Explique también por qué la fuerza bruta de la Parte 1 es Θ(n²).
