import matplotlib.pyplot as plt

class CHARTS:
    """
    Drawe chart's
    """

    def cities_chart( self, temp, location ):

        plt.bar( location,  temp )
        plt.xlabel('Cities')
        plt.ylabel('Temperature')

        plt.title('Yours graph')

        plt.show()