import code
import numpy as np
from itertools import cycle

class Board:
    def __init__(self, x_max, y_max):
        self.x_max = x_max
        self.y_max = y_max
        self.board = np.zeros((x_max+1,y_max+1), dtype=int)
    
    def mark_line(self,line):
        if line.straight is True:
            x_range = range(line.x_start, line.x_end + 1)
            y_range = range(line.y_start, line.y_end + 1)
            zip_list = zip(x_range, cycle(y_range)) if len(x_range) >= len(y_range) else zip(cycle(x_range),y_range)
            for x, y in zip_list:
                self.board[x,y] += 1
                
    def count_danger(self):
        return len(self.board[self.board > 1])

    def __repr__(self):
        return f'{self.board}'
        
class Line:
    def __init__(self, x_start, y_start, x_end, y_end):
        self.x_start = min(x_start, x_end)
        self.y_start = min(y_start, y_end)
        self.x_end = max(x_start, x_end)
        self.y_end = max(y_start, y_end)
        self.straight = True if x_start == x_end or y_start == y_end else False
    
    def __str__(self):
        return f"""x_start: {self.x_start}, x_end: {self.x_end}. y_start: {self.y_start}, y_end: {self.y_end}. straight:{self.straight} """
    
    def __repr__(self):
        return f"""x_start: {self.x_start}, x_end: {self.x_end}. y_start: {self.y_start}, y_end: {self.y_end}. straight:{self.straight} """

def main():
    with open("input") as f:
        data = f.read().replace(' -> ',',').splitlines()
        data = [list(map(int, d.split(','))) for d in data]
    lines = [Line(*d) for d in data]
    max_x = max([x.x_end for x in lines])
    max_y = max([y.y_end for y in lines])
    B = Board(max_x,max_y)
    for m in lines:
        B.mark_line(m)
    
    #np.savetxt("output", B.board, fmt='%i')
    
    #print(max_x, max_y)
    #print(np.fliplr(np.rot90(B.board,3)))
    print(B.count_danger())

    #code.InteractiveConsole(locals=locals()).interact(banner="",exitmsg="")


if __name__ == "__main__":
    main()

