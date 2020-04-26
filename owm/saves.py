from datetime import datetime
from threading import Timer

from . import owmconect

class INTEVAL:

    def __init__( self, apikey ):
        self.owm = owmconect.OWM( apikey )

    def dayli( self ):
        return 'dzień'