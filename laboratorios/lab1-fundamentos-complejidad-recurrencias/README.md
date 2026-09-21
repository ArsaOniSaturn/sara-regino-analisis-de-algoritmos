# LABORATORIO 01 - FUNDAMENTOS, COMPLEJIDAD Y RECURRENCIAS

Nombre Estudiante: Sara Regino Ferraro

## Instrucciones para reproducir el experimento

INSTRUCCIONES*


## Situación Problema a Resolver

**Plataforma Tamiza — Secretaría de Salud departamental.**

La Secretaría de Salud opera un programa de tamizaje cardiovascular en 340 laboratorios e IPS del departamento. Cada laboratorio envía durante el día los resultados de las pruebas que procesó. Al cierre de la jornada, la plataforma Tamiza tiene acumulados 1.200.000 registros pendientes de gestión: los resultados de los últimos treinta días que todavía no han sido contactados.

Cada registro trae un índice de riesgo entre 0 y 1000, calculado por la plataforma a partir de los valores de laboratorio y de la historia clínica del paciente. Entre las 2:00 a. m. y las 6:00 a. m. corre un proceso automático que debe ordenar los 1.200.000 registros por índice de riesgo, de mayor a menor, y generar la lista de llamadas del día. A las 6:00 a. m. el centro de contacto abre y empieza a llamar por esa lista, de arriba hacia abajo: los pacientes con mayor riesgo son contactados primero para citarlos a valoración médica. La ventana del proceso es, por lo tanto, de cuatro horas y no es negociable.

**El problema.** La plataforma fue escrita hace ocho años, cuando el programa cubría 4 municipios y unos 20.000 registros. El ordenamiento se implementó entonces con insertion sort y nunca se volvió a tocar: siempre funcionó. Con la ampliación del programa a todo el departamento, el proceso empezó a desbordar la ventana. En las últimas semanas, la lista de llamadas ha quedado incompleta tres veces: el proceso no alcanzó a terminar antes de las 6:00 a. m. y el centro de contacto trabajó con una lista parcial, no ordenada por riesgo.

**La decisión sobre la mesa.** El área de infraestructura propone duplicar la capacidad del servidor —contratar una máquina del doble de velocidad de reloj— y dejar el software como está. El argumento es que el algoritmo "ya está probado, lleva ocho años funcionando y entrega el resultado correcto". La Secretaría le pide a usted un concepto técnico antes de firmar el contrato.

**Cómo llega el lote de registros.** El equipo de la plataforma le informa que la forma en que llegan los datos depende del canal de origen, y que hay tres escenarios posibles:

| Escenario | Canal de Origen | Cómo llega el lote de registros
| :--- | :--- | :---
| A - Aleatorio | Cargue directo desde el portal web de los laboratorios | Los registros quedan en el  orden en que cada laboratorio los subió: sin ninguna relación con el índice de riesgo.
| B - Casi Ordenado | Reproceso sobre la lista del día anterior | El 98 % del lote es la lista de ayer, que ya quedó ordenada por riesgo; el 2 % restante son los resultados nuevos del día, que se anexan al final sin ordenar.
| C - Orden inverso | Migración desde el sistema legado de historia clínica | El sistema anterior exporta los registros del índice de riesgo menor al mayor, es decir, exactamente al revés de lo que Tamiza necesita.


### PARTE 1 - Analizar el algoritmo antes de comprar hardware:

**Pregunta:**

"La Secretaría está por firmar la compra de un servidor del doble de velocidad para que el proceso de Tamiza quepa en la ventana de cuatro horas. ¿Por qué debe analizarse primero el algoritmo, si el que está en producción lleva ocho años entregando el resultado correcto?"

**Respuesta:** 

Aunque es verdad que el algorítmo anterior funcionaba, éste estaba diseñado para procesar una cierta cantidad de datos que, en ese entonces, era bastante menor. Se hablaba de 20.000 registros en una zona relativamente más pequeña. Sin embargo, a medida que la Secretaría de Salud fue expandiendo su campo de aplicación con su programa Tamiza, éste a su vez requería una mejora que estuviese a la altura de la información que recibía. O sea, la capacidad de ordenar los datos que llegan en el tiempo que se requiere. 

El orden en el que el sistema recibe la información y cómo está diseñado el algoritmo para afrontar esa carga, influyen de manera significativa en el resultado que se espera en el tiempo estipulado. Entonces, a pesar de que la solución que parece más obvia sea la de invertir en un servidor más rápido, no sería una decisión sabia si, al analizar el cómo funciona el flujo del algoritmo, se ve que este puede ser mejorado a las necesidades que se tienen en la actualidad con los mismos recursos.



### PARTE 2 — Responsabilidad ambiental y ética de la implementación

**Pregunta:**

"Como responsable técnico de Tamiza, ¿qué responsabilidad ambiental y ética asume al decidir qué algoritmo de ordenamiento se ejecuta cada madrugada sobre los datos de 1.200.000 pacientes?"

**Respuesta:** 

El simple hecho de que un programa se ejecute, independientemente del tiempo en que se demoró en terminar, se traduce en consumo energético. Y si a eso le sumamos que éste corre durante 4 horas seguidas durante años, a largo plazo se convierte en factores críticos de costos (para la empresa) y un incumplimiento a la sostenibilidad para con el medio ambiente.

Además, es de suma importancia que un algoritmo funcione rápida y correctamente. En especial uno que se dedica a ordenar las listas de llamadas a pacientes con resultados graves que necesitan que el proceso avance. Y si este falla, podría decirse que activaría un efecto dominó: el operador de llamadas, con la lista incompleta, llamaría a la persona con menos riesgo y se saltaría al más urgente; esto resultaría en que el paciente que sí necesitaba con urgencia los resultados, lo dejen de lado y afecte a su salud de manera irreversible o crítica. A su vez, también perjudicaría la reputación de la Secretaría de Salud y su confiabilidad en entregar un servicio óptimo a la gente. Es una situación en donde todo el mundo queda manchado por la falta de revisión y mantenimiento del algoritmo que el equipo de desarrollo debió haber previsto/solucionado de manera inmediata antes de siquiera haber alcanzado al cliente.



### PARTE 3 — Peor caso, mejor caso y caso promedio, demostrados en Python

#### 3.1 — Explicación

El mejor de los casos es aquel donde solo se necesita de una comparación para ordenar los datos. O sea, el algoritmo toma la menor cantidad de tiempo o recursos, aquí la información ya entra ordenada. El peor de los casos es cuando el algoritmo debe revisar todos los elementos, toma mayor cantidad de recursos y más tiempo. En cuanto al caso promedio, se podría decir que es el más común, el comportamiento habitual que se espera de un algoritmo al recibir entradas aleatorias. 

Para decidir si el algoritmo de Tamiza entra en producción, lo ideal sería usar el mejor de los casos. Como se había mencionado antes, en el mejor de los casos su entrada ya estaría ordenada por lo que no se necesitaría de mucho tiempo para tener las listas de llamadas completada. Sin embargo, en el mundo real no todo es perfecto. Así que, realistamente, el caso más adecuado sería el caso promedio. En donde se tendría la mitad de comparaciones y desplazamientos para ordenar el arreglo, en especial con una ventana tan estricta de 4 horas. 

Predicción de Tamiza para Insertion Sort:
- El escenario A es el caso promedio.
- El escenario B es el mejor caso.
- El escenario C es el peor caso.

#### 3.2 — Demostración experimental

![Texto alternativo de la imagen]()

Después de haber hecho experimentos con datos generados aleatoriamente, casi ordenados e inversos con insertion sort y, como se había predicho y observando las gráficas, el escenario A es el caso promedio, el escenario B es el mejor caso y el escenario C es el peor caso.


### PARTE 4 — Complejidad de merge sort e insertion sort: cálculo y validación

#### 4.1 — Cálculo teórico



