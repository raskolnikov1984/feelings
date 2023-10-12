from process_text import ProcesarTexto
import unittest


class TestProcesarTexto(unittest.TestCase):
    def setUp(self):
        self.nube_palabras = 'data/nube_palabras_base.csv'
        self.propuesta = 'data/albert_yordano_corredor.txt'
        self.procesador = ProcesarTexto(
            self.propuesta, self.nube_palabras)

    def test_1(self):
        """Crear Instancia de ProcesarTexto"""
        self.assertIsInstance(self.procesador, ProcesarTexto)

    def test_2(self):
        """Leer por lineas propuesta"""
        pg_propuesta_uno = self.procesador.leer_archivo_por_lineas()
        self.assertIsInstance(pg_propuesta_uno, list)

    def test_3(self):
        """Cargar en una lista las secuencias de palbras"""
        secuencia_palabras = self.procesador.cargar_columna_csv()
        self.assertIsInstance(secuencia_palabras, list)

    def test_tokenizar_palabras_spanish(self):
        texto = "Hola, este es un ejemplo de tokenización de palabras."
        resultado = self.procesador.tokenizar_texto(texto)
        self.assertIsInstance(resultado, list)
        self.assertTrue(all(isinstance(token, str) for token in resultado))

    def test_extraer_cadenas(self):
        # Prueba la función con una cadena que contiene cadenas entre corchetes
        cadena = '[cadena1]-[cadena2]-[cadena3]'
        resultado = self.procesador.extraer_cadenas_entre_corchetes(cadena)

        # Verifica si el resultado es una lista
        self.assertIsInstance(resultado, list)

        # Verifica si las cadenas esperadas están en el resultado
        self.assertIn('cadena1', resultado)
        self.assertIn('cadena2', resultado)
        self.assertIn('cadena3', resultado)

    def test_sin_cadenas_entre_corchetes(self):
        """
        Prueba la función con una cadena que no contiene
        cadenas entre corchetes
        """
        cadena = 'Esta cadena no tiene corchetes.'
        resultado = self.procesador.extraer_cadenas_entre_corchetes(cadena)

        # Verifica si el resultado es una lista vacía
        self.assertIsInstance(resultado, list)
        self.assertEqual(len(resultado), 0)

    def test_tokenizar_oraciones_spanish(self):
        texto = "¡Hola! Esto es una oración de ejemplo. Y esta es otra."
        resultado = self.procesador.tokenizar_texto(texto, tipo='oraciones')
        self.assertIsInstance(resultado, list)
        self.assertTrue(all(
            isinstance(oracion, str) for oracion in resultado))

    def test_tokenizar_tipo_invalido(self):
        texto = "Este es un ejemplo."
        with self.assertRaises(ValueError):
            self.procesador.tokenizar_texto(texto, tipo='invalido')

    def test_flujo_principal(self):

        procesador = ProcesarTexto(self.propuesta,
                                   self.nube_palabras)
        coincidencias = procesador.run()

        self.assertIsInstance(coincidencias, list)


if __name__ == 'main':
    unittest.main()
