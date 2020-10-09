from .filtro import revisa
from .request import doRequest

class almacen:

    Ciudades = {}

    def almacenamiento(self, lugar):
        if lugar in Ciudades:
            continue
        else:
            iata = revisa(self, lugar)
            datos = doRequest(iata)
            auxiliar = datos.split(", ")
            Ciudades[auxiliar[0]] = auxiliar[1:3]
    return lugar + """: su temperatura maxima es {}, 
    su temperatura minima es {} 
    y su humedad es {}""".format(Ciudades[lugar][0], Ciduades[lugar][1], Ciudades[lugar][2])
            


        
    
