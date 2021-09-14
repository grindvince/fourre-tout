#!/usr/bin/env python3
# coding:utf8
import random
import time
import string

mot_de_passe = input("Quel est le mot de passe à deviner : ")  # parfois il convient d'utiliser raw_input pour éviter d'interpréter le contenu fourni


def mot_aleatoire():
    lettres = string.printable
    suiv = ""
    resultat = ""
    for i in range(len(mot_de_passe)):
        while mot_de_passe[i] != suiv:
            print(resultat + suiv)
            # time.sleep(0.05)
            suiv = random.choice(lettres)
        resultat += suiv
    return resultat


debut = time.time()
print(mot_aleatoire())
print("Durée : " + str(time.time() - debut) + " secondes")
