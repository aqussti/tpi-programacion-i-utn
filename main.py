"""
Trabajo Práctico Integrador - Programación 1
Gestión de Datos de Países en Python: filtros, ordenamientos y estadísticas

Archivo: main.py
Rol: Integración, menú principal y experiencia de usuario.
"""

import os
import sys

from datos import leer_paises, agregar_pais, actualizar_pais
from consultas import (
    normalizar,
    buscar_por_nombre,
    filtrar_por_continente,
    filtrar_por_poblacion,
    filtrar_por_superficie,
    obtener_continentes,
)
from validaciones import (
    pedir_texto_no_vacio,
    pedir_entero_positivo,
    pedir_rango,
    pedir_opcion_menu,
)
from ordenar import ordenar_paises
from estadisticas import calcular_estadisticas


# ---------------------------------------------------------------------------
# Contrato de integración con los módulos de los compañeros
# ---------------------------------------------------------------------------
# datos.py
#   leer_paises() -> list[dict]
#   agregar_pais(paises, nombre, poblacion, superficie, continente) -> bool
#   actualizar_pais(paises, nombre, nueva_poblacion, nueva_superficie) -> bool
#
# consultas.py
#   buscar_por_nombre(paises, texto, exacta=False) -> list[dict]
#   filtrar_por_continente(paises, continente) -> list[dict]
#   filtrar_por_poblacion(paises, minimo, maximo) -> list[dict]
#   filtrar_por_superficie(paises, minimo, maximo) -> list[dict]
#   obtener_continentes(paises) -> list[str]
#
# validaciones.py
#   pedir_texto_no_vacio(mensaje) -> str
#   pedir_entero_positivo(mensaje, permitir_cero=False) -> int
#   pedir_rango(mensaje_min, mensaje_max) -> tuple[int, int]
#   pedir_opcion_menu(mensaje, opciones_validas) -> str
#
# ordenar.py
#   ordenar_paises(paises, criterio="nombre", ascendente=True) -> list[dict]
#
# estadisticas.py
#   calcular_estadisticas(paises) -> dict
#
# Criterio de integración: consultas.py, ordenar.py y estadisticas.py
# reciben datos, calculan y devuelven resultados sin imprimir por consola.
# datos.py y validaciones.py emiten mensajes puntuales de confirmación o
# error. main.py concentra la presentación principal, las preguntas al
# usuario y la navegación entre opciones.
# ---------------------------------------------------------------------------


# Opciones del menú principal y de los submenús. Se usan cadenas porque
# validaciones.pedir_opcion_menu() compara directamente lo ingresado.
OPCIONES_MENU = [str(numero) for numero in range(1, 8)]
OPCIONES_FILTRO = ["1", "2", "3", "0"]
OPCIONES_ORDEN = ["1", "2", "3", "0"]
OPCIONES_SENTIDO = ["1", "2"]

CRITERIOS = {
    "1": "nombre",
    "2": "poblacion",
    "3": "superficie",
}

ETIQUETAS_CRITERIO = {
    "nombre": "nombre",
    "poblacion": "población",
    "superficie": "superficie",
}


# ---------------------------------------------------------------------------
# Utilidades de consola y formato
# ---------------------------------------------------------------------------

def configurar_consola():
    """Configura la consola de Windows para mostrar correctamente el UTF-8."""
    if os.name != "nt":
        return

    try:
        os.system("chcp 65001 > nul")
        # Se reconfiguran los tres flujos para que las tildes y la "ñ"
        # funcionen tanto en la consola como en entradas redirigidas.
        sys.stdin.reconfigure(encoding="utf-8")
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        # Si la consola no admite la configuración, se usan sus valores
        # predeterminados sin interrumpir el programa.
        pass


def limpiar_consola():
    """Limpia la pantalla en Windows (cls) y en Linux/macOS (clear)."""
    try:
        os.system("cls" if os.name == "nt" else "clear")
        sys.stdout.flush()
    except Exception:
        # Si la consola no permite limpiar, el programa continúa normalmente.
        pass


def pausar():
    """Espera a que el usuario presione Enter para continuar."""
    try:
        input("\nPresione Enter para continuar...")
    except (EOFError, KeyboardInterrupt):
        # Si la entrada se cierra o el usuario interrumpe, se informa con un
        # salto de línea y el bucle principal decide cómo continuar.
        print()


def formatear_numero(valor):
    """Devuelve un número entero con puntos de miles (ej. 45.376.763)."""
    try:
        return f"{int(valor):,}".replace(",", ".")
    except (TypeError, ValueError):
        return str(valor)


def formatear_decimal(valor, decimales=2):
    """Devuelve un número decimal con coma decimal y puntos de miles."""
    try:
        texto = f"{float(valor):,.{decimales}f}"
    except (TypeError, ValueError):
        return str(valor)
    return texto.replace(",", "X").replace(".", ",").replace("X", ".")


def mostrar_pais(pais):
    """Muestra un país con un formato legible para la consola."""
    if not isinstance(pais, dict):
        return

    nombre = pais.get("nombre", "(sin nombre)")
    poblacion = pais.get("poblacion", 0)
    superficie = pais.get("superficie", 0)
    continente = pais.get("continente", "(sin continente)")

    print(
        f"  - {nombre} | "
        f"Población: {formatear_numero(poblacion)} hab. | "
        f"Superficie: {formatear_numero(superficie)} km² | "
        f"Continente: {continente}"
    )


def mostrar_lista(paises, titulo):
    """Muestra una lista de países con su cantidad de resultados."""
    if not paises:
        print("\nNo se encontraron resultados.")
        return

    cantidad = len(paises)
    plural = "s" if cantidad != 1 else ""
    print(f"\n--- {titulo} ({cantidad} resultado{plural}) ---")
    for pais in paises:
        mostrar_pais(pais)


def cargar_datos():
    """Carga los países desde el CSV controlando cualquier error inesperado."""
    try:
        paises = leer_paises()
        if isinstance(paises, list):
            return paises

        print("[ERROR] El módulo de datos no devolvió una lista válida.")
        return []
    except Exception as error:
        print(f"[ERROR] No se pudieron cargar los datos: {error}")
        return []


def normalizar_continente(paises, texto):
    """Unifica el continente ingresado con uno ya existente, si coincide.

    Si el usuario escribe "america" y en el dataset figura "América", se
    devuelve "América" para no crear dos continentes distintos por la tilde
    o por las mayúsculas. Si el continente es nuevo, se devuelve con la
    primera letra en mayúscula.
    """
    texto = texto.strip()
    for continente in obtener_continentes(paises):
        if normalizar(continente) == normalizar(texto):
            return continente
    return texto.capitalize()


# ---------------------------------------------------------------------------
# Menú principal
# ---------------------------------------------------------------------------

def mostrar_menu(cantidad_paises=None):
    """Muestra las opciones del menú principal."""
    print("=" * 62)
    print("   SISTEMA DE GESTIÓN DE DATOS DE PAÍSES (UTN)")
    print("=" * 62)
    print("  1. Agregar país")
    print("  2. Actualizar datos")
    print("  3. Buscar país")
    print("  4. Filtrar países")
    print("  5. Ordenar países")
    print("  6. Ver estadísticas")
    print("  7. Salir")
    print("-" * 62)
    if cantidad_paises is not None:
        print(f"  Países cargados: {cantidad_paises}")
        print("-" * 62)


# ---------------------------------------------------------------------------
# Opción 1: agregar un país
# ---------------------------------------------------------------------------

def opcion_agregar(paises):
    """Solicita los datos de un país nuevo y lo guarda en el CSV."""
    print("=" * 62)
    print("  AGREGAR PAÍS")
    print("=" * 62)

    # [INTEGRACIÓN] validaciones.pedir_texto_no_vacio() repite la pregunta
    # hasta obtener un texto con contenido.
    nombre = pedir_texto_no_vacio("Nombre del país: ")

    # [INTEGRACIÓN] Antes de llamar a datos.agregar_pais() se controla la
    # duplicación con la búsqueda exacta de consultas.py, que ignora tildes
    # y mayúsculas. Así se evita cargar "Mexico" y "México" a la vez.
    if buscar_por_nombre(paises, nombre, exacta=True):
        print("\n[ERROR] Ya existe un país con ese nombre.")
        return

    poblacion = pedir_entero_positivo("Población: ")
    superficie = pedir_entero_positivo("Superficie en km²: ")

    continentes = obtener_continentes(paises)
    if continentes:
        print(f"\nContinentes registrados: {', '.join(continentes)}")

    continente = normalizar_continente(
        paises,
        pedir_texto_no_vacio("Continente: "),
    )

    # [INTEGRACIÓN] datos.agregar_pais() valida, guarda el CSV y actualiza
    # la lista en memoria. Devuelve True si la operación fue exitosa.
    agregado = agregar_pais(paises, nombre, poblacion, superficie, continente)

    if agregado:
        print("\n[OK] El país quedó registrado y guardado en el archivo CSV.")
    else:
        print(
            "\n[ERROR] No se pudo agregar el país. "
            "Revise los datos ingresados."
        )


# ---------------------------------------------------------------------------
# Opción 2: actualizar población y superficie
# ---------------------------------------------------------------------------

def opcion_actualizar(paises):
    """Solicita un país existente y actualiza su población y superficie."""
    print("=" * 62)
    print("  ACTUALIZAR DATOS")
    print("=" * 62)

    if not paises:
        print("\nNo hay países cargados. Agregue uno primero.")
        return

    termino = pedir_texto_no_vacio("Nombre del país a actualizar: ")

    # [INTEGRACIÓN] Se busca primero la coincidencia exacta. Si no existe,
    # se muestran las coincidencias parciales para ayudar al usuario.
    exactos = buscar_por_nombre(paises, termino, exacta=True)

    if not exactos:
        parciales = buscar_por_nombre(paises, termino)
        if parciales:
            print("\nNo hay una coincidencia exacta. Países encontrados:")
            for pais in parciales:
                mostrar_pais(pais)
            print("Vuelva a intentarlo con el nombre exacto.")
        else:
            print(f"\n[ERROR] No se encontró ningún país llamado '{termino}'.")
        return

    pais_actual = exactos[0]
    print("\nDatos actuales:")
    mostrar_pais(pais_actual)

    poblacion = pedir_entero_positivo("Nueva población: ")
    superficie = pedir_entero_positivo("Nueva superficie en km²: ")

    # [INTEGRACIÓN] datos.actualizar_pais() guarda los cambios en el CSV y
    # actualiza la lista en memoria. Devuelve True si pudo actualizar.
    actualizado = actualizar_pais(
        paises,
        pais_actual["nombre"],
        poblacion,
        superficie,
    )

    if actualizado:
        print("\n[OK] Los cambios quedaron guardados en el archivo CSV.")
    else:
        print(
            "\n[ERROR] No se pudo actualizar el país. "
            "Revise los datos ingresados."
        )


# ---------------------------------------------------------------------------
# Opción 3: buscar por nombre
# ---------------------------------------------------------------------------

def opcion_buscar(paises):
    """Busca países por coincidencia parcial o exacta del nombre."""
    print("=" * 62)
    print("  BUSCAR PAÍS")
    print("=" * 62)

    if not paises:
        print("\nNo hay países cargados.")
        return

    termino = pedir_texto_no_vacio("Ingrese el nombre o parte del nombre: ")

    # [INTEGRACIÓN] buscar_por_nombre() normaliza mayúsculas y tildes y
    # devuelve una lista nueva con las coincidencias parciales.
    resultados = buscar_por_nombre(paises, termino)

    if resultados:
        mostrar_lista(resultados, f"Resultados para '{termino}'")
    else:
        print(f"\nNo se encontraron países que coincidan con '{termino}'.")


# ---------------------------------------------------------------------------
# Opción 4: filtrar países
# ---------------------------------------------------------------------------

def filtrar_continente(paises):
    """Muestra los continentes disponibles y filtra por el elegido."""
    continentes = obtener_continentes(paises)

    if not continentes:
        print("\nNo hay continentes registrados.")
        return

    print("\nContinentes disponibles:")
    for indice, continente in enumerate(continentes, start=1):
        print(f"  {indice}. {continente}")
    print("  0. Volver")

    opciones = [str(indice) for indice in range(1, len(continentes) + 1)]
    opciones.append("0")
    opcion = pedir_opcion_menu(
        "Seleccione un continente: ",
        opciones,
    )

    if opcion == "0":
        return

    continente = continentes[int(opcion) - 1]

    # [INTEGRACIÓN] filtrar_por_continente() compara sin distinguir
    # mayúsculas ni tildes.
    resultados = filtrar_por_continente(paises, continente)
    mostrar_lista(resultados, f"Países de {continente}")


def filtrar_poblacion(paises):
    """Filtra los países por un rango de población."""
    # [INTEGRACIÓN] pedir_rango() valida enteros no negativos y que el
    # mínimo no supere al máximo antes de devolver la tupla.
    minimo, maximo = pedir_rango(
        "Población mínima: ",
        "Población máxima: ",
    )

    resultados = filtrar_por_poblacion(paises, minimo, maximo)
    mostrar_lista(
        resultados,
        f"Países con población entre {formatear_numero(minimo)} "
        f"y {formatear_numero(maximo)}",
    )


def filtrar_superficie(paises):
    """Filtra los países por un rango de superficie."""
    minimo, maximo = pedir_rango(
        "Superficie mínima en km²: ",
        "Superficie máxima en km²: ",
    )

    resultados = filtrar_por_superficie(paises, minimo, maximo)
    mostrar_lista(
        resultados,
        f"Países con superficie entre {formatear_numero(minimo)} "
        f"y {formatear_numero(maximo)} km²",
    )


def opcion_filtrar(paises):
    """Muestra el submenú de filtros y ejecuta el elegido."""
    print("=" * 62)
    print("  FILTRAR PAÍSES")
    print("=" * 62)

    if not paises:
        print("\nNo hay países cargados.")
        return

    print("  1. Por continente")
    print("  2. Por rango de población")
    print("  3. Por rango de superficie")
    print("  0. Volver al menú principal")
    print("-" * 62)

    opcion = pedir_opcion_menu(
        "Seleccione una opción (0-3): ",
        OPCIONES_FILTRO,
    )

    if opcion == "0":
        return
    if opcion == "1":
        filtrar_continente(paises)
    elif opcion == "2":
        filtrar_poblacion(paises)
    elif opcion == "3":
        filtrar_superficie(paises)


# ---------------------------------------------------------------------------
# Opción 5: ordenar países
# ---------------------------------------------------------------------------

def opcion_ordenar(paises):
    """Solicita criterio y sentido, y muestra la lista ordenada."""
    print("=" * 62)
    print("  ORDENAR PAÍSES")
    print("=" * 62)

    if not paises:
        print("\nNo hay países cargados.")
        return

    print("  1. Por nombre")
    print("  2. Por población")
    print("  3. Por superficie")
    print("  0. Volver al menú principal")
    print("-" * 62)

    opcion = pedir_opcion_menu(
        "Seleccione el criterio (0-3): ",
        OPCIONES_ORDEN,
    )

    if opcion == "0":
        return

    criterio = CRITERIOS[opcion]

    print("\n  1. Ascendente (menor a mayor)")
    print("  2. Descendente (mayor a menor)")
    sentido = pedir_opcion_menu(
        "Seleccione el sentido (1-2): ",
        OPCIONES_SENTIDO,
    )

    ascendente = sentido == "1"

    # [INTEGRACIÓN] ordenar_paises() recibe una copia y no modifica la
    # lista original. Devuelve una lista nueva ya ordenada.
    ordenados = ordenar_paises(
        paises,
        criterio=criterio,
        ascendente=ascendente,
    )

    etiqueta_criterio = ETIQUETAS_CRITERIO[criterio]
    etiqueta_sentido = "ascendente" if ascendente else "descendente"
    mostrar_lista(
        ordenados,
        f"Países ordenados por {etiqueta_criterio} ({etiqueta_sentido})",
    )


# ---------------------------------------------------------------------------
# Opción 6: estadísticas
# ---------------------------------------------------------------------------

def opcion_estadisticas(paises):
    """Calcula y muestra los indicadores del módulo estadisticas.py."""
    print("=" * 62)
    print("  ESTADÍSTICAS DEL DATASET")
    print("=" * 62)

    if not paises:
        print("\nNo hay países cargados para calcular estadísticas.")
        return

    # [INTEGRACIÓN] calcular_estadisticas() devuelve un diccionario con los
    # extremos, los promedios y el conteo por continente. No imprime nada.
    resumen = calcular_estadisticas(paises)

    if not isinstance(resumen, dict):
        print("\n[ERROR] No se pudieron calcular las estadísticas.")
        return

    mayor = resumen.get("mayor_poblacion")
    menor = resumen.get("menor_poblacion")
    promedio_poblacion = resumen.get("promedio_poblacion")
    promedio_superficie = resumen.get("promedio_superficie")
    por_continente = resumen.get("cantidad_por_continente") or {}

    if mayor and menor:
        print(
            f"\nPaís con mayor población: {mayor.get('nombre', '(sin nombre)')} "
            f"({formatear_numero(mayor.get('poblacion', 0))} hab.)"
        )
        print(
            f"País con menor población: {menor.get('nombre', '(sin nombre)')} "
            f"({formatear_numero(menor.get('poblacion', 0))} hab.)"
        )
    else:
        print("\nNo hay datos suficientes para calcular los extremos.")

    if promedio_poblacion is not None:
        print(
            "Promedio de población: "
            f"{formatear_decimal(promedio_poblacion)} hab."
        )
    if promedio_superficie is not None:
        print(
            "Promedio de superficie: "
            f"{formatear_decimal(promedio_superficie)} km²"
        )

    print("\nCantidad de países por continente:")
    if por_continente:
        for continente in sorted(por_continente):
            print(f"  - {continente}: {por_continente[continente]}")
    else:
        print("  (sin datos)")

    print(f"\nTotal de países: {len(paises)}")


# ---------------------------------------------------------------------------
# Punto de entrada y bucle principal
# ---------------------------------------------------------------------------

def ejecutar_opcion(opcion, paises):
    """Deriva la opción elegida a la función correspondiente."""
    if opcion == "1":
        opcion_agregar(paises)
    elif opcion == "2":
        opcion_actualizar(paises)
    elif opcion == "3":
        opcion_buscar(paises)
    elif opcion == "4":
        opcion_filtrar(paises)
    elif opcion == "5":
        opcion_ordenar(paises)
    elif opcion == "6":
        opcion_estadisticas(paises)


def main():
    """Punto de entrada del sistema."""
    configurar_consola()
    limpiar_consola()

    print("Cargando datos desde el archivo CSV...")
    paises = cargar_datos()

    if paises:
        print(f"\n[OK] Se cargaron {len(paises)} países.")
    else:
        print(
            "\n[AVISO] No hay países cargados. "
            "Puede agregar uno nuevo o revisar el archivo CSV."
        )

    try:
        pausar()
    except (KeyboardInterrupt, EOFError):
        print("\nSaliendo del programa...")
        return

    while True:
        limpiar_consola()
        mostrar_menu(len(paises))

        try:
            # [INTEGRACIÓN] pedir_opcion_menu() rechaza letras y números
            # fuera de rango sin lanzar una excepción: repite la pregunta
            # hasta recibir una opción válida. El try-except externo queda
            # como red de seguridad para errores inesperados del sistema.
            opcion = pedir_opcion_menu(
                "Seleccione una opción (1-7): ",
                OPCIONES_MENU,
            )

            if opcion == "7":
                limpiar_consola()
                print("=" * 62)
                print("  Gracias por usar el Sistema de Gestión de Países.")
                print("=" * 62)
                break

            limpiar_consola()
            ejecutar_opcion(opcion, paises)
            pausar()

        except (KeyboardInterrupt, EOFError):
            print("\n\nSaliendo del programa...")
            break
        except ValueError as error:
            # Salvaguarda ante datos numéricos inválidos provenientes de
            # alguna función integrada.
            print(f"\n[ERROR] Dato inválido: {error}")
            pausar()
        except Exception as error:
            print(f"\n[ERROR] Ocurrió un problema inesperado: {error}")
            pausar()

    print("\nFin del programa.")


if __name__ == "__main__":
    main()
