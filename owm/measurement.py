from tinydb import TinyDB, Query
import datetime;

class DB:
    """
    Save data in local JSON file
    """
    def __init__( self ):

        self.url = 'owm/db/measurement.json'
        self.db = TinyDB( self.url )
        self.currenthistory = self.db.table('currenthistory')
        self.citieshistory = self.db.table('citieshistory')

    def current_data( self, data, location, typeplase ):

        data['timestamp'] = datetime.datetime.now().timestamp()
        data['location'] = location
        data['typeplase'] = typeplase
        self.currenthistory.insert( data )

    def cities_data( self, data ):

        data['timestamp'] = datetime.datetime.now().timestamp()
        self.citieshistory.insert( data )

    def get_data( self ):

        return self.db.all()