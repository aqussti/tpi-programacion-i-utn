"""
Trabajo Práctico Integrador - Programación 1
Gestión de Datos de Países en Python: filtros, ordenamientos y estadísticas

Archivo: main.py
Rol: Integración, menú principal y experiencia de usuario.
"""

import os
import sys

from datos import leer_paises, agregar_pais, actualizar_pais
from consultas import buscar_pais, filtrar_paises
from validaciones import pedir_entero, pedir_cadena, validar_opcion
from ordenar import ordenar_paises
from estadisticas import calcular_estadisticas


# ---------------------------------------------------------------------------
# Contrato de integración con los módulos de los compañeros
# ---------------------------------------------------------------------------
# datos.leer_paises() -> list[dict]
# datos.agregar_pais(paises, nombre, poblacion, superficie, continente) -> bool
# datos.actualizar_pais(paises, nombre, nueva_poblacion,
#                        nueva_superficie) -> bool
#
# consultas.buscar_pais(paises, termino) -> list[dict]
# consultas.filtrar_paises(paises, continente=None, poblacion_min=None,
#                          poblacion_max=None, superficie_min=None,
#                          superficie_max=None) -> list[dict]
#
# validaciones.pedir_entero(mensaje) -> int
# validaciones.pedir_cadena(mensaje) -> str
# validaciones.validar_opcion(opcion, opciones_validas) -> bool
#
# ordenar.ordenar_paises(paises, criterio="nombre",
#                        ascendente=True) -> list[dict]
# estadisticas.calcular_estadisticas(paises) -> dict
#
# Nota: estadisticas.py devuelve un diccionario con los indicadores. La
# presentación por consola se centraliza en main.py para mantener separadas
# la lógica de cálculo y la interfaz de usuario.
# ---------------------------------------------------------------------------

OPCIONES_MENU = [1, 2, 3, 4, 5, 6, 7]
OPCIONES_FILTRO = [1, 2, 3, 4]
OPCIONES_CRITERIO = [1, 2, 3, 4]
OPCIONES_SENTIDO = [1, 2]

CRITERIOS = {
    1: "nombre",
    2: "poblacion",
    3: "superficie",
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
    except EOFError:
        # Si la entrada se cierra, se evita un error y el bucle principal
        # se encarga de finalizar de forma ordenada.
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


def normalizar_lista(resultado):
    """Adapta el resultado de una consulta a una lista de países."""
    if resultado is None:
        return []
    if isinstance(resultado, dict):
        return [resultado]
    if isinstance(resultado, (list, tuple)):
        return list(resultado)
    return []


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

    nombre = pedir_cadena("Nombre del país: ")
    if nombre is None or not nombre.strip():
        print("\n[ERROR] El nombre es obligatorio.")
        return

    poblacion = pedir_entero("Población: ")
    if poblacion is None or poblacion <= 0:
        print("\n[ERROR] La población debe ser un número entero positivo.")
        return

    superficie = pedir_entero("Superficie en km²: ")
    if superficie is None or superficie <= 0:
        print("\n[ERROR] La superficie debe ser un número entero positivo.")
        return

    continente = pedir_cadena("Continente: ")
    if continente is None or not continente.strip():
        print("\n[ERROR] El continente es obligatorio.")
        return

    agregado = agregar_pais(
        paises,
        nombre.strip(),
        poblacion,
        superficie,
        continente.strip(),
    )

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

    nombre = pedir_cadena("Nombre del país a actualizar: ")
    if nombre is None or not nombre.strip():
        print("\n[ERROR] El nombre es obligatorio.")
        return

    termino = nombre.strip()
    coincidencias = normalizar_lista(buscar_pais(paises, termino))
    exactos = [
        pais for pais in coincidencias
        if str(pais.get("nombre", "")).strip().casefold() == termino.casefold()
    ]

    if not exactos:
        if coincidencias:
            print("\nNo hay una coincidencia exacta. Países encontrados:")
            for pais in coincidencias:
                mostrar_pais(pais)
            print("Vuelva a intentarlo con el nombre exacto.")
        else:
            print(f"\n[ERROR] No se encontró ningún país llamado '{termino}'.")
        return

    pais_actual = exactos[0]
    print("\nDatos actuales:")
    mostrar_pais(pais_actual)

    poblacion = pedir_entero("Nueva población: ")
    if poblacion is None or poblacion <= 0:
        print("\n[ERROR] La población debe ser un número entero positivo.")
        return

    superficie = pedir_entero("Nueva superficie en km²: ")
    if superficie is None or superficie <= 0:
        print("\n[ERROR] La superficie debe ser un número entero positivo.")
        return

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

    termino = pedir_cadena("Ingrese el nombre o parte del nombre: ")
    if termino is None or not termino.strip():
        print("\n[ERROR] El término de búsqueda no puede estar vacío.")
        return

    termino = termino.strip()
    resultados = normalizar_lista(buscar_pais(paises, termino))

    if resultados:
        mostrar_lista(resultados, f"Resultados para '{termino}'")
    else:
        print(f"\nNo se encontraron países que coincidan con '{termino}'.")


# ---------------------------------------------------------------------------
# Opción 4: filtrar países
# ---------------------------------------------------------------------------

def filtrar_por_continente(paises):
    """Filtra los países por continente."""
    continente = pedir_cadena("Continente a filtrar (ej. América): ")
    if continente is None or not continente.strip():
        print("\n[ERROR] Debe ingresar un continente.")
        return

    continente = continente.strip()
    resultados = normalizar_lista(
        filtrar_paises(paises, continente=continente)
    )
    mostrar_lista(resultados, f"Países de {continente}")


def filtrar_por_poblacion(paises):
    """Filtra los países por un rango de población."""
    minimo = pedir_entero("Población mínima: ")
    maximo = pedir_entero("Población máxima: ")

    if minimo is None or maximo is None or minimo < 0 or maximo < 0:
        print("\n[ERROR] Los valores deben ser enteros no negativos.")
        return
    if minimo > maximo:
        print(
            "\n[ERROR] La población mínima no puede ser "
            "mayor que la máxima."
        )
        return

    resultados = normalizar_lista(
        filtrar_paises(paises, poblacion_min=minimo, poblacion_max=maximo)
    )
    mostrar_lista(
        resultados,
        f"Países con población entre {formatear_numero(minimo)} "
        f"y {formatear_numero(maximo)}",
    )


def filtrar_por_superficie(paises):
    """Filtra los países por un rango de superficie."""
    minimo = pedir_entero("Superficie mínima en km²: ")
    maximo = pedir_entero("Superficie máxima en km²: ")

    if minimo is None or maximo is None or minimo < 0 or maximo < 0:
        print("\n[ERROR] Los valores deben ser enteros no negativos.")
        return
    if minimo > maximo:
        print(
            "\n[ERROR] La superficie mínima no puede ser "
            "mayor que la máxima."
        )
        return

    resultados = normalizar_lista(
        filtrar_paises(paises, superficie_min=minimo, superficie_max=maximo)
    )
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
    print("  4. Volver al menú principal")
    print("-" * 62)

    opcion = pedir_entero("Seleccione una opción (1-4): ")
    if opcion is None or not validar_opcion(opcion, OPCIONES_FILTRO):
        print("\n[ERROR] Opción inválida.")
        return

    if opcion == 1:
        filtrar_por_continente(paises)
    elif opcion == 2:
        filtrar_por_poblacion(paises)
    elif opcion == 3:
        filtrar_por_superficie(paises)


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
    print("  4. Volver al menú principal")
    print("-" * 62)

    opcion = pedir_entero("Seleccione el criterio (1-4): ")
    if opcion is None or not validar_opcion(opcion, OPCIONES_CRITERIO):
        print("\n[ERROR] Opción inválida.")
        return

    if opcion == 4:
        return

    criterio = CRITERIOS[opcion]

    print("\n  1. Ascendente (menor a mayor)")
    print("  2. Descendente (mayor a menor)")
    sentido = pedir_entero("Seleccione el sentido (1-2): ")
    if sentido is None or not validar_opcion(sentido, OPCIONES_SENTIDO):
        print("\n[ERROR] Opción inválida.")
        return

    ascendente = sentido == 1
    ordenados = normalizar_lista(
        ordenar_paises(paises, criterio=criterio, ascendente=ascendente)
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

def mostrar_estadisticas(paises):
    """Calcula y muestra los indicadores del módulo estadisticas.py."""
    if not paises:
        print("\nNo hay países cargados para calcular estadísticas.")
        return

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
        nombre_mayor = mayor.get("nombre", "(sin nombre)")
        print(
            f"\nPaís con mayor población: {nombre_mayor} "
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


def opcion_estadisticas(paises):
    """Muestra el encabezado y los indicadores estadísticos."""
    print("=" * 62)
    print("  ESTADÍSTICAS DEL DATASET")
    print("=" * 62)
    mostrar_estadisticas(paises)


# ---------------------------------------------------------------------------
# Punto de entrada y bucle principal
# ---------------------------------------------------------------------------

def ejecutar_opcion(opcion, paises):
    """Deriva la opción elegida a la función correspondiente."""
    if opcion == 1:
        opcion_agregar(paises)
    elif opcion == 2:
        opcion_actualizar(paises)
    elif opcion == 3:
        opcion_buscar(paises)
    elif opcion == 4:
        opcion_filtrar(paises)
    elif opcion == 5:
        opcion_ordenar(paises)
    elif opcion == 6:
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
            opcion = pedir_entero("Seleccione una opción (1-7): ")

            if opcion is None or not validar_opcion(opcion, OPCIONES_MENU):
                print(
                    "\n[ERROR] Opción inválida. "
                    "Ingrese un número del 1 al 7."
                )
                pausar()
                continue

            if opcion == 7:
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
            print(f"\n[ERROR] {error}")
            pausar()
        except Exception as error:
            print(f"\n[ERROR] Ocurrió un problema inesperado: {error}")
            pausar()

    print("\nFin del programa.")


if __name__ == "__main__":
    main()



