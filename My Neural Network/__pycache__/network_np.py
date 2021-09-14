#import random
import numpy as np

from activation_functions import *


class NeuralNetwork:
    
    def __init__(self,name='Unknown',learn='sigmoid',error=0.001):
        

        self.name = name #Le nom du réseau
        if 'tangent' == str.lower(learn): # Fonction d'apprentissage
            self.fun_learn = tangent
            self.fun_learn_prime = tangentPrime
            self.name_fun_learn = 'tangent'
        else:
            self.fun_learn = sigmoid
            self.fun_learn_prime = sigmoidPrime
            self.name_fun_learn = 'sigmoid'
        self.error = error #Erreur d'apprentissage
        self.layer = [] #Tableau de couches avec le nombre de neurones par couche
        self.link = np.array(([]),dtype=float) #Le tableau avec tout les poids
        self.cell = np.array(([]),dtype=float) #Le tableau avec les différentes valeurs des neurones

        self.lock = 0 #verouillage après l'initialisation

    # Modifier ou afficher les parametres

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
        
    def set_error(self, nbr):
        if (nbr >0):
            self.error = nbr
    
    def get_error(self):
        return self.error
    
    def set_fun_learn(self,name):

        if (str.lower(name) == 'tangent'):
            self.fun_learn = tangent
            self.fun_learn_prime = tangentPrime
            self.name_fun_learn = 'tangent'

        else :
            self.fun_learn = sigmoid
            self.fun_learn_prime = sigmoidPrime
            self.name_fun_learn = 'sigmoid'
    
    def get_name_fun_learn(self):
        return self.name_fun_learn

    def get_layer_cnt(self):
        return len(self.layer)

    def get_data(self):
        return [self.get_name(),self.get_name_fun_learn(),self.get_error(),self.get_layer_cnt()]

    def get_output_layer(self):
        return self.cell[-1]

    # Construction du réseau

    def set_layers(self,count=2):# Initilisation des couches du réseau

        if (self.lock == 0):
            if (count>=2):
                for i in range(0,count):
                    self.layer.append(0)
            else:
                print("Il doit y avoir au moins 2 couches")
        else:
            print("Le réseau est déjà créé, vous ne pouvez plus le modifier")

    def add_couche(self,pos): # ajouter une couche

        if (self.lock == 0):
            if (pos>=0 and pos<len(self.layer)):
                self.layer.insert(pos,0)
            else:
                print("Vous pouvez ajouter une couche dans l'intervalle [0,",len(self.layer)-1,"]")
        else :
            print("Le réseau est déjà créé, vous ne pouvez plus le modifier")
    
    def add_cell(self,layer,count=1): # ajout de neurone(s)

        if (self.lock == 0):
            if (layer>=0 and layer<len(self.layer) and count>0):
                self.layer[layer] += count
        else :
            print("Le réseau est déjà créé, vous ne pouvez plus le modifier")

    def add_all_cells(self,tab): # ajout de tout les neurones

        if (self.lock == 0):
            if(len(tab) == len(self.layer)):
                for i in range(0,len(tab)):
                    self.add_cell(i,tab[i])
            else:
                print("Le tableau doit etre de taille ",len(self.layer))
        else :
            print("Le réseau est déjà créé, vous ne pouvez plus le modifier")

    def network_build(self): # Initialisation du réseau, poids aleatoirs, valeur des neurones à 0

        test = 0
        for i in range(0,len(self.layer)):
            if (self.layer[i] <= 0):
                print("La couche ",i," doit contenir au moins 1 neurone")
                test = 1
        if (test != 1):
            if (self.lock == 0):
                self.lock = 1
                for i in range(0,len(self.layer)):
                    add = []
                    add1 = []
                    add_value = []
                    for j in range(0,self.layer[i]):
                        if (i != len(self.layer)-1):
                            for k in range(0,self.layer[i+1]):
                                add1.append(0.5)                  # à corriger pour le rendre aléatoire !!!!!!!!!!!!!!!!!!!! : random.uniform(0,1)
                            add.append(add1)
                            add1 = []
                        add_value.append(0)
                    if (i != len(self.layer)-1):
                        self.link.append(add)
                    self.cell.append(add_value)
            else:
                print("Reseau deja initialise")
        else :
            print("Vous ne pouvez pas lancer l'initialisation")

    # Apprentissage

    def fordward(self, tab): # Propagation, tab correspond aux valeurs a entrer dans la 1ere couche
        
        if (self.lock == 1):
            if (len(tab) == self.layer[0]):

                for i in range(0,len(tab)): # On stock dans la première couche les données d'entrées
                    self.cell[0][i] = tab[i]

                for i in range(1,len(self.cell)):
                    for j in range(0,len(self.cell[i])):
                        value = 0
                        for k in range(0,len(self.cell[i-1])):

                            # On stock la somme pondéré pour le prochain neurone :
                            value += self.cell[i-1][k] * self.link[i-1][k][j]
                        self.cell[i][j] = self.fun_learn(value)
            else:
                print("La couche d'entree doit contenir ",self.couche[0],"valeurs")
        else:
            print("Reseau non initialise")


    def backward(self, tab): # Retropropagation, tap correspond aux valeurs de sorties attendues

        if (len(tab) == len(self.cell[len(self.cell)-1])):

            for i in range(0,len(tab)):# On stock l'erreur dans la dernière couche (valeur_voulue - valeur_trouvée)
                self.cell[len(self.cell)-1][i] = tab[i] - self.cell[len(self.cell)-1][i]

            for i in range(len(self.cell)-1,0,-1):
                for j in range(0,len(self.cell[i-1])):
                    for k in range(0,len(self.link[i-1][j])):
                        somme = 0
                        for l in range(0,len(self.cell[i-1])):

                            # On effectue la somme pondérée du neurone vers lequel pointe la connexion :
                            somme += self.cell[i-1][l] * self.link[i-1][l][k]
                            
                        somme = self.fun_learn(somme)

                        # On met à jour le poids de la connexion 
                        self.link[i-1][j][k] -= self.get_erreur() * (-1 * self.cell[i][k] * somme * (1 - somme) * self.cell[i-1][j])
                for j in range(0,len(self.cell[i-1])):
                    somme = 0
                    for k in range(0,len(self.cell[i])):

                        # On met à jour les neurones de la prochaine couche en fonction de l'erreur qui se retropropage :
                        somme += self.cell[i][k] * self.link[i-1][j][k]
                    self.cell[i-1][j] = somme


    def learn(self, entree, sortie):
        
        """
            # Fonction d'apprentissage du reseau
            # Le premier paramètre est l'ensemble de valeurs à tester
            # Le second est le résultat attendu
        """
        if (self.control == 1):
            if(len(entree)==self.couche[0] and len(sortie)==self.couche[len(self.couche)-1]):
                self.parcourir(entree)
                self.retropropagation(sortie)
            else:
                print("La couche d'entrée doit contenir ",self.couche[0],"valeurs",
                      "La couche de sortie soit contenir ",self.couche[len(self.couche)-1],"valeurs")
        else:
            print("Reseau non initialise")



res = NeuralNetwork()

res.set_error(0.5)

res.set_layers(3)
res.add_all_cells([3,4,2])
res.network_build()

tab = res.get_data()
print("Nom du reseau :", tab[0],
      "\nFonction d'apprentissage :", tab[1],
      "\nValeur d'erreur d'apprentissage :", tab[2],
      "\nNombre de couche dans le réseau :", tab[3],
      "\n\n",res.cell,"\n",res.layer,"\n",res.link)

res.fordward([0.1,0.5,1])

tab = res.get_data()
print("Nom du reseau :", tab[0],
      "\nFonction d'apprentissage :", tab[1],
      "\nValeur d'erreur d'apprentissage :", tab[2],
      "\nNombre de couche dans le réseau :", tab[3],
      "\n\n",res.cell,"\n",res.layer,"\n",res.link)