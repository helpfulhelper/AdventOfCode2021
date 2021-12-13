import numpy as np

opening = ["{", "[", "(", "<"]
closing = ["}", "]", ")", ">"]
mpoints = [1197,57,3,25137]
ipoints = [")", "]", "}", ">"]

def gobble(filename):
    with open(filename) as f:
#        data = [line.split() for line in f]
        data = f.readlines()
    return data

def match(line):
    op = []
    for c in line:
        if c in opening:
            op.append(c)
        if c in closing:
            o = op.pop()
            if o is opening[closing.index(c)]:
                pass
            else:
                return c
                
    #print(op)
    return op

def score(line):
    score = 0
    p = [closing[opening.index(x)] for x in line]
    for c in p:
        score = score * 5
        score += ipoints.index(c) + 1
    return score


def main():
    data = gobble('input')
    results = [match(d) for d in data]
    #print(results)
    
    k = []
    for x in results:
        if type(x) == type(list()):
            k.append(list(reversed(x)))
    #print(k)

    s_list = sorted([score(x) for x in k])
    #print(s_list)
    print(s_list[int((len(s_list)-1)/2)])
    
    
    
    #print(match(data[0]))
    #print(results)



#    mismatch = []
#    for d in [match(d) for d in data]:
#        if d != None:
#            mismatch.append(d)
#    print(sum([mpoints[closing.index(x)] for x in mismatch]))

if __name__ == "__main__":
    main()
