import unittest
import sys
sys.path.append("..")
from cifrado_descifrado.cifrado import *

cifrado = cifrado()

class test(unittest.TestCase):
    """Clase prueba usada para probar cada una de las funciones de la clase cifrado.
    
    Metodos:
        test_hashea_contraseña(self)
            revisa que la contraseña dada sea convertida a decimal de manera correcta.
        test_evaluaciones(self)
            revisa que cada una de las evaluaciones del polinomio esten bien
            hechas revisandolas linea por linea y comparandolas con el calculo
            hecho a mano
        test_archivo_cifrado(self)
            revisa que el archivo se haya cifrado de manera correcta comparando su
            contenido con el archivo original"""

    def test_hashea_contraseña(self):
        contraseña = "cifrado23-y01"
        self.assertEqual(cifrado.hashea_contraseña(contraseña), 85760135360152140931000324643647336360276469685010011892589949052914622207615)

    def test_evaluaciones(self):
        archivo = "documentos/evaluaciones_prueba.txt"
        t = "2"
        n = "3"
        k = 85760135360152140931000324643647336360276469685010011892589949052914622207615
        cifrado.genera_evaluaciones(archivo, n, t, k)
        archivo_prueba = open("documentos/evaluaciones_prueba.txt", "r")
        aux = 1
        for linea in archivo_prueba:
            lista_ev = linea.split(sep=', ')
            parentesis = lista_ev[1].index(")")
            evaluacion = lista_ev[1][0:parentesis]
            self.assertEqual(evaluacion, str(k + aux))
            aux += 1
        archivo_prueba.close()
        
    def test_archivo_cifrado(self):
        archivo_claro_prueba = "archivo_claro.txt"
        k = 85760135360152140931000324643647336360276469685010011892589949052914622207615
        cifrado.cifra_documento(k,archivo_claro_prueba)
        archivo_sin_cifrar = open("documentos/"+archivo_claro_prueba, "rb")
        archivo_cifrado = open("documentos/archivo_claro.aes", "rb")
        for linea in archivo_sin_cifrar:
            for linea1 in archivo_cifrado:
                self.assertNotEqual(linea, str(linea1))
        archivo_cifrado.close()
        archivo_sin_cifrar.close()

if __name__ == "main":
    unittest.main()

