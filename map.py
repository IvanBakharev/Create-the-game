from utils import randbool
from utils import radcell

CELL_TYPES = "🟩🌳🌊🏥🏬"
class Map:     
    def generate_river(self, l):
        rc = radcell(self.w, self.h)

    def generate_forest(self, r, mxr):
        for ri in range(self.h):
            for ci in range(self.w):
                if randbool(r, mxr):
                 self.cells[ri][ci] = 1

    def print_map(self):
        print("⬜️" * (self.w +2))
        for row in self.cells:
            print("⬜️", end="")
            for cell in row:
                if (cell >= 0 and cell < len(CELL_TYPES)):
                 print(CELL_TYPES[cell], end="")
            print("⬜️")        
        print("⬜️" * (self.w +2))

    def check_bounds(self, x, y):
        if (x < 0 or y < 0 or x >= self.h or y >= self.w):
            return False
        return True          
            
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]

tmp = Map(20, 10)
#tmp.generate_forest(3, 10)
tmp.print_map()        
        
