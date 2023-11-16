# 7.1 : la vitesse du véhicule en km/h et la limitation de vitesse en km/h

# 7.2 : (entrée = 70, 50) --> amende (euro) : 135, retrait de points : 1, suspension de permis (annee) : 0
# (entree = 110, 90) --> amende (euro) : 68, retrait de points : 1, suspension de permis (annee) : 0
# (entree = 200, 130) --> amende (euro) : 1500, retrait de points : 6, suspension de permis (annee) : 3
# (entree = 150, 110) --> amende (euro) : 135, retriat de points : 4, suspension de permis (annee) : 3

#7.3 : 

def contravention_vitesse(vitesse_vehicule, limitation):
	"""Donne les sanctions encourues par un automobiliste en fonction de la vitesse de son vehicule et de la limitation en vigueur

	Args:
		vitesse_vehicule (int): la vitesse du vehicule de l'automobiliste en km/h
		limitation (int): limitation en vigueur de la vitesse en km/h

	Returns:
		tuple: (montant de l'amende en euro, nombre de point(s) retirés, nombre d'annee de suspension de permis)
	"""
	dif = vitesse_vehicule - limitation #diference entre la vitesse du vehicule et la limitation

	if dif <= 0 :
		amende = 0
		points_retires = 0
		suspension_permis = 0

	elif dif <= 20 and limitation <= 50 :
		amende = 135
		points_retires = 1
		suspension_permis = 0

	elif dif <= 20 and limitation > 50:
		amende = 68
		points_retires = 1
		suspension_permis = 0

	elif dif <= 30 :
		amende = 135
		points_retires = 2
		suspension_permis = 0
	
	suspension_permis = 3
	if dif <= 40 :
		amende = 135
		points_retires = 4
		

	elif dif <= 50 :
		amende = 135
		points_retires = 4
		

	else :
		amende = 1500
		points_retires = 6

	return (amende, points_retires, suspension_permis)

def test_contrav() :
	assert contravention_vitesse(70, 50) == (135, 1, 0)
	assert contravention_vitesse(110, 90) == (68, 1, 0)
	assert contravention_vitesse(200, 130) == (1500, 6, 3)
	assert contravention_vitesse(150, 110) == (135, 4, 3)
	print('OK')

print (contravention_vitesse(100,110), test_contrav())