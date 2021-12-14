import numpy as np
from collections import Counter
from sys import getsizeof

def gobble(filename):
    with open(filename) as f:
        data = [line.strip().split() for line in f]
    return data

###WAIT WE DON'T CARE ABOUT THE ACTUAL STRING - WE CARE ABOUT THE DIGRAPHS
#split initial string into digraphs
#if not a match, that digraph stays at 1
#BUT for each match to our rules generates TWO digraphs - i[0] + new, and new + i[0]. add these to the counts
#as such we can iterate over our curent set of counts for each digraph, and generate a new count for each new step
def step(rules:dict, prev:Counter()):
    new = Counter()
    for k in prev:
        if k in rules:
            #print(rules[k])
            new[rules[k][0]] += prev[k]
            new[rules[k][1]] += prev[k]
    #print(prev, new)
    return new

def main():
    data = gobble('input')
    start = data[0][0]
    rules = dict([(i[0],i[2]) for i in [d for d in data[2:]]])
    for k,v in rules.items():
        #print(k[0])
        rules[k] = k[0]+v, v+k[1]
    
    digraphs = Counter(["".join(f) for f in zip(start, start[1:])])

    #step4 = "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"
    #ds4 = Counter(["".join(f) for f in zip(step4, step4[1:])])
    #print(digraphs)


    for x in range(40):
        digraphs = step(rules, digraphs)

    tots = Counter()
    for x in digraphs:
        tots[x[0]] += digraphs[x]
        tots[x[1]] += digraphs[x]
    #print(tots)
    most = tots.most_common(1)[0][1]
    least = tots.most_common()[:-1-1:-1][0][1]
    print((most - least)/2)

if __name__ == "__main__":
    main()
