import unittest
import sys
sys.path.append("..")
from cifrado_descifrado.descifrado import *

descifrado=descifrado()

class test(unittest.TestCase):

	'''Clase prueba usada para probar cada una de las funciones de la clase descifrado.
    
	Metodos:
		test_polinomios_base(self)
			revisa que los polinomios base sean calculados correctamente
		test_forma_lagrange(self):
			revisa que dada la lista de polinomios base y evaaluaciones, calcule correctamente a k
		test_descifra_archivo(self)
			revisa que el archivo se haya descifrado de manera correcta comparando su
			contenido con el archivo original'''


	def test_polinomios_base(self):
		a=descifrado.polinomios_base("evaluaciones_prueba.txt")
		P_i=[1,3,-3,1]
		self.assertEqual(a,P_i)

	def test_forma_lagrange(self):
		p=descifrado.polinomios_base("evaluaciones_prueba.txt")
		a=descifrado.forma_lagrange("evaluaciones_prueba.txt",p)
		k=85760135360152140931000324643647336360276469685010011892589949052914622207615
		self.assertEqual(a,k)

	def test_descifra_archivo(self):
		archivo_cifrado_prueba="archivo_claro2.aes"
		k = 85760135360152140931000324643647336360276469685010011892589949052914622207615
		descifrado.descifra_archivo(k,archivo_cifrado_prueba)
		archivo_cifrado=open("documentos/"+archivo_cifrado_prueba,"rb")
		archivo_sin_cifrar=open("documentos/archivo_claro2.txt","rb")
		for linea in archivo_cifrado :
			for linea1 in archivo_sin_cifrar:
				self.assertNotEqual(linea,str(linea1))
		archivo_sin_cifrar.close()
		archivo_cifrado.close()


if __name__ == "main":
    unittest.main()
