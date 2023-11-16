# --------------------------------------
# DONNEES
# --------------------------------------

# exemple de liste d'oiseaux observables
oiseaux = [("Merle", "Turtidé"), ("Moineau", "Passereau"), ("Mésange", "Passereau"),
           ("Pic vert", "Picidae"), ("Pie", "Corvidé"), ("Pinson", "Passereau"),
           ("Rouge-gorge", "Passereau"), ("Tourterelle", "Colombidé")] 

# exemples de listes de comptage ces listes ont la même longueur que oiseaux
comptage1 = [2, 5, 0, 1, 2, 0, 3, 5]
comptage2 = [2, 1, 3, 0, 0, 3, 5, 1]
comptage3 = [0, 0, 4, 3, 2, 1, 2, 4]

# exemples de listes d'observations. Notez que chaque liste correspond à la liste de comptage de
# même numéro
observations1 = [("Merle", 2), ("Moineau", 5), ("Pic vert", 1), ("Pie", 2),
                 ("Rouge-gorge", 3), ("Tourterelle", 5)]

observations2 = [("Merle", 2), ("Mésange", 1), ("Moineau", 3),
                 ("Pinson", 3), ("Tourterelle", 5), ("Rouge-gorge", 1)]

observations3 = [("Mésange", 4), ("Pic vert", 3), ("Pie", 2), ("Pinson", 1),
                 ("Rouge-gorge", 2), ("Tourterelle", 4)]


# --------------------------------------
# FONCTIONS
# --------------------------------------

def oiseau_le_plus_observe(liste_observations):
    """ recherche le nom de l'oiseau le plus observé de la liste
        (si il y en a plusieur on donne le 1er trouve)

    Args:
        liste_observations (list): une liste de tuples (nom_oiseau, nb_observes)

    Returns:
        str: l'oiseau le plus observé (None si la liste est vide)
    """
    oiseau_max = None
    for observation in liste_observations:
        if oiseau_max is None :
            oiseau_max = observation
        if observation[1] > oiseau_max[1]:
            oiseau_max = observation
    if oiseau_max is None:
        return None
    return oiseau_max[0]


def oiseau_le_plus_observe_ind(liste_observations):
    oiseau_max = None
    for ind in range(len(liste_observations)):
        if oiseau_max is None :
            oiseau_max = liste_observations[ind]
        if liste_observations[ind][1] > oiseau_max[1]:
            oiseau_max = liste_observations[ind]
    if oiseau_max is None:
        return None
    return oiseau_max[0]

def recherche_oiseau(liste_oiseaux,nom_oiseau):
    """donne les infos de l'oiseau demandé si il est dans la liste des oiseaux

    Args:
        liste_oiseaux (list): la liste des oiseaux
        nom_oiseau (str): le nom d'un oiseau 

    Returns:
        tuple: les informations de l'oiseau demandé

    Invariant:
        le nom de l'oiseau i de la liste des oiseaux n'est pas égal au nom de l'oiseau demandé 
    """
    for oiseau in liste_oiseaux:
        if nom_oiseau == oiseau[0]:
            return oiseau
    return None

def recherche_par_famille(liste_oiseaux,famille):
    """donne la liste des oiseaux de la liste des oiseaux appartenant à la famille demandée

    Args:
        liste_oiseaux (list): la liste des oiseaux
        famille (str): le nom d'une famille d'oiseaux

    Returns:
        list: la liste des oiseaux de la liste des oiseaux appartenants à la famille demandée

    Invariant:
        liste_famille contient tous les oiseaux appartenants à la famille demandée parmi les oiseaux traités
    """
    liste_famille = []
    for oiseau in liste_oiseaux:
        if famille == oiseau[1]:
            liste_famille.append(oiseau[0])
    return liste_famille

def est_liste_observation(liste_observ):
    """verifie si une liste est bien une liste d'observation

    Args:
        liste_observ (list): une liste 

    Returns:
        bool: True si la liste est une liste d'observations, False sinon

    Invariant:
        les éléments de la liste traités jusqu'ici sont de la forme d'une observartion
    """
    for ind in range(1,len(liste_observ)):
        if liste_observ[ind -1] > liste_observ[ind] or len(liste_observ[ind]) != 2 or not liste_observ[ind][0].isaplha or not liste_observ[ind][1].isint():
            return False
    return True

def max_observation(liste_observation):
    """donne le nombre du maximum d'observation

    Args:
        liste_observation (list): une liste d'observations

    Returns:
        int: le nombre maximum d'observations dans la liste d'observations

    Invariant:
        observ_mav contient le nombre maximum d'obresvations dans la partie de la liste d'observation déjà traitée
    """
    observ_max = 0
    for observation in liste_observation:
        if observation[1] > observ_max:
            observ_max = observation[1]
    return observ_max

def moyenne_oiseaux_observes(liste_observations):
    """donne le nombre moyen de spécimen observé dans la liste des observations

    Args:
        liste_observations (_type_): _description_

    Returns:
        _type_: _description_
    """
    somme = 0
    cpt = 0
    for observation in liste_observations:
        somme += observation[1]
        cpt += 1
    return somme/cpt

#--------------------------------------
# PROGRAMME PRINCIPAL
#--------------------------------------

# afficher_graphique_observation(construire_liste_observations(oiseaux, comptage3))
# observes = saisie_observations(oiseaux)
# afficher_graphique_observation(observes)
# afficher_observations(oiseaux, observes)


