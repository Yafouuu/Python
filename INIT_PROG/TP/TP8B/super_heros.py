avengers = {
' Spiderman ': (5 , 5 , ' araign é e a quatre pattes ') ,
' Hulk ': (7 , 4 , " Grand homme vert " ) ,
' Agent 13 ': (2 , 3 , ' agent 13 ') ,
'M Melin ': (2 , 6 , ' expert en archi ') 
}

def intelligence_moyenne(dico_hero):
    """Calcule l'intelligence moyenne des héros du dictionnaire

    Args:
        dico_hero (dict): un dictionnaire de héros

    Returns:
        float: la moyenne de l'intelligence des héros

    Invariant:
        somme contient la somme des intelligences des héros du dico traités jusqu'ici
        cpt contient le nombre de héros traités jusqu'ici
    """
    somme = 0
    cpt = 0
    for info in dico_hero.values():
        somme += info[1]
        cpt += 1
    if dico_hero == dict():
        return 0
    return somme/cpt

def kikelplusfort(dico_hero):
    """Renvoie le nom du héros le plus fort du dictionnaire

    Args:
        dico_hero (dict): un dictionnaire de héros

    Returns:
        str: le héros le plus fort du dictionnaire, None si le dictionnaire est vide

    Invariant:
        plus_fort contient le nom du héros le plus fort parmi les héros déjà traités
    """
    plus_fort = None
    force_max = 0
    for (nom,info) in dico_hero.items():
        if info[0] > force_max:
            plus_fort = nom
            force_max = info[0]
    return plus_fort

def combienDeCretins(dico_hero):
    """compte le nombre de héros dont l'intelligence est strictement inferieure à la moyenne

    Args:
        dico_hero (dict): un dictionnaire de héros

    Returns:
        int: le nombre de héros dont l'intelligence est strictement inferieure à la moyenne

    Invariant:
        nb_cretins contient le nombre de héros dont l'intelligence est strictement inferieure à la moyenne parmi les héros déjà traités
    """
    inte_moy = intelligence_moyenne(dico_hero)
    nb_cretins = 0
    for info in dico_hero.values():
        if info[0] < inte_moy :
            nb_cretins += 1
    return nb_cretins