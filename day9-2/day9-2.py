import numpy as np

#cheat
from pylab import *
from scipy.ndimage import measurements



class Points:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"{self.data}"

    def __str__(self):
        return f"{self.data}"
    
    def is_lowest(self, x, y):
          return np.all(self.data[x,y] < self.get_neighbors(x, y))
    
    def get_neighbors(self, x, y):
        neighbors = []

        if x != 0:
            neighbors.append(self.data[x - 1, y])
            
        if x != (np.shape(self.data)[0] - 1):
            neighbors.append(self.data[x + 1, y])

        if y != 0:
            neighbors.append(self.data[x, y - 1])

        if y != (np.shape(self.data)[1] - 1):
            neighbors.append(self.data[x, y + 1])
        
        return neighbors

    def get_neighbor_coords(self, x, y):
        neighbors = []
        
        #left
        if x != 0:
            neighbors.append([x - 1, y])
        #right    
        if x != (np.shape(self.data)[0] - 1):
            neighbors.append([x + 1, y])
        #up
        if y != 0:
            neighbors.append([x, y - 1])
        #down
        if y != (np.shape(self.data)[1] - 1):
            neighbors.append([x, y + 1])
        
        return neighbors

    def get_basins(self, start_x, start_y, basin = set()):
        if basin == set():
            basin.add(tuple([start_x, start_y]))
        #print(basin)
        #print(type(basin))
#        print(self.get_neighbor_coords(start_x, start_y))
#        print(self.get_neighbor_coords(start_x, start_y))
#        print(list(zip(self.get_neighbors(start_x, start_y), self.get_neighbor_coords(start_x,start_y))))
        for v, c in zip(self.get_neighbors(start_x, start_y), self.get_neighbor_coords(start_x,start_y)):
            #print(v,c)
            #print(basin)
            if v != 9: 
                if tuple(c) not in basin:
                    basin.add(tuple(c))
                    print(basin)
                    return self.get_basins(c[0],c[1], basin)
                #else:
                #    return basin
                #return self.get_basins(c[0],c[1], basin)
            return basin



    def get_lowest(self):
        x_max, y_max = np.shape(self.data)
        p = []
        for x in range(x_max):
            for y in range(y_max):
                if self.is_lowest(x,y):
                    p.append([x,y])
        return p

def gobble(filename):
    with open(filename) as f:
        data = [line.strip().split() for line in f]
    return data

def main():
#    data = gobble('input')
    data = np.genfromtxt('input', dtype=str)
    data = np.array([[int(d) for d in str(word)] for word in data])
    d = Points(data)
    cheat_truth = np.isin(data, arange(9))
    cheat, num = measurements.label(cheat_truth)
    area = measurements.sum(cheat_truth, cheat, index=arange(cheat.max() + 1))
    
    
    print(sort(area))
    #print(cheat)
    #print(cheat_truth)


    t = []
#    temp = [[x,y] for x,y in d.get_lowest()]
    #print(temp[1])
#    print(d.get_basins(temp[1][0],temp[1][1]))
    #for x,y in temp:
    #    t.append(d.get_basins(x, y))
    #print(len(t))
    #print(d.get_neighbor_coords(0, 1))
    #print(d.get_neighbors(0, 9))


    #p_val = [d.data[x,y] for x,y in d.get_lowest()]
    #print(sum(p_val) + len(p_val))

if __name__ == "__main__":
    main()
