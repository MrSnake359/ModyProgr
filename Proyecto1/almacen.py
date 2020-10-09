from filtro import revisa
from request import doRequest

class almacen:

    Ciudades = {}
    
    def revisor(self, lugar):
        if not lugar in Ciudades:
            iata = revisa(self, lugar)
            datos = doRequest(iata)
            auxiliar = datos.split(", ")
            Ciudades[auxiliar[0]] = auxiliar[1:3]

        return lugar + """: su temperatura maxima es {}, 
        su temperatura minima es {} 
        y su humedad es {}""".format(Ciudades[lugar][0], Ciduades[lugar][1], Ciudades[lugar][2])
            


        
    
