#Exo 7
def crible_eratostene(liste_rangee):
    """Renvoie la liste des nombres premiers de la liste d'entree

    Args:
        liste_rangee (lst): Une liste de nombre rangés en ordre croissant 

    Returns:
        lst: liste des nombres premiers de liste_rangee
    """    

    liste_nombres_premiers = []
    cpt = 0
    for i in range(len(liste_rangee)):
        for j in range(len(liste_nombres_premiers)):
            if liste_rangee[i] % liste_nombres_premiers[j] != 0:
                cpt += 1
        if cpt == len(liste_nombres_premiers):
            liste_nombres_premiers.append(liste_rangee[i])

    return liste_nombres_premiers