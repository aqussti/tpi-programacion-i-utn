# 🌍 Gestión de Datos de Países en Python

**Trabajo Práctico Integrador (TPI) – Programación 1**  
**Institución:** Universidad Tecnológica Nacional (UTN)  
**Carrera:** Tecnicatura Universitaria en Programación a Distancia  

---

## 📋 Descripción del Programa

Este proyecto consiste en una aplicación de consola desarrollada en **Python 3.x** que permite gestionar, consultar y analizar información demográfica y geográfica de distintos países a partir de un archivo de datos en formato **CSV**.

El sistema implementa estructuras de datos fundamentales (listas y diccionarios), modularización por responsabilidades, validaciones robustas de entrada, manejo de excepciones en la lectura/escritura de archivos, algoritmos de ordenamiento y cálculo de indicadores estadísticos clave.

---

## 📁 Estructura del Proyecto

El código fuente está organizado de manera modular, asignando una responsabilidad clara a cada archivo:

```text
├── main.py              # Punto de entrada, menú interactivo y bucle principal
├── datos.py             # Lectura/escritura de CSV, alta y actualización de países
├── consultas.py         # Búsqueda por nombre y filtros por continente y rangos
├── validaciones.py      # Validaciones transversales de entradas de usuario
├── ordenar.py           # Ordenamiento ascendente y descendente por distintos criterios
├── estadisticas.py      # Cálculo de máximos, mínimos, promedios y conteos
├── paises.csv           # Dataset base con información de países
├── Informe_TPI.pdf      # Documentación académica, marco teórico y capturas
└── README.md            # Documentación general del repositorio
```

---

## 🚀 Requisitos e Instrucciones de Uso

### Requisitos previos
* Tener instalado **Python 3.8** o superior.
* No requiere instalación de librerías externas (utiliza únicamente la biblioteca estándar de Python).

### Ejecución
1. Clonar el repositorio en tu máquina local:
   ```bash
   git clone https://github.com/usuario-lider/nombre-del-repositorio.git
   ```
2. Ingresar al directorio del proyecto:
   ```bash
   cd nombre-del-repositorio
   ```
3. Ejecutar el archivo principal desde la consola:
   ```bash
   python main.py
   ```
   *(En sistemas Linux/macOS puede requerirse el comando `python3 main.py`).*

---

## ⚙️ Funcionalidades Principales

1. **Agregar país:** Permite registrar un nuevo país validando que ningún campo quede vacío y que los valores numéricos sean enteros positivos.
2. **Actualizar datos:** Modifica la población y la superficie (en $\text{km}^2$) de un país existente y persiste los cambios en el archivo CSV.
3. **Buscar por nombre:** Realiza búsquedas por coincidencia exacta o parcial (insensible a mayúsculas/minúsculas).
4. **Filtrar países:**
   * Por continente.
   * Por rango de población (mínimo y máximo).
   * Por rango de superficie en $\text{km}^2$ (mínimo y máximo).
5. **Ordenar países:** Permite ordenar el listado de forma ascendente o descendente por **Nombre**, **Población** o **Superficie**.
6. **Mostrar estadísticas:**
   * País con mayor y menor población.
   * Promedio general de población.
   * Promedio general de superficie.
   * Cantidad total de países agrupados por continente.

---

## 💻 Ejemplos de Entradas y Salidas

### Formato del archivo `paises.csv`
```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
Brasil,213993437,8515767,América
Alemania,83149300,357022,Europa
```

### Ejemplo de interacción en consola

**Menú Principal:**
```text
==================================================
   SISTEMA DE GESTIÓN DE DATOS DE PAÍSES (UTN)
==================================================
1. Agregar un país
2. Actualizar población y superficie de un país
3. Buscar país por nombre
4. Filtrar países (Continente / Población / Superficie)
5. Ordenar países
6. Mostrar estadísticas
7. Salir
--------------------------------------------------
Seleccione una opción (1-7): 3
```

**Ejemplo de Búsqueda (Entrada y Salida):**
```text
Ingrese el nombre (o parte del nombre) del país a buscar: argen

--- Resultados encontrados (1) ---
• Argentina | Población: 45,376,763 hab. | Superficie: 2,780,400 km² | Continente: América
```

**Ejemplo de Estadísticas (Salida):**
```text
--- INDICADORES ESTADÍSTICOS DEL DATASET ---
• País con mayor población: Brasil (213,993,437 hab.)
• País con menor población: Argentina (45,376,763 hab.)
• Promedio de población: 117,079,875.00 hab.
• Promedio de superficie: 3,007,791.00 km²
• Cantidad de países por continente:
   - América: 2
   - Asia: 1
   - Europa: 1
```

---

## 🔗 Enlaces y Documentación Obligatoria

* **🎥 Video Demostrativo (Acceso Público):** [Ver video en YouTube / Google Drive](https://enlace-al-video-publico.com) *(Asegurar permisos de visualización pública)*.
* **📄 Informe Académico y Técnico (PDF):** Disponible directamente en la raíz de este repositorio como [`Informe_TPI.pdf`](./Informe_TPI.pdf) *(o mediante [este enlace externo](https://enlace-al-pdf.com))*.

---

## 👥 Participación de los Integrantes

El desarrollo del código, la documentación teórica y la presentación audiovisual se dividieron equitativamente entre los cuatro integrantes del equipo:

### 1. Facundo Piriz (@Fakzup) — *Datos y Gestión*
* **Desarrollo (`datos.py`):** Implementación de lectura del CSV con control de errores de formato, guardado de datos, alta de nuevos países y actualización de población y superficie.
* **Dataset:** Confección y validación del archivo base `paises.csv`.
* **Documentación (PDF):** Redacción del marco teórico sobre *Listas*, *Diccionarios* y *Archivos CSV*.

### 2. Francisco Ruiz (@fran1399) — *Consultas y Validaciones*
* **Desarrollo (`consultas.py`):** Implementación de búsqueda por nombre (parcial/exacta) y filtros por continente, rango de población y rango de superficie.
* **Desarrollo (`validaciones.py`):** Creación de funciones transversales de validación (entero positivo, texto no vacío, rango válido y opción de menú) utilizadas en todo el sistema.
* **Documentación (PDF):** Redacción del marco teórico sobre *Condicionales* y *Funciones*, y confección del *Diagrama de Flujo* de operaciones principales.

### 3. Agustin Tromba (@aqussti) — *Ordenamiento, Estadísticas y Repositorio*
* **Desarrollo (`ordenar.py` y `estadisticas.py`):** Implementación de algoritmos de ordenamiento (ascendente/descendente por nombre, población y superficie) y cálculo de métricas estadísticas.
* **Repositorio y `README.md`:** Creación y administración del repositorio en GitHub, y redacción integral del archivo `README.md`.
* **Documentación (PDF):** Redacción del marco teórico sobre *Ordenamientos* y *Estadísticas básicas*, además de la sección de *Decisiones Técnicas y Arquitectura*.

### 4. Fausto Rivero (@faustorivero69-hue) — *Integración, Menú e Informe Final*
* **Desarrollo (`main.py`):** Diseño del menú de consola, bucle principal de ejecución, integración de todos los módulos y manejo de mensajes claros de éxito y error.
* **Documentación (PDF):** Armado, maquetación y revisión final del documento PDF (carátula, índice, numeración de páginas, capturas de ejecución, bibliografía y enlaces).
* **Entrega y Video:** Apertura y cierre de la presentación en video, subida con permisos públicos y armado del archivo `.zip` final para la entrega.
