"""Classe abstraite representant un individu generique"""

class Individu (object):
    """Constructeur"""
    def __init__(self) :
        """Comme c'est une methode abstraite, son code n'est pas defini, et donc l'appel a cette methode produit une exception"""
        raise NotImplementedError

    """Redefinition de l'operateur de comparaison inferieur (less than) permettant de trier une liste d'individu par exemple"""
    def __lt__(self, individu) :
        """Comme c'est une methode abstraite, son code n'est pas defini, et donc l'appel a cette methode produit une exception"""
        raise NotImplementedError

    """La fonction d'adaption doit renvoyer un un score flottant permettant d'evaluer son adaptation au contraintes de l'environnement"""
    def fitness (self) :
        """Comme c'est une methode abstraite, son code n'est pas defini, et donc l'appel a cette methode produit une exception"""
        raise NotImplementedError

    def reproduction(self) :
        """Comme c'est une methode abstraite, son code n'est pas defini, et donc l'appel a cette methode produit une exception"""
        raise NotImplementedError

    def mutation(self) :
        """Comme c'est une methode abstraite, son code n'est pas defini, et donc l'appel a cette methode produit une exception"""
        raise NotImplementedError

