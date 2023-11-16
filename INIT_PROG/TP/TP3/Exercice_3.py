# exercice 3
def nb_mots(phrase):
    """Fonction qui compte le nombre de mots d'une phrase

    Args:
        phrase (str): une phrase dont les mots sont
        séparés par des espaces (éventuellement plusieurs)

    Returns:
        int: le nombre de mots de la phrase
    """
    resultat = 0
    c1 = ' '
    cpt = 0
    # au début de chaque tour de boucle
    # c1 vaut ''
    # c2 vaut un caractère
    # resultat vaut 0
    for c2 in phrase:
        if c1 != ' ' and c1 != ''  and c2 == ' ':
            cpt += 1
        elif c1 == ' ' and c2 != ' ' and cpt == 1:
            resultat += 1
            cpt =0
        c1 = c2
    if resultat > 0:
        resultat += 1
    return resultat

def test_nb_mots():
    """tests
    """    
    assert nb_mots("bonjour, il fait beau") == 4
    assert nb_mots("houla!     je    mets beaucoup   d'  espaces    ") == 6
    assert nb_mots(" ce  test ne  marche pas ") == 5
    assert nb_mots("") == 0  # celui ci non plus