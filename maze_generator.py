#!/usr/bin/python

import random
from PIL import Image, ImageDraw
import sys
from cell import Cell
from maze import Maze
import pygame

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
        cell.cells_unvisited[cell.cells_unvisited.index(move)] = None
        cell.connections.append(move)
        move.connections.append(cell)
        print(cell.n, cell.connections)
        depth_first(move, image)
        image.draw_line(cell.n, move.n, (255, 255, 255))

def gen_field(width, height):
    field = []
    for i in range(height):
        field.append(list())
        for j in range(width):
            field[i].append(Cell(i * width + j))
            nmax = i * width + j
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
    return field, nmax

def draw_path(cell, nmax, image, source):
    #print(len(cell.connections))
    if cell.n == nmax:
        print(cell.n, 1)
        return 1
    if len(cell.connections) == 1 and cell.n != 0:
        print(cell.n, 0)
        return 0
    for connection in cell.connections:
        if connection != source:
            if draw_path(connection, nmax, image, cell) == 1:
                image.draw_line(cell.n, connection.n, (255, 0, 0))
                return 1
    return 0

def main():
    sys.setrecursionlimit(1000000)

    width, height = input('width, height: ').split()
    filename = 'maze' + width + 'x' + height + '.png'
    width, height = int(width), int(height)

    pygame.init()
    window = pygame.display.set_mode(((width * 2 + 1) * 5, (height * 2 + 1) * 5))

    field, nmax = gen_field(width, height)
    print(nmax)

    x = random.random() * width
    y = random.random() * height
    cell = field[int(y)][int(x)]
    image = Maze(width, height, window)
    depth_first(cell, image)
    image.img.save(filename)
    draw_path(field[0][0], nmax, image, field[0][0])
    print('done')
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

if __name__ == '__main__':
    main()
