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