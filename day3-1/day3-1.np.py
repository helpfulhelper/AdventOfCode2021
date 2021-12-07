import numpy as np
from dataclasses import dataclass
from collections import Counter

def gobble(filename):
    with open(filename) as f:
        data = [line.strip().split() for line in f]
    return data

def get_count(arr, ind=None):
    return [np.bincount(d) for d in np.transpose(arr)][ind] if ind is not None else [np.bincount(d) for d in np.transpose(arr)]

def get_col_max(arr, ind=None):
    counts = get_count(arr, ind)
    if ind is None:
        return [np.argmax(d) for d in counts]
    else:
        return np.argmax(counts)

def get_col_min(arr, ind=None):
    counts = get_count(arr, ind)
    if ind is None:
        return [np.argmin(d) for d in counts]
    else:
         return np.argmin(counts)

def get_eps(arr):
    eps = ""
    for s in get_col_min(arr):
        eps += str(s)
    return int(eps,2)

def get_gamma(arr):
    gamma =""
    for s in get_col_max(arr):
        gamma += str(s)
    return int(gamma,2)

def get_power(arr):
    return get_eps(arr) * get_gamma(arr)

def get_oxy(arr, pos = 0):
    if len(arr) == 1:
        return arr
    else:
        curr = [x[0] for x in arr]
#        curr = np.where([arr[pos] == get_col_max(arr,pos)])
        print(curr)
#        get_oxy(arr[get_col_max(arr, pos)],pos + 1)

def get_co2(arr):
    pass

def get_lifesupport(arr):
    return get_oxy(arr) * get_co2(arr)

def main():
#    data = gobble('example')
    npd = np.genfromtxt('example', delimiter=1, dtype=int)

#   print([np.bincount(d) for d in np.transpose(npd)])
#    print(get_eps(npd))
#    print(get_power(npd))
    print(get_oxy(npd,2))
    #print(npd[get_col_max(npd,0)])

if __name__ == "__main__":
    main()