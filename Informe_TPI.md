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

[Texto aquí: explicar la decisión de dividir la aplicación en módulos con responsabilidades bien definidas. Mencionar las ventajas: legibilidad, mantenimiento, pruebas independientes, trabajo paralelo del equipo y bajo acoplamiento. Indicar que main.py actúa como integrador y que los módulos de lógica no se encargan de la presentación por consola.]

```text
tpi-programacion-i-utn/
├── main.py              # Punto de entrada, menú e integración
├── datos.py             # Lectura/escritura del CSV, alta y actualización
├── consultas.py         # Búsqueda y filtros
├── validaciones.py      # Validación de entradas del usuario
├── ordenar.py           # Ordenamiento por nombre, población y superficie
├── estadisticas.py      # Cálculo de indicadores
├── paises.csv           # Dataset base
├── Informe_TPI.pdf      # Documento académico final
├── Informe_TPI.md       # Fuente editable del informe
└── README.md            # Documentación del repositorio
```

| Archivo | Responsabilidad | Funciones principales | Integrante |
|---|---|---|---|
| `main.py` | Punto de entrada, menú, navegación, mensajes y unión de los módulos | `main()`, `mostrar_menu()`, `ejecutar_opcion()` | Fausto Rivero |
| `datos.py` | Lectura y escritura del CSV; alta y actualización de países | `leer_paises()`, `guardar_paises()`, `agregar_pais()`, `actualizar_pais()` | Facundo Piriz |
| `consultas.py` | Búsqueda por nombre y filtros por continente y rangos | `buscar_pais()`, `filtrar_paises()` | Francisco Ruiz |
| `validaciones.py` | Validación transversal de entradas y opciones de menú | `pedir_entero()`, `pedir_cadena()`, `validar_opcion()` | Francisco Ruiz |
| `ordenar.py` | Ordenamiento ascendente y descendente por tres criterios | `ordenar_paises()` | Agustín Tromba |
| `estadisticas.py` | Cálculo de extremos, promedios y conteos por continente | `calcular_estadisticas()` | Agustín Tromba |
| `paises.csv` | Dataset persistente con los registros de países | — | Facundo Piriz |

### 3.2 Modelo de datos del dominio

[Texto aquí: explicar que cada país se representa mediante un diccionario y que el conjunto de países se almacena en una lista. Justificar por qué esta estructura facilita el recorrido, la búsqueda, el filtrado y el ordenamiento.]

| Campo | Tipo de dato | Descripción | Validación aplicada |
|---|---|---|---|
| `nombre` | `str` | Nombre del país | No vacío; sin duplicados |
| `poblacion` | `int` | Cantidad de habitantes | Entero positivo |
| `superficie` | `int` | Superficie en km² | Entero positivo |
| `continente` | `str` | Continente al que pertenece | No vacío |

**Ejemplo de registro:**

```python
{
    "nombre": "Argentina",
    "poblacion": 45376763,
    "superficie": 2780400,
    "continente": "América",
}
```

### 3.3 Flujo principal del sistema

[Texto aquí: describir el flujo general. El programa inicia, carga el CSV, valida los datos, muestra el menú principal y espera una opción. Según la opción elegida, ejecuta la operación correspondiente, muestra el resultado, realiza una pausa y vuelve al menú. El ciclo termina cuando el usuario selecciona la opción Salir.]

> **[Insertar aquí el diagrama de flujo de las operaciones principales]**
>
> *Figura 1. Flujo general del sistema: carga del CSV, menú, operaciones y persistencia.*
>
> Sugerencia para el diagrama: incluir un rombo de decisión para "¿Opción válida?", otro para "¿País encontrado?" y una rama de error que regrese al menú sin finalizar el programa.

**Flujo resumido:**

1. Inicio.
2. Cargar `paises.csv` y construir la lista de diccionarios.
3. Mostrar el menú principal.
4. Leer y validar la opción ingresada.
5. Ejecutar la operación seleccionada (agregar, actualizar, buscar, filtrar, ordenar o estadísticas).
6. Mostrar el resultado y pausar.
7. Volver al paso 3 mientras la opción no sea Salir.
8. Guardar los cambios cuando corresponda y finalizar.

### 3.4 Decisiones de diseño

[Texto aquí: desarrollar cada decisión y justificarla. Se sugieren los siguientes ejes:]

- **Lista de diccionarios:** [Texto aquí: justificar frente a listas paralelas, tuplas u objetos.]
- **Persistencia en CSV:** [Texto aquí: justificar frente a JSON, base de datos o archivo de texto plano.]
- **Separación entre lógica y presentación:** [Texto aquí: los módulos calculan y devuelven datos; main.py muestra y pide entradas.]
- **Validaciones centralizadas:** [Texto aquí: reutilización de funciones y mensajes uniformes.]
- **Retorno booleano en altas y actualizaciones:** [Texto aquí: permite que el menú informe éxito o error sin duplicar la lógica.]
- **Codificación UTF-8:** [Texto aquí: asegurar acentos y caracteres especiales en el CSV y en la consola.]
- **Limpieza de consola multiplataforma:** [Texto aquí: uso de `cls` en Windows y `clear` en Linux/macOS.]
- **Manejo de errores con try-except:** [Texto aquí: evitar que una entrada inválida finalice el programa.]
- **Ordenamiento sobre una copia:** [Texto aquí: preservar el orden original de la lista en memoria.]

### 3.5 Interfaz de consola y experiencia de usuario

[Texto aquí: describir el menú principal, los submenús de filtros y ordenamiento, el formato de los mensajes, la separación visual con líneas, la pausa con Enter y el formateo de números con separadores de miles. Explicar cómo se guía al usuario ante un error y cómo se evita que la pantalla quede saturada.]

| Elemento | Decisión adoptada | Beneficio |
|---|---|---|
| Menú principal | [Texto aquí] | [Texto aquí] |
| Submenús | [Texto aquí] | [Texto aquí] |
| Mensajes de éxito | [Texto aquí] | [Texto aquí] |
| Mensajes de error | [Texto aquí] | [Texto aquí] |
| Pausas | [Texto aquí] | [Texto aquí] |
| Limpieza de pantalla | [Texto aquí] | [Texto aquí] |
| Formato numérico | [Texto aquí] | [Texto aquí] |

<div style="page-break-after: always;"></div>

### 3.6 Pruebas y capturas de ejecución

[Texto aquí: describir el plan de pruebas. Indicar que se utilizó el dataset base de `paises.csv` y que se probaron tanto casos exitosos como entradas inválidas. Mencionar que las pruebas se ejecutaron desde la carpeta raíz del proyecto con `python main.py`.]

**Tabla de casos de prueba**

| N° | Caso de prueba | Entrada | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|---|---|
| 1 | Alta de un país válido | [Nombre, población, superficie y continente] | [El país se agrega y se guarda en el CSV] | [Texto aquí] | [OK / Falló] |
| 2 | Alta con campos vacíos | [Cadena vacía] | [Mensaje de error; no se guarda] | [Texto aquí] | [OK / Falló] |
| 3 | Alta con población negativa | [-100] | [Mensaje de error; no se guarda] | [Texto aquí] | [OK / Falló] |
| 4 | Actualización válida | [País existente y nuevos valores] | [Datos actualizados en el CSV] | [Texto aquí] | [OK / Falló] |
| 5 | Actualización de país inexistente | [Nombre no registrado] | [Mensaje de error; sin cambios] | [Texto aquí] | [OK / Falló] |
| 6 | Búsqueda parcial | [Parte del nombre] | [Lista de coincidencias] | [Texto aquí] | [OK / Falló] |
| 7 | Búsqueda sin resultados | [Nombre inexistente] | [Mensaje informativo] | [Texto aquí] | [OK / Falló] |
| 8 | Filtro por continente | [Continente] | [Países del continente] | [Texto aquí] | [OK / Falló] |
| 9 | Filtro por rango de población | [Mínimo y máximo] | [Países dentro del rango] | [Texto aquí] | [OK / Falló] |
| 10 | Filtro por rango de superficie | [Mínimo y máximo] | [Países dentro del rango] | [Texto aquí] | [OK / Falló] |
| 11 | Ordenamiento ascendente | [Criterio] | [Lista de menor a mayor] | [Texto aquí] | [OK / Falló] |
| 12 | Ordenamiento descendente | [Criterio] | [Lista de mayor a menor] | [Texto aquí] | [OK / Falló] |
| 13 | Estadísticas con datos | [Dataset cargado] | [Extremos, promedios y conteos] | [Texto aquí] | [OK / Falló] |
| 14 | Estadísticas sin datos | [Lista vacía] | [Mensaje informativo] | [Texto aquí] | [OK / Falló] |
| 15 | Opción de menú inválida | [Número fuera de rango o texto] | [Mensaje de error; el menú continúa] | [Texto aquí] | [OK / Falló] |

#### 3.6.1 Menú principal

> **[Insertar captura de pantalla: menú principal]**
>
> *Figura 2. Menú principal del sistema con las siete opciones disponibles.*

[Texto aquí: comentar brevemente qué muestra la captura y cómo se interpreta.]

#### 3.6.2 Alta de un país

> **[Insertar captura de pantalla: alta de país]**
>
> *Figura 3. Ingreso de los datos de un país y confirmación del alta.*

[Texto aquí: indicar los datos utilizados en la prueba y el mensaje obtenido.]

#### 3.6.3 Actualización de datos

> **[Insertar captura de pantalla: actualización de población y superficie]**
>
> *Figura 4. Actualización de los datos de un país existente.*

[Texto aquí: indicar el país actualizado, los valores anteriores y los nuevos.]

#### 3.6.4 Búsqueda por nombre

> **[Insertar captura de pantalla: búsqueda por nombre]**
>
> *Figura 5. Resultados de una búsqueda parcial por nombre.*

[Texto aquí: comentar la coincidencia parcial y el formato de los resultados.]

#### 3.6.5 Filtro por continente

> **[Insertar captura de pantalla: filtro por continente]**
>
> *Figura 6. Listado de países filtrado por continente.*

[Texto aquí: indicar el continente elegido y la cantidad de resultados.]

#### 3.6.6 Filtro por rango de población o superficie

> **[Insertar captura de pantalla: filtro por rango]**
>
> *Figura 7. Filtro por rango de población o de superficie.*

[Texto aquí: indicar los límites utilizados y los países que cumplen la condición.]

#### 3.6.7 Ordenamiento

> **[Insertar captura de pantalla: ordenamiento]**
>
> *Figura 8. Listado ordenado por el criterio y el sentido seleccionados.*

[Texto aquí: comparar el orden obtenido con el esperado.]

#### 3.6.8 Estadísticas

> **[Insertar captura de pantalla: estadísticas]**
>
> *Figura 9. Indicadores estadísticos calculados sobre el dataset.*

[Texto aquí: comentar los extremos, los promedios y la distribución por continente.]

#### 3.6.9 Manejo de errores

> **[Insertar captura de pantalla: entrada inválida]**
>
> *Figura 10. Mensaje de error ante una entrada inválida sin interrumpir el menú.*

[Texto aquí: describir el caso probado y confirmar que el programa continuó funcionando.]

### 3.7 Trazabilidad de requisitos

[Texto aquí: explicar que la siguiente matriz permite verificar que cada requisito de la consigna fue implementado y probado.]

| Requisito de la consigna | Implementación | Evidencia |
|---|---|---|
| Agregar un país sin campos vacíos | [Texto aquí] | [Figura / caso de prueba] |
| Actualizar población y superficie | [Texto aquí] | [Figura / caso de prueba] |
| Buscar por nombre (parcial o exacta) | [Texto aquí] | [Figura / caso de prueba] |
| Filtrar por continente | [Texto aquí] | [Figura / caso de prueba] |
| Filtrar por rango de población | [Texto aquí] | [Figura / caso de prueba] |
| Filtrar por rango de superficie | [Texto aquí] | [Figura / caso de prueba] |
| Ordenar por nombre, población y superficie | [Texto aquí] | [Figura / caso de prueba] |
| Ordenar en forma ascendente y descendente | [Texto aquí] | [Figura / caso de prueba] |
| Mostrar estadísticas | [Texto aquí] | [Figura / caso de prueba] |
| Controlar errores de formato del CSV | [Texto aquí] | [Caso de prueba] |
| Evitar fallos ante entradas inválidas | [Texto aquí] | [Caso de prueba] |
| Mensajes claros de éxito y error | [Texto aquí] | [Figuras] |
| README con descripción y enlaces | [Texto aquí] | [Enlace al repositorio] |
| Informe PDF con carátula, índice y bibliografía | [Texto aquí] | [Este documento] |
| Video demostrativo público | [Texto aquí] | [Enlace al video] |

### 3.8 Limitaciones y mejoras futuras

[Texto aquí: reconocer las limitaciones del desarrollo actual. Se sugieren: aplicación de consola, persistencia en un único archivo CSV, ausencia de concurrencia, dependencia de la codificación del sistema, falta de pruebas automatizadas y ausencia de interfaz gráfica.]

**Mejoras posibles:**

- [Incorporar una interfaz gráfica o web.]
- [Migrar la persistencia a SQLite u otra base de datos.]
- [Agregar pruebas automatizadas con unittest o pytest.]
- [Incorporar más indicadores estadísticos y gráficos.]
- [Implementar exportación de reportes a PDF o CSV.]
- [Agregar autenticación y control de usuarios, si el sistema creciera.]

<div style="page-break-after: always;"></div>

## 4. Dificultades y Conclusiones

### 4.1 Dificultades técnicas

[Texto aquí: introducir las principales dificultades técnicas encontradas durante el desarrollo. No limitarse a enumerarlas: explicar por qué fueron desafiantes y cómo se resolvieron.]

| Dificultad | Impacto en el proyecto | Solución adoptada | Aprendizaje |
|---|---|---|---|
| [Integración de módulos con interfaces distintas] | [Texto aquí] | [Texto aquí] | [Texto aquí] |
| [Manejo de acentos y codificación del CSV] | [Texto aquí] | [Texto aquí] | [Texto aquí] |
| [Validación de entradas sin romper el menú] | [Texto aquí] | [Texto aquí] | [Texto aquí] |
| [Coordinación de cambios en GitHub] | [Texto aquí] | [Texto aquí] | [Texto aquí] |
| [Pruebas de casos límite] | [Texto aquí] | [Texto aquí] | [Texto aquí] |
| [Organización del tiempo para la entrega] | [Texto aquí] | [Texto aquí] | [Texto aquí] |

### 4.2 Dificultades de organización del equipo

[Texto aquí: describir los desafíos de coordinar un equipo de cuatro integrantes con responsabilidades distribuidas. Mencionar horarios, comunicación, definición de contratos entre módulos, revisión de cambios y unificación de criterios.]

### 4.3 Estrategias de resolución

[Texto aquí: explicar las estrategias utilizadas: reuniones de avance, definición temprana de interfaces, ramas de Git, revisión cruzada, pruebas de integración, documentación compartida y acuerdos de estilo de código.]

### 4.4 Conclusiones grupales

[Texto aquí: redactar entre tres y cinco párrafos. Se sugieren los siguientes ejes:]

- [Qué aprendió el grupo sobre la modularización y la importancia de definir interfaces claras.]
- [Cómo influyó la validación de datos en la estabilidad del programa.]
- [Qué aportó el trabajo con archivos CSV y estructuras de datos.]
- [Cómo se organizó el equipo y qué se podría mejorar en una próxima entrega.]
- [Valoración general del resultado y de los aprendizajes alcanzados.]

### 4.5 Aprendizajes individuales

| Integrante | Aprendizajes principales | Aporte central al proyecto |
|---|---|---|
| Facundo Piriz | [Texto aquí] | [Datos, CSV y documentación teórica] |
| Francisco Ruiz | [Texto aquí] | [Consultas, validaciones y diagrama de flujo] |
| Agustín Tromba | [Texto aquí] | [Ordenamientos, estadísticas y repositorio] |
| Fausto Rivero | [Texto aquí] | [Integración, menú, informe final y video] |

### 4.6 Reflexión final

[Texto aquí: cerrar el apartado con una reflexión grupal sobre el proceso de aprendizaje, el valor del trabajo colaborativo y la proyección de los conocimientos adquiridos.]

<div style="page-break-after: always;"></div>

## 5. Enlaces del Proyecto

### 5.1 Repositorio de GitHub

**URL:** https://github.com/aqussti/tpi-programacion-i-utn

[Texto aquí: indicar que el repositorio contiene el código fuente completo, el archivo `paises.csv`, el `README.md` y el informe en PDF. Verificar que el acceso sea público y que la rama principal sea `main`.]

### 5.2 Video demostrativo

**URL:** [Pegar aquí el enlace público de YouTube]

[Texto aquí: indicar la duración del video, los temas abordados y la participación de cada integrante. El video debe tener entre 10 y 15 minutos, mostrar el sistema en funcionamiento y explicar la estructura de datos utilizada. La configuración de privacidad debe ser "Público"; la opción "No listado" no cumple con el requisito de acceso público.]

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

**URL / ubicación:** [Enlace al PDF o indicar que se encuentra en la raíz del repositorio]

[Texto aquí: indicar si el PDF está subido al repositorio o enlazado desde el README. Verificar que el enlace sea accesible sin iniciar sesión.]

### 5.4 Verificación de enlaces

| Recurso | URL | Estado |
|---|---|---|
| Repositorio GitHub | https://github.com/aqussti/tpi-programacion-i-utn | [Verificado / Pendiente] |
| Video YouTube | [Pegar enlace] | [Verificado / Pendiente] |
| Informe PDF | [Pegar enlace] | [Verificado / Pendiente] |

<div style="page-break-after: always;"></div>

## 6. Bibliografía y Webgrafía

[Texto aquí: ordenar las referencias alfabéticamente y utilizar un estilo uniforme, preferentemente APA 7.ª edición. Agregar las fuentes consultadas por cada integrante y verificar que todas las citas del marco teórico tengan su referencia correspondiente.]

### 6.1 Bibliografía

Las siguientes obras se incluyen como apoyo bibliográfico: conservar únicamente las que hayan sido efectivamente consultadas por el equipo.

Cátedra de Programación 1. ([Año]). *Consigna del Trabajo Práctico Integrador: Gestión de Datos de Países en Python*. Universidad Tecnológica Nacional.

Downey, A. B. (2015). *Think Python: How to Think Like a Computer Scientist* (2.ª ed.). O'Reilly Media.

Lutz, M. (2013). *Learning Python* (5.ª ed.). O'Reilly Media.

Matthes, E. (2023). *Python Crash Course: A Hands-On, Project-Based Introduction to Programming* (3.ª ed.). No Starch Press.

Sweigart, A. (2019). *Automate the Boring Stuff with Python: Practical Programming for Total Beginners* (2.ª ed.). No Starch Press.

[Agregar aquí otros libros, apuntes de cátedra o materiales utilizados por el equipo.]

### 6.2 Webgrafía

Python Software Foundation. (s. f.). *The Python Tutorial*. Recuperado el [Fecha de consulta], de https://docs.python.org/es/3/tutorial/

Python Software Foundation. (s. f.). *Data Structures*. Recuperado el [Fecha de consulta], de https://docs.python.org/es/3/tutorial/datastructures.html

Python Software Foundation. (s. f.). *Defining Functions*. Recuperado el [Fecha de consulta], de https://docs.python.org/es/3/tutorial/controlflow.html#defining-functions

Python Software Foundation. (s. f.). *csv — CSV File Reading and Writing*. Recuperado el [Fecha de consulta], de https://docs.python.org/es/3/library/csv.html

Python Software Foundation. (s. f.). *Sorting Techniques*. Recuperado el [Fecha de consulta], de https://docs.python.org/es/3/howto/sorting.html

Python Software Foundation. (s. f.). *statistics — Mathematical statistics functions*. Recuperado el [Fecha de consulta], de https://docs.python.org/es/3/library/statistics.html

Python Software Foundation. (s. f.). *Errors and Exceptions*. Recuperado el [Fecha de consulta], de https://docs.python.org/es/3/tutorial/errors.html

Python Software Foundation. (s. f.). *os — Miscellaneous operating system interfaces*. Recuperado el [Fecha de consulta], de https://docs.python.org/es/3/library/os.html

[Agregar aquí las demás fuentes web consultadas, incluyendo tutoriales, artículos o documentación complementaria.]

### 6.3 Nota sobre el uso de fuentes

[Texto aquí: aclarar que las fuentes fueron utilizadas con fines académicos y que el código fue desarrollado por el equipo. Si se utilizaron fragmentos de código o ideas de terceros, indicar la fuente correspondiente.]

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

[Texto aquí: indicar que el archivo debe estar en la misma carpeta que `main.py`, que la primera fila contiene los encabezados y que los valores de población y superficie deben ser enteros positivos.]

### Anexo B. Participación de los integrantes

| Integrante | Rol principal | Módulos / tareas | Documentación | Video |
|---|---|---|---|---|
| Facundo Piriz | [Datos y gestión] | [datos.py, paises.csv] | [Listas, diccionarios y CSV] | [Participación] |
| Francisco Ruiz | [Consultas y validaciones] | [consultas.py, validaciones.py] | [Condicionales, funciones y diagrama] | [Participación] |
| Agustín Tromba | [Ordenamiento y estadísticas] | [ordenar.py, estadisticas.py] | [Ordenamientos y estadísticas] | [Participación] |
| Fausto Rivero | [Integración y cierre] | [main.py, informe y video] | [Introducción, arquitectura y conclusiones] | [Participación] |

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

---

**Fin del documento.**





