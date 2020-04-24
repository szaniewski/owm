import matplotlib.pyplot as plt

class CHARTS:

    def __init__( self ):
        self.temp_c =[]
        self.location = []

    def all_city_day( self, data ):

        for d in data:
            self.temp_c.append( d['temp_c'] )
            self.location.append( d['location'] )

        plt.bar( self.location, self.temp_c )
        plt.xlabel('Miasta')
        plt.ylabel('Temperatury')

        plt.title('Yours wheter grah')

        plt.show()