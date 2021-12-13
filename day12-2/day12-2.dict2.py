import numpy as np
from collections import defaultdict
#from pprint import pprint

def gobble(filename):
    with open(filename) as f:
        data = [line.strip() for line in f]
    return data

def all_paths(graph, start, end, path=[]):
    #include our current location to our path.
    path = path + [start]
    #Found the end! Return the path we took
    if start == end:
        return [path]
    #Building our list of paths
    paths = []
    #From our current starting node, iterate through connected nodes
    for node in graph[start]:
        #If we haven't visited here before:
        if node not in path:
            #Recurse with the starting point of our current node
            newpaths = all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
        #If we have been here before, and it's not the start or end nodes
        elif node in path and node!= 'start' and node != "end":
            #If it's a large cave, we can visit it as many times as we want
            if node.isupper():
                newpaths = all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)            
            #else it's a small cave, and if we've only visited it once before AND we haven't visited any other small cave twice, we can add it to our pathing
            elif path.count(node) == 1 and is_all_small_uniq(path):
                newpaths = all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
    return paths

def is_all_small_uniq(paths):
    smalls = []
    #extract all small caves
    for ele in paths:
        if ele.islower():
            smalls.append(ele)
    #if all smalls are unique, the lengths should be equal
    return len(set(smalls)) == len(smalls)

def main():
    data = gobble('input')
    entry = [x.split('-') for x in data]

    #holy shit defaultdict is amazing.
    graph = defaultdict(list)
    for key,value in entry:
        graph[key].append(value)
        graph[value].append(key)
    paths = all_paths(graph, 'start', 'end')
#    print(paths)
    print(len(paths))

if __name__ == "__main__":
    main()
