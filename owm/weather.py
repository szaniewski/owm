import json
import requests
from . import lib

h = lib.Helpers()

class Temp:

    def current( self, typeplase, owm_key, *plase ):

        BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

        if typeplase == 'curent':
            ep_current_weather = BASE_URL + h.mylocation() + '&appid=' + owm_key
        elif typeplase == 'city':
            ep_current_weather = BASE_URL + 'q=' + plase[0] + '&appid=' + owm_key

        try:
            # Gest data
            weather = requests.get( ep_current_weather )
            weather_info = weather.json()

            # VARTIBLE --- Set data
            current = {
                'weather_main' : weather_info['weather'][0]['main'],
                'weather_description' : weather_info['weather'][0]['description'],
                'feel_c' : h.kelvin_to_celsius( weather_info['main']['feels_like'] ),
                'temp_c' : h.kelvin_to_celsius( weather_info['main']['temp'] )
            }

        finally:
            return current