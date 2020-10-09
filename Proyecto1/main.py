""" Programa que consulta el clima de diversas
ciudades usando Web Service, especificamente
OpenWeather API.
funciones:
	-lee: recibe un archivo .csv y lee linea por linea buscando unicamente
		los nomrbes o IATAs de las ciudades que se hara la busqueda
	-esInt: revisa si el primer caracter de la palabra es un int, 
			regresa True si es y False si no
	- main: funcion princpal del programa la cual usa los archivos .csv
"""
import csv
from almacen import *

almacen = almacen()

def lee(file_name):
	with open (file_name, 'r') as csvFile:
		csv_reader = csv.reader(csvFile)
		row_line = 0
		for row in csv_reader:
			if row_line == 0:
				row_line += 1
				continue
			if not(esInt(row[0])):
				print(almacen.revisor(row[0]))
			if not(esInt(row[1])):
				print(almacen.revisor(row[1]))

def esInt(palabra):

	try:
		int(palabra[0])
		return True
	except ValueError:
		return False

def main():
	print(lee("dataset1.csv"))
	print(lee("dataset2.csv"))

if __name__ == "__main__":
	main()
