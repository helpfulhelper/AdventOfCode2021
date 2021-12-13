import numpy as np
from collections import defaultdict
from pprint import pprint

def gobble(filename):
    with open(filename) as f:
        data = [line.strip() for line in f]
    return data

def all_paths(graph, start, end, path=[]):
    path = path + [start]
    #Found the end! Return the path we took
    if start == end:
        return [path]
    #Building our list of paths
    paths = []
    #From our current starting node, iterate through connected nodes
    for node in graph[start]:
        #print((node in path), (node.isupper()))
        #If we haven't visited here before:
        if node not in path:
            #Recurse with the starting point of our current node
            newpaths = all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
        #If we have been here before, and it's a small cave, we can visit it twice
        if node in path and path.count(node) == 1 and node != 'start' and node != "end":
            newpaths = all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)            
        #But if we have been here before, see if it's a large cave
        elif node in path and node.isupper():
            #If it is, recurse all available paths again
            #print("in a large cave")
            newpaths = all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

#oh god damn it.  visit only a single small cave a 2nd time, not every small cave can be visited twice.

def main():
    data = gobble('Sexample')
    entry = [x.split('-') for x in data]

    #holy shit defaultdict is amazing.
    graph = defaultdict(list)
    for key,value in entry:
        graph[key].append(value)
        graph[value].append(key)
    paths = all_paths(graph, 'start', 'end')
    print(len(paths))

    #print([x for x in graph])
    #pprint(paths)
    a = (set([",".join(x) for x in paths]))
    sex = set(gobble('sexample.ans'))
    diff = list(a - sex)
    print(diff)



if __name__ == "__main__":
    main()
