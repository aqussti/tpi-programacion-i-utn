
"""
validaciones.py
Funciones reutilizables para validar entradas del usuario.
Todos los módulos del TPI pueden importarlas.
Cada función tiene una única responsabilidad.
"""

import unicodedata


def normalizar_texto(texto):
    """Normaliza espacios, mayúsculas y tildes para comparar nombres."""
    texto = unicodedata.normalize("NFD", texto.strip().casefold())
    return "".join(c for c in texto if unicodedata.category(c) != "Mn")


def validar_nombre_pais(nombre):
    """Comprueba que el nombre contenga letras, espacios, guiones o apóstrofes."""
    if not isinstance(nombre, str) or not nombre.strip():
        raise ValueError("El nombre del país es obligatorio.")

    nombre = nombre.strip()

    if not all(
        unicodedata.category(c).startswith("L")
        or c.isspace()
        or c in "-'’"
        for c in nombre
    ):
        raise ValueError("El nombre del país solo puede contener letras, espacios y guiones.")

    if not any(unicodedata.category(c).startswith("L") for c in nombre):
        raise ValueError("El nombre debe contener al menos una letra.")

    return nombre.title()


def normalizar_continente(texto):
    """Devuelve la escritura común del continente o informa un valor inválido."""
    continentes = {
        "america": "América", "europa": "Europa", "asia": "Asia",
        "africa": "África", "oceania": "Oceanía", "antartida": "Antártida",
    }
    clave = normalizar_texto(texto)
    if clave not in continentes:
        raise ValueError("Continente inválido. Use América, Europa, Asia, África, Oceanía o Antártida.")
    return continentes[clave]


def entero_positivo(valor):
    """Convierte enteros o texto entero; rechaza decimales y booleanos."""
    if isinstance(valor, bool) or not isinstance(valor, (int, str)):
        raise ValueError("El valor debe ser un número entero positivo.")
    try:
        numero = int(valor)
    except ValueError:
        raise ValueError("El valor debe ser un número entero positivo.") from None
    if numero <= 0:
        raise ValueError("El valor debe ser un número entero positivo.")
    return numero


def pedir_texto_no_vacio(mensaje):
    """Pide un texto por consola hasta que no esté vacío. Devuelve el texto sin espacios sobrantes."""
    while True:
        try:
            texto = validar_nombre_pais(input(mensaje))
            return texto
        except ValueError as error:
            print(f"Error: {error}")


def pedir_entero_positivo(mensaje, permitir_cero=False):
    """Pide un número entero positivo. Repite hasta que el valor sea válido."""
    while True:
        entrada = input(mensaje).strip()
        try:
            numero = int(entrada)
        except ValueError:
            print("Error: debe ingresar un número entero (sin letras ni decimales).")
            continue

        if numero > 0 or (permitir_cero and numero == 0):
            return numero
        print("Error: el número debe ser mayor que cero." if not permitir_cero
              else "Error: el número no puede ser negativo.")


def pedir_rango(mensaje_min, mensaje_max):
    """
    Pide un valor mínimo y uno máximo (enteros no negativos).
    Valida que mínimo <= máximo. Devuelve una tupla (minimo, maximo).
    """
    while True:
        minimo = pedir_entero_positivo(mensaje_min, permitir_cero=True)
        maximo = pedir_entero_positivo(mensaje_max, permitir_cero=True)

        if minimo <= maximo:
            return minimo, maximo
        print("Error: el mínimo no puede ser mayor que el máximo. Intente de nuevo.")


def pedir_opcion_menu(mensaje, opciones_validas):
    """
    Pide una opción de menú y verifica que esté entre las válidas.
    opciones_validas: lista de strings, por ejemplo ["1", "2", "3", "0"].
    """
    while True:
        opcion = input(mensaje).strip()
        if opcion in opciones_validas:
            return opcion
        print(f"Error: opción inválida. Elija una de: {', '.join(opciones_validas)}.")
