from math import exp,tanh

# Fonctions d'activation
def sigmoid(s):
    return 1/(1+exp(-s))

def tangent(s):
    return tanh(s)

# Dérivée des fonctions d'activation
def sigmoidPrime(s):
    return s * (1 - s)

def tangentPrime(s):
    return 1 - s **2