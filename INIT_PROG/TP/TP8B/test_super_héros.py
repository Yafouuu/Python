import super_heros

def test_intelligence_moyenne():
    assert super_heros.intelligence_moyenne(super_heros.avengers) == 18/4
    assert super_heros.intelligence_moyenne({'Hulk':(7,4,"Grand homme vert"), 'Drax':(6,2,'Benêt tatoué')}) == 3.0
    assert super_heros.intelligence_moyenne({}) == 0

def test_kikelplusfort():
    assert super_heros.kikelplusfort(super_heros.avengers) == 'Hulk'

def test_combienDeCretins():
    assert super_heros.combienDeCretins(super_heros.avengers) == 2