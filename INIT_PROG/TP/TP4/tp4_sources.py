#Exo 1 
def plus_long_plateau(chaine):
    """recherche la longueur du plus grand plateau d'une chaine
    Args:
        chaine (str): une chaine de caractères

    Returns:
        int: la longueur de la plus grande suite de lettres consécutives égales
    """
    lg_max = 0  # longueur du plus grand plateau déjà trouvé
    lg_actuelle = 1  # longueur du plateau actuel
    # caractère précédent dans la chaine
    for indice in range(len(chaine)-1):
        if chaine[indice] == chaine[indice +1] :  # si la lettre actuelle est égale à la précédente
            lg_actuelle += 1
        else:  # si la lettre actuelle est différente de la précédente
            if lg_actuelle > lg_max:
                lg_max = lg_actuelle
            lg_actuelle = 1
    if lg_actuelle > lg_max :  # cas du dernier plateau
        lg_max = lg_actuelle
    if len(chaine) == 0:
        lg_max = 0 
    
    return lg_max


def test_plus_long_plateau():
    """tests
    """
    assert plus_long_plateau('aaazzzeeerrrttt') == 3
    assert plus_long_plateau('') == 0
    assert plus_long_plateau('aaeeebbbbbbcr') == 6
    assert plus_long_plateau('aaasssssserrrttttttt') == 7
    assert plus_long_plateau("aabcd") == 2
    assert plus_long_plateau('aabcdddefgggg') == 4


#Exo 2
# --------------------------------------
# Exemple de villes avec leur population
# --------------------------------------
liste_villes1 = ["Blois", "Bourges", "Chartres", "Châteauroux", "Dreux",
                "Joué-lès-Tours", "Olivet", "Orléans", "Tours", "Vierzon"]
population = [45871, 64668,  38426, 43442, 30664, 38250, 22168, 116238, 136463,
              25725]

def plus_peuplee(liste_nom_villes, liste_nombre_habitants):
    """Renvoie le nom de la ville avec le nombre d'habitants le plus élevé

    Args:
        liste_nom_villes (lst): liste de villes
        liste_nombre_habitants (_type_): liste du nombre d'habitants des villes de liste_nom_villes, necessairement de la meme taille que celle-ci

    Returns:
        str: la ville avec le plus d'habitants
    """    
    assert len(liste_nom_villes) == len(liste_nombre_habitants) , "Les listes doivent être de même longueur !!"
    res = [0]
    prec = -1
    for indice in range(len(liste_nom_villes)):
        if liste_nombre_habitants[indice] > prec:
            res.append(liste_nom_villes[indice])
            prec = liste_nombre_habitants[indice]
    
    return res[-1]

def test_plus_peuplee():
    """tests
    """
    assert plus_peuplee([], []) == 0
    assert plus_peuplee(['a'], [0]) == 'a'
    assert plus_peuplee(['Checy'], [4500]) == 'Checy'
    assert plus_peuplee(liste_villes1, population) == 'Tours'


def transfo_str_int(chaine):
    """Transforme la chaine de caracteres numériques de type str en type int  

    Args:
        chaine (str): une chaine de caracteres numériques

    Returns:
        int: l'equivalent int de la chaine str de caracteres numériques
    """
    res = None
    
    if len(chaine) != 0 :
        for carac in chaine:
            if res is not None :
                res = res*10
                res += ord(carac) - ord('0')
            else:
                res = ord(carac) - ord('0')
            
    return res

def test_transfo():
    assert transfo_str_int('') is None
    assert transfo_str_int('0') == 0
    assert transfo_str_int('2021') == 2021
    assert transfo_str_int('1') == 1


def recherche_mot(liste_mot, lettre):
    """Renvoie la liste des mots de liste_mot commencants par lettre

    Args:
        liste_entree (lst): une liste de mot(s)
        lettre (str): une lettre

    Returns:
        lst: les mots de liste_mot qui commencent par lettre
    """

    res = []
    for mot in liste_mot:
        if mot[0] == lettre:
            res.append(mot)

    return res

def test_recherche_mot():
    assert recherche_mot([],'') == []
    assert recherche_mot(['alphabet','booleen', 'caractere'],'d') == []
    assert recherche_mot([], 'e') == []
    assert recherche_mot(["salut","hello","hallo","ciao","hola"],'h') == ["hello", "hallo", "hola"]


def decoupage_mots(phrase):
    """Découpe une chaine de caracteres en liste de mots

    Args:
        phrase (str): une chaine de caracteres

    Returns:
        lst: la liste des mots (alphabétiques) de phrase
    """

    res = []
    mot = ''
    for carac in phrase:
        if carac.isalpha():
            mot += carac
        else:
            if mot != '':    
                res += [mot]
                mot = ''

    return res

def test_decoupage():
    assert decoupage_mots('') == []
    assert decoupage_mots('(3*2)+1') == []
    assert decoupage_mots('!:,;*&') == []
    assert decoupage_mots("Cela fait déjà 28 jours! 28 jours à l’IUT’O! Cool!!") == ["Cela", "fait", "déjà", "jours", "jours", "à", "l", "IUT", "O", "Cool"]


def recherche_ultime(texte, lettre):
    """Recherche les mots de texte qui commencent par lettre

    Args:
        texte (str): Un texte
        lettre (str): Une lettre

    Returns:
        lst: liste des mots de texte commençant par lettre
    """

    return recherche_mot(decoupage_mots(texte), lettre)

def test_recherche_ultime():
    assert recherche_ultime('','') == []
    assert recherche_ultime("Cela fait déjà 28 jours! 28 jours à l’IUT’O! Cool!!", 'C') == ["Cela", "Cool"]
    assert recherche_ultime("Cela fait déjà 28 jours! 28 jours à l’IUT’O! Cool!!", 'O') == ['O']
    assert recherche_ultime("Cela fait déjà 28 jours! 28 jours à l’IUT’O! Cool!!", 'x') == []


def creer_liste_true(nombre):
    """créée une liste de booléens True sauf les deux premiers qui seront False

    Args:
        nombre (int): Un entier qui sera la valeur de la longueur +1 de la liste de sortie

    Returns:
        lst: Une liste de booléens True sauf les éléments d'indice 0 et 1
    """

    res = [0*nombre+1]
    for i in range(nombre+1):
        if i <= 2:
            res[i] = False
        else:
            res[i] = True

    return res 

def test_creer_liste():
    assert creer_liste_true(0) == [False]
    assert creer_liste_true(7) == [False,False,True,True,True,True,True,True]
    assert creer_liste_true(1) == [False,False]
    assert creer_liste_true(2) == [False,False,True]

def multiple_a_faux(liste_bool, multiple):
    """Met a faux les booléens de liste_bool aux indice multiples de multiple

    Args:
        liste_bool (lst): Une liste de booléens avec les deux premiers élément faux
        multiple (int): Un entier compris entre 2 et la longueur de liste_bool

    Returns:
        lst: La liste des booléens avec les éléments d'indice multiples de multiple mis à faux
    """

    for i in range(2, len(liste_bool)):
        if i != multiple and i%multiple == 0:
            liste_bool[i] = False

    return liste_bool

def test_multiple_a_faux():
    assert multiple_a_faux([]) == []
    assert multiple_a_faux([False]) == [False]
    assert multiple_a_faux([False,False,True,True,True,True,True,True,True,True]) == [False,False,True,True,False,True,False,True,False,False]
    assert multiple_a_faux([False,False]) == [False,False]


def crible_d_eratostene(taille_liste):
    """Renvoie tous les nombres premiers jusqu'a taille_liste

    Args:
        taille_liste (int): Un entier

    Returns:
        lst: la liste de tous les nombre premiers jusqu'a taille_liste
    """

    res = []
    liste = creer_liste_true(taille_liste)
    for i in range(len(liste)):
        liste = multiple_a_faux(liste,i)
        if liste[i]:
            res += i

    return res

def test_crible():
    assert crible_d_eratostene(0) == []
    assert crible_d_eratostene(1) == []
    assert crible_d_eratostene(6) == [2,3,5]
    assert crible_d_eratostene(20) == [2,3,5,7,11,13,17,19]