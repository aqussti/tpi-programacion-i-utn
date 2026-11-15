# Guion del video demostrativo

Duración objetivo: 12 minutos. Participan Facundo, Francisco, Agustín y Fausto. Grabar la consola y explicar las operaciones con sus propias palabras. Los tiempos siguientes son una guía, no una grabación ya realizada.

## Preparación

Usar una copia de la carpeta del proyecto para no modificar el dataset de entrega. Abrir la terminal con letra grande, comprobar el micrófono y ejecutar `python main.py`. Preparar el código para mostrar brevemente la lista de diccionarios, la lectura CSV y el algoritmo de inserción. El video debe poder abrirse sin iniciar sesión.

## 0:00 a 3:00 - Fausto: presentación e integración

Presentar el título, la materia, la comisión y los cuatro integrantes. Explicar el problema: consultar y modificar datos de países sin editar manualmente el CSV. Mostrar los seis módulos y cómo el menú llama a sus funciones. Arrancar el programa, mostrar los 19 registros cargados y las siete opciones. Ingresar una opción fuera de rango para mostrar que el programa continúa.

## 3:00 a 6:00 - Facundo: datos y persistencia

Mostrar el encabezado del CSV y explicar que cada país se convierte en un diccionario dentro de una lista. Agregar Portugal con población `10000000`, superficie `92212` y continente `europa`. Aclarar que son valores de demostración. Probar un campo vacío y un número negativo antes de ingresar los válidos. Actualizar Portugal a `10500000` habitantes. Intentar agregarlo de nuevo para mostrar el control de duplicados. Mostrar que el archivo conserva el cambio tras salir y volver a ejecutar el programa.

## 6:00 a 9:00 - Francisco: consultas y validaciones

Buscar `argen` en modo parcial y `japon` en modo exacto. Buscar un nombre inexistente. Elegir América en el submenú de continentes. Explicar que las entradas de continentes se normalizan al guardar. Filtrar población entre `0` y `5000000` y superficie entre `0` y `200000`. Invertir un rango para mostrar el mensaje de error. Explicar que los filtros incluyen ambos extremos y devuelven listas nuevas.

## 9:00 a 12:00 - Agustín: ordenamiento, estadísticas y cierre

Ordenar nombres de menor a mayor; población de mayor a menor; superficie en ambos sentidos. Mostrar brevemente el ciclo de inserción: guardar el elemento, desplazar anteriores e insertarlo. Explicar que se trabaja sobre una copia y que los empates conservan el orden. Mostrar estadísticas, explicar la media como suma dividida por cantidad y aclarar que corresponden al dataset cargado. Mencionar que con una lista vacía se informa la falta de datos. Mostrar la ejecución de `python -B -m unittest -v test_sistema`. Cerrar con las dificultades resueltas: integración de nombres de funciones, normalización y protección del CSV. Mostrar el repositorio y el informe PDF.

## Antes de entregar

1. Verificar que el video dure entre 10 y 15 minutos y que se escuche a todos.
2. Subirlo y probar el enlace en una ventana sin sesión iniciada.
3. Reemplazar la nota pendiente de video en el README y agregar el enlace al informe editable y PDF.
4. Volver a armar el ZIP para que incluya esas versiones finales.
