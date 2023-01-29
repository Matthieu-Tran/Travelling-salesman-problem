from PopulationLego import PopulationLego

fini = 'Y'
while fini == 'Y' or fini == 'y':
    choix = input("Quelles critères voulez-vous choisir ? \n1. Les Individus rouges survivent mieux. \n2. Les Individus les plus variés en terme de couleur survivent le mieux. \n3. Les individus les plus petits survivent mieux. \n4. Les individus les plus grands survivent mieux.\n")
    while not choix.isnumeric() or int(choix)<1 or int(choix)>4:
        choix = input("Veuillez choisir un bon nombre\n")

    choix=int(choix)

    print("On gerere 10 individus de lego")
    # Creation une population de 10 tour de lego
    populationLegos = PopulationLego(10)
    print(populationLegos)
    print("Populating")

    i = 0
    while i<1000:
        print("Selection, on ne garde que les 5 individus les meilleurs")
        populationLegos.selection(choix)
        print(populationLegos)

        print("Reproduction, on fait se reproduire le meilleur individu avec le reste de la population")
        populationLegos.reproduction()
        print(populationLegos)

        print("On fait subir une mutation a un individus aléatoire de la population")
        populationLegos.mutation()
        print(populationLegos)
        i = i+1

    print("La meilleure tour de lego")
    print(populationLegos.best(choix))
    # On affiche le nombre de legos différents pour le deuxieme choix
    if choix == 2:
        print("Il y a: " + str(populationLegos.compterDiff()) + " legos différents")
    fini = input("Voulez vous recommencer ? Y|N \n")