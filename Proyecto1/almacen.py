from filtro import *
from request import doRequest

class almacen:
 
    filtro = filtro()    

    def revisor(self, lugar):
        ciudades = {}  
        if not lugar in ciudades:
            iata = filtro.revisa(self, lugar)
            datos = doRequest(iata)
            auxiliar = datos.split(", ")
            print(auxiliar)
            ciudades[lugar] = auxiliar[1:3]
            print(ciudades)
            if ciudades[lugar] == 'Ciudad inválida':
                return ciudades[lugar]
            else:
                return lugar + """: su clima es {}, 
                su temperatura minima es {}, su temperatura maxima es {}
                y su humedad es {}""".format(ciudades[lugar][0], ciudades[lugar][1], ciudades[lugar][2], ciudades[lugar][3])
   


        
    
