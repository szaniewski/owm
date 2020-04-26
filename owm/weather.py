import json
import requests

from . import lib
from . import measurement
from . import charts
#from . import saves
from . import owmconect
from . import processingdata

class Temp():

    def __init__( self, apikey ):
        self.owm = owmconect.OWM( apikey )
        self.ch = charts.CHARTS()
        self.h = lib.Helpers()
        self.db = measurement.DB()
       # self.autosave = saves.INTEVAL()
        self.alldata = self.db.get_data()
        self.processing = processingdata.DATAS( apikey )

    def get_current( self, typeplase, *plase  ):
        data = self.processing.current( typeplase, plase )
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
            self.db.cities_data( data )
            temp.append(  self.h.kelvin_to_celsius( data['main']['temp'] ) )

        self.ch.cities_chart( temp, cities )

    # def save_data( self ):
    #     return self.autosave.dayli()
