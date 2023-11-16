# exercice 1
def cpt_nb_pairs(liste_entree):
    """ Vérifie s'il y a de nombre pairs que de nombres impairs dans la liste d'entree

    Args:
        liste_entree (lst): un liste de nombres

    Returns:
        bool: Vrai si plus de nombre pairs dans la liste d'entree, Faux sinon
    """
    pairs = 0
    impairs = 0
    # au début de chaque tour de boucle
    #  A COMPLETER
    for elt in liste_entree:
        if elt % 2 == 0:
            pairs += 1
        else:
            impairs += 1
    return pairs >= impairs


def test_pairs():
    assert cpt_nb_pairs([1,4,6,-2,-5,3,10]) == True
    assert cpt_nb_pairs([-4,5,-11,-56,5,-11]) == False
    assert cpt_nb_pairs([5,4,4,4,1,9,9,2]) == True
    assert cpt_nb_pairs([1,1,1,1,1,1,1,2]) == False