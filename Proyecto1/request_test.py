import unittest
from request import doRequest
from main import lee

class test(unittest.TestCase):
    """Clase prueba usada para probar las peticiones hechas
    de forma independiente.
    
    Metodos:
        test_ciudad_invalida(self)
            verifica que sucede cuando se busca una ciudad inexistente
            para la API de OpenWeather
        test_ciudad_invalida(self)
            verifica que sucede cuando se busca una ciudad valida
            dentro de la API de OpenWeather
        test_ciudad_mayusculas(self)
            verifica que sucede cuando el nombre de la ciudad
            buscada esta escrito unicamente en mayusculas
        test_ciudad_minusculas(self)
            verifica que sucede cuando el nombre de la ciudad
            buscada esta escrito unicamente en minusculas"""
    
    def test_ciudad_invalida(self):
        ciudad = "ciudad X"
        self.assertEqual(doRequest(ciudad), ", Ciudad inválida")
        print(doRequest(ciudad))

    def test_ciudad_valida(self):
        ciudad = "México"
        self.assertNotEqual(doRequest(ciudad), ", Ciudad inválida")
        print(doRequest(ciudad))

    def test_ciudad_mayusculas(self):
        ciudad = "CHICAGO"
        self.assertNotEqual(doRequest(ciudad), ", Ciudad inválida")
        print(doRequest(ciudad))

    def test_ciudad_minusculas(self):
        ciudad = "singapore"
        self.assertNotEqual(doRequest(ciudad), ", Ciudad inválida")
        print(doRequest(ciudad))

    def test_archivo_nulo(self):
        archivo = None
        self.assertEqual(lee(archivo), None)

if __name__ == 'main':
    unittest.main()