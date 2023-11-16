# TP8 B - Manipuler des listes, ensembles et dictionnaires

troupeau_de_jean = { ' vache ' :12 , ' cochon ' :17 , ' veau ' :3} #il y a 12 vaches, 17 cochons et 3 veaux
troupeau_vide = dict() #il y a aucun animal dans ce troupeau
mon_troupeau = {'mouton': 45, 'brebis': 4, 'chien' :7}

def total_animaux(troupeau):
    """ Calcule le nombre total d'animaux dans un troupeau

    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        int: le nombre total d'animaux dans le troupeau

    Invariant:
        somme contient le nombre d'animaux déjà traités
    """
    somme = 0
    for nombre in troupeau.values():
        somme += nombre
    return somme


def tous_les_animaux(troupeau):
    """ Détermine l'ensemble des animaux dans un troupeau

    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        set: l'ensemble des animaux du troupeau
    
    Invariant:
        animaux contient le nom des animaux de la partie du troupeau déjà traitée
    """
    animaux = set()
    for animal in troupeau:
        animaux.add(animal)
    return animaux


def specialise(troupeau):
    """ Vérifie si le troupeau contient 30 individus ou plus d'un même type d'animal 

    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        bool: True si le troupeau contient 30 (ou plus) individus d'un même type d'animal,
        False sinon 

    Invariant:
        auncun animal de la liste n'a plus de 30 individus
    """
    animal_spe = False
    for nombre in troupeau.values():
        if nombre >= 30:
            return True
    return False


def le_plus_represente(troupeau):
    """ Recherche le nom de l'animal qui a le plus d'individus dans le troupeau
    
    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        str: le nom de l'animal qui a le plus d'individus  dans le troupeau
        None si le troupeau est vide) 
    
    Invariant:
        indiv_max contient le nom de l'animal avec le plus grand nombre d'individus parmi les animaux déjà traités
    """
    indiv_max = None
    max = 0
    for (animal,nombre) in troupeau.items():
        if nombre > max :
            indiv_max = animal
            max = nombre
    return indiv_max

def quantite_suffisante(troupeau):
    """ Vérifie si le troupeau contient au moins 5 individus de chaque type d'animal

    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        bool: True si le troupeau contient au moins 5 individus de chaque type d'animal
        False sinon
    
    Invariant:
        les annimaux traités jusqu'ici ont au moins 5 individus
    """
    for nombre in troupeau.values():
        if nombre < 5:
            return False
    return True


def reunion_troupeaux(troupeau1, troupeau2):
    """ Simule la réunion de deux troupeaux

    Args:
        troupeau1 (dict): un dictionnaire modélisant un premier troupeau {nom_animaux: nombre}
        troupeau2 (dict): un dictionnaire modélisant un deuxième troupeau        

    Returns:
        dict: le dictionnaire modélisant la réunion des deux troupeaux

    Invariant:
        troupeau_res contient les informations des animaux du troupeau1 et de la partie du troupeau2 déjà traitée  
    """
    troupeau_res = troupeau1.copy()
    for (animal,nombre) in troupeau2.items():
        if animal in troupeau_res:
            troupeau_res[animal] += nombre
        else:
            troupeau_res[animal] = nombre
    return troupeau_res


