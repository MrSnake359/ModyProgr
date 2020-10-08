from .filtro import revisa

class almacen:

    Dciudades = {}

    def vacio():
        if Dciudades == {}:
            return True
        else: 
            return False
    
    def revisor(self, lugar):
        if vacio() == True:
            
        elif lugar in Dciudades:
            return lugar + """: su temperatura maxima es {}, 
            su temperatura minima es {} 
            y su humedad es{}""".format(Dciudades[lugar][0], Dciduades[lugar][1], Dciudades[lugar][2])
        else:
            


        
    
