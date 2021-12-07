import numpy as np


def gobble(filename):
    with open(filename) as f:
        data = [line.strip().split() for line in f]
    return data


def main():
#    data = gobble('example')
    data = np.genfromtxt('input',dtype=int,delimiter=',')
    maxi = np.max(data)
    mini = np.min(data)
    cost = []
#    print([abs(7-d) for d in data])
    for x in range(mini, maxi+1):
        c_e = []
        for d in data:
            units = abs(x-d)
            u = sum([x for x in range(1,int(units))])
            c_e.append(u+units)
        cost.append(c_e)
    tot_cost = [sum(d) for d in cost]
    print(min(tot_cost))
    
###THIS IS TERRIBLE A TERRIBLE IMPLEMENTATION. SO UGLY

if __name__ == "__main__":
    main()
