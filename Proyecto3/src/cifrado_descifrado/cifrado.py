import hashlib
import math
import os
import sys
from Crypto.Cipher import AES

class cifrado:
	"""Clase que se encarga de cifrar el archivo requerido y de generar las evaluaciones
	requeridas a partir de los datos recibidos.
	
	Métodos:
	hashea_contraseña(self,contraseña)
		Se encarga de ulizar la funcion de dispersión hash sobra la contraseña dada
		por el usuario para despues convertirla a un número decimal.
	genera_evaluaciones(self.archivo_evaluaciones, n, t, k)
		Se encarga de generar las evaluaciones necesarias y las guardar en un archivo
		de texto.
	cifra_documento(self, k, archivo_claro)
		Se encarga de cifrar el documento a partir de la contraseña convertida
		en decimal y crea un nuevo archivo de tipo aes con los datos del archivo
		original a manera de bytes."""
	def hashea_contraseña(self,contraseña):
		"""Parametros:
			contraseña: un string recibido desde la terminal que servira como contraseña.
		Variables:
			a: guarda el resultado de la funcion hash.
			contraseña_bytes: guarda la contraseña convertida de string a bytes.
			k_decimal: convierte la contraseña de hexadecimal a decimal.
		Regresa:
			La contraseña convertida en decimal.
		"""
		a = hashlib.sha256()
		contraseña_bytes = bytes(contraseña, 'ascii')
		a.update(contraseña_bytes)
		k_decimal = abs(int(a.hexdigest(), 16))
		return(k_decimal)


	def genera_evaluaciones(self, archivo_evaluaciones, n, t, k):
		"""Parametros:
			archivo_evaluaciones: nombre del archivo donde se guardaran las evaluaciones.
			n: cantidad de evaluaciones que se haran.
			t: minimo de puntos necesario para descifrar.
			k: contraseña convertida en decimal.
		Variables:
			primo: un número primo de 78 caracteres para reducir el valor final.
			grado: auxiliar que maneja el grado del polinomio.
			evaluaciones: archivo creado para escribir las evaluaciones.
			constante: auxiliar que maneja las constantes del polinomio.
			resultado: se guarda el resultado del polinomio para luego guardarlo en el archivo.
		Regresa:
			Un archivo nuevo o modificado con las parejas ordenadas de las evaluaciones."""
		primo=208351617316091241234326746312124448251235562226470491514186331217050270460481 #78 caracteres
		grado = int(t)
		evaluaciones = open(archivo_evaluaciones, "w")
		constante = 1
		resultado = 0
		for x in range(int(n)):
			while grado >1:
				grado -= 1
				resultado += (constante * ((x+1)**grado))%primo
				constante += 1
			evaluaciones.write("("+str((x+1)) + ", " + str((resultado + k))+")")
			evaluaciones.write("\n")
			grado=int(t)
			constante=1
			resultado=0
		evaluaciones.close()

	def cifra_documento(self,k,archivo_claro):
		"""Parametros:
			k: contraseña convertida a decimal.
			archivo_claro: archivo que se quiere cifrar.
		Variables:
			IV_SIZE: tamaño del vertor usado para cifrar.
			KEY_SIZE: tamaño de la llave.
			SALT_SIZE: tamaño de salt usado para cifrar.
			cleartext: guarda los bytes de los datos originales.
			k_sting: convierte la contraseña de int a string.
			k_bytes: convierte la contraseña de string a bytes.
			salt: buffer de bytes.
			derived: contraseña en tipo PKSC#5.
			iv: parte inicial de la contraseña
			key: parte final de la contraseña
			encypted: cadena de bytes con los datos del archivo original cifrados.
			nombre de archivo: separa el nombre del archivo de su extension.
			prim_nombre: guarda el nombre del archivo sin su extension.
			archivo_cifrado: nombre del archivo con la nueva extension .aes.
			ruta_actual: ruta donde se guardara el archivo cifrado.
			archivo2: abre el archivo cifrado para escribir los datos en bytes.
		Regresa:
			El archivo cifrado con extension aes con los datos del archivo original 
			guardados en bytes para que sean ilegibles"""
		IV_SIZE = 16    # 128 bit
		KEY_SIZE = 32   # 256 bit
		SALT_SIZE = 16  # Arbitrario

		sys.path.append("..")
		sys.path.append("..")

		with open("documentos/"+archivo_claro,"rb") as archivo:
			cleartext=archivo.read()

		k_string = str(k)
		k_bytes = bytes(k_string, 'ascii')
		salt = os.urandom(SALT_SIZE)
		derived = hashlib.pbkdf2_hmac('sha256', k_bytes, salt, 100000, dklen=IV_SIZE + KEY_SIZE)
		iv = derived[0:IV_SIZE]
		key = derived[IV_SIZE:]

		encrypted = salt + AES.new(key, AES.MODE_CFB, iv).encrypt(cleartext)

		nombre_archivo=archivo_claro.split(".")
		prim_nombre_archivo=nombre_archivo[0]
		archivo_cifrado="/"+prim_nombre_archivo+".aes"


		ruta_actual=os.getcwd()

		archivo2 = open("documentos/"+archivo_cifrado, "wb")
		archivo2.write(bytes(archivo_claro, "ascii"))
		archivo2.write(bytes("\n", "ascii"))
		archivo2.write(encrypted)
		archivo2.close()
