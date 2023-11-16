#6
def somme_liste(liste_entree):
    """Renvoie la somme des éléments de liste_entree

    Args:
        liste_entree (liste): Une liste d'entiers

    Returns:
        int: la somme de tous les éléments de liste_entree
    """    

    res = None
    for nombre in liste_entree:
        if res is None :
            res = nombre
        else:
            res += nombre

    return res 

def test_somme_liste():
    """tests
    """    
    assert somme_liste([]) is None
    assert somme_liste([0]) == 0
    assert somme_liste([1,2,3,4,5,6]) == 21
    assert somme_liste([1,2,3,-4]) == 2

def max_liste(liste_entree):
    """Retourne le maximum de la liste_entree 

    Args:
        liste_entree (lst): une liste de nombre entiers

    Returns:
        int : le maximum de la liste_entree
    """    

    res = None
    for nbr in liste_entree :
        if res is None:
            res = nbr
        elif nbr > res :
            res = nbr

    return res

def test_max_liste():
    """tests
    """    
    assert max_liste([]) is None
    assert max_liste([0, 0, 0, 0, 0]) == 0
    assert max_liste([1,2,3,4,5,6,7,12,3]) == 12
    assert max_liste([1]) == 1


def nb_occ_mot(mot, lettre):
    """Renvoie le nombre de fois qu'apparait lettre dans mot

    Args:
        mot (str): un mot
        lettre (str): une lettre

    Returns:
        int: nombre de fois qu'apparait lettre dans mot
    """    

    res = 0 
    for carac in mot :
        if carac == lettre:
            res += 1

    return res

def test_nb_occ():
    """tests
    """    
    assert nb_occ_mot('', 'm') == 0
    assert nb_occ_mot('mamamia','') == 0
    assert nb_occ_mot('mamamia', 'x') == 0
    assert nb_occ_mot('mamamia', 'm') == 3

def min_liste(liste_entree):
    """Renvoie le minimum de liste_entree

    Args:
        liste_entree (lst): une liste d'entiers

    Returns:
        _type_: _description_
    """    
    res = None
    for nbr in liste_entree :
        if res is None:
            res = nbr
        elif nbr < res :
            res = nbr

    return res   

def test_min_liste():
    """tests
    """    
    assert min_liste([]) is None
    assert min_liste([0]) == 0
    assert min_liste([1,2,3,4,5,6,7,-7,10]) == -7
    assert min_liste([1,1,1,1,1,1,1]) == 1

def dif_min_max(liste_entree):
    """Renvoie la différence entre le minimum et le maximum de liste_entree

    Args:
        liste_entree (_type_): _description_

    Returns:
        _type_: _description_
    """    

    elt_min = None
    elt_max = None
    res = None
    for elt in liste_entree:
        elt_min = liste_entree[0]
        elt_max = liste_entree[0]
        res = 0
        if elt < elt_min:
            elt_min = elt
        else:
            elt_max = elt
    if res is not None :
        res = elt_max - elt_min

    return res

def test_dif_min_max():
    """tests
    """    
    assert dif_min_max([]) is None
    assert dif_min_max([0,0,0,0,0,0,0,0]) == 0
    assert dif_min_max([0]) == 0
    assert dif_min_max([1,2,3,4,5,6,7,8,9]) == 8

def cpt_sup10(liste_entree):
    """Renvoie combien il y a de nombre strictement supérieurs à 10 dans liste_entree

    Args:
        liste_entree (lst): une liste d'entiers

    Returns:
        int: combien il y a de nombre strictement supérieur à 10 dans liste_entree
    """    
    compteur = None
    for elt in liste_entree:
        compteur = 0
        if elt > 10 :
            compteur += 1

    return compteur

def test_sup10():
    """tests
    """    
    assert cpt_sup10([1,12,2,3,4,5,6,7]) == 1
    assert cpt_sup10([11,111,11,11,11,11,11,11]) == 8
    assert cpt_sup10([]) is None
    assert cpt_sup10([0,0,0,0,0,0,0,0,0]) == 0