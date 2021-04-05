from fractions import Fraction
import os
import hashlib
import sys
from Crypto.Cipher import AES
import numpy as np

"""primo: variable global. Número primo de 257 bits para realizar operaciones modulo primo"""
primo=208351617316091241234326746312124448251235562226470491514186331217050270460481 

class descifrado:
	"""Clase que se encarga de descifrar un archivo previamente cifrado a partir 
	de mínimo t evaluaciones entregadas.

	Métodos:
	def polinomios_base(self,t_evaluaciones):
		Función que recibe las t evaluaciones y crea los polinomios base
		a partir de los cuales se obtendrá la k para desencriptar.
		Regresa una lista con el resultado de cada polinomio
	def forma_lagrange(self,t_evaluaciones,resultados_polinomios):
		Función que recibe los resultados de los polinomios base y las t evaluaciones
		y a partir de ellos con ayuda de la Forma de Lagrange obtiene la k para
		descifrar.
		Regresa a k.
	def descifra_archivo(self,k,archivo_cifrado):
		Función que a partir de la k obtenida descifra el archivo cifrado.
		Devuelve el archivo descifrado con el nombre original de éste

	"""
	
	def polinomios_base(self,t_evaluaciones):
		"""Parametros:
			t_evaluaciones: Archivo txt con al menos t de las n evaluaciones entregadas.
			Deben tener el mismo formato con el que se generaron: (x, y)
		Variables:
			archivo: nombre que se asigna archivo t_evaluaciones para lectura
			t:número de evaluaciones entegadas (se lee el número de lineas en archivo)
			x_i: Lista para introducir todas las x de archivo 
			indice _oma: Indice de la coma en cada linea de archivo
			P_i: Lista para introducir los resultados de los t polinomios base
				(No se utiliza el índice 0)
			numerador: Numerador de cada Polinomio generado
			denominador: Denominador de cada Polinomio generado

		Regresa:
			P_i con los resultados de cada polinomio
		"""		

		archivo= open("documentos/"+t_evaluaciones, "r")
		t=(len(archivo.readlines()))
		archivo.close()

		x_i=[] #Lista de x's
		

		archivo= open("documentos/"+t_evaluaciones, "r")
		for linea in archivo:
			indice_coma=linea.index(',')
			x_i.append(int(linea[1:indice_coma]))
		archivo.close()

		P_i=[] #Lista de resultados de Polinomios base

		for i in range(t+1):
			P_i.append(1)

		numerador=1
		denominador=1

		#El índice 0 de la lista P_i no lo usamos

		for i in range(1,t+1):
			for j in range(1,t+1):
				if(j!=i):
					numerador=(numerador*((-x_i[j-1])))				
					denominador=(denominador*((x_i[i-1])-(x_i[j-1])))
					P_i[i]=int(numerador/denominador)
			numerador=1
			denominador=1

		return(P_i)

	def forma_lagrange(self,t_evaluaciones,resultados_polinomios):
		"""Parametros:
			t_evaluaciones: Archivo txt con al menos t de las n evaluaciones entregadas.
			Deben tener el mismo formato con el que se generaron: (x, y)
			resultado_polinomio: Lista cque entrega la función polinomios_base con el resultado
			de los polinomios base
		Variables:
			archivo: nombre que se asigna archivo t_evaluaciones para lectura
			t:número de evaluaciones entegadas (se lee el número de lineas en archivo)
			y_i; Lista para introducir las "y" de archivo 
			indice _coma: Indice de la coma en cada linea de archivo
			indice_parentesis: El índice del paréntesis que cierra ")" en cada linea
			k=llave que se obtiene a partir de aplicar la forma de Lagrange
		Regresa:
			k%primo, la llave obtenida módulo el numero primo definido
		"""

		archivo= open("documentos/"+t_evaluaciones, "r")
		t=(len(archivo.readlines()))
		archivo.close()

		y_i=[] #Lista de y's

		archivo= open("documentos/"+t_evaluaciones, "r")
		for linea in archivo:
			indice_coma=linea.index(',')
			indice_parentesis=linea.index(')')
			y_i.append(int(linea[indice_coma+1:indice_parentesis]))
		archivo.close()

		k=0

		for i in range(0,t):
			k+=(Fraction(y_i[i])*Fraction(resultados_polinomios[i+1]))%primo

		return (int(k)%primo)

	def descifra_archivo(self,k,archivo_cifrado):
		"""Parametros:
			k: contraseña obtenida de la función forma_lagrange
			archivo_cifrado: archivo que se quiere descifrar
		Variables:
			IV_SIZE: tamaño del vertor usado para descifrar.
			KEY_SIZE: tamaño de la llave.
			SALT_SIZE: tamaño de salt usado para descifrar.
			encrypted: contenido en bytes del archivo cifrado
			archivo: nombre con el que se abre para lectura el archivo cifrado
			linea: primera linea del archivo en bytes
			linea_str: primera linea del archivo en string
			linea_arreglo: linea_str dividida en dos por una diagonal
			bnombre:nombre del archivo original (se encontraba en la primera linea 
			der archivo cifrado) con  b' al principio
			nombre_original: nombre original del archivo antes de cifrarse
			k_string: convierte la contraseña de int a string.
			k_bytes: convierte la contraseña de string a bytes.
			salt: buffer de bytes.
			derived: contraseña en tipo PKSC#5.
			iv: parte inicial de la contraseña
			key: parte final de la contraseña
			ruta_actual: ruta donde se guardara el archivo descifrado.
			cleartext: cadena de bytes con los datos del archivo original descifrados.

			nombre de archivo: separa el nombre del archivo de su extension.
			prim_nombre: guarda el nombre del archivo sin su extension.
			archivo_cifrado: nombre del archivo con la nueva extension .aes.
			archivo2: nombre con el que se abre para escritura el archivo descifrado
		Regresa:
			El archivo cifrado con extension aes con los datos del archivo original 
			guardados en bytes para que sean ilegibles"""

		IV_SIZE = 16    # 128 bit
		KEY_SIZE = 32   # 256 bit
		SALT_SIZE = 16  # Arbitrario

		sys.path.append("..")
		sys.path.append("..")


		with open("documentos/"+archivo_cifrado,"rb") as archivo:
			next(archivo)
			encrypted=archivo.read()


		archivo = open("documentos/"+archivo_cifrado, "rb")
		linea = archivo.readline()
		linea_str=str(linea)
		linea_arreglo=linea_str.split("\\")
		bnombre=linea_arreglo[0]
		nombre_original=bnombre[2:]
		archivo.close()

		k_string = str(k)
		k_bytes = bytes(k_string, 'ascii')
		salt = encrypted[0:SALT_SIZE]
		derived = hashlib.pbkdf2_hmac('sha256', k_bytes, salt, 100000, dklen=IV_SIZE + KEY_SIZE)
		iv = derived[0:IV_SIZE]
		key = derived[IV_SIZE:]

		ruta_actual=os.getcwd()

		cleartext = AES.new(key, AES.MODE_CFB, iv).decrypt(encrypted[SALT_SIZE:])

		archivo2 = open("documentos/"+nombre_original, "wb")
		archivo2.write(cleartext)
		archivo2.close()
	
