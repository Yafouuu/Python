def nb_occ_sup(liste, valeur):
    """renvoie none si le nombre d'elements dans la liste si le nombre d'elements dans la liste egaux à valeur est superieur a 3
    None sinon.

    Args:
        liste (list): une liste de nombres
        valeur (int): un nombre 

    Returns:
        int ou None_type: si plus de 3 elements de liste sont egaux a valeur 
    """
    ind_liste = 0
    idem_val_et_sup_3 = 0
    for elem in liste:
        if elem == valeur:
            idem_val_et_sup_3 += 1
            if idem_val_et_sup_3 > 3:
                return ind_liste
        ind_liste += 1
    return None

def test_nb_occ_sup_a_3():
    assert nb_occ_sup([12, 5, 8, 48, 12, 418, 185, 17, 5, 87],20) is None
    assert nb_occ_sup([], 16) is None
    assert nb_occ_sup([1,1,1,1,5,7,85,1,23,6,4,55],1) == 3
    assert nb_occ_sup([1,548,5,8,6,26,55,66,95,1,1,55,1,22222,548,333,8],1) == 12


#1.1) yyy contient le compte des elements == valeur et <= 3
#     xxx contient le compte des elements de liste
#1.2) return xxx est executee à condition que elem == valeur et que yyy > 3

#l'invariant est idem_val_et_sup_3 : le nombre < 3 d'elements = à valeur jusqu'ici

#exo 2
#2.1 :
def recherche_premier_ind(chaine):
    """Renvoie l'indice du premier element de la chaine qui est un chiffre

    Args:
        chaine (str): Une chaine 

    Returns:
        int: l'indice du premier element de chaine qui est egal a carac
    """
    for ind in range(len(chaine)):
        if chaine[ind].isdigit():
            return ind
    return None

#l'invariant est tous les caracteres traites jusqu'ici ne sont pas des chiffres

def test_recherche_ind():
    assert recherche_premier_ind('') is None
    assert recherche_premier_ind('on est le 30/09/2021') == 10
    assert recherche_premier_ind('demain on est le 01/10/2021') == 17
    assert recherche_premier_ind('hier on etait le 29/09/2021') == 17

# --------------------------------------
# Exemple de villes avec leur population
# --------------------------------------
liste_villes = ["Blois", "Bourges", "Chartres", "Châteauroux", "Dreux",
                "Joue-lès-Tours", "Olivet", "Orleans", "Tours", "Vierzon"]
population = [45871, 64668,  38426, 43442, 30664, 38250, 22168, 116238,
              136463,  25725]

#2.2

#l'invariant est : tous les noms des villes traitees jusqu'ici ne sont pas le nom de la ville demandee

def pop_ville(tab_ville,tab_pop,nom_ville):
    """renvoie le nombre d'habitant de la ville demandee

    Args:
        tab_ville (list): Une liste de noms de villes
        tab_pop (_type_): La liste de la population de la ville de tab_ville correspondant
        nom_ville (_type_): Le nom d'une ville

    Returns:
        int ou None_type: La population de la ville au nom correspondant a nom_ville 
    """
    popu = None
    for i in range(len(tab_ville)):
        if tab_ville[i] == nom_ville:
            popu = tab_pop[i]
    return popu

def test_pop_ville():
    assert pop_ville(liste_villes,population,"Blois") == 45871
    assert pop_ville(liste_villes,population,"Grenoble") == None
    assert pop_ville([],[],"") == None
    assert pop_ville(liste_villes,population,"Vierzon") == 25725

#invariant : jusqu'ici la liste est triee dans l'ordre croissant

def triee_croissante(liste):
    """verifie si la liste est triee dans l'ordre croissant

    Args:
        liste (list): Une liste de nombres

    Returns:
        bool: True si la liste est triee dans l'ordre croissant, False sinon
    """
    for i in range(len(liste)-1):
        if liste[i] > liste[i+1]:
            return False
    return True

def test_triee():
    assert triee_croissante([1,2,3,4,5,6,])
    assert triee_croissante([])
    assert triee_croissante([1,1,1,1,1,1])
    assert not triee_croissante([2,4,1,5,7,5,1,2])

#invariant : aucune valeur traitee jusqu'ici ne depasse seuil

def depasse_seuil(liste,seuil):
    """Verifie si aucun nombre de la liste depasse le seuil indique

    Args:
        liste (list): Une liste de nombres
        seuil (int): Une valeur definissant un seuil

    Returns:
        bool: True si aucune valeur de la liste ne depasse le seuil, False sinon
    """
    for val in liste :
        if val > seuil:
            return False
    return True

def test_seuil():
    assert depasse_seuil([1,1,4,5,2,1,4,2,1,3],5)
    assert not depasse_seuil([9,8,89,5,7,4,5,6,74,56,7],9)
    assert depasse_seuil([], 47)
    assert not depasse_seuil([9],7)


#invariant : le caractère n'est pas un espace et le caractère est un @ si on n'a pas rencontre de @ parmis les caractères dejà traites

def est_adresse_mail(chaine):
    """Regarde si la chaine de caratere en entree est une adresse mail potentielle 

    Args:
        chaine (str): Une chaine de caractere

    Returns:
        bool: True si la chaine est une adresse mail potentielle, False sinon
    """
    cpt_at = 0
    res = None
    if chaine[0] != '@' and chaine[-1] != '.':
        for ind in range(len(chaine)) :
            if chaine[ind] != ' ':
                if cpt_at == 0:
                    if chaine[ind] == '@':
                        cpt_at += 1
                elif cpt_at == 1:
                    if chaine[ind] == '.':
                        res = True
                else:
                    return False
            else:
                return False
        return res
    return False

def test_est_adresse_mail():
    assert est_adresse_mail('adresse_mail@valide.fr')
    assert not est_adresse_mail('@dresse.mail@nonvalide.com')
    assert not est_adresse_mail('adressemail@nonvalide.com.')
    assert est_adresse_mail('adresse.mail@valide.fr.com')

# ---------------------------------------
# Exemple de scores
# ---------------------------------------
scores = [352100, 325410, 312785, 220199, 127853]
joueurs = ['Batman', 'Robin', 'Batman', 'Joker', 'Batman']

#4.1
#invariant : le nom du joueur nom_joueur n'est pas dans la liste

def meilleur_score_joueur(tab_scores,tab_joueurs,nom_joueur):
    """Donne le meilleur score d'un joueur entre en parametre

    Args:
        tab_scores (list): La liste des scores 
        tab_joueurs (list): La liste des joueurs ayant fait les scores de la liste de scores
        nom_joueur (str): Le nom d'un joueur

    Returns:
        int ou None_type: Le meilleur score du joueur nom_joueur, None si nom_joueur n'est pas dans tab_joueurs
    """
    for ind in range(len(tab_scores)):
        if tab_joueurs[ind] == nom_joueur:
            meilleur_score = tab_scores[ind]
            return meilleur_score
    return None

def test_meilleur_score_joueur():
    assert meilleur_score_joueur(scores,joueurs,'Batman') == 352100
    assert meilleur_score_joueur(scores,joueurs,'Robin') == 325410
    assert meilleur_score_joueur([],[],'Harley Queen') is None
    assert meilleur_score_joueur(scores,joueurs,'Harley Queen') is None

#4.2
#invariant : jusqu'ici la liste est triee par ordre dercroissant

def score_sont_tries(tab_scores):
    """Verifie que la liste des scores est bien triee dans l'ordre decroissant

    Args:
        tab_scores (list): La liste des scores

    Returns:
        bool: True si la liste des scores est triee dans l'ordre decroissant, False sinon
    """
    for ind in range(len(tab_scores)-1):
        if tab_scores[ind] < tab_scores[ind+1]:
            return False
    return True

def test_score_sont_tries():
    assert score_sont_tries(scores)
    assert not score_sont_tries([7542,544,28888,1454,9617])
    assert score_sont_tries([17864,14596,11562,1])
    assert score_sont_tries([])

#4.3
#invariant : cpt est égal au le nombre de fois qu'il y a nom_joueur dans la liste traitee

def occurrences_joueur(tab_joueurs,nom_joueur):
    """Compte combien de fois un joueur apparait dans la liste des joueurs

    Args:
        tab_joueurs (list): La liste des joueurs associes aux scores
        nom_joueur (str): Un joueur

    Returns:
        int: le nombre de fois que le joueur apparait dans la liste des joueurs ayant fait les meilleurs scores
    """
    cpt = 0
    for joueur in tab_joueurs:
        if nom_joueur == joueur:
            cpt += 1
    return cpt

def test_occurrences_joueur():
    assert occurrences_joueur(['Batman', 'Robin', 'Batman', 'Joker', 'Batman'],'Batman') == 3
    assert occurrences_joueur([],'Joker') == 0
    assert occurrences_joueur(['Batman', 'Robin', 'Batman', 'Joker', 'Batman'],'Robin') == 1
    assert occurrences_joueur(['Batman', 'Robin', 'Batman', 'Joker', 'Batman'],'Harley Queen') == 0

#4.4
#invariant : le joueur nom_joueur n'est pas dans tab_classement

def meilleur_classement(tab_classement,nom_joueur):
    """Renvoie le meilleur classement du joueur nom_joueur dans la liste tab_classement

    Args:
        tab_classement (list): le classement des meilleurs joueurs 
        nom_joueur (str): le nom d'un joueur

    Returns:
        int ou None_type: le meilleur classement du joueur nom_joueur, None si le joueur n'est pas dans tab_classement
    """
    for ind in range(len(tab_classement)):
        if nom_joueur == tab_classement[ind]:
            return ind + 1
    return None

def test_meilleur_classement():
    assert meilleur_classement(['Batman', 'Robin', 'Batman', 'Joker', 'Batman'],'Batman') == 1
    assert meilleur_classement([],'Joker') is None
    assert meilleur_classement(['Batman', 'Robin', 'Batman', 'Joker', 'Batman'],'Robin') == 2
    assert meilleur_classement(['Batman', 'Robin', 'Batman', 'Joker', 'Batman'],'Harley Queen') is None

#4.5
#invariant : le score testé est inferieur au score entré en parametre

def ind_inser_score(tab_scores,score):
    """Retourne l'indice auquel il faut ajouter le score pour que la liste reste triee

    Args:
        tab_score (list): Une liste triee des scores
        score (int): Un score

    Returns:
        int: L'indice auquel ajouter le score pour que la liste de scores reste triee
    """
    if len(tab_scores) is None:
        return 0
    for ind in range(len(tab_scores)):
        if score > tab_scores[ind]:
            return ind
    return len(tab_scores)

def test_ind_inser_score():
    assert ind_inser_score([352100, 325410, 312785, 220199, 127853],314570) == 2
    assert ind_inser_score([352100, 325410, 312785, 220199, 127853],105247) == 5
    assert ind_inser_score([352100, 325410, 312785, 220199, 127853],374201) == 0
    assert ind_inser_score([],255411) == 0

#4.6 

def insere_score_et_joueur(score,joueur,tab_scores,tab_joueurs):
    """Ajoute score et joueur dans les liste tab_scores et tab_joueurs

    Args:
        score (int): score d'un joueur
        joueur (str): nom du joueur associé à score 
        tab_scores (list): Une liste de scores
        tab_joueurs (list): La liste des noms des joueurs associés aux scores de tab_scores
    """
    tab_scores.insert(ind_inser_score(tab_scores,score),score)
    tab_joueurs.insert(ind_inser_score(tab_scores,score),joueur)


def test_insere_score_et_joueur():
    scores = []
    joueurs = []
    insere_score_et_joueur(721,"alberto",scores,joueurs)
    assert scores == [721]
    assert joueurs == ["alberto"]
    insere_score_et_joueur(214,"bob",scores,joueurs)
    assert scores == [721,214]
    assert joueurs == ["alberto","bob"]
