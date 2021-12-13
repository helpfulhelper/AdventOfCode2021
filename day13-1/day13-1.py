import numpy as np

def gobble(filename):
    with open(filename) as f:
        data = [line.strip().split() for line in f]
    return data

def main():
    d = gobble('input')
    footer = d[d.index([])+1:]
    data = np.genfromtxt('input',skip_footer=len(footer),delimiter=",", dtype=int)
    footer = [x[2].split("=") for x in footer]
    max_x = max([x[0] for x in data])+1
    max_y = max([y[1] for y in data])+1
    print(max_x, max_y)
    grid = np.zeros((max_x,max_y), dtype=bool)
    for x,y in data:
        grid[x,y] = 1
    #print(footer[0][2])
    print(footer)

    axis = 0 if footer[0][0] == "x" else 1
    idx = int(footer[0][-1])
    p1,_,p2 = np.split(grid, [idx,idx+1], axis)
    p2 = np.flipud(p2) if not axis else np.fliplr(p2)
    print(p2.shape)
    #print(p1.shape - p2.shape)
    #print((p1.shape[1]-p2.shape[1],0),(p1.shape[0] - p2.shape[0],0))
    p2 = np.pad(p2, ((p1.shape[0]-p2.shape[0],0),(p1.shape[1] - p2.shape[1],0)),'constant')
    print(p2.shape)
    p3 = p1 + p2
    print(p3)
    print(sum(sum(p3)))
    #p1,p2 = temp[0],temp[1]
    #print(p1,p2) 
    #print(np.flipud(np.rot90(grid)))
    
    
    #print(data)
    #print(data.pop(len(data)-2))
    #print(footer)
if __name__ == "__main__":
    main()
