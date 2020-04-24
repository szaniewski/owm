from tinydb import TinyDB, Query
import datetime;

class DB:

    def __init__( self ):

        self.url = 'owm/db/measurement.json'

    def set_data( self, current, location ):

        current['timestamp'] = datetime.datetime.now().timestamp()
        current['location'] = location
        #Set in local DB
        db = TinyDB( self.url )
        db.insert( current )