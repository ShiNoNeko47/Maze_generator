#!/usr/bin/python

import random

class Cell:
    def __init__(self, n):
        self.n = n
        self.walls = [True, True, True, True]
        self.cells_unvisited= [None, None, None, None]
        self.cells = [None, None, None, None]

    def remove_wall(self, n):
        self.walls[n] = False
        self.cells_unvisited[n].walls[n - 2] = False # n - 2 oposite wall

    def set_visited(self):
        for i in range(4):
            try:
                self.cells[i].cells_unvisited[i - 2] = None
                #print(self.cells_unvisited[i].n, self.cells_unvisited[i].cells_unvisited)
            except Exception:
                pass

def deptfirst(cell):
    cell.set_visited()
    while True:
        neighbours = 4 - cell.cells_unvisited.count(None)
        if neighbours == 0:
            return 0
        moves = []
        for i in cell.cells_unvisited:
            if i != None:
                moves.append(i)
        rand = int(random.random() * len(moves))
        move = moves[rand]
        cell.remove_wall(cell.cells_unvisited.index(move))
        print(cell.n, move.n)
        #print(cell.cells_unvisited)
        print()
        cell.cells_unvisited[cell.cells_unvisited.index(move)] = None
        deptfirst(move)

def gen_field(width, height):
    field = []
    for i in range(height):
        field.append(list())
        for j in range(width):
            field[i].append(Cell(i * width + j))
    for i in range(height):
        for j in range(width):
            if i != 0:
                field[i][j].cells_unvisited[0] = field[i - 1][j]
                field[i][j].cells[0] = field[i - 1][j]
            if j != 0:
                field[i][j].cells_unvisited[1] = field[i][j - 1]
                field[i][j].cells[1] = field[i][j - 1]
            if i != height - 1:
                field[i][j].cells_unvisited[2] = field[i + 1][j]
                field[i][j].cells[2] = field[i + 1][j]
            if j != width - 1:
                field[i][j].cells_unvisited[3] = field[i][j + 1]
                field[i][j].cells[3] = field[i][j + 1]
            #print(field[i][j].cells_unvisited)
    return field

def main():
    width, height = input('width, height: ').split()
    x, y = input('start(x y): ').split()
    field = gen_field(int(width), int(height))
    cell = field[int(y)][int(x)]
    deptfirst(cell)

if __name__ == '__main__':
    main()
