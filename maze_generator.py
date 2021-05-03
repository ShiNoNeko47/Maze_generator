#!/usr/bin/python

import random

class Cell:
    def __init__(self):
        self.walls = [True, True, True, True]
        self.cells = [None, None, None, None]

    def remove_wall(self, n):
        self.walls[n] = False
        self.cells[n].remove_wall(n - 2) # n - 2 oposite wall

    def set_visited(self):
        for i in range(4):
            try:
                self.cells[i].cells[i - 2] = None
            except Exception:
                continue

def gen_field(width, height):
    field = []
    for i in range(height):
        field.append(list())
        for j in range(width):
            field[i].append(Cell())
    for i in range(height):
        for j in range(width):
            if i != 0:
                field[i][j].cells[0] = field[i - 1][j]
            if j != 0:
                field[i][j].cells[1] = field[i][j - 1]
            if i != height - 1:
                field[i][j].cells[2] = field[i + 1][j]
            if j != width - 1:
                field[i][j].cells[3] = field[i][j + 1]
            print(field[i][j].cells)

def main():
    width, height = input('width, height: ').split()
    gen_field(int(width), int(height))
    x, y = input('start(x y): ').split()

if __name__ == '__main__':
    main()
