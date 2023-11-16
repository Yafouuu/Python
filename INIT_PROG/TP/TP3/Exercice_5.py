#5.1
def somme_n_entiers(ent):
    """Renvoie la somme des entiers de 0 a ent

    Args:
        ent (int): un entier

    Returns:
        int: la somme des entiers de 0 a ent
    """

    res = 0
    for chiffre in range(1, ent+1):
        res += chiffre   
    return res

def test_somme_ent():
    """tests
    """    
    assert somme_n_entiers(4) == 10
    assert somme_n_entiers(3) == 6
    assert somme_n_entiers(6) == 21
    assert somme_n_entiers(0) == 0

#5.2
def Syracuse(val_init, num_terme):
    """renvoie le terme numero n de la suite de syracuse

    Args:
        val_init (int): valeur initiale Uo de la suite
        num_terme (int): numero du terme final attendu

    Returns:
        int: valeur du terme numero n (Un) de la suite 
    """
    res = val_init
    for indice in range(num_terme):
        if res%2 == 0:
            res = res // 2
        else:
            res = res*3 - 1 

    return res

def test_syracuse():
    """tests
    """    
    assert Syracuse(12,2) == 3
    assert Syracuse(4,2) == 1
    assert Syracuse(5,2) == 7
    assert Syracuse(5,4) == 10