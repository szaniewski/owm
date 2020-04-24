import time
import geocoder

class Helpers():

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

    def city_dic( self ):
        #TO DO connect to Goole API for city list
        citys = ('Warszawa','Poznań','Wrocała','Kraków', 'Katowice')
        return citys
