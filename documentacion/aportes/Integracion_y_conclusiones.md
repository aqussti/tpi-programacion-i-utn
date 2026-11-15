# Aporte de integración y conclusiones

Texto recibido en la revisión grupal del 15/11/2026. Se conserva como respaldo; el informe final consolidado está en la raíz.

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



