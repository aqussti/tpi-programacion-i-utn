# Gestión de Datos de Países en Python

Trabajo Práctico Integrador de Programación 1 - UTN. Tecnicatura Universitaria en Programación, comisión 4. Entrega: 16/11/2026.

Aplicación de consola para administrar un CSV de países mediante listas, diccionarios, funciones, búsquedas, filtros, ordenamiento por inserción y estadísticas.

## Ejecución

Requiere Python 3.8 o superior. El programa y sus pruebas usan únicamente la biblioteca estándar.

```bash
git clone https://github.com/aqussti/tpi-programacion-i-utn.git
cd tpi-programacion-i-utn
python main.py
```

En Linux/macOS puede usarse `python3`. El CSV se busca junto a `datos.py`, independientemente de la carpeta desde la que se ejecute el programa.

## Funcionalidades

1. Agregar países sin campos vacíos ni nombres duplicados.
2. Actualizar la población y superficie de un país existente.
3. Buscar por nombre, con opción parcial o exacta, sin distinguir mayúsculas ni tildes.
4. Filtrar por continente o rangos inclusivos de población y superficie.
5. Ordenar por nombre, población o superficie en ambos sentidos, conservando la lista original.
6. Consultar extremos de población, promedios y cantidad de países por continente.
7. Salir. Las altas y actualizaciones se guardan inmediatamente.

Las poblaciones y superficies deben ser enteros positivos. Los rangos admiten cero. Los continentes se normalizan a América, Europa, Asia, África, Oceanía o Antártida. Si un CSV existente es inválido, el programa informa el problema y termina sin sobrescribirlo. Si falta el archivo, se puede comenzar una lista nueva.

## Archivos

| Archivo | Responsabilidad |
| --- | --- |
| `main.py` | Menú, entradas y presentación de resultados |
| `datos.py` | Lectura, guardado, alta y actualización |
| `consultas.py` | Búsquedas y filtros |
| `validaciones.py` | Validación de entradas y normalización |
| `ordenar.py` | Ordenamiento por inserción |
| `estadisticas.py` | Extremos, promedios y conteos |
| `paises.csv` | Dataset académico de 19 países |
| `test_sistema.py` | Pruebas de funciones, integración y persistencia |
| `Informe_TPI.md` / `Informe_TPI.pdf` | Informe editable y versión de entrega |
| `documentacion/` | Diagrama y salidas capturadas de las pruebas |
| `Guion_video.md` | Recorrido sugerido para la presentación grupal |

Los valores del dataset se utilizan para ejercitar programación; no se presentan como cifras demográficas actualizadas ni como una base estadística oficial.

## Ejemplo de datos

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Brasil,213993437,8515767,América
```

## Ejemplos de uso

Búsqueda exacta: elegir `3`, ingresar `japon` y elegir `2` (exacta).

```text
Japón | Población: 125.800.000 hab. | Superficie: 377.975 km² | Continente: Asia
```

Filtro: elegir `4`, luego `2` (población), mínimo `0` y máximo `5000000`. Con el dataset base, el resultado es Uruguay.

Estadísticas sobre los 19 países originales:

```text
País con mayor población: China (1.412.000.000 hab.)
País con menor población: Uruguay (3.426.260 hab.)
Cantidad de países por continente:
  América: 6
  Europa: 4
  Asia: 4
  África: 3
  Oceanía: 2
```

## Pruebas

```bash
python -B -m unittest -v test_sistema
```

Las 14 pruebas usan archivos temporales y no alteran `paises.csv`. Incluyen el menú, altas y actualizaciones, persistencia, seis ordenamientos, búsquedas, filtros, estadísticas, listas vacías, CSV inválidos, duplicados, continentes y fallos simulados de escritura. Fueron ejecutadas con Python 3.14; se comprobó además la sintaxis compatible con Python 3.8.

## Integración

- `ordenar_paises(paises, criterio="nombre", ascendente=True)` devuelve una nueva lista. Los empates conservan el orden inicial. Los nombres se comparan sin mayúsculas, conservando tildes; no se aplica orden regional.
- `calcular_estadisticas(paises)` devuelve `mayor_poblacion`, `menor_poblacion`, `promedio_poblacion`, `promedio_superficie` y `cantidad_por_continente`. Sin datos, los extremos y promedios son `None` y el conteo es `{}`.
- Las búsquedas y filtros devuelven listas, incluso si no encuentran resultados. `buscar_por_nombre` acepta `exacta=True`.
- `leer_paises()` devuelve registros validados o comunica un error mediante una excepción. `agregar_pais` y `actualizar_pais` devuelven un booleano y solo cambian la lista después de guardar correctamente.
- El guardado usa un archivo temporal en la misma carpeta y reemplaza el CSV cuando termina la escritura. No está previsto el uso simultáneo por varios usuarios.

## Documentación y entrega

- [Informe académico y técnico en PDF](Informe_TPI.pdf).
- [Fuente editable del informe](Informe_TPI.md).
- [Guion y pasos para grabar el video](Guion_video.md).
- **Video demostrativo:** pendiente de grabación y publicación por el grupo. Antes de entregar, reemplazar esta nota por el enlace accesible sin iniciar sesión y agregar el mismo enlace al informe.
- El ZIP de entrega debe contener código, dataset, documentación y recursos. No incluir `.git`, archivos temporales ni `__pycache__`.

## Participación de los integrantes

| Integrante | Desarrollo y documentación asignados |
| --- | --- |
| Facundo Piriz (@Fakzup) | Datos y CSV; listas, diccionarios y archivos |
| Francisco Ruiz (@fran1399) | Consultas y validaciones; funciones, condicionales y flujo |
| Agustin Tromba (@aqussti) | Ordenamiento, estadísticas, repositorio y README; teoría y decisiones técnicas |
| Fausto Rivero (@faustorivero69-hue) | Menú e integración; armado del informe, video y entrega |

La presentación requiere participación de los cuatro integrantes. Revisar el PDF y completar el enlace del video antes de enviar el ZIP.
