import numpy as np
from collections import Counter
from sys import getsizeof

def gobble(filename):
    with open(filename) as f:
        data = [line.strip().split() for line in f]
    return data

###WAIT WE DON'T CARE ABOUT THE ACTUAL STRING - WE CARE ABOUT THE DIGRAPHS
#split initial string into digraphs
#if not a match in our rules, that digraph will disappear
#BUT for each match to our rules generates TWO digraphs - i[0] + new, and new + i[0]. add these to the counts
#as such we can iterate over our curent set of counts for each digraph, and generate a new count for each new step




def step(rules:dict, prev:Counter()):
    #new is gonna be our counts of each digraph after the iteration
    new = Counter()
    #for each digraph in our previous round
    for k in prev:
    #digraph foo is in our rule book, counts of digraph xA and Ay += foo
        new[rules[k][0]] += prev[k]
        new[rules[k][1]] += prev[k]
    #print(prev, new)
    return new

def main():
    data = gobble('input')
    #start is our initial polymer state
    start = data[0][0]
    #parse our set of rules once to generate dictionary of valid rules (xy = xAy)
    rules = dict([(i[0],i[2]) for i in [d for d in data[2:]]])
    #simplify our rules - every match will give us xA and Ay as a digraph pairing.
    for k,v in rules.items():
        #print(k[0])
        rules[k] = k[0]+v, v+k[1]
    #convert our initial polymer state into a set of digraphs, and establish an initial count for each digraph
    digraphs = Counter(["".join(f) for f in zip(start, start[1:])])

    for x in range(40000):
        digraphs = step(rules, digraphs)

    tots = Counter()
    for x in digraphs:
        tots[x[0]] += digraphs[x]
        tots[x[1]] += digraphs[x]
    tots[start[0]] += 1
    tots[start[-1]] += 1
#    print(tots)
    most = tots.most_common(1)[0][1]
    least = tots.most_common()[:-1-1:-1][0][1]
    most = most>>1
    least = least>>1

    #print(most - least)

if __name__ == "__main__":
    main()
