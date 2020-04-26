import time
import schedule

from . import processingdata
from . import measurement
from . import lib

class INTEVAL:

    def __init__( self, apikey ):
        self.processing = processingdata.DATAS( apikey )
        self.db = measurement.DB()
        self.h = lib.Helpers()

    def data( self ):
        plase_type = 'current'
        data = self.processing.current( plase_type )
        location = self.h.mylocation()
        self.db.current_data( data, location, plase_type  )

        return data

    def dayli( self ):
        schedule.every().day.at( '12:00' ).do( self.data() )