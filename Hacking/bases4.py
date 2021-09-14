#!/usr/bin/env python3
# coding:utf8

age = 19
homme = True

if age >= 18 and homme:  # conditions avec if et elif + and
    print("Vous êtes majeur ET vous êtes un homme")
elif age < 18 and homme:
    print("Vous n'êtes pas majeur ET vous êtes un homme")
elif age >= 18 and not homme:
    print("Vous êtes majeur ET vous n'êtes pas un homme")
elif age < 18 and not homme:
    print("Vous n'êtes pas majeur ET vous n'êtes pas un homme")
else:
    print("Cas par défaut si aucune condition n'est remplie")

if age >= 18 or homme:
    print("Vous êtes majeur OU BIEN vous êtes un homme, OU les deux !")

i = 0

while i <= 10:  # boucle "tant que"
    print("i vaut : " + str(i))
    i = i + 1

amis = ["Pierre", "Paul", "Jacques"]

for ami in amis:  # pour chaque
    print(ami)

for i in range(10):  # faisable avec n'importe quel objet énumérable
    print(i)
