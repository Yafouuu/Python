#4.1
def somme_pairs_liste(liste):
    """Renvoie la somme des entiers pairs de la liste d'entree

    Args:
        liste (lst): Une liste d'entiers

    Returns:
        int: la somme des nombre pairs de la liste d'entree
    """

    res = 0

    for elt in liste:
        if elt % 2 == 0:
            res += elt

    return res

def test_somme_pairs_liste():
    """tests
    """    
    assert somme_pairs_liste([12,6,7,9,5,3]) == 18
    assert somme_pairs_liste([5,5,5,5,5,5,5]) == 0
    assert somme_pairs_liste([2,2,2,2,2,2,2,2,2,2]) == 20
    assert somme_pairs_liste([]) == 0

#4.2
def derniere_voyelle(chaine):
    """Retourne la derniere voyelle de la chaine de caractere d'entree

    Args:
        chaine (str): une chaine de caracteres

    Returns:
        str: derniere voyelle de la chaine d'entree
    """

    res = None

    for lettre in chaine:
        if lettre in 'aeiouy':
            res = lettre
    return res

def test_derniere_voyelle():
    """tests
    """
    assert derniere_voyelle('bongiorno') == 'o'
    assert derniere_voyelle('bonjour') == 'u'
    assert derniere_voyelle('nnnnnnnnzzzzzzqsd') is None
    assert derniere_voyelle('') is None

#4.3
def proportion_negatifs_liste(liste):
    """Renvoir la proportion de nombres negatifs dans la liste d'entree 

    Args:
        liste (lst): une liste d'entiers

    Returns:
        float: proportion de negatifs dans la liste d'entree
    """

    res = 0
    compteur = 0

    for elt in liste:
        if elt < 0:
            compteur += 1


    if len(liste) == 0:
        res = None
    else:
        res = compteur / len(liste)
        
    return res

def test_prop_neg_liste():
    """tests
    """
    assert proportion_negatifs_liste([4,-2,8,-1,5,-8]) == 0.5
    assert proportion_negatifs_liste([1,15,7,8,55,2,333,36]) == 0.0
    assert proportion_negatifs_liste([-1,-1,-2,-55,-8,-8-7,-6]) == 1.0
    assert proportion_negatifs_liste([]) is None