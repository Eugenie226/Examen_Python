import numpy as np
import matplotlib.pyplot as plt

class Curve:
    def __init__(self, start, stop, nbr_points=5432):
        self.start = start
        self.stop = stop
        self.nbr_points = nbr_points

    def __f(self, x):
        return x**5

    def fig_plot(self):
        valeur_x = np.linspace(self.start, self.stop, self.nbr_points)
        valeur_y = self.__f(valeur_x)
        plt.plot(valeur_x, valeur_y)
        plt.title("La courbe $y = x^5$ sur l'intervalle [{}, {}]".format(self.start, self.stop))
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.show()

    def emplacement_point(self, x, y):
        if y > self.__f(x):
            return "au-dessus"
        else:
            return "en dessous"   
        