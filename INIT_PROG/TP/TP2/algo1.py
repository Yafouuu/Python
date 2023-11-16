def algo1(a, b, c, d):
    """Renvoie le plus petit nombre entre a, b, c et d

    Args:
        a (int): un nombre quelconque
        b (int): un nombre quelconque
        c (int): un nombre quelconque
        d (int): un nombre quelconque

    Returns:
        int : le plus petit nombre
    """

    if a < b :
        res = a
    else :
        res = b
    if c < res :
        res = c
    if d < res : 
        res = d

    return res 

def test_algo1():
    assert algo1(1, 2, 3, 4) == 1
    assert algo1(-6, 2, 544, -84) == -84
    assert algo1(1, 1, 1, 1) == 1
    assert algo1(0, 0, 0, 0) == 0
