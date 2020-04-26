from . import lib
from . import owmconect

class DATAS:

    def __init__( self, apikey ):
        self.h = lib.Helpers()
        self.owm = owmconect.OWM( apikey )

    def current( self, typeplase, *plase ):
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