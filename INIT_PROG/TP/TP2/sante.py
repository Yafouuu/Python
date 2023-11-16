def sante(taille, poids):
    """Permet de detecter un pb de sante en fonction de l'imc

    Args:
        taille (float): la taille de la personne en mètre
        poids (int): le poids de la personne en kg

    Returns:
        str: le probmème eventuellement detecté
    """
    imc = poids/(taille*taille)

    if imc < 16.5:
        res = "famine"
    elif imc < 18.5:
        res = "maigreur"
    elif imc < 25:
        res = "normal"
    elif imc < 30:
        res = "surpoids"
    else:
        res = "obésité"
    return res 

def test_sante():
    assert sante(1.8, 80) == "normal" #indique que sante(1.8, 80) doit retourner "normal"
    assert sante(1.6, 67) == "surpoids" #indique que sante(1.6, 67) doit retourner "surpoids"
    assert sante(2.2, 40) == "normal" #test d'assert erroné