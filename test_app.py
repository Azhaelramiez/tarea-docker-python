import unittest
import app  # Esto ya lo tienes

class TestApp(unittest.TestCase):
    def test_app_logic(self):
        # LLAMA a la función de tu app aquí:
        resultado = app.hola_mundo() 
        self.assertEqual(resultado, "Esperado")