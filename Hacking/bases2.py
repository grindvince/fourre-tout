#!/usr/bin/env python3
# coding:utf8
import math

couleurs = ["Bleu", "Blanc", "Rouge", "Vert", 0, 1.2, True]  # pas logique tout de même !
couleurs.append("Noir")  # ajoute une couleur
print(couleurs)

autre_liste = [1, 2, 3]
couleurs.extend(autre_liste)  # concatène une autre liste
print(couleurs)

couleurs.insert(1, "Jaune")
print(couleurs)

couleurs.pop()
print(couleurs)

couleurs.remove("Noir")
print(couleurs)

print(math.cos(180))
