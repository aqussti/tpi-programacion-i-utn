"""Indicadores de población, superficie y distribución por continente."""


def pais_mayor_poblacion(paises):
    """Devuelve el país más poblado, o None si no hay países.

    En caso de empate, devuelve el primero de la lista.
    """
    if not paises:
        return None

    mayor = paises[0]
    for pais in paises:
        if pais["poblacion"] > mayor["poblacion"]:
            mayor = pais
    return mayor


def pais_menor_poblacion(paises):
    """Devuelve el país menos poblado, o None si no hay países.

    En caso de empate, devuelve el primero de la lista.
    """
    if not paises:
        return None

    menor = paises[0]
    for pais in paises:
        if pais["poblacion"] < menor["poblacion"]:
            menor = pais
    return menor


def promedio_poblacion(paises):
    """Calcula la media de población; devuelve None para una lista vacía."""
    if not paises:
        return None

    total = 0
    for pais in paises:
        total += pais["poblacion"]
    return total / len(paises)


def promedio_superficie(paises):
    """Calcula la media de superficie en km², o None si no hay países."""
    if not paises:
        return None

    total = 0
    for pais in paises:
        total += pais["superficie"]
    return total / len(paises)


def contar_por_continente(paises):
    """Devuelve las cantidades por continente, usando nombres ya normalizados."""
    cantidades = {}
    for pais in paises:
        continente = pais["continente"]
        if continente not in cantidades:
            cantidades[continente] = 0
        cantidades[continente] += 1
    return cantidades


def calcular_estadisticas(paises):
    """Reúne los indicadores sin imprimir ni modificar los datos recibidos.

    Recibe países validados, con población y superficie enteras y nombres
    de continente uniformes. Con una lista vacía, los extremos y promedios
    son None y el conteo por continente es un diccionario vacío.
    """
    return {
        "mayor_poblacion": pais_mayor_poblacion(paises),
        "menor_poblacion": pais_menor_poblacion(paises),
        "promedio_poblacion": promedio_poblacion(paises),
        "promedio_superficie": promedio_superficie(paises),
        "cantidad_por_continente": contar_por_continente(paises),
    }
