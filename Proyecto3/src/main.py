"""Programa que se encarga de encriptar un archivo de forma segura a partir de una contraseña
dada por el usuario y que se basa en el esquema de secreto compartido de Shamir, al igual que
desencriptarlo.
Funciones:
    lee_entrada: se encarga de leer los datos de entrada del usuario que son:
                -bandera: indica lo que se quiere hacer, si encriptar o descenriptar
                -nombre del archivo de la evaluaciones: en el que seran guardadas las
                evaluaciones del polinomio
                -n: la cantidad de evaluaciones que se haran
                -t: el numero mínimo de puntos para desencriptar
                -nombre del documento: documento que se quiere cifrar, puede ser de
                cualquier tipo.
    es_valido: se encarga de revisar los valores de "n" y "t" principalmente que sean 
                numeros y que n sea mayor a t.
    main: funcion principal del programa que recibe los parametros necesarios para
            que el programa funcione."""
import sys
import getpass
from cifrado_descifrado.cifrado import *
from cifrado_descifrado.descifrado import *

cifrado=cifrado()
descifrado=descifrado()

def lee_entrada(llamada):
        
	if(llamada[1]=="c" and len(llamada)==6):
		archivo_evaluaciones=llamada[2]
		n=llamada[3]
		t=llamada[4]
		archivo_claro=llamada[5]

		if es_valido(n,t) == False:
			print("Ingresa n y t válidos separados por un espacio (n t):")
			numeros = input()
			lista_aux = numeros.split()
			n = lista_aux[0]
			t = lista_aux[1]
			if es_valido(n,t) == False:
				print("Números inválidos, intente de nuevo más tarde")
				sys.exit()

		contraseña= getpass.getpass("Ingresa tu contraseña: ")
		k=cifrado.hashea_contraseña(contraseña)

		#ruta_actual=os.getcwd()

		cifrado.genera_evaluaciones("documentos/"+archivo_evaluaciones, n, t, k)
		try:
			cifrado.cifra_documento(k,archivo_claro)    
		except FileNotFoundError:
			print("El archivo a cifrar no se encontró")

	elif(llamada[1]=="d" and len(llamada)==4):
		t_evaluaciones = llamada[2]
		archivo_cifrado = llamada[3]

		try:
			resultados_polinomios=descifrado.polinomios_base(t_evaluaciones) 
		except FileNotFoundError:
			print("El archivo con las t evaluaciones no se encontró")
			sys.exit()
		k=descifrado.forma_lagrange(t_evaluaciones,resultados_polinomios)

		try:
			descifrado.descifra_archivo(k,archivo_cifrado)
		except FileNotFoundError:
			print("El archivo cifrado no se encontró")
			sys.exit()

	else:
		print ("La llamada es incorrecta")
    	

def es_valido(n, t):
	if n.isdigit() == False:
   		return False
	elif t.isdigit() == False:
   		return False
	elif int(n) < int(t):
   		return False
	elif int(n)<=2:
   		return False
	else:
		return True

def main():
    lee_entrada(sys.argv)

if __name__ == "__main__":
    main()

