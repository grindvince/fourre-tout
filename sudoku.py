from random import choice

class Sudoku:
    def __init__(self,grid):
        
            self.grid = grid

    def display(self): # fonction affichage grille
        for y in range(9):
            print (self.grid[y])
        print("\n")

    def solve(self): #solution avec backtracking
        find = self.find_empty()
        if not find :
            return True
        else :
            y,x = find
        h=self.hypothesis(x,y)
        for i in h:
            self.grid[y][x] = i
            if self.solve():
                return True
            self.grid[y][x] = 0
        return False

    def find_empty(self): 
        for y in range(9):
            for x in range(9):
                if self.grid[y][x] == 0:
                    return y,x
        return None

    def hypothesis(self,x,y): # recherches des hypotheses ou possibilités
        test = [1,2,3,4,5,6,7,8,9]

        for i in range(9):
            if self.grid[y][i] in test:  #ligne
                test.remove(self.grid[y][i])
            if self.grid[i][x] in test:  #Colonne
                test.remove(self.grid[i][x])

        for j in range(3):#region
            for i in range(3):
                if self.grid[y//3*3+j][x//3*3+i] in test:
                    test.remove(self.grid[y//3*3+j][x//3*3+i])
        return test

grid = [
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
Sudoku_1 = Sudoku(grid)
Sudoku_1.display()
Sudoku_1.solve()
Sudoku_1.display()