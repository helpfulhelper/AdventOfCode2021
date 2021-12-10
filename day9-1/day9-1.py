import numpy as np


class Points:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"{self.data}"

    def __str__(self):
        return f"{self.data}"
    
    def is_lowest(self, x, y):
        #Is the x,y coord a local minima?
        p = self.data[x,y]
        neighbors = []

        if x != 0:
            neighbors.append(self.data[x - 1, y])
            
        if x != (np.shape(self.data)[0] - 1):
            neighbors.append(self.data[x + 1, y])

        if y != 0:
            neighbors.append(self.data[x, y - 1])

        if y != (np.shape(self.data)[1] - 1):
            neighbors.append(self.data[x, y + 1])

        val_list = np.array(neighbors)
        
        return np.all(p < val_list) 


def gobble(filename):
    with open(filename) as f:
        data = [line.strip().split() for line in f]
    return data

def main():
#    data = gobble('input')
    data = np.genfromtxt('input', dtype=str)
    data = np.array([[int(d) for d in str(word)] for word in data])
    d = Points(data)
    x_max, y_max = np.shape(data)
    
    points = []
    for x in range(x_max):
        for y in range(y_max):
            if d.is_lowest(x,y):
                points.append(d.data[x,y])
                print(f"x: {x}, y: {y}, val: {d.data[x,y]}")
     
    print(sum(points) + len(points))

if __name__ == "__main__":
    main()
