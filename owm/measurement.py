from tinydb import TinyDB, Query
import datetime;

class DB:

    def __init__( self ):

        self.url = 'owm/db/measurement.json'
        self.db = TinyDB( self.url )

    def set_data( self, current, location, typeplase ):

        current['timestamp'] = datetime.datetime.now().timestamp()
        current['location'] = location
        current['typeplase'] = typeplase
        #Set in local DB
        self.db.insert( current )

    def get_data( self ):

        return self.db.all()