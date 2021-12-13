import numpy as np
from PIL import Image as im

def gobble(filename):
    with open(filename) as f:
        data = [line.strip().split() for line in f]
    return data

def step(grid, inst):
    axis = 0 if inst[0] == "x" else 1
    idx = int(inst[1])
    p1,_,p2 = np.split(grid, [idx,idx+1], axis)
    p2 = np.flipud(p2) if not axis else np.fliplr(p2)
    p2 = np.pad(p2, ((p1.shape[0]-p2.shape[0],0),(p1.shape[1] - p2.shape[1],0)),'constant')
    p3 = p1 + p2
    return p3


def main():
    d = gobble('input')
    footer = d[d.index([])+1:]
    footer = [x[2].split("=") for x in footer]
    data = np.genfromtxt('input',skip_footer=len(footer),delimiter=",", dtype=int)

    max_x = max([x[0] for x in data])+1
    max_y = max([y[1] for y in data])+1
    grid = np.zeros((max_x,max_y), dtype=bool)

    for x,y in data:
        grid[x,y] = 1

    folded=grid
    for c in footer:
        folded = step(folded,c)

    rotated = np.flipud(np.rot90(folded))

    np.savetxt("answer", rotated, fmt='%i')

    img = im.fromarray(rotated)
    img.save('answer.png')

if __name__ == "__main__":
    main()
