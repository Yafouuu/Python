# Codé par Papy Force X, jeune padawan de l'informatique

def longueur_ok(chaine):
    """Vérifie si la chaine a une longueur adaptée pour un mot de passe

    Args:
        chaine (str): une chaine de caracteres

    Returns:
        bool: True si la haine contient plus de 8, False sinon
    """
    return len(chaine) > 8

def chiffre_ok(chaine):
    """Vérifie si la chaine contient au moins un chiffre

    Args:
        chaine (str): une chaine de caracteres

    Returns:
        bool: True si la chaine contient un chiffre, False sinon

    Invariant :
        la partie de la chaine traitée jusqu'ici ne contient pas de chiffre 
    """
    nb_chiffre = 0
    for lettre in chaine:
        if lettre.isdigit():
            nb_chiffre += 1
    return nb_chiffre >= 3

def chiffre_consec_ok(chaine):
    """Vérifie si la chaine ne contient pas de chiffres consecutif

    Args:
        chaine (str): une chaine de caracteres

    Returns:
        bool: True si la chaine ne contient pas de chiffres consecutifs, False sinon

    Invariant:
        aucun des caracteres traités jusqu'ici ne sont deux à deux des chiffres
    """
    for ind_chaine in range(1,len(chaine)):
        if chaine[ind_chaine-1].isdigit() and chaine[ind_chaine].isdigit():
            return False
    return True

def plus_petit_chiffre_solo(chaine):
    """Vérifie si le plus petit chiffre de la chaine est bien présent une seule fois dans la chaine

    Args:
        chaine (str): une chaine de caracteres

    Returns:
        bool: True si le plus petit chiffre de la chaine est présent une eule fois dans celle-ci, False sinon

    Invariant:
        test indique si un des chiffres testés jusqu'ici est le plus petit et s'il apparrait bien qu'une seule fois
    """
    test = True
    min = chaine[0]
    for chiffre in chaine:
        if chiffre < min:
            min = chiffre
            test = True
        elif chiffre == min:
            test = False
    return test



def sans_espace(chaine):
    """Vérifie si la chaine ne contient pas d'espace

    Args:
        chaine (str): une chaine de caracteres

    Returns:
        bool: True si la chaine ne contient pas d'espaces, False sinon

    Invariant:
        aucun des caracteres traités jusqu'ici n'est un espace
    """
    for lettre in chaine:
        if lettre == " ":
            return False
    return True


def stocke_dans_fichier():
    """Fait entrer un mot de passe à l'utilisateur et le stocke dans un fichier

    Invariant:
        l'utilisateur n'a pas entré de mot de passe correct
    """
    fichier = open('mdpUltraSecret.txt', 'a')
    login = input("Entrez votre nom : ")
    mot_de_passe_correct = False
    while not mot_de_passe_correct :
        mot_de_passe = input("Entrez votre mot de passe : ")
        # Gère l'affichage
        if not longueur_ok(mot_de_passe):
            print("Votre mot de passe doit comporter au moins 8 caractères")
        elif not chiffre_ok(mot_de_passe):
            print("Votre mot de passe doit comporter au moins 3 chiffres")
        elif not sans_espace(mot_de_passe):
            print("Votre mot de passe ne doit pas comporter d'espace")
        elif not chiffre_consec_ok(mot_de_passe):
            print("Votre mot de passe ne doit pas comporter deux chiffres consécutifs") 
        elif not plus_petit_chiffre_solo(mot_de_passe):
            print("Le chiffre le plus petit doit apparaître une seule fois")
        else:
            mot_de_passe_correct = True        
    print("Votre mot de passe est correct")
    fichier.write(mot_de_passe)
    fichier.close()
    return mot_de_passe

def dialogue_mot_de_passe():
    """Fait entrer un mot de passe à l'utilisateur

    Returns:
        str: le mot de passe de l'utilisateur
    """
    login = input("Entrez votre nom : ")
    mot_de_passe_correct = False
    while not mot_de_passe_correct :
        mot_de_passe = input("Entrez votre mot de passe : ")
        # Gère l'affichage
        if not longueur_ok(mot_de_passe):
            print("Votre mot de passe doit comporter au moins 8 caractères")
        elif not chiffre_ok(mot_de_passe):
            print("Votre mot de passe doit comporter au moins 3 chiffres")
        elif not sans_espace(mot_de_passe):
            print("Votre mot de passe ne doit pas comporter d'espace")
        elif not chiffre_consec_ok(mot_de_passe):
            print("Votre mot de passe ne doit pas comporter deux chiffres consécutifs") 
        elif not plus_petit_chiffre_solo(mot_de_passe):
            print("Le chiffre le plus petit doit apparaître une seule fois")
        else:
            mot_de_passe_correct = True        
    print("Votre mot de passe est correct")
    return mot_de_passe

stocke_dans_fichier()
