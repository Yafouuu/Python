"""Init Dev : TP9"""


# ==========================
# Petites bêtes
# ==========================

def toutes_les_familles(pokedex):
    """détermine l'ensemble des familles représentées dans le pokedex

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)

    Returns:
        set: l'ensemble des familles représentées dans le pokedex

    Invariant:
        ens_final contient de manière unique les type de tous les pokémons traités jusqu'ici

    Complexité:
        O(n)
    """
    ens_final = set()
    for (_,type_poke) in pokedex:
        ens_final.add(type_poke)
    return ens_final

def nombre_pokemons(pokedex, famille):
    """calcule le nombre de pokemons d'une certaine famille dans un pokedex

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)
        famille (str): le nom de la famille concernée

    Returns:
        int: le nombre de pokemons d'une certaine famille dans un pokedex

    Invariant :
        cpt contient le nombre de pokémons de la famille demandée parmi la partie du pokedex déjà traitée

    Complexité :
        O(n)
    """
    cpt = 0
    for (_,type_poke) in pokedex:
        if type_poke == famille:
            cpt += 1
    return cpt

def frequences_famille(pokedex):
    """Construit le dictionnaire de fréqeunces des familles d'un pokedex

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)

    Returns:
        dict: un dictionnaire dont les clés sont le nom de familles (str)
        et la valeur associée est le nombre de représentants de la famille (int)

    Invariant :
        dico_famille contient le nom des type de pokémon et leur nombre de représentants parmi les pokémons du pokedex déjà traités

    Complexité:
        O(n)
    """
    dico_famille = dict()
    for (_,type_poke) in pokedex:
        if type_poke in dico_famille:
            dico_famille[type_poke] += 1
        else:
            dico_famille[type_poke] = 1
    return dico_famille

def dico_par_famille(pokedex):
    """Construit un dictionnaire dont les les clés sont le nom de familles (str)
    et la valeur associée est l'ensemble (set) des noms des pokemons de cette
    famille dans le pokedex

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)

    Returns:
        dict: un dictionnaire dont les clés sont le nom de familles (str) et la valeur associée est
        l'ensemble (set) des noms des pokemons de cette famille dans le pokedex

    Invariant :
        dico_nom contient les familles et l'ensemble des représentants de ces familles parmi les pokemons déjà traités 

    Complexité :
        O(n)
    """
    dico_noms = dict()
    for (nom_poke,type_poke) in pokedex :
        if type_poke in dico_noms:
            dico_noms[type_poke].add(nom_poke)
        else:
            dico_noms[type_poke] = set()
            dico_noms[type_poke].add(nom_poke)
    return dico_noms

def famille_la_plus_representee(pokedex):
    """détermine le nom de la famille la plus représentée dans le pokedex

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)

    Returns:
        str: le nom de la famille la plus représentée dans le pokedex
    """
    famille_plus_grande = (None, 0)
    for (_,type_poke) in pokedex:
        nb_poke = nombre_pokemons(pokedex,type_poke)
        if nb_poke > famille_plus_grande[1]:
            famille_plus_grande = (type_poke,nb_poke)
    return famille_plus_grande[0]


# ==========================
# Petites bêtes (la suite)
# ==========================


def toutes_les_familles_v2(pokedex):
    """détermine l'ensemble des familles représentées dans le pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)

    Returns:
        set: l'ensemble des familles représentées dans le pokedex
    """
    ...

def nombre_pokemons_v2(pokedex, famille):
    """calcule le nombre de pokemons d'une certaine famille dans un pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)
        famille (str): le nom de la famille concernée

    Returns:
        int: le nombre de pokemons d'une certaine famille dans un pokedex
    """
    ...

def frequences_famille_v2(pokedex):
    """Construit le dictionnaire de fréqeunces des familles d'un pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)

    Returns:
        dict: un dictionnaire dont les clés sont le nom de familles (str) et la valeur
        associée est le nombre de représentants de la famille (int)
    """
    ...

def dico_par_famille_v2(pokedex):
    """Construit un dictionnaire dont les les clés sont le nom de familles (str)
    et la valeur associée est l'ensemble (set) des noms des pokemons de
    cette famille dans le pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)

    Returns:
        dict: un dictionnaire dont les clés sont le nom de familles (str) et la valeur associée est
        l'ensemble (set) des noms des pokemons de cette famille dans le pokedex
    """
    ...

def famille_la_plus_representee_v2(pokedex):
    """détermine le nom de la famille la plus représentée dans le pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)

    Returns:
        str: le nom de la famille la plus représentée dans le pokedex
    """
    ...
