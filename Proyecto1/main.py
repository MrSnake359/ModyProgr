import csv
from almacen import *

almacen = almacen()

def lee(file_name):
	with open (file_name, 'r') as csvFile:
		csv_reader = csv.reader(csvFile)
		row_line = 0
		for row in csv_reader:
			if row_line is 0:
				row_line += 1
				continue
			if not(esInt(row[0])):
				return almacen.revisor(row[0])
			if not(esInt(row[1])):
				return almacen.revisor(row[1])

def esInt(palabra):

	try:
		int(palabra[0])
		return True
	except ValueError:
		return False

def main():
	lee("dataset1.csv")
	lee("dataset2.csv")

if __name__ == "__main__":
	main()
