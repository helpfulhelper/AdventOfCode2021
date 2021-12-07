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
        tot = []
        for d in data:
            tot.append(abs(x-d))
        cost.append(tot)
    tot_cost = [sum(d) for d in cost]
    print(min(tot_cost))
    


if __name__ == "__main__":
    main()
