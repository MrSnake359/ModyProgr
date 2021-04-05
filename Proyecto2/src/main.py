""" Programa que calcula el
Indice de Cobertura Nubosa
de una fotografía del cielo"
"""
from proceso_pixel import *
import sys

""" Variables globales: 
    proceso_pixel: variable usada como objeto de tipo proceso_pixel
    para usar los métodos de la clase proceso_pixel
"""
proceso_pixel = proceso_pixel()

""" Método principal. Llama a la función lee_entrada del programa
proceso_pixel con los argumentos recibidos en terminal 
"""
def main():
    proceso_pixel.lee_entrada(sys.argv)

if __name__ == "__main__":
    main()



