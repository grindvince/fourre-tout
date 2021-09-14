sudoku = [
    [6,0,0, 1,7,0, 0,0,5],
    [0,0,0, 0,4,0, 0,2,0],
    [0,0,0, 0,0,0, 8,9,0],

    [0,3,7, 8,0,0, 0,0,2],
    [5,0,0, 0,0,1, 0,0,9],
    [0,0,2, 0,0,0, 0,0,0],

    [0,0,5, 0,2,4, 0,0,0],
    [0,0,0, 0,1,0, 6,0,0],
    [7,0,0, 3,0,0, 0,0,0]
]

def display(grid): # fonction affichage grille
     for y in range(9):
         print (grid[y])

def solve(grid): #solution avec backtracking
    find = find_empty(grid)
    if not find :
        return True
    else :
        y,x = find
    h=hypothesis(grid,x,y)
    for i in h:
        grid[y][x] = i
        if solve(grid):
            return True
        grid[y][x] = 0
    return False

def find_empty(grid): 
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                return y,x
    return None

def hypothesis(grid,x,y): # recherches des hypotheses ou possibilités
    test = [1,2,3,4,5,6,7,8,9]

    for i in range(9):
        if grid[y][i] in test:  #ligne
            test.remove(grid[y][i])
        if grid[i][x] in test:  #Colonne
            test.remove(grid[i][x])

    for j in range(3):#region
        for i in range(3):
            if grid[y//3*3+j][x//3*3+i] in test:
                test.remove(grid[y//3*3+j][x//3*3+i])
    return test


display(sudoku)
solve(sudoku)
print("___________________________")
display(sudoku)