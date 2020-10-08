import requests
import sys

apiKey = "7e3456a48830bb5ac31552fe1bc9f269"

def doRequest(iata):
    
    try:
        url = "https://api.openweathermap.org/data/2.5/weather?q={}&lang=es&units=metric&appid={}".format(iata, apiKey)
        request = requests.get(url)
        dictionary = request.json()
    except:
        sys.exit("Ocurrió un error al comunicarse con el servidor")

    if(dictionary.get("cod") == "404"):
        return "Ciudad inválida"

    clima=  str(dictionary.get("weather"))  

    cadena = "{}, ".format(dictionary.get("name"))
    cadena += clima [(clima.find("description")+15):(clima.find("icon")-4)]
    cadena  += " ,{}°C, ".format(dictionary.get("main",{}).get("temp_min"))
    cadena  += "{}°C, ".format(dictionary.get("main",{}).get("temp_max"))
    cadena  += "{}%".format(dictionary.get("main",{}).get("humidity"))
    


    # in the JSON dictionary['weather'] is a list, with a string, down is splitted
    #weather += str(dictionary.get('weather')).split("main")[1].split("\'")[2] 
    #weather += " and a temperature of {}°C".format(dictionary.get("main",{}).get("temp")) 
    return cadena
    
