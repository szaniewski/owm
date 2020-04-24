import json
import requests

from . import lib
from . import measurement
from . import charts

h = lib.Helpers()
d = measurement.DB()
ch = charts.CHARTS()

class Temp:

    def __init__( self ):
        self.baseurl =  'http://api.openweathermap.org/data/2.5/weather?'
        self.h = lib.Helpers()
        self.d = measurement.DB()
        self.history_data = self.d.get_data()

    def check_data( self ):
        #Validatr file data
        if not self.history_data:
            return 'No data ;( - si so sad'
        else:
            return True

    def get_owm_data( self, typeplase, owm_key, *plase ):
        """
            Conet to Open Weather Map
            Return JSON file from API
            @typeplase - You can use you location from geoapi if you set 'curent'
        """
        if typeplase == 'curent':
            location = self.h.mylocation()
        elif typeplase == 'city':
            location = plase[0]
        # Create API endpoint
        ep_current_weather = self.baseurl + 'q=' + location[0] + '&appid=' + owm_key

        try:
            # Gest data
            weather = requests.get( ep_current_weather )
            data = weather.json()
        finally:
            return data

    def get_current( self, typeplase, owm_key, *plase  ):
        """
            Retrirn current Temp, Feel Temp and Description
            Also save data in local DB
        """
        weather_info = self.get_owm_data( typeplase, owm_key, plase )
        location = weather_info['name']
        # # VARTIBLE --- Set data
        current = {
            'weather_main' : weather_info['main'],
            'weather_description' : weather_info['weather'][0]['description'],
            'feel_c' : h.kelvin_to_celsius( weather_info['main']['feels_like'] ),
            'temp_c' : h.kelvin_to_celsius( weather_info['main']['temp'] ),
        }

        self.d.save_current_data( current, location, typeplase )
        return current

    def get_local_data( self ):

        if self.check_data() == True:
            data = self.history_data
            return data

    def show_data_chart( self, typechart ):

        if self.check_data() == True:

            if typechart == 'all_city_day':
                ch.all_city_day ( self.history_data )