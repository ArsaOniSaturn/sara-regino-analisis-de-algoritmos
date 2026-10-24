# LABORATORIO 03 - ESTRUCTURAS DE DATOS

Nombre Estudiante: Sara Regino Ferraro

## Instrucciones para reproducir el experimento

### 1. Clonar el repositorio y acceder a la carpeta

```bash
git clone <https://github.com/ArsaOniSaturn/sara-regino-analisis-de-algoritmos.git>
cd laboratorios/lab3-estructuras-datos ##REVISAAAAARRRR
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

#### Parte 1: Ejecutar pruebas

```

```

#### Parte 2: Ejecutar mediciones y generar la gráfica

```

```

## Situación Problema a Resolver

**Rutas del Caribe — empresa de mensajería.**

Rutas del Caribe mantiene unos 400.000 envíos activos. Cada envío tiene un número de guía (un entero único de diez dígitos) y un estado (por ejemplo, "en bodega" o "en reparto"). La plataforma, escrita cuando la empresa movía unos pocos miles de envíos, guarda los envíos en una lista enlazada: cada guía nueva se agrega al inicio.

El call center atiende a los clientes que preguntan por el estado de su envío: el operador digita el número de guía y la plataforma recorre la lista hasta encontrarlo. Con el crecimiento de la empresa, en hora pico los operadores esperan varios segundos por cada consulta y los clientes cuelgan. Además, muchas consultas son por guías que no existen (números mal digitados), y esas obligan a recorrer la lista completa.

El área de operaciones tiene dos necesidades más:

Consulta puntual: el estado de una guía, el caso del call center.
Monitoreo por rango: un supervisor pide a diario "todas las guías entre el número X y el número Y", para revisar los lotes de una ruta.
La jefa de operaciones le pide un concepto técnico: ¿qué estructura debe reemplazar a la lista enlazada, y sirve para las dos necesidades? Una serie de ejemplo, con pocas guías:

```
guía:    1000000010   1000000024   1000000017   1000000005
estado:  en bodega    en reparto   en bodega    entregado
```


### PARTE 1 - Implementar y verificar las dos estructuras

Para garantizar el correcto funcionamiento de la ListaEnlazada y la TablaHash (encuentrese en: [estructuras.py](estructuras.py)), se desarrolló un conjunto de pruebas unitarias automatizadas [(pruebas.py)](pruebas.py) mediante aserciones (assert), cubriendo los siguientes escenarios:

**1. Búsqueda exitosa e infructuosa:**
- Se insertaron elementos en ambas estructuras y se verificó que la búsqueda devuelva el valor correcto cuando la guía existe.
- Se consultaron guías inexistentes para confirmar que ambas devuelven None sin generar errores.

**2. Manejo de colisiones forzadas:**
- Con un tamaño de tabla $m = 7$, se insertaron las guías 10, 24 y 17. Se verificó mediante la función hash ($k \bmod 7$) que las tres colisionan en la casilla indexada con el índice $3$.
- Se comprobó que la casilla 3 contenga una ListaEnlazada de tamaño 3 y que las tres guías se puedan recuperar individualmente sin pérdida de información.

**3. Cálculo del factor de carga:**
- Se validó que el método factor_carga() devuelva exactamente el valor teórico $\alpha = \frac{n}{m} = \frac{3}{7} \approx 0.4285$ tras las tres inserciones iniciales.

**4. Equivalencia de comportamiento en conjuntos aleatorios:**
- Se evaluaron 25 colecciones generadas aleatoriamente (con variaciones en $m$ entre 5 y 50, y $n$ entre 10 y 100).
- Para cada colección, se contrastaron búsquedas de guías existentes e inexistentes, confirmando que la ListaEnlazada y la TablaHash retornan respuestas idénticas en el 100% de los casos.


### PARTE 2 - Medir y graficar





### PARTE 3 - Análisis