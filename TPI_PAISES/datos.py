
import csv
from pathlib import Path

# Ruta del archivo CSV, ubicado en la misma carpeta que datos.py
ARCHIVO_CSV = Path(__file__).with_name("paises.csv")

# Columnas obligatorias del archivo
COLUMNAS = ["nombre", "poblacion", "superficie", "continente"]


def leer_paises(ruta=ARCHIVO_CSV):
    """
    Lee los países desde un archivo CSV.
    Devuelve una lista de diccionarios.
    """

    paises = []

    try:
        with open(ruta, "r", encoding="utf-8-sig", newline="") as archivo:
            lector = csv.DictReader(archivo)

            if lector.fieldnames != COLUMNAS:
                raise ValueError("Las columnas del CSV no son correctas.")

            for numero_linea, fila in enumerate(lector, start=2):

                # Controlar campos vacíos o columnas adicionales
                if None in fila or any(
                    fila.get(campo) is None or not fila[campo].strip()
                    for campo in COLUMNAS
                ):
                    raise ValueError(
                        f"Datos incompletos en la línea {numero_linea}."
                    )

                try:
                    poblacion = int(fila["poblacion"])
                    superficie = int(fila["superficie"])
                except ValueError:
                    raise ValueError(
                        f"Población o superficie inválida "
                        f"en la línea {numero_linea}."
                    )

                if poblacion <= 0 or superficie <= 0:
                    raise ValueError(
                        f"Los valores deben ser positivos "
                        f"en la línea {numero_linea}."
                    )

                pais = {
                    "nombre": fila["nombre"].strip(),
                    "poblacion": poblacion,
                    "superficie": superficie,
                    "continente": fila["continente"].strip()
                }

                paises.append(pais)

        print("Países cargados correctamente.")
        return paises

    except FileNotFoundError:
        print("Error: no se encontró el archivo CSV.")
        return []

    except (OSError, csv.Error, ValueError) as error:
        print(f"Error al leer el archivo: {error}")
        return []


def guardar_paises(paises, ruta=ARCHIVO_CSV):
    """
    Guarda una lista de países en un archivo CSV.
    """

    try:
        with open(ruta, "w", encoding="utf-8", newline="") as archivo:

            escritor = csv.DictWriter(
                archivo,
                fieldnames=COLUMNAS
            )

            escritor.writeheader()
            escritor.writerows(paises)

        print("Datos guardados correctamente.")
        return True

    except (OSError, csv.Error) as error:
        print(f"Error al guardar los datos: {error}")
        return False


def agregar_pais(paises, nombre, poblacion, superficie, continente):
    """
    Agrega un país nuevo a la lista y guarda los cambios.
    """

    nombre = nombre.strip()
    continente = continente.strip()

    if not nombre or not continente:
        print("Error: el nombre y el continente son obligatorios.")
        return False

    try:
        poblacion = int(poblacion)
        superficie = int(superficie)
    except (ValueError, TypeError):
        print("Error: población y superficie deben ser números enteros.")
        return False

    if poblacion <= 0 or superficie <= 0:
        print("Error: los valores deben ser positivos.")
        return False

    # Evitar países duplicados
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print("Error: el país ya existe.")
            return False

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    nuevos_datos = paises + [nuevo_pais]

    if guardar_paises(nuevos_datos):
        paises.append(nuevo_pais)
        print(f"País {nombre} agregado correctamente.")
        return True

    return False


def actualizar_pais(paises, nombre, nueva_poblacion, nueva_superficie):
    """
    Actualiza la población y superficie de un país.
    """

    try:
        nueva_poblacion = int(nueva_poblacion)
        nueva_superficie = int(nueva_superficie)
    except (ValueError, TypeError):
        print("Error: los valores deben ser números enteros.")
        return False

    if nueva_poblacion <= 0 or nueva_superficie <= 0:
        print("Error: los valores deben ser positivos.")
        return False

    nuevos_datos = [pais.copy() for pais in paises]

    for pais in nuevos_datos:

        if pais["nombre"].lower() == nombre.strip().lower():

            pais["poblacion"] = nueva_poblacion
            pais["superficie"] = nueva_superficie

            if guardar_paises(nuevos_datos):
                paises[:] = nuevos_datos
                print(f"Datos de {pais['nombre']} actualizados correctamente.")
                return True

            return False

    print("Error: no se encontró el país.")
    return False
