import code
import numpy as np
from itertools import cycle
import matplotlib.pyplot as plt

class Board:
    def __init__(self, x_max, y_max):
        self.x_max = x_max
        self.y_max = y_max
        self.board = np.zeros((x_max+1,y_max+1), dtype=int)
    
    def mark_line(self,line):
        if line.straight is True:
            for x, y in line.zipper():
                self.board[x,y] += 1
    
    def mark_diags(self,line):
        if line.diag is True:
            for x, y in line.zipper():
                self.board[x,y] += 1

    def count_danger(self):
        return len(self.board[self.board > 1])

    def __repr__(self):
        return f'{self.board}'
        
class Line:
    def __init__(self, x_start, y_start, x_end, y_end):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.straight = True if (x_start == x_end) or (y_start == y_end) else False
        self.diag = True if (y_end -  y_start == x_end - x_start) or (y_end - y_start == x_start - x_end)  else False
    
    def __str__(self):
        return f"""x_start: {self.x_start}, x_end: {self.x_end}. y_start: {self.y_start}, y_end: {self.y_end}. straight:{self.straight} diag:{self.diag}"""
    
    def __repr__(self):
        return f"""x_start: {self.x_start}, x_end: {self.x_end}. y_start: {self.y_start}, y_end: {self.y_end}. straight:{self.straight} diag:{self.diag}"""

    def zipper(self):
        x = self.gen_range(self.x_start, self.x_end)
        y = self.gen_range(self.y_start, self.y_end)
        return zip(x, cycle(y)) if len(x) >= len(y) else zip(cycle(x),y)

    def gen_range(self, start, end):
        if end > start:
            return range(start, end + 1, 1)
        elif start > end:
            return range(start, end - 1, -1)
        elif start == end:
            return [start]

def main():
    with open("input") as f:
        data = f.read().replace(' -> ',',').splitlines()
        data = [list(map(int, d.split(','))) for d in data]
    lines = [Line(*d) for d in data]
    max_x = max([x.x_end for x in lines])
    max_y = max([y.y_end for y in lines])
    #hacky fix - i'll clean up getting the max of all 4 possibilities
    max_z = max(max_x, max_y)
    B = Board(max_z,max_z)
    for m in lines:
        B.mark_line(m)
        B.mark_diags(m)

    plt.imshow(B.board)
    plt.show()
    #print(np.fliplr(np.rot90(B.board,3)))
    print(B.count_danger())

#    code.InteractiveConsole(locals=locals()).interact(banner="",exitmsg="")



if __name__ == "__main__":
    main()

