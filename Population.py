"""import du la classe Individu du fichier python Individu.py"""
from Individu import Individu

"""Classe abstraite representant une population d'individu generique"""
class Population (object) :
    """Constructeur"""
    def __init__(self, size):
        """Une population est une liste d'individu"""
        self.individus = []
        """Une population comporte un nombre arbitraire d'individu parametre par l'utilisateur"""
        self.size=size

    """Methode qui remplit permet de creer la population initiale d'individus differents"""
    def populating(self) :
        """Comme c'est une methode abstraite, son code n'est pas defini, et donc l'appel a cette methode produit une exception"""
        raise NotImplementedError

    """Methode qui selectionne les meilleurs individus (fonction fitness), de la population en supprimant les autres de la liste"""
    def selection(self) :
        """Comme c'est une methode abstraite, son code n'est pas defini, et donc l'appel a cette methode produit une exception"""
        raise NotImplementedError

    """Methode qui fait se reproduire les meilleurs individus selectionne pour reconstruire une population d'individu de la taille souhaitee"""
    def reproduction(self) :
        """Comme c'est une methode abstraite, son code n'est pas defini, et donc l'appel a cette methode produit une exception"""
        raise NotImplementedError

    def best(self) :
        """Comme c'est une methode abstraite, son code n'est pas defini, et donc l'appel a cette methode produit une exception"""
        raise NotImplementedError
