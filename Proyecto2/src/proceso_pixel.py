from PIL import Image

class proceso_pixel:
    """ Clase proceso_pixel. Recibe una imagen, 
    devuelve su ICN y una imagen en B/N

    Métodos: 
        analisis_pixel(self,imagen)
            Recibe una imagen, la recorta, cuenta los pixeles clasificados como nube y los
            clasificados como cielo, calcula el ICN. Modifica los pixeles clasificados
            como nube a blanco y los clasificados como cielo a negro.

        lee_entrada(self,llamada)
            Lee la llamada en terminal, extrae el nombre de la imagen y llama
            al método analisis_pixel con él. Identifica si hay una bandera s o S
            y nombra la nueva imagen en B/N, la guarda y la despliega.
    """

    def analisis_pixel(self, imagen):
        """Parametros:
        recibe un string con el nombre de la imagen a analizar
        
        Variables:
            foto: foto original del cielo
            foto_recortada: foto del cielo recortada
            total_pixeles: numero total de pixeles clasificados como cielo o nube
            total_nubes: numero total de pixeles clasificados como nube
            dato_pixel: arreglo de coordenadas i,j del pixel que está siendo analizado

        Regresa:
            Imagen del cielo recortada y con los pixeles clasificados como nube modificados a color blanco,
            y los pixeles clasificados como cielo modificados a color negro.
        """

        foto = Image.open(imagen)
        box = (834, 106, 3534, 2806)
        foto_recortada = foto.crop(box)
        pixeles = foto_recortada.load()
        total_pixeles=0
        total_nubes=0
    
        for j in range(2700):
            for i in range(2700):
                dato_pixel = foto_recortada.getpixel((i,j))
                if dato_pixel[0]>80 and dato_pixel[1]>80 and dato_pixel[2]>80:
                    total_pixeles=total_pixeles+1
                    if dato_pixel[0]>=dato_pixel[2]:
                        total_nubes=total_nubes+1
                        pixeles[i,j] = (255,255,255)
                    else:
                        pixeles[i,j] = (0,0,0)

        print("El total de pixeles es: {}".format(str(total_pixeles)))
        print("El total de pixeles clasificados como nube es: {}".format(str(total_nubes)))
        print("El indice de cobertura nuboso es: {}".format(str(total_nubes/total_pixeles)))
        return foto_recortada

       
    def lee_entrada(self,llamada):
        """Parametros:
        recibe un arreglo con la información ingresada en terminal (ya sea solo el nombre de la imagen, o
        además una bandera s o S)
        
        Variables:
            cadena_entrada: información de entrada concatenada en una cadena
            entrada: arreglo con información de entrada
            img_resultante: imagen devuelta por el método analisis_pixel
            nuevo_nombre: nombre para img_resultante
            resultado: imagen nueva para desplegarse.
        """        

        if(len(llamada)==3):
            cadena_entrada=llamada[1]+" "+llamada[2]
        else:
            cadena_entrada=llamada[1]
        entrada = cadena_entrada.split(" ")
        img_resultante=proceso_pixel.analisis_pixel(self,entrada[0])
        if len(entrada) == 2:
            if(entrada[1]=="s" or entrada[1]=="S"):
                nombre_img=entrada[0].split(".")
                nuevo_nombre=nombre_img[0]+"-seg."+nombre_img[1]
                img_resultante.save(nuevo_nombre)
                print("La imagen a blanco y negro se guardo como:"+nuevo_nombre)
                resultado = Image.open(nuevo_nombre)
                resultado.show()  
