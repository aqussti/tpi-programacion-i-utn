"""
validaciones.py
Funciones reutilizables para validar entradas del usuario.
Todos los módulos del TPI pueden importarlas.
Cada función tiene una única responsabilidad.
"""


def pedir_texto_no_vacio(mensaje):
    """Pide un texto por consola hasta que no esté vacío. Devuelve el texto sin espacios sobrantes."""
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("Error: el campo no puede estar vacío.")


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
