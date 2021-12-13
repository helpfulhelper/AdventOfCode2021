import numpy as np

opening = ["{", "[", "(", "<"]
closing = ["}", "]", ")", ">"]
points = [1197,57,3,25137]


def gobble(filename):
    with open(filename) as f:
#        data = [line.split() for line in f]
        data = f.readlines()
    return data
#
#def match(line, o = "", c = ""):
#    if len(line) == 0:
#        return
#    print(line[0])
#    if line[0] in opening:
#        o=line[0]
#        o_pos = opening.index(o)
#        c = match(line[1:])
#        print(f"{o} {o_pos} {close}")
#        if close != closing[o_pos]:
#        #print(close)
#        #print(closing[o_pos])
#            print(f"Corrupted line! Found {close}, expected {closing[o_pos]}, points = {points[closing.index(close)]}")
#            return points[closing.index(close)]
#    elif line[0] in closing:
#        return line[0]
#    else:
#        return 
#        
#
#def match(line, o="", c=""):
#    print(f'o = {o}, c = {c}')
#    if len(line) == 0:
#        print(f"end of line")
#        return
#    #if o == c:
#        print(f"match")
#
#    if line[0] in opening:
#        o = line[0]
#        #print(f'o = {o}')
#        return match(line[1:], o)
#    if line[0] in closing:
#        c = line[0]
#        if o == c:
#            print(f"match")
#            return match(line[1:], c)
#        #print(f'c = {c}')
#        #return match(line[1:], c)
#

def match(line):
    op = []
    for c in line:
        if c in opening:
            op.append(c)
            #print(op)
        if c in closing:
            o = op.pop()
            #print(f'does {o} match {opening[closing.index(c)]} ? {o is opening[closing.index(c)]}')
            if o is opening[closing.index(c)]:
                #print(f"match")
                pass
            else:
                #print(f"not a match")
                return c
    #return 
    
def main():
    data = gobble('input')
    mismatch = []
    for d in [match(d) for d in data]:
        if d != None:
            mismatch.append(d)
    print(sum([points[closing.index(x)] for x in mismatch]))
    #print(match(data[2]))


if __name__ == "__main__":
    main()
