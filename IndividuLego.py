"""import du la classe Individu du fichier python Individu.py"""
from Individu import Individu

"""Pour faire des copies de liste par valeur"""
import copy

"""Pour generer des nombres aleatoires ou melanger aleatoirement des listes"""
import random

class IndividuLego(Individu):
    def __init__(self, legos):
        """un individuLego est compose d'une liste de legos"""
        self.legos = legos

    def __repr__(self):
        tourLego=""
        for lego in self.legos:
            tourLego+=str(lego)+"\n"
        hauteur = self.fitness()
        tourLego += "hauteur totale: " + str(hauteur)
        return tourLego

    # Creation d'une tour aleatoire de legos
    @staticmethod
    def random(legos):
        l = copy.copy(legos)
        p = IndividuLego(l)
        random.shuffle(p.legos)
        return p

    def fitness(self):
        hauteurTotale = 0.0
        for lego in self.legos:
            hauteurTotale += lego.hauteur
        return hauteurTotale

    def __lt__(self, IndividuLego):
        return self.fitness()<IndividuLego.fitness()
