import time
import geocoder

class Helpers():

    def kelvin_to_celsius( self,  k ):
        return round( int( k ) - 273.15 , 2)

    def mylocation( self ):

        g = geocoder.ip('me')
        latlng = g.latlng
        latlng_url = 'lat=' + str(latlng[0]) + '&lon=' + str(latlng[1])

        return latlng_url

    def date( self, difference ):

        # 24h is 86400s
        days =  difference * 86400
        start = int( time.time() )
        end = start - days
        date = { 'start': start, 'end': end }

        return date
