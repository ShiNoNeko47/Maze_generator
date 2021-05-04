from PIL import Image, ImageDraw

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.img = Image.new('RGB', (width * 2 + 1, height * 2 + 1))

    def draw_line(self, a, b):
        self.draw = ImageDraw.Draw(self.img)
        point = lambda a: (int(a % self.width) * 2 + 1, int(a / self.width) * 2 + 1)
        self.draw.line(point(a) + point(b), (255, 255, 255), 1)

