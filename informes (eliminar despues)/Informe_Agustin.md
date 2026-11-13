# Agustin Tromba – Ordenamientos, estadísticas y arquitectura

## 1. Introducción

Mi responsabilidad en el proyecto fue desarrollar los módulos encargados de ordenar los países y calcular estadísticas a partir de sus datos. También participé en la definición de algunas decisiones técnicas para organizar el funcionamiento del programa.

Para esto se crearon los archivos `ordenar.py` y `estadisticas.py`.

## 2. Conceptos utilizados

**Ordenamientos:** Consisten en organizar una lista de elementos según un criterio determinado. En nuestro proyecto se utilizan para ordenar los países por nombre, población o superficie, tanto de manera ascendente como descendente.

Se implementó el algoritmo de ordenamiento por inserción (*Insertion Sort*), que compara los elementos y los ubica en su posición correspondiente. Se eligió este método para practicar los conceptos de recorridos, comparaciones y desplazamientos de elementos.

**Estadísticas básicas:** Permiten obtener información general a partir de los datos disponibles. En nuestro proyecto se utilizan para identificar los países con mayor y menor población, calcular promedios de población y superficie y contar cuántos países hay por continente.

## 3. Desarrollo realizado

Se desarrollaron dos módulos principales:

- `ordenar.py`: permite ordenar los países por nombre, población y superficie. Trabaja sobre una copia de la lista original para conservar el orden de los datos iniciales.
- `estadisticas.py`: calcula los indicadores solicitados, utilizando recorridos de listas y diccionarios para obtener los resultados.

También se contemplaron situaciones en las que no existen países cargados, evitando errores al realizar cálculos o buscar valores máximos y mínimos.

## 4. Decisiones técnicas y arquitectura

Se decidió separar las funciones de ordenamiento y estadísticas del menú principal para que cada módulo tenga una responsabilidad específica.

Las funciones reciben una lista de diccionarios con los datos de los países y devuelven los resultados correspondientes, sin encargarse de mostrar información por consola ni modificar el archivo CSV.

La organización general del proyecto quedó dividida en diferentes módulos:

- `datos.py`: lectura y almacenamiento de información.
- `consultas.py`: búsquedas y filtros.
- `validaciones.py`: controles de entradas.
- `ordenar.py`: ordenamiento de países.
- `estadisticas.py`: cálculo de indicadores.
- `main.py`: menú e integración del programa.

La integración con el menú principal queda a cargo del desarrollo grupal.

## 5. Ejemplo de resultados

Utilizando los cuatro países del ejemplo del README, se obtienen los siguientes resultados:

| Indicador | Resultado |
|---|---|
| Mayor población | Brasil |
| Menor población | Argentina |
| Promedio de población | 117.079.875 habitantes |
| Promedio de superficie | 3.007.791 km² |
| Países por continente | América: 2, Asia: 1, Europa: 1 |

Estos resultados corresponden únicamente al conjunto de datos utilizado como ejemplo.

## 6. Conclusión

El desarrollo de esta parte permitió poner en práctica los algoritmos de ordenamiento y el cálculo de estadísticas básicas. También fue importante comprender cómo dividir un programa en módulos independientes para facilitar su mantenimiento e integración.

## 7. Bibliografía y webgrafía

1. Python Software Foundation. *Sorting Techniques*. Documentación oficial de Python. https://docs.python.org/es/3/howto/sorting.html
2. Python Software Foundation. *Estructuras de datos*. https://docs.python.org/es/3/tutorial/datastructures.html
3. Python Software Foundation. *statistics: Mathematical statistics functions*. https://docs.python.org/es/3/library/statistics.html#statistics.mean

**Archivos desarrollados:** `ordenar.py` y `estadisticas.py`.