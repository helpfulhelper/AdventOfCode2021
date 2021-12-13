import numpy as np

def gobble(filename):
    with open(filename) as f:
        data = [line.strip() for line in f]
    return data

class Node:
    def __init__(self, identity:str):
        self.id = identity
        self.edges = set()
        self.small = self.id.islower()

    def add_edge(self, p1):
        self.edges.add(p1)

    def __repr__(self):
        return f'{self.id}'
    def __str__(self):
        return f'{self.id}'

class Graph:
    def __init__(self):
        self.data = {}
        self.nodes = set()
        self.graph = {}

    def add_node(self, id):
        self.nodes.add(Node(id))
    
    def add_edge(self, p1, p2):
        allval = self.graph[p1]
        
        self.graph.update({p1: })

    def __repr__(self):
        return f'{self.data}'
    def __str__(self):
        return f'{self.data}'

def main():
    data = gobble('Sexample')
    print(data)
    arr = [x.split('-') for x in data]
    print(arr)
    ids = set(np.array([x.split('-') for x in data]).flatten())
    print(ids)
    nodes = [Node(x) for x in ids]
    print(nodes)

if __name__ == "__main__":
    main()
