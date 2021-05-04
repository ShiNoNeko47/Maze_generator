#!/usr/bin/python

import random
from PIL import Image, ImageDraw
import sys

sys.setrecursionlimit(5000)

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

class Draw:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.img = Image.new('RGB', (width * 2 + 1, height * 2 + 1))

    def draw_line(self, a, b):
        self.draw = ImageDraw.Draw(self.img)
        self.draw.line((int(a % self.width) * 2 + 1, int(a / self.width) * 2 + 1, int(b % self.width) * 2 + 1, int(b / self.width) * 2 + 1), (255, 255, 255), 1)

def deptfirst(cell, image):
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
        image.draw_line(cell.n, move.n)
        #print(cell.cells_unvisited)
        cell.cells_unvisited[cell.cells_unvisited.index(move)] = None
        try:
            deptfirst(move, image)
        except RecursionError:
            print('Size too big!')

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
    filename = 'maze' + width + 'x' + height + '.png'
    width, height = int(width), int(height)
    x, y = input('start(x y): ').split()
    field = gen_field(width, height)
    cell = field[int(y)][int(x)]
    image = Draw(width, height)
    deptfirst(cell, image)
    image.img.save(filename)

if __name__ == '__main__':
    main()
