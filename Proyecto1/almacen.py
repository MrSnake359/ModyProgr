from filtro import *
from request import doRequest

class almacen:
    """Clase usada para almacenar los datos ya buscados en la API
    en un diccionario para su facil acceso.
    
    Variables globales: 
        filtro: variable usada como objeto de tipo filtro
                para usar los metodos de la clase filtro
    
    Metodos:
        revisor(self, lugar)
            busca la ciudad en el diccionario y devuelve los datos de clima.
     """
 
    filtro = filtro()    

    def revisor(self, lugar):
        """Parametros:
        recibe un string de la ciudad a buscar.
        
        Variables:
            ciudades: diccionario usado para almacenar las ciudades buscadas 
                    previamente en la API.
        Regresa:
            Cadena con los datos de clima, temperatura minima y maxima
            y su % de humedad
        """
        ciudades = {}  
        if lugar in ciudades:
            print(ciudades)
            return ciudades[lugar]
        else:
            iata = filtro.revisa(self, lugar)
            datos = doRequest(iata)
            ciudades[lugar] = datos
            print(ciudades)
            return ciudades[lugar]

        
    
