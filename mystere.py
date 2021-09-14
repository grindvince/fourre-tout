from random import randint
nombre_mystere = randint (0, 100)
nombre = int(input("Quel est le nombre mystere ? "))
if nombre_mystere == nombre:
    print ("Bravo, vous avez trouvé le nombre mystère !")
elif nombre_mystere > nombre:
    print ("Votre nombre est trop petit !")
else:
    print ("Votre nombre est trop grand")