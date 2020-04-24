import json
import requests
from . import lib
from . import measurement

h = lib.Helpers()
d = measurement.DB()

class Temp:

    def __init__( self ):
        self.baseurl =  'http://api.openweathermap.org/data/2.5/weather?'

    def current( self, typeplase, owm_key, *plase ):

        if typeplase == 'curent':
            location = h.mylocation()
        elif typeplase == 'city':
            location = plase[0]
        ep_current_weather = self.baseurl + 'q=' + location + '&appid=' + owm_key

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
            d.set_data( current, location )
            return current