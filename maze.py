from PIL import Image, ImageDraw
import pygame


class Maze:
    def __init__(self, width, height, window):
        self.width = width
        self.height = height
        self.img = Image.new('RGB', (width * 2 + 1, height * 2 + 1))
        self.window = window

        try:
            self.visual = True
        except ImportError:
            self.visual = False

    def draw_line(self, a, b, color):
        self.draw = ImageDraw.Draw(self.img)

        def point(a): return (int(a % self.width) *
                              2 + 1, int(a / self.width) * 2 + 1)

        def point5(a): return ((int(a % self.width) * 2 + 1)
                               * 5, (int(a / self.width) * 2 + 1) * 5)
        self.draw.line(point(a) + point(b), (255, 255, 255), 1)
        if self.visual:
            pygame.draw.line(self.window, color, point5(a), point5(b), 5)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.visual = False
