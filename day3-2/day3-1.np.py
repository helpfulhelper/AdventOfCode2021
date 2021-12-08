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
        return [np.argmax(d) if d[0] != d[1] else 1 for d in counts]
    else:
        return np.argmax(counts) if counts[0] != counts[1] else 1

def get_col_min(arr, ind=None):
    counts = get_count(arr, ind)
    if ind is None:
        return [np.argmin(d) if d[0] != d[1] else 0 for d in counts]
    else:
         return np.argmin(counts) if counts[0] != counts[1] else 0

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

def get_oxy_bin(arr, pos = 0):
    if len(arr) == 1:
        return arr
    else:
        com = get_col_max(arr, pos)
        f = arr[np.where(arr[:,pos] == com)]
        return get_oxy_bin(f, pos+1)

def get_co2_bin(arr, pos = 0):
    if len(arr) == 1:
        print(arr)
        print(len(arr))
        return arr
    else:
        com = get_col_min(arr, pos)
        f = arr[np.where(arr[:,pos] == com)]
        return get_co2_bin(f, pos+1)

def get_lifesupport(arr):
    o = get_oxy_bin(arr)[0]
    c = get_co2_bin(arr)[0]
    print(o, c)
    oxy = int("".join(str(i) for i in o),2)
    co2 = int("".join(str(i) for i in c),2)
    print(oxy, co2)
    return oxy*co2

def main():
#    data = gobble('example')
    npd = np.genfromtxt('input', delimiter=1, dtype=int)

#   print([np.bincount(d) for d in np.transpose(npd)])



    ls = get_lifesupport(npd)
    print(ls)

    #print(get_oxy(npd,2))
    #print(npd[get_col_max(npd,0)])

if __name__ == "__main__":
    main()