"""Lectura, escritura y actualización del dataset de países."""
import csv
import os
import tempfile
from pathlib import Path
from validaciones import entero_positivo, normalizar_continente, normalizar_texto

ARCHIVO_CSV = Path(__file__).with_name("paises.csv")
COLUMNAS = ["nombre", "poblacion", "superficie", "continente"]


def validar_pais(nombre, poblacion, superficie, continente):
    """Construye un registro válido con los tipos y nombres comunes."""
    if not isinstance(nombre, str) or not nombre.strip():
        raise ValueError("El nombre del país es obligatorio.")
    if not isinstance(continente, str):
        raise ValueError("El continente debe ser un texto.")
    return {"nombre": nombre.strip(), "poblacion": entero_positivo(poblacion),
            "superficie": entero_positivo(superficie),
            "continente": normalizar_continente(continente)}


def leer_paises(ruta=None):
    """Lee el CSV. Un archivo inválido genera un error y no se sobrescribe."""
    ruta = ARCHIVO_CSV if ruta is None else Path(ruta)
    paises = []
    nombres = set()
    with open(ruta, "r", encoding="utf-8-sig", newline="") as archivo:
        lector = csv.DictReader(archivo, strict=True)
        if lector.fieldnames != COLUMNAS:
            raise ValueError("Las columnas del CSV no son correctas.")
        for numero_linea, fila in enumerate(lector, start=2):
            if None in fila or any(fila.get(c) is None for c in COLUMNAS):
                raise ValueError(f"Cantidad de campos incorrecta en la línea {numero_linea}.")
            try:
                pais = validar_pais(**fila)
                clave = normalizar_texto(pais["nombre"])
                if clave in nombres:
                    raise ValueError("País duplicado.")
            except ValueError as error:
                raise ValueError(f"Línea {numero_linea}: {error}") from error
            nombres.add(clave)
            paises.append(pais)
    return paises


def guardar_paises(paises, ruta=None):
    """Reemplaza el CSV solo después de validar y escribir todos los registros."""
    ruta = ARCHIVO_CSV if ruta is None else Path(ruta)
    temporal = None
    try:
        registros = []
        nombres = set()
        for pais in paises:
            registro = validar_pais(**pais)
            clave = normalizar_texto(registro["nombre"])
            if clave in nombres:
                raise ValueError("No se pueden guardar países duplicados.")
            nombres.add(clave)
            registros.append(registro)
        # El temporal está en la misma carpeta para permitir el reemplazo.
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", newline="",
                                         dir=ruta.parent, delete=False) as archivo:
            temporal = Path(archivo.name)
            escritor = csv.DictWriter(archivo, fieldnames=COLUMNAS)
            escritor.writeheader()
            escritor.writerows(registros)
        os.replace(temporal, ruta)
        return True
    except (OSError, csv.Error, ValueError, TypeError) as error:
        print(f"Error al guardar los datos: {error}")
        return False
    finally:
        if temporal is not None and temporal.exists():
            try:
                temporal.unlink()
            except OSError:
                # Un fallo de limpieza no debe ocultar el error de guardado.
                pass


def agregar_pais(paises, nombre, poblacion, superficie, continente, ruta=None):
    """Agrega un país sin duplicados y conserva la memoria si falla el guardado."""
    try:
        nuevo = validar_pais(nombre, poblacion, superficie, continente)
    except ValueError as error:
        print(f"Error: {error}")
        return False
    if any(normalizar_texto(p["nombre"]) == normalizar_texto(nuevo["nombre"])
           for p in paises):
        print("Error: el país ya existe.")
        return False
    if guardar_paises(paises + [nuevo], ruta):
        paises.append(nuevo)
        return True
    return False


def actualizar_pais(paises, nombre, nueva_poblacion, nueva_superficie, ruta=None):
    """Actualiza población y superficie solo si el guardado funciona."""
    try:
        poblacion = entero_positivo(nueva_poblacion)
        superficie = entero_positivo(nueva_superficie)
    except ValueError as error:
        print(f"Error: {error}")
        return False
    nuevos = [p.copy() for p in paises]
    for pais in nuevos:
        if normalizar_texto(pais["nombre"]) == normalizar_texto(nombre):
            pais["poblacion"] = poblacion
            pais["superficie"] = superficie
            if guardar_paises(nuevos, ruta):
                paises[:] = nuevos
                return True
            return False
    print("Error: no se encontró el país.")
    return False
