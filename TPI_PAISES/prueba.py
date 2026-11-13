import datos

paises = datos.leer_paises()

print("\n--- PRUEBAS DE VALIDACIÓN ---")

# Nombre vacío
datos.agregar_pais(paises, "", 1000, 1000, "Europa")

# Población negativa
datos.agregar_pais(paises, "Prueba", -100, 1000, "Europa")

# Superficie negativa
datos.agregar_pais(paises, "Prueba", 1000, -100, "Europa")

# País inexistente
datos.actualizar_pais(paises, "Atlantis", 1000, 1000)