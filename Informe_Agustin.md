# Aporte al informe: ordenamientos, estadísticas y arquitectura

**Integrante:** Agustin Tromba  
**Proyecto:** Gestión de Datos de Países en Python

Este documento contiene las secciones correspondientes a ordenamientos, estadísticas básicas y decisiones técnicas. Se integrará al informe PDF grupal junto con las secciones de los demás integrantes.

## Marco teórico: ordenamientos

Ordenar consiste en reorganizar una colección según un criterio. En este proyecto, cada elemento es un diccionario que representa un país y la clave elegida determina qué dato se compara: nombre, población o superficie. El orden ascendente ubica primero los valores menores; el descendente ubica primero los mayores. Para los nombres, se utiliza una comparación de texto sin distinguir mayúsculas y minúsculas mediante `casefold()`. Las tildes se conservan, por lo que no se aplica un orden alfabético regional específico.

Python dispone de `list.sort()`, que modifica una lista, y `sorted()`, que devuelve una nueva lista ordenada [1]. En este trabajo se implementa manualmente el **ordenamiento por inserción** para practicar recorridos, comparaciones y desplazamientos de elementos.

El algoritmo comienza en el segundo elemento. En cada paso guarda el país actual, lo compara con los anteriores y desplaza los que deben quedar después. Finalmente, coloca el país guardado en el lugar disponible. Así, la parte inicial de la lista queda ordenada y se amplía hasta abarcar todos los registros.

Por ejemplo, para ordenar las poblaciones `30, 10, 20` de menor a mayor, primero se inserta `10` antes de `30`, obteniendo `10, 30, 20`. Luego se inserta `20` entre ambos y se obtiene `10, 20, 30`.

En el peor caso, la cantidad de comparaciones y desplazamientos crece de forma cuadrática respecto de la cantidad de países: O(n²). Si la lista ya está ordenada, se realiza una comparación por paso y el recorrido es O(n). Es una elección adecuada para practicar con un conjunto pequeño; para volúmenes grandes convendría utilizar las herramientas incorporadas de Python.

La función `ordenar_paises` trabaja sobre una copia superficial de la lista [2]. Esto requiere O(n) de espacio adicional y conserva el orden original. Los diccionarios son compartidos, pero la función no modifica sus campos. Cuando dos valores son iguales, no se desplazan entre sí: el algoritmo es estable tanto en orden ascendente como descendente.

## Marco teórico: estadísticas básicas

Las estadísticas descriptivas permiten resumir las características de los países cargados. Los resultados corresponden exclusivamente al dataset utilizado y no deben interpretarse como indicadores de todos los países del mundo si la lista está incompleta.

Para hallar el país con mayor población se toma el primero como referencia y se recorre la lista, reemplazándolo cuando aparece otro con más habitantes. Para el mínimo se aplica el mismo procedimiento con la comparación inversa. En caso de empate, se conserva el primer país encontrado.

La media aritmética es la suma de los valores dividida por su cantidad [3]:

```text
Promedio de población = suma de las poblaciones / cantidad de países
Promedio de superficie = suma de las superficies / cantidad de países
```

Cada país tiene el mismo peso en estos promedios. La población se expresa en habitantes y la superficie en kilómetros cuadrados. El resultado puede tener decimales aunque los datos originales sean enteros. El módulo devuelve el valor calculado; el menú puede mostrarlo con dos decimales sin modificar los datos.

Para contar países por continente se utiliza un diccionario de frecuencias. Cada continente es una clave y su valor aumenta en uno por cada país encontrado. Con los cuatro registros del ejemplo del README, los resultados son:

| Indicador | Resultado |
| --- | --- |
| Mayor población | Brasil: 213.993.437 habitantes |
| Menor población | Argentina: 45.376.763 habitantes |
| Promedio de población | 117.079.875 habitantes |
| Promedio de superficie | 3.007.791 km² |
| Países por continente | América: 2; Asia: 1; Europa: 1 |

Si no hay países, los extremos y los promedios devuelven `None`, mientras que el conteo devuelve `{}`. Un promedio sin datos no se representa con cero porque eso confundiría la ausencia de información con una media válida. Esta comprobación también evita dividir por cero.

## Decisiones técnicas y arquitectura

### Organización por responsabilidades

La arquitectura prevista separa la interacción por consola del procesamiento de datos:

| Módulo | Responsabilidad |
| --- | --- |
| `main.py` | Mostrar el menú, solicitar opciones y presentar resultados o errores. |
| `datos.py` | Leer y guardar el CSV, agregar países y actualizar registros. |
| `validaciones.py` | Validar textos, números, rangos y opciones. |
| `consultas.py` | Buscar y filtrar países. |
| `ordenar.py` | Devolver una lista ordenada por el criterio seleccionado. |
| `estadisticas.py` | Calcular y devolver los indicadores. |

Los módulos de ordenamiento y estadísticas están implementados de manera independiente. Los restantes módulos y la conexión con el menú corresponden a las otras partes del proyecto y están pendientes de integración.

### Formato compartido de los datos

Las funciones reciben una lista de diccionarios con las claves `nombre`, `poblacion`, `superficie` y `continente`. Los dos campos numéricos deben llegar convertidos a enteros positivos. La lectura del CSV y las validaciones deben garantizar esos tipos, los campos completos y una escritura uniforme de los continentes. Por ejemplo, todos los registros americanos deben usar `América`, evitando que `américa` o espacios adicionales generen grupos distintos.

No se repite la validación completa de cada registro en los módulos de cálculo. Sí se verifica que el criterio de ordenamiento sea válido y que el sentido sea un booleano. Si esos parámetros son incorrectos se lanza `ValueError`, que el menú debe manejar con un mensaje claro.

### Separación entre cálculo y presentación

Las funciones no solicitan entradas, no imprimen resultados y no acceden al CSV. Devuelven listas, diccionarios, números o `None`, según la operación. Esto permite reutilizarlas con el dataset completo o con una lista filtrada y comprobarlas sin recorrer el menú.

`calcular_estadisticas` reúne las funciones individuales en un único diccionario. Aunque recorre la lista varias veces, el número de recorridos es fijo y su costo total sigue siendo O(n). Se prioriza que cada función tenga una responsabilidad clara.

### Secuencia de integración

```text
Menú: ordenar
  -> Solicitar criterio y sentido
  -> Validar la opción
  -> Llamar a ordenar_paises
  -> Mostrar la lista devuelta o informar que no hay países
  -> Volver al menú

Menú: estadísticas
  -> Comprobar si hay países cargados
  -> Si no hay: mostrar un mensaje y volver
  -> Si hay: llamar a calcular_estadisticas
  -> Mostrar extremos, promedios y cantidades por continente
  -> Volver al menú
```

Las capturas del programa completo se incorporarán una vez integrado el menú. Este esquema describe únicamente las operaciones de estos módulos y sirve como apoyo al diagrama general.

## Bibliografía y webgrafía

1. Python Software Foundation. *Sorting Techniques*. Documentación oficial de Python. https://docs.python.org/es/3/howto/sorting.html
2. Python Software Foundation. *Estructuras de datos*. Documentación oficial de Python. https://docs.python.org/es/3/tutorial/datastructures.html
3. Python Software Foundation. *statistics: Mathematical statistics functions*, apartado de media aritmética. Documentación oficial de Python. https://docs.python.org/es/3/library/statistics.html#statistics.mean
