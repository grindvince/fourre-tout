#!/usr/bin/env python3
# coding:utf8

print("Début du code")


def dire_bonjour():  # déclaration de fonction
    print("Dans la fonction")
    print("Bonjour à tous")
    print("Fin de la fonction")


print("On appelle maintenant la fonction :")
dire_bonjour()  # appel de fonction
print("Fin du code")


def affiche_addition(nombre1, nombre2):
    print(nombre1 + nombre2)


affiche_addition(1, 2)  # affiche via le print de la fonction


def retourne_addition(nombre1, nombre2):
    return nombre1 + nombre2


resultat = retourne_addition(1, 3)  # n'affiche rien mais créé une variable
print(resultat)  # affiche via le print
