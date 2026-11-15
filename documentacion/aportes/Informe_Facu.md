# Facundo Piriz – Datos y gestión

## 1. Introducción

Mi responsabilidad en el proyecto fue desarrollar el módulo encargado de gestionar los datos de los países. Para esto trabajé con Python y archivos CSV, creando las funciones necesarias para leer, guardar, agregar y actualizar información.

## 2. Conceptos utilizados

**Listas:** Se utilizaron para almacenar todos los países cargados desde el archivo CSV. Esto permite recorrer los registros y trabajar con ellos fácilmente.

**Diccionarios:** Cada país se representa mediante un diccionario que contiene cuatro datos: nombre, población, superficie y continente. Esto facilita el acceso y la modificación de cada valor.

**Archivos CSV:** Se utilizó el archivo `paises.csv` para almacenar la información de los países de forma permanente. Para leer y escribir los datos se empleó la biblioteca `csv` de Python.

## 3. Desarrollo realizado

Se creó el archivo `datos.py`, que contiene cuatro funciones principales:

- `leer_paises()`: lee los datos del CSV y los convierte en una lista de diccionarios.
- `guardar_paises()`: almacena los datos y los cambios realizados en el archivo.
- `agregar_pais()`: permite incorporar nuevos países, comprobando que los datos sean válidos y que no existan duplicados.
- `actualizar_pais()`: permite modificar la población y superficie de un país existente.

También se incorporaron controles para evitar campos vacíos, valores numéricos incorrectos y datos negativos o iguales a cero.

## 4. Pruebas realizadas

Se comprobó el funcionamiento de las funciones mediante un archivo temporal llamado `prueba.py`.

Se realizaron pruebas de lectura de los 19 países iniciales, incorporación de Portugal y actualización de la población de Argentina. También se probaron entradas incorrectas y búsquedas de países inexistentes.

Los resultados fueron satisfactorios y los cambios se guardaron correctamente en el CSV.

## 5. Conclusión

Este trabajo permitió aplicar los conocimientos sobre listas, diccionarios y archivos CSV, además de comprender la importancia de dividir un programa en funciones y módulos independientes. También aprendí a controlar errores y organizar información para que pueda ser utilizada por las diferentes partes de un mismo proyecto.

**Archivos desarrollados:** `datos.py` y `paises.csv`.