# exercice 2
def min_sup(liste_nombres, valeur):
    """trouve le plus petit nombre d'une liste supérieur à une certaine valeur

    Args:
        liste_nombres (list): la liste de nombres
        valeur (int ou float): la valeur limite du minimum recherché

    Returns:
        int ou float: le plus petit nombre de la liste supérieur à valeur
    """
    res = None
    # au début de chaque tour de boucle res est le plus petit élément
    # déjà énuméré supérieur à valeur
    for elem in liste_nombres:
        if elem > valeur :
            if res is None:
                res = elem
            else :
                if elem < res:
                    res = elem
    return res


def test_min_sup():
    """ tests
    """    
    assert min_sup([8, 12, 7, 3, 9, 2, 1, 4, 9], 5) == 7
    assert min_sup([-2, -5, 2, 9.8, -8.1, 7], 0) == 2
    assert min_sup([5, 7, 6, 5, 7, 3, 12, 14, -5], 10) == 12
    assert min_sup([], 5) is None