"""Pruebas del sistema con archivos temporales; no modifica el dataset base."""
import contextlib
import copy
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import consultas
import datos
import main
import validaciones
from estadisticas import calcular_estadisticas
from ordenar import ordenar_paises


class PruebasSistema(unittest.TestCase):
    def setUp(self):
        self.temporal = tempfile.TemporaryDirectory(dir=Path(__file__).parent)
        self.addCleanup(self.temporal.cleanup)
        self.ruta = Path(self.temporal.name) / "paises.csv"
        self.paises = datos.leer_paises()
        self.addCleanup(patch.stopall)
        patch("datos.ARCHIVO_CSV", self.ruta).start()
        self.salida = io.StringIO()
        contexto = contextlib.redirect_stdout(self.salida)
        contexto.__enter__()
        self.addCleanup(contexto.__exit__, None, None, None)

    def ejecutar(self, funcion, entradas, paises=None):
        with patch("builtins.input", side_effect=entradas):
            funcion(self.paises if paises is None else paises)

    def test_dataset(self):
        self.assertEqual(len(self.paises), 19)
        self.assertTrue(all(isinstance(p["poblacion"], int) for p in self.paises))

    def test_alta_y_actualizacion_persisten(self):
        self.ejecutar(main.opcion_agregar, ["Portugal", "100", "90", "europa"])
        self.assertEqual(datos.leer_paises(self.ruta)[-1]["continente"], "Europa")
        self.ejecutar(main.opcion_actualizar, ["portugal", "200", "99"])
        self.assertEqual(datos.leer_paises(self.ruta)[-1]["poblacion"], 200)

    def test_normalizacion_y_duplicados(self):
        self.assertTrue(datos.agregar_pais(self.paises, "Prueba", 1, 1, "america"))
        self.assertEqual(self.paises[-1]["continente"], "América")
        self.assertEqual(calcular_estadisticas(self.paises)["cantidad_por_continente"]["América"], 7)
        self.assertFalse(datos.agregar_pais(self.paises, "japon", 1, 1, "asia"))
        for entrada, esperado in [("AFRICA", "África"), ("oceania", "Oceanía")]:
            self.assertEqual(validaciones.normalizar_continente(entrada), esperado)

    def test_rechazo_datos_invalidos(self):
        copia = copy.deepcopy(self.paises)
        for valor in (0, -1, "abc", "1.2", 1.9, True):
            self.assertFalse(datos.agregar_pais(self.paises, "Prueba", valor, 1, "Asia"))
        self.assertFalse(datos.agregar_pais(self.paises, " ", 1, 1, "Asia"))
        self.assertFalse(datos.agregar_pais(self.paises, "Prueba", 1, 1, "otro"))
        self.assertFalse(datos.actualizar_pais(self.paises, "No existe", 1, 1))
        self.assertEqual(self.paises, copia)

    def test_guardado_fallido_no_modifica_memoria_ni_archivo(self):
        datos.guardar_paises(self.paises)
        original = self.ruta.read_bytes()
        copia = copy.deepcopy(self.paises)
        with patch("datos.os.replace", side_effect=OSError("Sin permiso")):
            self.assertFalse(datos.agregar_pais(self.paises, "Prueba", 1, 1, "Asia"))
            self.assertFalse(datos.actualizar_pais(self.paises, "Argentina", 1, 1))
        self.assertEqual(self.paises, copia)
        self.assertEqual(self.ruta.read_bytes(), original)
        self.assertEqual(list(self.ruta.parent.iterdir()), [self.ruta])

    def test_csv_invalido(self):
        cabecera = "nombre,poblacion,superficie,continente\n"
        for texto in ("incorrecto\n", cabecera + "X,abc,1,Asia\n",
                      cabecera + "X,1,1\n", cabecera + "X,1,1,Asia,extra\n",
                      cabecera + "X,1,1,Asia\nx,1,1,Asia\n",
                      cabecera + "X,-1,1,Asia\n"):
            self.ruta.write_text(texto, encoding="utf-8")
            with self.assertRaises(ValueError):
                datos.leer_paises(self.ruta)

    def test_arranque_con_csv_invalido_no_sobrescribe(self):
        self.ruta.write_text("incorrecto\n", encoding="utf-8")
        with patch("main.configurar_consola"), patch("main.limpiar_consola"):
            main.main()
        self.assertIn("No se modificaron", self.salida.getvalue())
        self.assertEqual(self.ruta.read_text(encoding="utf-8"), "incorrecto\n")

    def test_busquedas(self):
        self.assertEqual(consultas.buscar_por_nombre(self.paises, "japon", True)[0]["nombre"], "Japón")
        self.assertEqual(len(consultas.buscar_por_nombre(self.paises, "ar")), 1)
        self.assertEqual(consultas.buscar_por_nombre(self.paises, "ar", True), [])
        self.assertEqual(consultas.buscar_por_nombre(self.paises, ""), [])
        self.ejecutar(main.opcion_buscar, ["japon", "2"])
        self.assertIn("Japón", self.salida.getvalue())

    def test_filtros_y_limites(self):
        self.assertEqual(len(consultas.filtrar_por_continente(self.paises, "america")), 6)
        p = self.paises[0]
        for campo, funcion in [("poblacion", consultas.filtrar_por_poblacion),
                               ("superficie", consultas.filtrar_por_superficie)]:
            self.assertIn(p, funcion(self.paises, p[campo], p[campo]))
            self.assertEqual(funcion(self.paises, 10, 1), [])
        self.ejecutar(main.opcion_filtrar, ["1", "1"])
        self.ejecutar(main.opcion_filtrar, ["2", "0", "5000000"])
        self.ejecutar(main.opcion_filtrar, ["3", "0", "200000"])
        self.assertIn("Uruguay", self.salida.getvalue())

    def test_ordenamientos_estables(self):
        copia = copy.deepcopy(self.paises)
        for campo in ("nombre", "poblacion", "superficie"):
            for asc in (True, False):
                clave = lambda p: p[campo].casefold() if campo == "nombre" else p[campo]
                self.assertEqual(ordenar_paises(self.paises, campo, asc),
                                 sorted(self.paises, key=clave, reverse=not asc))
        self.assertEqual(self.paises, copia)
        empate = [dict(nombre="a", poblacion=1), dict(nombre="b", poblacion=1)]
        self.assertEqual(ordenar_paises(empate, "poblacion", False), empate)
        self.ejecutar(main.opcion_ordenar, ["2", "2"])
        with self.assertRaises(ValueError):
            ordenar_paises([], "otro")

    def test_estadisticas(self):
        r = calcular_estadisticas(self.paises)
        self.assertEqual(r["mayor_poblacion"]["nombre"], "China")
        self.assertEqual(r["menor_poblacion"]["nombre"], "Uruguay")
        self.assertEqual(r["cantidad_por_continente"], {"América": 6, "Europa": 4, "Asia": 4, "África": 3, "Oceanía": 2})
        self.assertEqual(r["promedio_poblacion"], sum(p["poblacion"] for p in self.paises) / 19)
        self.assertEqual(r["promedio_superficie"], sum(p["superficie"] for p in self.paises) / 19)
        main.opcion_estadisticas(self.paises)

    def test_listas_vacias(self):
        self.assertEqual(ordenar_paises([]), [])
        self.assertIsNone(calcular_estadisticas([])["promedio_poblacion"])
        for funcion in (main.opcion_buscar, main.opcion_filtrar, main.opcion_ordenar,
                        main.opcion_actualizar, main.opcion_estadisticas):
            funcion([])
        self.assertIn("No hay países", self.salida.getvalue())

    def test_validaciones_interactivas(self):
        with patch("builtins.input", side_effect=["abc", "-1", "1.2", "0", "5"]):
            self.assertEqual(validaciones.pedir_entero_positivo("Número: "), 5)
        with patch("builtins.input", side_effect=[" ", " Hola "]):
            self.assertEqual(validaciones.pedir_texto_no_vacio("Texto: "), "Hola")
        with patch("builtins.input", side_effect=["8", "1", "0", "10"]):
            self.assertEqual(validaciones.pedir_rango("Mínimo", "Máximo"), (0, 10))

    def test_menu_completo_y_salida(self):
        datos.guardar_paises(self.paises)
        entradas = ["", "99", "3", "argen", "1", "", "4", "1", "1", "",
                    "5", "1", "1", "", "6", "", "7"]
        with patch("main.configurar_consola"), patch("main.limpiar_consola"), patch("builtins.input", side_effect=entradas):
            main.main()
        self.assertIn("opción inválida", self.salida.getvalue())
        self.assertIn("Fin del programa", self.salida.getvalue())
        self.assertIn("China", self.salida.getvalue())


if __name__ == "__main__":
    unittest.main()
