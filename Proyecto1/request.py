import requests
import sys
"""Modulo que mediante una peticion a OpenWeather
recopila los datos de clima de la ciudad requerida
    Funciones:
        doRequest(iata)
            a partir del codigo IATA de la ciudad hace una peticion
            para recopilar sus datos de clima
    Variables Globales:
        apiKey: llave necesaria para realizar peticiones a OpenWeather
"""

apiKey = "7e3456a48830bb5ac31552fe1bc9f269"

def doRequest(iata):
    """Parametros:
    recibe un string con el codigo IATA de la ciudad o su nombre
    
    Regresa:
        Un String con los datos de clima, temperatura 
        minima y maxima y el % de humedad de la ciudad buscada"""
    
    try:
        url = "https://api.openweathermap.org/data/2.5/weather?q={}&lang=es&units=metric&appid={}".format(iata, apiKey)
        request = requests.get(url)
        dictionary = request.json()
    except:
        sys.exit("Ocurrió un error al comunicarse con el servidor")

    if(dictionary.get("cod") == "404"):
        return ", Ciudad inválida"

    clima=  str(dictionary.get("weather"))  

    cadena = "El clima de {} es ".format(dictionary.get("name"))
    cadena += clima [(clima.find("description")+15):(clima.find("icon")-4)]
    cadena  += " su temperatura minima es de {}°C, ".format(dictionary.get("main",{}).get("temp_min"))
    cadena  += "su temperatura maxima es de {}°C, ".format(dictionary.get("main",{}).get("temp_max"))
    cadena  += "su humedad es de {}%".format(dictionary.get("main",{}).get("humidity"))
    return cadena
    
