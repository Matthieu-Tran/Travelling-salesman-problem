
"""import la classe random"""
import random

"""Un classe ville est defini par ses coordonnnees x et y"""
hauteurs = [1.0,2.0,6.0,12.0]
couleurs = ['r', 'v', 'o', 'b', 'j', 'n', 'B', 'g']
class Lego :
    def __init__(self) :
        self.hauteur = random.choice(hauteurs)
        self.couleur = random.choice(couleurs)
    """renvoie la hauteur entre d'un lego"""
    def hauteur(self) :
        return self.hauteur
    """renvoie la couleur d'un lego"""
    def couleur(self) :
        return self.couleur
    """renvoie la representation d'une ville sous forme de chaine de caractere"""
    def __repr__(self) :
        return self.couleur
