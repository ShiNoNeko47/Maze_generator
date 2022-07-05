class Cell:
    def __init__(self, n):
        self.n = n
        self.cells_unvisited = [None, None, None, None]
        self.connections = []
        self.cells = [None, None, None, None]

    def set_visited(self):
        for i in range(4):
            try:
                self.cells[i].cells_unvisited[i - 2] = None
                # print(self.cells_unvisited[i].n, self.cells_unvisited[i].cells_unvisited)
            except Exception:
                pass
