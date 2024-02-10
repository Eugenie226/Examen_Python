# Importons les bibliothèques matplotlib et numpy
import matplotlib.pyplot as plt
import numpy as np

# Définissons une fonction f(x) = x^5
def f(x):
    return x**5

# Géneration d'une séquence de 100 valeurs de x allant de 0 à 1 avec un pas égal entre chaque valeur
valeur_x = np.linspace(0, 1, 100)

# Calculons les valeurs de y correspondantes en utilisant la fonction f(x)
valeur_y = f(valeur_x)

# Tracons la courbe avec la fonction plot
plt.plot(valeur_x, valeur_y, label='$x^5$')

# Tracons les côtés du carré délimité les droites: x=0, x=1, y=0, y=1
# En bas
plt.plot([0, 1], [0, 0], color='red') 
# A droite 
plt.plot([1, 1], [0, 1], color='red')
# En haut  
plt.plot([1, 0], [1, 1], color='red') 
# A gauche 
plt.plot([0, 0], [1, 0], color='red')  

# Configurons le graphique pour qu'il soit plus lisible
plt.title('Courbe $y = x^5$ et carré délimité par $x=0$, $x=1$, $y=0$, $y=1$')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Affichons le graphique
plt.show()
