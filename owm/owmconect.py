import json
import requests

from . import lib

class OWM:

    def __init__( self, apikey ):
        self.apikey = apikey
        self.baseurl =  'http://api.openweathermap.org/data/2.5/weather?'

    def get_data( self, location ):
        """
        Connect to Open Weather Map
        Return JSON file from API
        @typeplase - You can use you location from geoapi if you set 'current'
        """

        #Create API endpoint
        ep_current_weather = self.baseurl + 'q=' + location + '&appid=' + self.apikey

        try:
            # Gest data
            weather = requests.get( ep_current_weather )
            data = weather.json()
        finally:
            return data