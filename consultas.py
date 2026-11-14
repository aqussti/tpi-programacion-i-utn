"""
consultas.py
Búsqueda y filtrado de países.
Cada país es un diccionario:
    {"nombre": str, "poblacion": int, "superficie": int, "continente": str}
Las funciones reciben la lista de países y devuelven una NUEVA lista
con los resultados (nunca modifican la lista original).
Si no hay resultados devuelven una lista vacía; el menú decide qué mensaje mostrar.
"""

import unicodedata


def normalizar(texto):
    """Pasa a minúsculas y quita tildes para comparar sin importar el formato.
    Ej: 'América' -> 'america'."""
    texto = texto.strip().lower()
    descompuesto = unicodedata.normalize("NFD", texto)
    return "".join(c for c in descompuesto if unicodedata.category(c) != "Mn")


def buscar_por_nombre(paises, texto, exacta=False):
    """
    Busca países por nombre.
    - exacta=True: el nombre debe coincidir completo.
    - exacta=False: alcanza con que el texto esté contenido en el nombre.
    """
    buscado = normalizar(texto)
    if not buscado:
        return []

    resultados = []
    for pais in paises:
        nombre = normalizar(pais["nombre"])
        if exacta:
            if nombre == buscado:
                resultados.append(pais)
        else:
            if buscado in nombre:
                resultados.append(pais)
    return resultados


def filtrar_por_continente(paises, continente):
    """Devuelve los países del continente indicado (ignora mayúsculas y tildes)."""
    buscado = normalizar(continente)
    return [p for p in paises if normalizar(p["continente"]) == buscado]


def filtrar_por_rango(paises, campo, minimo, maximo):
    """
    Filtro genérico: devuelve los países cuyo 'campo' numérico
    está entre minimo y maximo (ambos incluidos).
    """
    if minimo > maximo:
        return []
    return [p for p in paises if minimo <= p[campo] <= maximo]


def filtrar_por_poblacion(paises, minimo, maximo):
    """Países con población dentro del rango indicado."""
    return filtrar_por_rango(paises, "poblacion", minimo, maximo)


def filtrar_por_superficie(paises, minimo, maximo):
    """Países con superficie (km²) dentro del rango indicado."""
    return filtrar_por_rango(paises, "superficie", minimo, maximo)


def obtener_continentes(paises):
    """Lista de continentes distintos presentes en el dataset (útil para mostrar opciones)."""
    return sorted({p["continente"] for p in paises})


# Prueba rápida: se ejecuta solo si corrés este archivo directamente
if __name__ == "__main__":
    datos = [
        {"nombre": "Argentina", "poblacion": 45376763, "superficie": 2780400, "continente": "América"},
        {"nombre": "Japón", "poblacion": 125800000, "superficie": 377975, "continente": "Asia"},
        {"nombre": "Brasil", "poblacion": 213993437, "superficie": 8515767, "continente": "América"},
        {"nombre": "Alemania", "poblacion": 83149300, "superficie": 357022, "continente": "Europa"},
    ]
    print(buscar_por_nombre(datos, "ar"))
    print(buscar_por_nombre(datos, "japon", exacta=True))
    print(filtrar_por_continente(datos, "america"))
    print(filtrar_por_poblacion(datos, 50_000_000, 150_000_000))
    print(filtrar_por_superficie(datos, 0, 400_000))
