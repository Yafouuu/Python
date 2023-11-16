def algo2(m):
    """Permet de savoir s'il y a strictement plus de voyelles que de consonnes dans un mot ou non

    Args:
        m (str): un mot en minuscule

    Returns:
        bool: - si True alors il y a strictement plus de voyelles dans le mot
              - si False alors il y a autant ou plus de consonnes dans le mot
    """
    res = 0 
    for l in m:
        if l in 'aeiouy':
            res += 1
        else :
            res -= 1

    return res>0

def test_algo2() :
    assert algo2('mordre') == False
    assert algo2('yael') == True
    assert algo2('ah') == False
    assert algo2('reverse') == False