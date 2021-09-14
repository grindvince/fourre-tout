from tkinter import *
from random import randrange

# creation des variables

lenghX,lenghY,lenghCell = 50,50,10
life = [[0 for x in range(lenghX)]for y in range(lenghY)]
neighbour = [[0 for x in range(lenghX)]for y in range(lenghY)]
# death_rule = [0,1,1,0,0,0,0,0]
# birth_rule = [0,0,1,0,0,0,0,0]

def genocide(): # tuer toutes les cellules
    for y in range(lenghY):
        for x in range(lenghX):
            life[y][x]=0
    draw_cells()

def random_init(): # placement aléatiore des cellules vivantes
    genocide()
    for i in range(lenghX*lenghY//4):
        life[randrange(lenghX)][randrange(lenghY)] = 1
    draw_cells()

def neighbour_count(): #decompte des voisins
    for y in range(lenghY):
        for x in range(lenghX):
            neighbour[y][x] = 0
            for yy in range(-1,2):
                for xx in range (-1,2):
                    if not(xx == 0 and yy == 0):
                        try :
                            if life[y+yy][x+xx] == 1:
                                neighbour[y][x] += 1
                        except :
                            pass

def evolve(): #evolution de la grille
    for y in range(lenghY):
        for x in range(lenghX):
            if life[y][x] == 0 and neighbour[y][x] == 3 :
                life[y][x] = 1
            if life[y][x] == 1:
                if neighbour[y][x] < 2 or neighbour[y][x] > 3 :
                    life[y][x] = 0

def draw_cells(): # Dessiner toutes les cellules en fonction de la grille
    for y in range(lenghY):
        for x in range(lenghX):
            if life[y][x]==0:
                coul = "black"
            else:
                coul = "red"
            cell_field.itemconfig(cell[x][y], fill=coul)

def cycle(): # Calculer et dessiner le prochain cycle
    neighbour_count()
    evolve()
    draw_cells()

def start_cycles(): #lancer les cycles en boucle
    cycle()
    fenetre.after(1, start_cycles)

def stop_cycles(): #stopper les cycles en boucle
    pass


# fenetre principale
fenetre = Tk()
fenetre.title("Conway game of life")
cell_field = Canvas(fenetre, width=lenghCell*lenghX, height=lenghCell*lenghY, highlightthickness=0)
cell_field.pack()

cell=[[cell_field.create_rectangle(i*lenghCell,j*lenghCell,(i+1)*lenghCell,(j+1)*lenghCell,fill="black",width=0) for i in range(lenghX)] for j in range(lenghY)]

# bouton pour lancer le genocide
Button_genocide=Button(fenetre,text='Kill Em All', command=genocide)
Button_genocide.pack(padx='20px',pady='10px')
# bouton pour lancer les naissances aléatoires
Buton_random_init=Button(fenetre,text='Mode aléatoire', command=random_init)
Buton_random_init.pack(padx='20px',pady='10px')
# bouton pour lancer le cycle suivant
Buton_cycle=Button(fenetre,text='cycle suivant', command=cycle)
Buton_cycle.pack(padx='20px',pady='10px')
# bouton pour lancer 100 cycles
Buton_100_cycle=Button(fenetre,text="Démarrer", command=start_cycles)
Buton_100_cycle.pack(padx='20px',pady='10px')



fenetre.mainloop()