import time
import geocoder

class Helpers():

    def check_data( self, data ):
        #Validatr file data
        if not data:
            return 'No data ;( - si so sad'
        else:
            return True

    def kelvin_to_celsius( self,  k ):
        return round( int( k ) - 273.15 , 2)

    def mylocation( self ):
        g = geocoder.ip('me')

        return g.city

    def date( self, difference ):

        # 24h is 86400s
        days =  difference * 86400
        start = int( time.time() )
        end = start - days
        date = { 'start': start, 'end': end }

        return date

    def cities_dic( self ):
        #TO DO connect to Goole API for city list
        data = ('Warszawa','Poznań','Kraków', 'Katowice')
        return data

