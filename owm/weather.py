import json
import requests

from . import lib
from . import measurement
from . import charts
#from . import everyday
from . import owmconect

class Temp():

    def __init__( self, apikey ):
        self.owm = owmconect.OWM( apikey )
        self.ch = charts.CHARTS()
        self.h = lib.Helpers()
        self.d = measurement.DB()
        #self.dayli = everyday.dayli()
        self.alldata = self.d.get_data()

    def get_current( self, typeplase, *plase  ):
        """
        Return Current Temp, Feel Temp and Description
        """
        if typeplase == 'current':
            location = str( self.h.mylocation() )
        elif typeplase == 'city':
            location = str( plase[0] )

        weather_info = self.owm.get_data( location )
        # # VARTIBLE --- Set data
        data = {
            'weather_main' : weather_info['main'],
            'weather_description' : weather_info['weather'][0]['description'],
            'feel_c' : self.h.kelvin_to_celsius( weather_info['main']['feels_like'] ),
            'temp_c' : self.h.kelvin_to_celsius( weather_info['main']['temp'] ),
        }

        return data

    def get_local_data( self ):

        if not self.alldata:
            data = 'Brak danych'
        else:
            data = self.alldata
        return data

    def show_data_chart( self ):
        cities =  self.h.cities_dic()
        temp = []

        for citie in cities:
            data = self.owm.get_data( citie )
            self.d.cities_data( data )
            temp.append(  self.h.kelvin_to_celsius( data['main']['temp'] ) )

        self.ch.cities_chart( temp, cities )

    def save_data( self ):
        data = self.get_current('current')
        self.dayli.current( data )
