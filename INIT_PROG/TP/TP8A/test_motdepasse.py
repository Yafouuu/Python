import motdepasse

# --------------------------------------
# FONCTIONS
# --------------------------------------

def test_longueur_ok():
    assert motdepasse.longueur_ok("choubouilli") # longueur ok
    assert not motdepasse.longueur_ok("chou") # longueur pas ok
    assert not motdepasse.longueur_ok("") # chaine vide


def test_chiffre_ok():
    assert motdepasse.chiffre_ok("chou94b4ouilli")
    assert motdepasse.chiffre_ok("7choubo7uilli7")
    assert motdepasse.chiffre_ok("choubouilli555")
    assert motdepasse.chiffre_ok("chou773boui8lli")   
    assert not motdepasse.chiffre_ok("chou1")
    assert not motdepasse.chiffre_ok("un deux trois12")

def test_chiffre_consec_ok():
    assert motdepasse.chiffre_consec_ok("chuf4kgs7fs7")
    assert motdepasse.chiffre_consec_ok("fj8dk1sg")
    assert not motdepasse.chiffre_consec_ok("fdgh45fihdf")
    assert motdepasse.chiffre_consec_ok("")

def test_plus_petit_chiffre_solo():
    assert motdepasse.plus_petit_chiffre_solo("sdjgksgjhf487")
    assert motdepasse.plus_petit_chiffre_solo("fkgjfkjg70")
    assert not motdepasse.plus_petit_chiffre_solo("1fgghd7875542482fjd1")

def test_sans_espace():
    assert motdepasse.sans_espace("choubouilli") # sans espace ok
    assert not motdepasse.sans_espace("chou bouilli") # espace au milieu
    assert not motdepasse.sans_espace(" choubouilli") # espace au début
    assert not motdepasse.sans_espace("choubouilli ") # espace à la fin
    assert motdepasse.sans_espace("") # chaine vide
