import numpy as np
from collections import Counter
from sys import getsizeof

def gobble(filename):
    with open(filename) as f:
        data = [line.strip().split() for line in f]
    return data

def step(rules, prev_poly):
    curr_poly = []
    curr_poly.append(prev_poly[0])
    for z in zip(prev_poly, prev_poly[1:]):
#        print(z)
        k = "".join(z)
#        print(k)
#        print(f"is k in rules? {'yes' if k in rules else 'no'}")
        if k in rules:
#            new_str = "".join((z[0],rules[k],z[1]))
            new_str = "".join((rules[k],z[1]))
#            print(f"inserting: {new_str}")
            curr_poly.append(new_str)
        else:
#            print(f"pair not in rules, inserting: {k}")
            curr_poly.append(k)
#        print(f'current: {curr_poly}')
    return "".join(curr_poly)

def main():
    data = gobble('input')
    start = data[0][0]
    rules = dict([(i[0],i[2]) for i in [d for d in data[2:]]])
    end = start

    for x in range(10):
#        print(f"Step {x+1}")
        end = step(rules,end)
#        print(f"Length: {len(end)}, size of: {getsizeof(end)}")
    
    counts = Counter(end)
    #print(end)
#    print(len(end))
    print(counts.most_common()[0][1] - counts.most_common()[-1][1])

if __name__ == "__main__":
    main()
