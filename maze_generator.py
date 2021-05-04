#!/usr/bin/python

import random
from PIL import Image, ImageDraw
import sys
from cell import Cell
from maze import Maze

def depth_first(cell, image):
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
        image.draw_line(cell.n, move.n, (255, 0, 0))
        #print(cell.cells_unvisited)
        cell.cells_unvisited[cell.cells_unvisited.index(move)] = None
        depth_first(move, image)
        image.draw_line(cell.n, move.n, (255, 255, 255))

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
    sys.setrecursionlimit(10000)

    width, height = input('width, height: ').split()
    filename = 'maze' + width + 'x' + height + '.png'

    width, height = int(width), int(height)
    field = gen_field(width, height)

    x = random.random() * width
    y = random.random() * height
    cell = field[int(y)][int(x)]
    image = Maze(width, height)
    depth_first(cell, image)
    image.img.save(filename)

if __name__ == '__main__':
    main()
