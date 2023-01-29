from Population import Population
from Lego import Lego
import copy
import random

from IndividuLego import IndividuLego

class PopulationLego(Population):
    def __init__(self, size):
        super(PopulationLego, self).__init__(size)
        self.populating()


    def populating(self):
        for i in range(0,self.size):
            legos = []
            legos.append(Lego())
            legos.append(Lego())
            legos.append(Lego())
            legos.append(Lego())
            legos.append(Lego())
            legos.append(Lego())
            legos.append(Lego())
            legos.append(Lego())
            legos.append(Lego())
            legos.append(Lego())
            self.individus.append(IndividuLego.random(legos))

    def selection(self, choix):
        if choix == 1:
            # On compte le nombre de tour de legos qui sont rouge dans la population
            list = self.compterRouge()
            # On trie les valeurs en fonction des items du dictionnaire
            dic2 = dict(sorted(list.items(),key= lambda x:x[1], reverse=True))
            list = []
            # On mets dans une liste les clés du dictionnaires qui sont les indices des individus dans la population
            for i in dic2:
                list.append(i)
            # On fait une deepcopy de l'indivus
            individus = copy.deepcopy(self.individus)
            # On mets dans l'ordre et dans la taille de la liste des individus, les tours de legos qui ont le plus de legos rouge
            for x in range(len(list)):
                individus[x] = self.individus[list[x]]
            #On met egale la liste d'individus a la copie qui contient en ordre croissant les individus qui ont le plus de legos rouge
            self.individus = individus[0:int(self.size/2)]
        elif choix == 2:
            list = self.compterDiversite()
            #Trie les valeurs en fonction des items du dictionnaire
            dic2 = dict(sorted(list.items(),key= lambda x:x[1], reverse=True))
            list = []
            for i in dic2:
                list.append(i)
            individus = copy.deepcopy(self.individus)
            for x in range(len(list)):
                individus[x]=self.individus[list[x]]
            self.individus=individus[0:int(self.size/2)]
        elif choix == 3:
            self.individus.sort()
            self.individus=self.individus[0:int(self.size/2)]
        elif choix == 4:
            self.individus.sort(reverse=True)
            self.individus=self.individus[0:int(self.size/2)]

    #Fonction qui retourne une liste qui comporte le nombre de legos differents dans la liste d'individus
    def compterDiversite(self):
        list = {}
        lengthIndividus = len(self.individus)
        lengthLegos = len(self.individus[0].legos)
        for i in range(lengthIndividus):
            cpt = 0
            trouveR = False
            trouveV = False
            trouveO = False
            trouveB = False
            trouveJ = False
            trouveN = False
            trouveBlanc = False
            trouveG = False
            for j in range(lengthLegos):
                # Si on trouve dans un individu qui a un lego rouge et qu'il n'a pas deja ete trouve, alors on incremente le compteur
                if (self.individus[i].legos[j].couleur == 'r') and not trouveR:
                    cpt = cpt + 1
                    trouveR=True
                if self.individus[i].legos[j].couleur == 'v' and not trouveV:
                    cpt = cpt + 1
                    trouveV=True
                if self.individus[i].legos[j].couleur == 'o' and not trouveO:
                    cpt = cpt + 1
                    trouveO=True
                if self.individus[i].legos[j].couleur == 'b' and not trouveB:
                    cpt = cpt + 1
                    trouveB=True
                if self.individus[i].legos[j].couleur == 'j' and not trouveJ:
                    cpt = cpt + 1
                    trouveJ=True
                if self.individus[i].legos[j].couleur == 'n' and not trouveN:
                    cpt = cpt + 1
                    trouveN=True
                if self.individus[i].legos[j].couleur == 'B' and not trouveBlanc:
                    cpt = cpt + 1
                    trouveBlanc=True
                if self.individus[i].legos[j].couleur == 'g' and not trouveG:
                    cpt = cpt + 1
                    trouveG=True
            #On met dans un dictionnaire, l'indice de l'individus et le compteur
            list[i] = cpt
        return list

    # Fonction qui retourne le nombre de legos différent pour le best individu
    def compterDiff(self):
        lengthLegos = len(self.individus[0].legos)
        cpt = 0
        trouveR = False
        trouveV = False
        trouveO = False
        trouveB = False
        trouveJ = False
        trouveN = False
        trouveBlanc = False
        trouveG = False
        for j in range(lengthLegos):
            # Si on trouve dans un individu qui a un lego rouge et qu'il n'a pas deja ete trouve, alors on incremente le compteur
            if (self.individus[0].legos[j].couleur == 'r') and not trouveR:
                cpt = cpt + 1
                trouveR = True
            if self.individus[0].legos[j].couleur == 'v' and not trouveV:
                cpt = cpt + 1
                trouveV = True
            if self.individus[0].legos[j].couleur == 'o' and not trouveO:
                cpt = cpt + 1
                trouveO = True
            if self.individus[0].legos[j].couleur == 'b' and not trouveB:
                cpt = cpt + 1
                trouveB = True
            if self.individus[0].legos[j].couleur == 'j' and not trouveJ:
                cpt = cpt + 1
                trouveJ = True
            if self.individus[0].legos[j].couleur == 'n' and not trouveN:
                cpt = cpt + 1
                trouveN = True
            if self.individus[0].legos[j].couleur == 'B' and not trouveBlanc:
                cpt = cpt + 1
                trouveBlanc = True
            if self.individus[0].legos[j].couleur == 'g' and not trouveG:
                cpt = cpt + 1
                trouveG = True
        return cpt

    # On compte le nombre de legos rouge parmis les individus et on renvoi un dictionnaire comportant l'indice et le nombre de legos rouge d'un individu
    def compterRouge(self):
        i=0
        list = {}
        lengthIndividus = len(self.individus)
        lengthLegos = len(self.individus[0].legos)
        for i in range(lengthIndividus):
            cpt=0
            for j in range(lengthLegos):
                # Si un individus comptient un lego rouge alors on increment un compteur
                if self.individus[i].legos[j].couleur == 'r':
                    cpt = cpt + 1
            list[i] =cpt
        return list

    #Reproduction sexuee des individus
    def reproduction(self):
        i=0
        while (len(self.individus)<self.size) :
            i=i+1
            # On se reproduit avec le meilleur individu (technique du mal dominant)
            list = copy.deepcopy(self.individus[0])
            list.legos[0], list.legos[2], list.legos[4], list.legos[6], list.legos[8] = self.individus[i].legos[8], self.individus[i].legos[6], self.individus[i].legos[4], self.individus[i].legos[2], self.individus[i].legos[0]
            self.individus.append(list)
            
    def best(self, choix):
        self.selection(choix)
        return self.individus[0]

    def mutation(self):
        #On choisi aléatoirement un individus dans la population
        rand = random.randint(0, self.size-1)
        #On choisi aléatoirement un lego d'un individu 
        randlego = random.randint(0, len(self.individus[0].legos)-1)
        #On change le lego
        self.individus[rand].legos[randlego] = Lego()


    # Representation d'une population de parcours sous forme de chaine de caracteres
    def __repr__(self):
        parcoursstr = ""
        for individu in self.individus :
            parcoursstr += str(individu)+"\n"
        return parcoursstr
