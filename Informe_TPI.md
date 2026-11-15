<!--
PLANTILLA DEL INFORME TÉCNICO – TRABAJO PRÁCTICO INTEGRADOR
Programación 1 – Tecnicatura Universitaria en Programación a Distancia

INSTRUCCIONES DE USO
1. Reemplazar todos los textos entre corchetes: [Texto aquí].
2. Actualizar los números de página [N] del índice después de exportar el PDF.
3. Guardar las imágenes en la carpeta img/ y reemplazar los marcadores de figura.
4. Exportar a PDF en A4, márgenes de 2,5 cm, fuente Calibri o Arial 11,
   interlineado 1,5 y numeración de páginas en el pie.
5. Verificar que el repositorio de GitHub y el video de YouTube sean públicos.
6. Eliminar este comentario antes de la exportación final.
-->

<div align="center">

<br><br>

<p><strong>UNIVERSIDAD TECNOLÓGICA NACIONAL</strong></p>

<p>[Facultad Regional / Sede]</p>

<p><strong>Tecnicatura Universitaria en Programación a Distancia</strong></p>

<br>

<p><strong>Programación 1</strong></p>

<br><br>

<p><strong>TRABAJO PRÁCTICO INTEGRADOR</strong></p>

<p><strong>Gestión de Datos de Países en Python:</strong><br>
<strong>filtros, ordenamientos y estadísticas</strong></p>

<br><br><br>

</div>

| Datos académicos | Detalle |
|---|---|
| **Comisión** | [N° de comisión] |
| **Grupo** | [N° de grupo] |
| **Docente** | [Nombre y apellido del docente] |
| **Modalidad** | A distancia |
| **Fecha de entrega** | [DD/MM/AAAA] |
| **Año lectivo** | [Año] |

**Integrantes**

| Nombre y apellido | Legajo / DNI | Usuario de GitHub |
|---|---|---|
| Facundo Piriz | [Legajo] | [@Fakzup] |
| Francisco Ruiz | [Legajo] | [@fran1399] |
| Agustín Tromba | [Legajo] | [@aqussti] |
| Fausto Rivero | [Legajo] | [@faustorivero69-hue] |

<div style="page-break-after: always;"></div>

## Índice

| Sección | Contenido | Página |
|---|---|---|
| — | Resumen | [N] |
| 1 | Introducción | [N] |
| 1.1 | Contexto y problemática | [N] |
| 1.2 | Objetivos | [N] |
| 1.3 | Alcance | [N] |
| 1.4 | Metodología y organización del trabajo | [N] |
| 2 | Marco Teórico | [N] |
| 2.1 | Listas | [N] |
| 2.2 | Diccionarios | [N] |
| 2.3 | Funciones y modularización | [N] |
| 2.4 | Condicionales y estructuras repetitivas | [N] |
| 2.5 | Archivos CSV | [N] |
| 2.6 | Ordenamientos | [N] |
| 2.7 | Estadísticas básicas | [N] |
| 2.8 | Validación de entradas y manejo de errores | [N] |
| 2.9 | Síntesis de los conceptos aplicados | [N] |
| 3 | Decisiones Técnicas y Arquitectura | [N] |
| 3.1 | Arquitectura modular del sistema | [N] |
| 3.2 | Modelo de datos del dominio | [N] |
| 3.3 | Flujo principal del sistema | [N] |
| 3.4 | Decisiones de diseño | [N] |
| 3.5 | Interfaz de consola y experiencia de usuario | [N] |
| 3.6 | Pruebas y capturas de ejecución | [N] |
| 3.6.1 | Menú principal | [N] |
| 3.6.2 | Alta de un país | [N] |
| 3.6.3 | Actualización de datos | [N] |
| 3.6.4 | Búsqueda por nombre | [N] |
| 3.6.5 | Filtro por continente | [N] |
| 3.6.6 | Filtro por rango de población o superficie | [N] |
| 3.6.7 | Ordenamiento | [N] |
| 3.6.8 | Estadísticas | [N] |
| 3.6.9 | Manejo de errores | [N] |
| 3.7 | Trazabilidad de requisitos | [N] |
| 3.8 | Limitaciones y mejoras futuras | [N] |
| 4 | Dificultades y Conclusiones | [N] |
| 4.1 | Dificultades técnicas | [N] |
| 4.2 | Dificultades de organización del equipo | [N] |
| 4.3 | Estrategias de resolución | [N] |
| 4.4 | Conclusiones grupales | [N] |
| 4.5 | Aprendizajes individuales | [N] |
| 4.6 | Reflexión final | [N] |
| 5 | Enlaces del Proyecto | [N] |
| 5.1 | Repositorio de GitHub | [N] |
| 5.2 | Video demostrativo | [N] |
| 5.3 | Documento PDF | [N] |
| 5.4 | Verificación de enlaces | [N] |
| 6 | Bibliografía y Webgrafía | [N] |
| 6.1 | Bibliografía | [N] |
| 6.2 | Webgrafía | [N] |
| 6.3 | Nota sobre el uso de fuentes | [N] |
| — | Anexos | [N] |
| A | Instructivo de instalación y ejecución | [N] |
| B | Participación de los integrantes | [N] |
| C | Glosario | [N] |

## Índice de figuras

| Figura | Descripción | Página |
|---|---|---|
| 1 | Diagrama de flujo de las operaciones principales | [N] |
| 2 | Menú principal del sistema | [N] |
| 3 | Alta de un país | [N] |
| 4 | Actualización de población y superficie | [N] |
| 5 | Búsqueda por nombre | [N] |
| 6 | Filtro por continente | [N] |
| 7 | Filtro por rango de población o superficie | [N] |
| 8 | Ordenamiento de países | [N] |
| 9 | Estadísticas del dataset | [N] |
| 10 | Manejo de errores en la consola | [N] |

<div style="page-break-after: always;"></div>

## Resumen

[Texto aquí: escribir entre 150 y 200 palabras. Describir el problema abordado, la solución desarrollada, los módulos que componen el sistema, las estructuras de datos utilizadas y los resultados principales obtenidos.]

**Palabras clave:** Python; archivos CSV; listas; diccionarios; modularización; ordenamientos; estadísticas; validación de datos.

---

## 1. Introducción

### 1.1 Contexto y problemática

[Texto aquí: explicar por qué es necesario gestionar información de países, qué dificultades presenta el manejo manual de estos datos y por qué resultan útiles las operaciones de búsqueda, filtrado, ordenamiento y cálculo de estadísticas. Mencionar el volumen creciente de información y la necesidad de evitar errores.]

[Texto aquí: justificar la elección de Python y del formato CSV como tecnologías adecuadas para el problema planteado, considerando que se trata de una aplicación de consola y de un trabajo práctico de Programación 1.]

### 1.2 Objetivos

**Objetivo general**

[Texto aquí: describir el objetivo general del proyecto en una o dos oraciones.]

**Objetivos específicos**

- [Implementar una aplicación de consola que permita gestionar un dataset de países.]
- [Leer y persistir los datos en un archivo CSV, controlando errores de formato.]
- [Permitir el alta de países y la actualización de población y superficie.]
- [Implementar búsquedas por nombre y filtros por continente, población y superficie.]
- [Ordenar los registros por nombre, población o superficie en forma ascendente y descendente.]
- [Calcular indicadores estadísticos: extremos, promedios y cantidad por continente.]
- [Aplicar validaciones de entrada y mensajes claros de éxito y error.]
- [Documentar el diseño, las decisiones técnicas y las pruebas realizadas.]

### 1.3 Alcance

[Texto aquí: delimitar el alcance. Indicar que se trata de una aplicación de consola, con persistencia local en CSV, sin base de datos, sin interfaz gráfica y sin servicios externos. Mencionar qué funcionalidades quedan fuera del alcance y por qué.]

### 1.4 Metodología y organización del trabajo

[Texto aquí: describir la metodología de trabajo: reuniones, división de responsabilidades, uso de GitHub, ramas, revisiones y pruebas de integración. Explicar cómo se coordinó el equipo y cómo se validó el funcionamiento conjunto de los módulos.]

| Etapa | Actividad principal | Responsable | Entregable |
|---|---|---|---|
| 1. Diseño | [Definición del dominio, estructura de datos y contratos entre módulos] | [Integrante/s] | [Documento de diseño] |
| 2. Desarrollo | [Implementación de módulos independientes] | [Integrante/s] | [Archivos .py] |
| 3. Integración | [Menú principal, pruebas y corrección de interfaces] | [Integrante/s] | [main.py] |
| 4. Documentación | [Marco teórico, arquitectura, capturas y conclusiones] | [Integrante/s] | [Informe PDF] |
| 5. Presentación | [Grabación del video demostrativo] | [Integrante/s] | [Video público] |

<div style="page-break-after: always;"></div>

## 2. Marco Teórico

[Texto aquí: presentar brevemente los conceptos teóricos que se aplican en el proyecto y explicar cómo se relacionan entre sí. Cada apartado debe incluir una definición, una explicación de su aplicación concreta en el sistema y, cuando corresponda, un ejemplo de código y la fuente consultada.]

### 2.1 Listas

[Texto aquí — responsable sugerido: Facundo Piriz. Definir el concepto de lista en Python, explicar su naturaleza ordenada y mutable, y describir las operaciones utilizadas en el proyecto: creación, recorrido, agregado, búsqueda y longitud. Explicar que la lista principal contiene todos los países cargados desde el CSV.]

```python
# [Insertar un ejemplo representativo del proyecto: lista de países,
# recorrido con for o acceso a un elemento.]
```

**Aplicación en el proyecto:** [Texto aquí: indicar en qué módulos se utilizan listas y para qué.]

**Fuente:** [Texto aquí: referencia bibliográfica o webgrafía consultada.]

### 2.2 Diccionarios

[Texto aquí — responsable sugerido: Facundo Piriz. Definir el concepto de diccionario, explicar la relación clave-valor y describir cómo se representa cada país con las claves nombre, poblacion, superficie y continente. Mencionar las ventajas de acceso directo y la legibilidad del modelo.]

```python
# [Insertar un ejemplo representativo del proyecto: diccionario de un país
# y acceso a sus campos.]
```

**Aplicación en el proyecto:** [Texto aquí: indicar en qué módulos se utilizan diccionarios y cómo se recorre la lista de registros.]

**Fuente:** [Texto aquí.]

### 2.3 Funciones y modularización

[Texto aquí — responsable sugerido: Francisco Ruiz. Definir qué es una función, explicar parámetros, argumentos, valor de retorno y ámbito. Desarrollar el principio de una función = una responsabilidad y la importancia de dividir el programa en módulos con bajo acoplamiento.]

[Texto aquí: describir la organización modular del proyecto y la comunicación entre main.py y los demás archivos. Mencionar las ventajas de mantenibilidad, reutilización y prueba independiente.]

```python
# [Insertar un ejemplo representativo del proyecto: definición y llamada
# a una función que recibe la lista de países y devuelve un resultado.]
```

**Aplicación en el proyecto:** [Texto aquí.]

**Fuente:** [Texto aquí.]

### 2.4 Condicionales y estructuras repetitivas

[Texto aquí — responsable sugerido: Francisco Ruiz. Explicar las estructuras if, elif y else, y los bucles while y for. Relacionarlas con la navegación del menú, la validación de entradas, el recorrido de listas y la repetición de operaciones hasta que el usuario elija salir.]

[Texto aquí: explicar por qué el menú principal utiliza un while True y cómo se evita un bucle infinito mediante la opción de salida y el manejo de errores.]

```python
# [Insertar un ejemplo representativo del proyecto: bucle del menú
# o validación repetitiva de una entrada.]
```

**Aplicación en el proyecto:** [Texto aquí.]

**Fuente:** [Texto aquí.]

### 2.5 Archivos CSV

[Texto aquí — responsable sugerido: Facundo Piriz. Definir el formato CSV, explicar su estructura de filas y columnas, la importancia de la primera fila de encabezados y el uso del módulo csv de la biblioteca estándar. Mencionar las funciones reader, writer, DictReader y DictWriter.]

[Texto aquí: explicar la persistencia de los datos, la codificación UTF-8, el tratamiento de acentos y la diferencia entre leer el archivo y mantener los datos en memoria.]

```python
# [Insertar un ejemplo representativo del proyecto: lectura o escritura
# de un registro en el archivo paises.csv.]
```

**Aplicación en el proyecto:** [Texto aquí: describir el archivo paises.csv, sus columnas y el momento en que se guardan los cambios.]

**Fuente:** [Texto aquí.]

### 2.6 Ordenamientos

[Texto aquí — responsable sugerido: Agustín Tromba. Definir el concepto de ordenamiento, explicar el criterio y el sentido ascendente o descendente. Describir el algoritmo de inserción utilizado, sus comparaciones y desplazamientos, y su comportamiento con listas pequeñas.]

[Texto aquí: explicar por qué se ordena sobre una copia de la lista, cómo se conserva el orden original ante empates y cómo se comparan los nombres sin distinguir mayúsculas y minúsculas.]

```python
# [Insertar un ejemplo representativo del proyecto: llamada a
# ordenar_paises() con un criterio y un sentido determinados.]
```

**Aplicación en el proyecto:** [Texto aquí.]

**Fuente:** [Texto aquí.]

### 2.7 Estadísticas básicas

[Texto aquí — responsable sugerido: Agustín Tromba. Definir los conceptos de máximo, mínimo, promedio y frecuencia. Explicar cómo se calculan recorriendo la lista de países y cómo se interpretan los resultados en el contexto del dataset.]

[Texto aquí: describir los indicadores implementados: país con mayor y menor población, promedio de población, promedio de superficie y cantidad de países por continente. Mencionar el tratamiento de listas vacías.]

```python
# [Insertar un ejemplo representativo del proyecto: cálculo de un
# indicador o llamada a calcular_estadisticas().]
```

**Aplicación en el proyecto:** [Texto aquí.]

**Fuente:** [Texto aquí.]

### 2.8 Validación de entradas y manejo de errores

[Texto aquí — responsable sugerido: Francisco Ruiz. Explicar la importancia de validar los datos ingresados por el usuario y de anticipar errores. Describir el uso de try, except, ValueError, FileNotFoundError y mensajes claros. Mencionar la diferencia entre un error de formato, un error de archivo y un error de lógica.]

[Texto aquí: explicar cómo el menú principal permanece activo ante una entrada inválida y cómo se evitan campos vacíos, valores negativos y opciones fuera de rango.]

```python
# [Insertar un ejemplo representativo del proyecto: bloque try-except
# con un mensaje amigable para el usuario.]
```

**Aplicación en el proyecto:** [Texto aquí.]

**Fuente:** [Texto aquí.]

### 2.9 Síntesis de los conceptos aplicados

| Concepto | Definición breve | Aplicación en el proyecto | Módulo principal | Fuente |
|---|---|---|---|---|
| Listas | [Texto aquí] | [Texto aquí] | [datos.py / main.py] | [Fuente] |
| Diccionarios | [Texto aquí] | [Texto aquí] | [datos.py] | [Fuente] |
| Funciones | [Texto aquí] | [Texto aquí] | [Todos los módulos] | [Fuente] |
| Condicionales | [Texto aquí] | [Texto aquí] | [main.py / validaciones.py] | [Fuente] |
| Bucles | [Texto aquí] | [Texto aquí] | [main.py / datos.py] | [Fuente] |
| Archivos CSV | [Texto aquí] | [Texto aquí] | [datos.py] | [Fuente] |
| Ordenamientos | [Texto aquí] | [Texto aquí] | [ordenar.py] | [Fuente] |
| Estadísticas | [Texto aquí] | [Texto aquí] | [estadisticas.py] | [Fuente] |
| Excepciones | [Texto aquí] | [Texto aquí] | [datos.py / main.py] | [Fuente] |

<div style="page-break-after: always;"></div>

## 3. Decisiones Técnicas y Arquitectura

### 3.1 Arquitectura modular del sistema

La aplicación se organizó en seis módulos de código y un archivo de datos. La división no respondió solamente a una necesidad de orden: buscó aislar responsabilidades para que cada integrante pudiera avanzar sobre una parte acotada, comprobable y reutilizable. `main.py` cumple el rol de integrador: inicia el programa, carga el dataset, presenta el menú, solicita las entradas, llama a las funciones de los demás módulos y muestra los resultados. Los módulos de cálculo —`consultas.py`, `ordenar.py` y `estadisticas.py`— reciben la lista de países y devuelven listas o diccionarios nuevos sin imprimir por consola. `datos.py` encapsula la persistencia en CSV y las operaciones de alta y actualización. `validaciones.py` reúne las funciones de lectura y validación de entradas.

Esta separación reduce el acoplamiento y permite probar cada módulo por separado. También evita duplicar reglas: la búsqueda sin tildes vive en `consultas.normalizar()`, la validación de enteros en `validaciones.pedir_entero_positivo()` y la escritura del archivo en `datos.guardar_paises()`. Si en el futuro se reemplaza la consola por una interfaz gráfica o web, las funciones de consulta, ordenamiento y estadísticas pueden reutilizarse sin cambios; solo debería adaptarse la capa de presentación.

```text
tpi-programacion-i-utn/
├── main.py              # Punto de entrada, menú, integración y experiencia de usuario
├── datos.py             # Lectura/escritura del CSV, alta y actualización
├── consultas.py         # Búsqueda, filtros y normalización de texto
├── validaciones.py      # Lectura y validación de entradas del usuario
├── ordenar.py           # Ordenamiento por nombre, población y superficie
├── estadisticas.py      # Cálculo de indicadores
├── paises.csv           # Dataset base
├── Informe_TPI.pdf      # Documento académico final
├── Informe_TPI.md       # Fuente editable del informe
└── README.md            # Documentación del repositorio
```

Para la entrega en formato `.zip` se incluyen únicamente los seis módulos, `paises.csv` y el informe final en PDF. El repositorio conserva además el `README.md` y la fuente editable del informe.

| Archivo | Responsabilidad | Funciones principales | Integrante |
|---|---|---|---|
| `main.py` | Punto de entrada, menú, navegación, mensajes y unión de los módulos | `main()`, `mostrar_menu()`, `ejecutar_opcion()`, `opcion_agregar()`, `opcion_actualizar()`, `opcion_buscar()`, `opcion_filtrar()`, `opcion_ordenar()`, `opcion_estadisticas()` | Fausto Rivero |
| `datos.py` | Lectura y escritura del CSV; alta y actualización de países | `leer_paises()`, `guardar_paises()`, `agregar_pais()`, `actualizar_pais()` | Facundo Piriz |
| `consultas.py` | Búsqueda por nombre, filtros por continente y rangos, normalización de texto | `normalizar()`, `buscar_por_nombre()`, `filtrar_por_continente()`, `filtrar_por_poblacion()`, `filtrar_por_superficie()`, `obtener_continentes()` | Francisco Ruiz |
| `validaciones.py` | Validación transversal de entradas y opciones de menú | `pedir_texto_no_vacio()`, `pedir_entero_positivo()`, `pedir_rango()`, `pedir_opcion_menu()` | Francisco Ruiz |
| `ordenar.py` | Ordenamiento ascendente y descendente por tres criterios | `ordenar_paises()` | Agustín Tromba |
| `estadisticas.py` | Cálculo de extremos, promedios y conteos por continente | `calcular_estadisticas()` y funciones auxiliares | Agustín Tromba |
| `paises.csv` | Dataset persistente con los registros de países | — | Facundo Piriz |

El contrato de integración quedó documentado al inicio de `main.py`. Cada función indica qué recibe y qué devuelve; por ejemplo, `buscar_por_nombre(paises, texto, exacta=False)` devuelve una lista nueva y `agregar_pais()` devuelve `True` o `False` según el resultado de la persistencia. Esa documentación fue clave para reemplazar las llamadas iniciales por las firmas reales entregadas por el equipo.

### 3.2 Modelo de datos del dominio

Cada país se representa mediante un diccionario con cuatro claves: `nombre`, `poblacion`, `superficie` y `continente`. El conjunto completo se almacena en una lista de diccionarios. Esta estructura refleja naturalmente el dominio: una colección ordenada de registros con campos identificables por nombre y no por posición. El acceso mediante claves (`pais["poblacion"]`) hace que el código sea legible y evita errores cuando se agrega o reorganiza un campo.

| Campo | Tipo de dato | Descripción | Validación aplicada |
|---|---|---|---|
| `nombre` | `str` | Nombre del país | No vacío; sin duplicados; se compara sin distinguir mayúsculas ni tildes |
| `poblacion` | `int` | Cantidad de habitantes | Entero positivo |
| `superficie` | `int` | Superficie en km² | Entero positivo |
| `continente` | `str` | Continente al que pertenece | No vacío; se normaliza con `capitalize()` y se unifica con los continentes existentes |

**Ejemplo de registro:**

```python
{
    "nombre": "Argentina",
    "poblacion": 45376763,
    "superficie": 2780400,
    "continente": "América",
}
```

`datos.leer_paises()` lee el archivo con `csv.DictReader`, verifica que las columnas sean exactamente `nombre`, `poblacion`, `superficie` y `continente`, convierte los valores numéricos a `int` y rechaza filas incompletas o con valores no positivos. `datos.agregar_pais()` y `datos.actualizar_pais()` aplican las mismas reglas antes de guardar. De este modo, las funciones de consulta, ordenamiento y estadísticas pueden suponer que los registros ya están validados.

### 3.3 Flujo principal del sistema

El programa comienza mostrando un mensaje de carga, lee `paises.csv` y construye la lista de diccionarios en memoria. Si el archivo no existe o tiene un formato inválido, `leer_paises()` devuelve una lista vacía y muestra el error correspondiente; el menú continúa funcionando para que el usuario pueda agregar un país o revisar el archivo. Luego se presenta el menú principal y se espera una opción. La opción se valida contra la lista de valores permitidos; si es incorrecta, se informa y se vuelve a preguntar sin finalizar el programa. Cuando la opción es válida, se limpia la pantalla, se ejecuta la operación, se muestra el resultado y se realiza una pausa con Enter antes de volver al menú.

> **[Insertar aquí el diagrama de flujo de las operaciones principales]**
>
> *Figura 1. Flujo general del sistema: carga del CSV, menú, operaciones y persistencia.*
>
> Sugerencia para el diagrama: incluir un rombo de decisión para "¿Opción válida?", otro para "¿País encontrado?" y una rama de error que regrese al menú sin finalizar el programa.

**Flujo resumido:**

1. Inicio y configuración de la consola (UTF-8 en Windows).
2. Carga de `paises.csv` y construcción de la lista de diccionarios.
3. Mostrar el menú principal con la cantidad de países cargados.
4. Leer y validar la opción ingresada.
5. Ejecutar la operación seleccionada: agregar, actualizar, buscar, filtrar, ordenar o calcular estadísticas.
6. Mostrar el resultado y pausar con Enter.
7. Volver al paso 3 mientras la opción no sea Salir.
8. Guardar los cambios en el CSV cuando la operación lo requiera y finalizar.

Las operaciones de alta y actualización trabajan en dos pasos: primero preparan una copia de los datos y llaman a `guardar_paises()`; solo si la escritura fue exitosa actualizan la lista en memoria. Si el guardado falla, la lista original queda intacta. La lectura se realiza una sola vez al inicio; las altas y actualizaciones mantienen sincronizadas la lista en memoria y el archivo CSV. Las consultas, los filtros y los ordenamientos no modifican la lista original: devuelven resultados nuevos para mostrar.

El bucle principal es un `while True` que solo se interrumpe con la opción Salir, con `Ctrl+C` o con el cierre de la entrada estándar. El menú utiliza `validaciones.pedir_opcion_menu()`, que rechaza letras y números fuera de rango sin lanzar excepciones. Además, `main()` envuelve el ciclo en un `try-except` para capturar `KeyboardInterrupt`, `EOFError`, `ValueError` y cualquier error inesperado, informar al usuario y continuar o salir de forma ordenada.

### 3.4 Decisiones de diseño

- **Lista de diccionarios:** se eligió porque el dataset es una colección de registros con campos nominales. El diccionario permite acceder por clave y la lista conserva el orden de lectura. Las listas paralelas habrían exigido mantener sincronizados varios arreglos; las tuplas habrían dificultado las actualizaciones; una clase `Pais` habría sido válida, pero incorporaba complejidad de programación orientada a objetos que la consigna no exigía.

- **Persistencia en CSV:** el formato es legible, editable con cualquier editor de texto, liviano y suficiente para 19 registros. También permite verificar la persistencia sin herramientas externas. JSON o SQLite serían alternativas más robustas para volúmenes mayores, pero agregaban dependencias o complejidad innecesaria para el alcance del trabajo. Se usa `csv.DictReader` y `csv.DictWriter` para no depender de separadores manuales.

- **Separación entre lógica y presentación:** `consultas.py`, `ordenar.py` y `estadisticas.py` no imprimen: reciben datos y devuelven resultados. `main.py` decide cómo mostrarlos. Esto permitió probar las funciones con listas armadas y reutilizarlas si en el futuro se agrega otra interfaz. `datos.py` y `validaciones.py` conservan mensajes puntuales de confirmación o error para no perder información en el punto donde se detecta el problema; el menú sigue siendo el responsable del formato general.

- **Validaciones centralizadas:** `validaciones.py` concentra la lectura de texto no vacío, enteros positivos, rangos y opciones de menú. Cada función repite la pregunta hasta obtener un valor válido. Esto unifica los mensajes, evita dispersar `while` y `try-except` por todos los módulos y garantiza que los datos que llegan a la lógica ya tengan el formato esperado.

- **Retorno booleano en altas y actualizaciones:** `agregar_pais()` y `actualizar_pais()` devuelven `True` o `False` según el resultado de la persistencia. `main.py` traduce ese booleano en un mensaje de éxito o error, sin necesidad de inspeccionar el CSV ni duplicar las reglas de validación. La lista en memoria solo se modifica después de que `guardar_paises()` confirma la escritura.

- **Codificación UTF-8:** el dataset contiene tildes y `ñ` (`América`, `México`, `Japón`, `Oceanía`, `África`). Se leyó con `utf-8-sig` para tolerar el BOM que suele agregar Excel y se guardó con `utf-8`. En Windows, `main.py` ejecuta `chcp 65001` y reconfigura `stdin`, `stdout` y `stderr` para evitar caracteres corruptos. La función `consultas.normalizar()` usa `unicodedata` para comparar sin tildes.

- **Limpieza de consola multiplataforma:** `limpiar_consola()` consulta `os.name`: usa `cls` en Windows y `clear` en Linux/macOS. La operación se envuelve en `try-except` para que un entorno sin consola interactiva no interrumpa el programa. Así el mismo código funciona en las distintas computadoras del equipo.

- **Manejo de errores con try-except:** las entradas numéricas se validan con `try-except ValueError` dentro de `pedir_entero_positivo()`. El menú principal agrega un `try-except` externo para `KeyboardInterrupt`, `EOFError`, `ValueError` y errores inesperados; ante cualquiera, informa y vuelve al menú o finaliza ordenadamente. La validación de opciones se hace por pertenencia a una lista de cadenas, de modo que una letra se rechaza sin producir una excepción.

- **Ordenamiento sobre una copia:** `ordenar_paises()` trabaja con `paises.copy()` y aplica ordenamiento por inserción. No modifica la lista original ni los diccionarios; así el orden del dataset se mantiene estable entre operaciones y el usuario puede ordenar varias veces con criterios distintos sin alterar la fuente.

- **Unificación de continentes:** en el alta, `main.normalizar_continente()` compara el texto ingresado con los continentes existentes usando `normalizar()`. Si coincide, reutiliza el nombre canónico (`América` en lugar de `America`); si es nuevo, lo capitaliza. Esto evita duplicados por mayúsculas o tildes y complementa la normalización que ya realiza `datos.py`.

- **Búsqueda exacta y parcial:** `buscar_por_nombre()` recibe `exacta=False` por defecto. La opción de búsqueda usa coincidencia parcial para mostrar varias alternativas; la actualización usa `exacta=True` para evitar modificar un país equivocado. Si no hay coincidencia exacta, se muestran las parciales como ayuda.

### 3.5 Interfaz de consola y experiencia de usuario

La interfaz es de consola, con menús numerados y mensajes en español. El menú principal presenta siete opciones y muestra la cantidad de países cargados. Los submenús de filtros y ordenamiento incluyen la opción `0` para volver sin ejecutar cambios. Los resultados se separan con líneas y se informa la cantidad de coincidencias. Los mensajes de éxito comienzan con `[OK]` y los de error con `[ERROR]` o `Error:`, para que el usuario distinga rápidamente el resultado de una operación.

Los números se muestran con puntos de miles y los promedios con coma decimal, de acuerdo con la convención utilizada en Argentina. Después de cada operación se solicita "Presione Enter para continuar", de modo que el usuario pueda leer el resultado antes de que la pantalla se limpie. La limpieza se adapta al sistema operativo y se evita cuando la consola no la admite.

| Elemento | Decisión adoptada | Beneficio |
|---|---|---|
| Menú principal | Siete opciones numeradas y conteo de países cargados | Navegación clara y contexto permanente |
| Submenús | Opciones numeradas y `0` para volver | Se evita escribir nombres largos y se puede cancelar |
| Mensajes de éxito | Prefijo `[OK]` y confirmación de la operación | El usuario sabe que el cambio se guardó |
| Mensajes de error | Prefijo `[ERROR]` o `Error:` y explicación breve | Se distingue el error y se indica cómo corregirlo |
| Pausas | "Presione Enter para continuar" | Permite leer los resultados antes de limpiar la pantalla |
| Limpieza de pantalla | `cls` en Windows y `clear` en Linux/macOS | La salida no se satura y el código es portable |
| Formato numérico | Puntos de miles y coma decimal | Mayor legibilidad para el usuario hispanohablante |

### 3.6 Pruebas y capturas de ejecución

El plan de pruebas combinó pruebas directas de los módulos y pruebas de integración por consola. Las pruebas destructivas de alta y actualización se ejecutaron sobre una copia del CSV y, al finalizar, se restauró el archivo original para no alterar el dataset entregado. Se utilizó Python 3.14.3 en Windows y se ejecutó `python main.py` desde la carpeta raíz del proyecto. Además de los casos exitosos, se probaron entradas vacías, letras, números negativos, rangos invertidos, países inexistentes, opciones inválidas y archivos CSV con formato incorrecto.

**Tabla de casos de prueba**

| N° | Caso de prueba | Entrada | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|---|---|
| 1 | Alta de un país válido | Testlandia; 1.000.000; 100.000; América | El país se agrega y se guarda en el CSV | Alta confirmada; la fila se incorporó al CSV y el menú informó `[OK]` | OK |
| 2 | Alta con campos vacíos | Nombre y continente vacíos; población y superficie válidas | Mensaje de error; no se guarda | `pedir_texto_no_vacio()` repitió la pregunta; no se guardó | OK |
| 3 | Alta con población negativa | -5 | Mensaje de error; no se guarda | `pedir_entero_positivo()` rechazó el valor y volvió a preguntar | OK |
| 4 | Actualización válida | Testlandia; 2.000.000; 200.000 | Datos actualizados en el CSV | `actualizar_pais()` guardó los cambios; la búsqueda posterior mostró los nuevos valores | OK |
| 5 | Actualización de país inexistente | Narnia | Mensaje de error; sin cambios | `[ERROR] No se encontró ningún país llamado 'Narnia'.` | OK |
| 6 | Búsqueda parcial | argent | Lista de coincidencias | Argentina (1 resultado), sin distinguir mayúsculas | OK |
| 7 | Búsqueda sin resultados | zzzz | Mensaje informativo | `No se encontraron países que coincidan con 'zzzz'.` | OK |
| 8 | Filtro por continente | América | Países del continente | 6 países de América en el dataset base | OK |
| 9 | Filtro por rango de población | 100.000.000 a 200.000.000 | Países dentro del rango | México, Japón y Egipto | OK |
| 10 | Filtro por rango de superficie | 0 a 400.000 km² | Países dentro del rango | Uruguay, Alemania, Italia, Japón, Corea del Sur y Nueva Zelanda | OK |
| 11 | Ordenamiento ascendente | Población | Lista de menor a mayor | Uruguay primero; China último | OK |
| 12 | Ordenamiento descendente | Población | Lista de mayor a menor | China primero; Uruguay último | OK |
| 13 | Estadísticas con datos | Dataset cargado | Extremos, promedios y conteos | China (1.412.000.000) y Uruguay (3.426.260); promedios 229.983.424,21 hab. y 2.642.743,79 km²; conteos 6/4/4/3/2 | OK |
| 14 | Estadísticas sin datos | Lista vacía | Mensaje informativo | `No hay países cargados para calcular estadísticas.` | OK |
| 15 | Opción de menú inválida | `abc` y `9` | Mensaje de error; el menú continúa | `pedir_opcion_menu()` rechazó ambas entradas y volvió a preguntar; `7` cerró el programa | OK |
| 16 | CSV con formato inválido | Columnas incorrectas, población no numérica o campo vacío | Mensaje de error; el programa no se cae | `leer_paises()` devolvió `[]` y mostró el error correspondiente en cada caso | OK |

#### 3.6.1 Menú principal

> **[Insertar captura de pantalla: menú principal]**
>
> *Figura 2. Menú principal del sistema con las siete opciones disponibles.*

La Figura 2 muestra el menú principal con el conteo de países cargados y las siete opciones. La opción 7 cierra el programa; las opciones 1 a 6 derivan a las operaciones correspondientes. El conteo se actualiza después de cada alta o actualización, porque `main.py` conserva la lista en memoria sincronizada con el CSV.

#### 3.6.2 Alta de un país

> **[Insertar captura de pantalla: alta de país]**
>
> *Figura 3. Ingreso de los datos de un país y confirmación del alta.*

Para la prueba se utilizó el registro ficticio "Testlandia", con población 1.000.000, superficie 100.000 km² y continente América. Se verificó que el país apareciera en el CSV y que el menú informara `[OK]`. También se probaron nombres vacíos, poblaciones con letras, valores negativos y superficies en cero; en todos los casos la pregunta se repitió sin guardar datos.

#### 3.6.3 Actualización de datos

> **[Insertar captura de pantalla: actualización de población y superficie]**
>
> *Figura 4. Actualización de los datos de un país existente.*

Se actualizó "Testlandia" de 1.000.000 a 2.000.000 de habitantes y de 100.000 a 200.000 km². El programa mostró los datos actuales antes de pedir los nuevos valores, guardó los cambios y confirmó la operación. Una búsqueda posterior permitió comprobar que la lista en memoria y el CSV reflejaban los valores nuevos.

#### 3.6.4 Búsqueda por nombre

> **[Insertar captura de pantalla: búsqueda por nombre]**
>
> *Figura 5. Resultados de una búsqueda parcial por nombre.*

La búsqueda de `argent` devolvió "Argentina" como única coincidencia. La comparación se realizó sin distinguir mayúsculas ni tildes, por lo que también funcionaron entradas como `ARGENTINA` o `mexico`. Cuando no hubo coincidencias, el programa mostró un mensaje informativo en lugar de una lista vacía.

#### 3.6.5 Filtro por continente

> **[Insertar captura de pantalla: filtro por continente]**
>
> *Figura 6. Listado de países filtrado por continente.*

El submenú de filtros muestra los continentes disponibles y permite elegir uno por número. Con el dataset base, el filtro por América devolvió 6 países. La función `filtrar_por_continente()` compara los nombres sin distinguir mayúsculas ni tildes, y `main.normalizar_continente()` evita que se agreguen variantes como "America" y "América" al mismo tiempo.

#### 3.6.6 Filtro por rango de población o superficie

> **[Insertar captura de pantalla: filtro por rango]**
>
> *Figura 7. Filtro por rango de población o de superficie.*

Se probaron dos rangos: población entre 100.000.000 y 200.000.000, que devolvió México, Japón y Egipto; y superficie entre 0 y 400.000 km², que devolvió Uruguay, Alemania, Italia, Japón, Corea del Sur y Nueva Zelanda. También se ingresó un mínimo mayor que el máximo: `pedir_rango()` detectó la inconsistencia y repitió la pregunta sin ejecutar el filtro.

#### 3.6.7 Ordenamiento

> **[Insertar captura de pantalla: ordenamiento]**
>
> *Figura 8. Listado ordenado por el criterio y el sentido seleccionados.*

El ordenamiento por población ascendente ubicó a Uruguay primero y a China último; el orden descendente invirtió los extremos. Se verificaron los tres criterios —nombre, población y superficie— y ambos sentidos. `ordenar_paises()` devolvió una lista nueva y no alteró el orden original del dataset.

#### 3.6.8 Estadísticas

> **[Insertar captura de pantalla: estadísticas]**
>
> *Figura 9. Indicadores estadísticos calculados sobre el dataset.*

Con el dataset base, China resultó el país con mayor población (1.412.000.000) y Uruguay el de menor población (3.426.260). El promedio de población fue 229.983.424,21 habitantes y el de superficie, 2.642.743,79 km². La distribución por continente fue América 6, Asia 4, Europa 4, África 3 y Oceanía 2. Con una lista vacía, el programa mostró un mensaje informativo y no intentó formatear valores inexistentes.

#### 3.6.9 Manejo de errores

> **[Insertar captura de pantalla: entrada inválida]**
>
> *Figura 10. Mensaje de error ante una entrada inválida sin interrumpir el menú.*

Se ingresaron letras (`abc`) y un número fuera de rango (`9`) en el menú principal. En ambos casos el programa mostró "Error: opción inválida" y volvió a preguntar; la opción `7` permitió salir normalmente. También se probaron archivos CSV con columnas incorrectas, población no numérica, campos vacíos y archivo inexistente: `leer_paises()` devolvió una lista vacía y mostró el error sin finalizar el programa.

### 3.7 Trazabilidad de requisitos

La siguiente matriz permite verificar que cada requisito de la consigna fue implementado y probado. Las referencias a figuras se completan cuando se incorporan las capturas de pantalla al PDF final.

| Requisito de la consigna | Implementación | Evidencia |
|---|---|---|
| Agregar un país sin campos vacíos | `validaciones.pedir_texto_no_vacio()`, `pedir_entero_positivo()` y `datos.agregar_pais()` | Casos 1 a 3; Figura 3 |
| Actualizar población y superficie | `datos.actualizar_pais()` y búsqueda exacta previa | Casos 4 y 5; Figura 4 |
| Buscar por nombre (parcial o exacta) | `consultas.buscar_por_nombre()` con `exacta=False` o `True` | Casos 6 y 7; Figura 5 |
| Filtrar por continente | `consultas.filtrar_por_continente()` y `obtener_continentes()` | Caso 8; Figura 6 |
| Filtrar por rango de población | `consultas.filtrar_por_poblacion()` y `validaciones.pedir_rango()` | Caso 9; Figura 7 |
| Filtrar por rango de superficie | `consultas.filtrar_por_superficie()` y `validaciones.pedir_rango()` | Caso 10; Figura 7 |
| Ordenar por nombre, población y superficie | `ordenar.ordenar_paises()` con los tres criterios | Casos 11 y 12; Figura 8 |
| Ordenar en forma ascendente y descendente | Parámetro `ascendente=True/False` | Casos 11 y 12; Figura 8 |
| Mostrar estadísticas | `estadisticas.calcular_estadisticas()` y presentación en `main.py` | Casos 13 y 14; Figura 9 |
| Controlar errores de formato del CSV | `datos.leer_paises()` con `try-except`, validación de columnas y valores | Caso 16 |
| Evitar fallos ante entradas inválidas | `validaciones.py`, `pedir_opcion_menu()` y `try-except` en `main()` | Caso 15; Figura 10 |
| Mensajes claros de éxito y error | Prefijos `[OK]`, `[ERROR]` y mensajes explicativos | Figuras 2 a 10 |
| README con descripción y enlaces | `README.md` del repositorio | Enlace de la sección 5.1 |
| Informe PDF con carátula, índice y bibliografía | Este documento | Sección 6 y anexos |
| Video demostrativo público | Video de 10 a 15 minutos | Enlace de la sección 5.2 |

### 3.8 Limitaciones y mejoras futuras

El desarrollo actual cumple los requisitos de la consigna, pero presenta limitaciones propias de una aplicación de consola con persistencia en un único archivo CSV. No existe concurrencia ni control de usuarios; si dos personas editaran el mismo archivo al mismo tiempo, la última escritura prevalecería. La validación de continentes es textual y solo unifica variantes cuando el nombre coincide sin tildes con uno existente. Tampoco se incluyen pruebas automatizadas dentro del repositorio: las pruebas fueron manuales y se ejecutaron sobre una copia del dataset. La interfaz depende de la codificación de la consola, aunque se mitigó con UTF-8 y `chcp 65001` en Windows. Por último, no hay interfaz gráfica, exportación de reportes ni respaldo automático del CSV.

**Mejoras posibles:**

- Incorporar una interfaz gráfica o web que reutilice las funciones de consulta, ordenamiento y estadísticas.
- Migrar la persistencia a SQLite u otra base de datos para soportar más registros y consultas concurrentes.
- Agregar pruebas automatizadas con `unittest` o `pytest`, incluyendo casos límite y archivos CSV inválidos.
- Incorporar más indicadores estadísticos y gráficos (distribución, medianas, densidades, comparaciones).
- Implementar exportación de reportes a PDF o CSV y un respaldo automático antes de cada escritura.
- Agregar un listado numerado de continentes en el alta para evitar errores de tipeo y unificar aún más los datos.

<div style="page-break-after: always;"></div>

## 4. Dificultades y Conclusiones

### 4.1 Dificultades técnicas

La integración fue la dificultad principal del trabajo. Los módulos se desarrollaron en paralelo y las primeras versiones de `main.py` suponían nombres y firmas que no coincidían con las funciones finalmente entregadas. Por ejemplo, se esperaba `buscar_pais()` y `filtrar_paises()`, pero `consultas.py` expuso `buscar_por_nombre()`, `filtrar_por_continente()`, `filtrar_por_poblacion()` y `filtrar_por_superficie()`. También se esperaba `pedir_entero()` y `pedir_cadena()`, mientras que `validaciones.py` entregó `pedir_entero_positivo()`, `pedir_texto_no_vacio()`, `pedir_rango()` y `pedir_opcion_menu()`. Fue necesario releer las firmas reales, documentar el contrato de integración y adaptar las llamadas antes de probar el programa completo.

| Dificultad | Impacto en el proyecto | Solución adoptada | Aprendizaje |
|---|---|---|---|
| Integración de módulos con interfaces distintas | Las primeras llamadas de `main.py` no coincidían con las funciones entregadas y el programa no podía ejecutarse | Se documentó el contrato al inicio de `main.py`, se ajustaron imports y llamadas, y se probó cada operación con el CSV real | Definir las interfaces antes de programar y revisar las firmas al integrar |
| Manejo de acentos y codificación del CSV | Los nombres con tildes se mostraban mal y podían aparecer continentes duplicados como "América" y "America" | `datos.py` leyó con `utf-8-sig`; `main.py` configuró UTF-8 y `chcp 65001`; `consultas.normalizar()` comparó sin tildes; se unificaron los continentes existentes | La codificación es parte del contrato de datos y debe probarse en cada sistema operativo |
| Validación de entradas sin romper el menú | Letras en campos numéricos, valores negativos, campos vacíos y opciones fuera de rango podían finalizar el programa | Se centralizaron las validaciones en `validaciones.py` y se agregó un `try-except` externo en `main()` para errores inesperados | Validar en el límite de entrada y mantener la lógica del dominio libre de preguntas |
| Coordinación de cambios en GitHub | Los módulos se subieron en momentos distintos y una actualización de `datos.py` cambió la normalización de continentes | Se hizo `pull` antes de integrar, se revisaron los diffs y se volvieron a ejecutar las pruebas después de cada cambio | Versionar en commits pequeños y comunicar los cambios de interfaz |
| Pruebas de casos límite | Los casos felices funcionaban, pero los rangos invertidos, los países inexistentes y los CSV inválidos no estaban cubiertos | Se armó una tabla de casos, se probaron entradas inválidas y se usó una copia del CSV para las pruebas destructivas | Probar los bordes y los errores, no solo el camino exitoso |
| Organización del tiempo para la entrega | La integración quedó para el final y concentró varios ajustes en pocos días | Se priorizaron los flujos principales, se documentó el contrato y se ejecutó una lista de verificación antes del cierre | Integrar temprano y reservar tiempo para pruebas y documentación |

### 4.2 Dificultades de organización del equipo

El equipo trabajó de forma distribuida y con responsabilidades separadas por módulo. La principal dificultad no fue la falta de tareas, sino la coordinación de los momentos de entrega: cada integrante avanzaba a su ritmo y las interfaces de los módulos debían coincidir para que `main.py` pudiera integrarlos. Al principio se dieron por supuestos nombres de funciones y formatos de retorno que no estaban acordados; eso obligó a revisar el código real y a reconstruir el contrato de integración.

También fue necesario acordar criterios que no estaban explícitos en la consigna: cómo normalizar los continentes, qué hacer ante un país duplicado con otra tilde, cómo mostrar los promedios y qué mensaje usar cuando una búsqueda no devuelve resultados. La comunicación por mensajería y el repositorio de GitHub permitieron compartir avances, pero no reemplazaron la revisión del código: fue necesario leer los archivos, ejecutar pruebas y detectar diferencias entre lo documentado y lo implementado.

La experiencia dejó una enseñanza clara: en un trabajo modular, la organización del equipo es tan importante como el código. Sin una definición temprana de interfaces, mensajes y criterios de datos, cada módulo puede funcionar por separado y fallar al integrarse. La figura del integrador ayudó a centralizar esa revisión, pero el acuerdo del grupo fue lo que permitió cerrar el trabajo.

### 4.3 Estrategias de resolución

Para resolver los problemas de integración se adoptaron varias estrategias:

- **Definición temprana del contrato:** se documentaron al inicio de `main.py` las funciones, los parámetros y los valores de retorno de cada módulo. Esa lista se contrastó con el código real antes de probar.
- **Integración incremental:** se probó primero la carga del CSV, luego cada operación por separado y finalmente el flujo completo desde el menú. Así fue más fácil identificar si el error estaba en un módulo o en la conexión entre módulos.
- **Pruebas con datos reales y con una copia:** las pruebas de lectura, búsqueda, filtros, ordenamiento y estadísticas se hicieron con `paises.csv`. Las pruebas de alta y actualización se hicieron sobre una copia y luego se restauró el archivo original para no alterar el dataset entregado.
- **Revisión cruzada:** cada integrante explicó las funciones de su módulo y el integrador verificó que las llamadas coincidieran con las firmas. Las diferencias se corrigieron antes de la entrega.
- **Acuerdos de estilo:** se usaron nombres de funciones en español, docstrings, mensajes uniformes y una estructura de diccionario común para todos los países.
- **Documentación compartida:** el informe, el `README.md` y los comentarios de integración de `main.py` funcionaron como referencia para el resto del equipo.
- **Lista de verificación:** antes del cierre se comprobó la carga, el alta, la actualización, la búsqueda, los tres filtros, los tres criterios de ordenamiento, las estadísticas, las entradas inválidas y la salida.

### 4.4 Conclusiones grupales

La modularización fue el aprendizaje más valioso del trabajo. Dividir el sistema en archivos con responsabilidades claras permitió que cada integrante se concentrara en un problema acotado y que las funciones pudieran probarse por separado. Sin embargo, también mostró que la modularización no termina en separar archivos: es necesario definir interfaces, formatos de datos y mensajes. La integración de `main.py` con los módulos reales exigió releer firmas y ajustar llamadas, y eso confirmó que un contrato claro ahorra tiempo y evita errores.

La validación de datos tuvo un impacto directo en la estabilidad del programa. Al centralizar las preguntas en `validaciones.py`, las letras, los valores negativos, los campos vacíos y los rangos invertidos dejaron de ser una amenaza para el menú. El usuario puede equivocarse y el programa continúa; además, los módulos de lógica reciben datos con el formato esperado. Esa separación entre validación, cálculo y presentación fue una de las decisiones que más mejoró la calidad del resultado.

El trabajo con archivos CSV y estructuras de datos permitió aplicar listas, diccionarios, funciones, condicionales, bucles, excepciones y ordenamientos en un problema concreto. Leer el archivo una vez, mantener la lista en memoria y guardar los cambios después de cada alta o actualización fue una solución simple y coherente con el alcance. También aparecieron problemas reales de datos —tildes, mayúsculas, continentes repetidos, nombres duplicados— que no se resuelven solo con sintaxis: requieren criterios y pruebas.

La organización del equipo tuvo aciertos y aspectos por mejorar. Los aciertos fueron la división de tareas, el uso de GitHub y la revisión conjunta. Los aspectos por mejorar fueron la definición temprana de interfaces, la integración continua y la comunicación de cambios que afectan a otros módulos. En una próxima entrega convendría acordar el contrato antes de programar, integrar todas las semanas y mantener una lista de pruebas compartida.

La valoración general es positiva. El sistema cumple los requisitos de la consigna, funciona con el dataset entregado y responde de forma controlada ante errores. El grupo aprendió que un programa no es solo un conjunto de funciones que funcionan por separado, sino un sistema donde los datos, las interfaces y los mensajes deben ser coherentes. Esa enseñanza es aplicable a cualquier proyecto futuro, incluso si se cambia la consola por una interfaz gráfica o el CSV por una base de datos.

### 4.5 Aprendizajes individuales

| Integrante | Aprendizajes principales | Aporte central al proyecto |
|---|---|---|
| Facundo Piriz | Lectura y escritura de CSV con `csv.DictReader` y `csv.DictWriter`; manejo de `utf-8-sig`; validación de columnas, filas incompletas y valores positivos; diferencia entre modificar la lista y persistir el archivo | `datos.py`, `paises.csv` y la documentación teórica sobre listas, diccionarios y archivos CSV |
| Francisco Ruiz | Búsqueda y filtrado con normalización de tildes y mayúsculas; diseño de funciones de validación reutilizables; uso de `while`, condicionales y `try-except` para entradas inválidas | `consultas.py`, `validaciones.py` y el diagrama de flujo de las operaciones principales |
| Agustín Tromba | Implementación de ordenamiento por inserción ascendente y descendente; cálculo de extremos, promedios y conteos; organización del repositorio y del `README.md` | `ordenar.py`, `estadisticas.py` y la documentación sobre ordenamientos y estadísticas |
| Fausto Rivero | Integración de módulos con interfaces reales; diseño de menús y submenús; manejo de excepciones; limpieza de consola multiplataforma; formato de números y armado del informe | `main.py`, la integración general, el informe final y la coordinación del video |

### 4.6 Reflexión final

El trabajo permitió comprobar que programar es también acordar. Las funciones pueden ser correctas por separado, pero el sistema solo funciona cuando los datos, las interfaces y los mensajes son coherentes. La experiencia de integrar módulos ajenos, detectar diferencias de nombres y adaptar `main.py` fue especialmente formativa: obligó a leer código, a documentar y a probar antes de dar por terminada una tarea.

Como proyección, el grupo queda con una base sólida para seguir aprendiendo. La aplicación puede crecer hacia una interfaz gráfica, una base de datos o pruebas automatizadas, pero los principios seguirán siendo los mismos: separar responsabilidades, validar en los límites, manejar los errores y documentar las decisiones. El resultado final no es solo un programa que funciona: es una experiencia de trabajo colaborativo que dejó aprendizajes aplicables a próximos proyectos.

<div style="page-break-after: always;"></div>

## 5. Enlaces del Proyecto

### 5.1 Repositorio de GitHub

**URL:** https://github.com/aqussti/tpi-programacion-i-utn

El repositorio contiene el código fuente completo, el archivo `paises.csv`, el `README.md` y la fuente editable del informe. La rama principal es `main` y el acceso es público. Para ejecutar el programa, se debe clonar el repositorio, ingresar a la carpeta `tpi-programacion-i-utn` y ejecutar `python main.py` con Python 3.8 o superior. No se requieren librerías externas.

La estructura del repositorio coincide con la arquitectura descripta en la sección 3.1. El informe final en PDF se incorpora en la raíz del repositorio una vez exportado desde `Informe_TPI.md`.

### 5.2 Video demostrativo

**URL:** [PEGAR AQUÍ EL ENLACE PÚBLICO DE YOUTUBE]

El video debe tener entre 10 y 15 minutos, mostrar el sistema en funcionamiento y explicar la estructura de datos utilizada. Se sugiere la siguiente distribución: presentación del problema y de los objetivos (2 minutos), explicación de la lista de diccionarios y del archivo CSV (2 minutos), demostración de alta, actualización, búsqueda, filtros, ordenamiento y estadísticas (6 a 8 minutos), casos de error y validaciones (2 minutos) y cierre con conclusiones (1 a 2 minutos). La participación debe ser equitativa entre los cuatro integrantes. La configuración de privacidad debe ser "Público"; la opción "No listado" no cumple con el requisito de acceso público.

**Checklist del video:**

- [ ] Duración entre 10 y 15 minutos.
- [ ] Permisos de visualización públicos.
- [ ] Presentación del problema y de los objetivos.
- [ ] Explicación de la estructura de datos (lista de diccionarios).
- [ ] Demostración de todas las funcionalidades.
- [ ] Demostración de casos de error y validaciones.
- [ ] Participación equitativa de los cuatro integrantes.
- [ ] Cierre con conclusiones y aprendizajes.

### 5.3 Documento PDF

**URL / ubicación:** [PEGAR AQUÍ EL ENLACE AL PDF O INDICAR QUE SE ENCUENTRA EN LA RAÍZ DEL REPOSITORIO]

Una vez exportado, el informe se ubicará en la raíz del repositorio como `Informe_TPI.pdf`. La URL prevista es:

`https://github.com/aqussti/tpi-programacion-i-utn/blob/main/Informe_TPI.pdf`

Antes de la entrega se debe verificar que el archivo esté subido, que el enlace sea accesible sin iniciar sesión y que la versión del PDF coincida con la última versión del código.

### 5.4 Verificación de enlaces

| Recurso | URL | Estado |
|---|---|---|
| Repositorio GitHub | https://github.com/aqussti/tpi-programacion-i-utn | Verificado (repositorio público, rama `main`) |
| Video YouTube | [Pegar enlace] | Pendiente de publicación |
| Informe PDF | [Pegar enlace] | Pendiente de exportación y carga |

<div style="page-break-after: always;"></div>

## 6. Bibliografía y Webgrafía

Las referencias se ordenaron alfabéticamente y se utilizó un estilo uniforme basado en APA 7.ª edición. Se incluyen las obras y los recursos consultados para el desarrollo del sistema y para la redacción del marco teórico.

### 6.1 Bibliografía

Cátedra de Programación 1. (2026). *Consigna del Trabajo Práctico Integrador: Gestión de Datos de Países en Python*. Universidad Tecnológica Nacional.

Downey, A. B. (2015). *Think Python: How to Think Like a Computer Scientist* (2.ª ed.). O'Reilly Media.

Lutz, M. (2013). *Learning Python* (5.ª ed.). O'Reilly Media.

Matthes, E. (2023). *Python Crash Course: A Hands-On, Project-Based Introduction to Programming* (3.ª ed.). No Starch Press.

Sweigart, A. (2019). *Automate the Boring Stuff with Python: Practical Programming for Total Beginners* (2.ª ed.). No Starch Press.

Van Rossum, G., Warsaw, B., & Coghlan, A. (2001). *PEP 8 – Style Guide for Python Code*. Python Software Foundation. https://peps.python.org/pep-0008/

### 6.2 Webgrafía

Python Software Foundation. (s. f.). *The Python Tutorial*. Recuperado el 15 de noviembre de 2026, de https://docs.python.org/es/3/tutorial/

Python Software Foundation. (s. f.). *Data Structures*. Recuperado el 15 de noviembre de 2026, de https://docs.python.org/es/3/tutorial/datastructures.html

Python Software Foundation. (s. f.). *Defining Functions*. Recuperado el 15 de noviembre de 2026, de https://docs.python.org/es/3/tutorial/controlflow.html#defining-functions

Python Software Foundation. (s. f.). *csv — CSV File Reading and Writing*. Recuperado el 15 de noviembre de 2026, de https://docs.python.org/es/3/library/csv.html

Python Software Foundation. (s. f.). *Sorting Techniques*. Recuperado el 15 de noviembre de 2026, de https://docs.python.org/es/3/howto/sorting.html

Python Software Foundation. (s. f.). *statistics — Mathematical statistics functions*. Recuperado el 15 de noviembre de 2026, de https://docs.python.org/es/3/library/statistics.html

Python Software Foundation. (s. f.). *Errors and Exceptions*. Recuperado el 15 de noviembre de 2026, de https://docs.python.org/es/3/tutorial/errors.html

Python Software Foundation. (s. f.). *os — Miscellaneous operating system interfaces*. Recuperado el 15 de noviembre de 2026, de https://docs.python.org/es/3/library/os.html

Python Software Foundation. (s. f.). *unicodedata — Unicode Database*. Recuperado el 15 de noviembre de 2026, de https://docs.python.org/es/3/library/unicodedata.html

Python Software Foundation. (s. f.). *pathlib — Object-oriented filesystem paths*. Recuperado el 15 de noviembre de 2026, de https://docs.python.org/es/3/library/pathlib.html

### 6.3 Nota sobre el uso de fuentes

Las fuentes se utilizaron con fines académicos. El código fue desarrollado por los integrantes del equipo y se apoyó en la documentación oficial de Python para el uso de `csv`, `pathlib`, `unicodedata`, `os` y las estructuras de datos. No se copiaron fragmentos de código de terceros sin indicar la fuente. Las citas del marco teórico remiten a las obras y a los recursos enumerados en este apartado.

<div style="page-break-after: always;"></div>

## Anexos

### Anexo A. Instructivo de instalación y ejecución

**Requisitos previos**

- Python 3.8 o superior.
- No se requieren librerías externas: se utiliza únicamente la biblioteca estándar.

**Pasos para ejecutar**

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/aqussti/tpi-programacion-i-utn.git
   ```
2. Ingresar a la carpeta del proyecto:
   ```bash
   cd tpi-programacion-i-utn
   ```
3. Ejecutar el programa:
   ```bash
   python main.py
   ```
   En Linux o macOS puede ser necesario usar `python3 main.py`.

**Formato del archivo `paises.csv`**

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
Brasil,213993437,8515767,América
Alemania,83149300,357022,Europa
```

El archivo `paises.csv` debe estar en la misma carpeta que `main.py` y `datos.py`, porque `datos.py` lo busca con `Path(__file__).with_name("paises.csv")`. La primera fila contiene los encabezados exactos `nombre,poblacion,superficie,continente`; no se deben agregar columnas ni cambiar sus nombres. Los valores de población y superficie deben ser enteros positivos y el continente no puede estar vacío. Se recomienda guardar el archivo en UTF-8 para conservar tildes y `ñ`.

**Solución de problemas frecuentes**

- Si los acentos se ven incorrectos en Windows, verificar que la consola use UTF-8; el programa ejecuta `chcp 65001` al iniciar.
- Si el programa informa que no encontró el CSV, confirmar que `paises.csv` esté en la misma carpeta que `datos.py`.
- Si el CSV tiene columnas incorrectas o valores vacíos, `leer_paises()` mostrará el error y devolverá una lista vacía; corregir el archivo y volver a ejecutar.

### Anexo B. Participación de los integrantes

| Integrante | Rol principal | Módulos / tareas | Documentación | Video |
|---|---|---|---|---|
| Facundo Piriz | Datos y gestión | `datos.py`, `paises.csv` | Listas, diccionarios y archivos CSV | Demostración de carga, alta, actualización y persistencia |
| Francisco Ruiz | Consultas y validaciones | `consultas.py`, `validaciones.py` | Condicionales, funciones y diagrama de flujo | Demostración de búsqueda, filtros y validaciones |
| Agustín Tromba | Ordenamiento y estadísticas | `ordenar.py`, `estadisticas.py`, repositorio | Ordenamientos y estadísticas básicas | Demostración de ordenamientos y estadísticas |
| Fausto Rivero | Integración y cierre | `main.py`, informe y video | Introducción, arquitectura y conclusiones | Apertura, integración, cierre y armado del ZIP |

### Anexo C. Glosario

| Término | Definición |
|---|---|
| Lista | Colección ordenada y mutable de elementos. |
| Diccionario | Estructura que almacena pares clave-valor. |
| Función | Bloque de código reutilizable que recibe datos y devuelve un resultado. |
| Parámetro | Variable declarada en la definición de una función. |
| Argumento | Valor concreto que se pasa a una función al llamarla. |
| CSV | Formato de texto plano con valores separados por comas. |
| Iteración | Repetición de un bloque de código mediante un bucle. |
| Excepción | Error detectado durante la ejecución que puede capturarse con try-except. |
| Ordenamiento | Organización de los elementos según un criterio. |
| Promedio | Suma de los valores dividida por la cantidad de elementos. |
| Normalización | Proceso de unificar mayúsculas, minúsculas y tildes para comparar textos. |
| UTF-8 | Codificación de caracteres que representa tildes, `ñ` y otros símbolos. |
| Persistencia | Conservación de los datos en un archivo para que estén disponibles entre ejecuciones. |
| Acoplamiento | Grado de dependencia entre módulos; un bajo acoplamiento facilita los cambios. |

---

**Fin del documento.**
