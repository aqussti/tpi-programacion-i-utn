"""Ordenamiento de países por nombre, población o superficie."""


def ordenar_paises(paises, criterio="nombre", ascendente=True):
    """Devuelve una nueva lista ordenada mediante inserción.

    Recibe registros ya validados, con población y superficie enteras.
    No modifica la lista original ni los diccionarios. En caso de empate,
    conserva el orden de entrada. Los nombres se comparan sin distinguir
    mayúsculas y minúsculas, manteniendo sus tildes.
    """
    if criterio not in ("nombre", "poblacion", "superficie"):
        raise ValueError("El criterio debe ser nombre, poblacion o superficie.")
    if not isinstance(ascendente, bool):
        raise ValueError("El sentido ascendente debe ser True o False.")

    ordenados = paises.copy()

    for i in range(1, len(ordenados)):
        actual = ordenados[i]
        valor_actual = actual[criterio]
        if criterio == "nombre":
            valor_actual = valor_actual.casefold()

        j = i - 1
        # Desplaza los elementos hasta encontrar el lugar del país actual.
        while j >= 0:
            valor_anterior = ordenados[j][criterio]
            if criterio == "nombre":
                valor_anterior = valor_anterior.casefold()

            desplazar = (ascendente and valor_anterior > valor_actual) or (
                not ascendente and valor_anterior < valor_actual
            )
            if not desplazar:
                break

            ordenados[j + 1] = ordenados[j]
            j -= 1

        ordenados[j + 1] = actual

    return ordenados
