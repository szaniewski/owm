import json
import requests

from . import lib
from . import measurement
from . import charts

h = lib.Helpers()
d = measurement.DB()
ch = charts.CHARTS()

class Temp():

    def __init__( self, apikey ):
        self.apikey = apikey
        self.baseurl =  'http://api.openweathermap.org/data/2.5/weather?'
        self.h = lib.Helpers()
        self.d = measurement.DB()
        self.history_data = self.d.get_data()

    def get_owm_data( self, typeplase, *plase ):
        """
        Connect to Open Weather Map
        Return JSON file from API
        @typeplase - You can use you location from geoapi if you set 'curent'
        """
        if typeplase == 'curent':
            location = str(self.h.mylocation())
        elif typeplase == 'city':
            location = str(plase[0])
        #Create API endpoint
        ep_current_weather = self.baseurl + 'q=' + location + '&appid=' + self.apikey

        try:
            # Gest data
            weather = requests.get( ep_current_weather )
            data = weather.json()
        finally:
            return data

    def get_current( self, typeplase, *plase  ):
        """
        Return Current Temp, Feel Temp and Description
        Also save data in local DB
        """
        weather_info = self.get_owm_data( typeplase, plase )
        location = weather_info['name']
        # # VARTIBLE --- Set data
        current = {
            'weather_main' : weather_info['main'],
            'weather_description' : weather_info['weather'][0]['description'],
            'feel_c' : h.kelvin_to_celsius( weather_info['main']['feels_like'] ),
            'temp_c' : h.kelvin_to_celsius( weather_info['main']['temp'] ),
        }

        self.d.current_data( current, location, typeplase )
        return current

    def get_local_data( self ):

        if self.h.check_data() == True:
            data = self.history_data
        else:
            data = 'Brak danych'

        return data

    def show_data_chart( self ):
        cities = h.cities_dic()
        temp = []

        for citie in cities:
            data = self.get_owm_data( 'city', citie )
            self.d.cities_data( data )
            temp.append( h.kelvin_to_celsius( data['main']['temp'] ) )

        ch.cities_chart( temp, cities)