import unittest
from request import doRequest

class test(unittest.TestCase):
    """Clase prueba usada para probar las peticiones hechas
    de forma independiente.
    
    Metodos:
        test_ciudad_invalida(self)
            verifica que sucede cuando se busca una ciudad inexistente
            para la API de OpenWeather
        test_ciudad_invalida(self)
            verifica que sucede cuando se busca una ciudad valida
            dentro de la API de OpenWeather"""
    
    def test_ciudad_invalida(self):
        ciudad = "ciudad X"
        self.assertEqual(doRequest(ciudad), ", Ciudad inválida")
        print(doRequest(ciudad))

    def test_ciudad_valida(self):
        ciudad = "México"
        self.assertNotEqual(doRequest(ciudad), ", Ciudad inválida")
        print(doRequest(ciudad))

if __name__ == 'main':
    unittest.main()