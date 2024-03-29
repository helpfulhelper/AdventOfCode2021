import numpy as np

def bincounts(data, val):
    counts = np.bincount(data)

def counts(data):
    arr = np.array([list(line) for line in data]).astype(np.int8)
    col_totals = arr.sum(axis=0)
    return col_totals

def get_gamma(data):
    tots = counts(data)
    num_logs = len(data)
    gamma = []
    for ind, col in enumerate(tots):
        gamma.append( 1 if col > num_logs/2 else 0 )
    return int("".join(str(i) for i in gamma),2)
    
def get_epsilon(data):
    tots = counts(data)
    num_logs = len(data)
    epsilon = []
    for ind, col in enumerate(tots):
        epsilon.append( 0 if col > num_logs/2 else 1 )
    return int("".join(str(i) for i in epsilon),2)

def get_eps_fast(gamma):
    return ~gamma

def get_power_rate(data):
    gamma = get_gamma(data)
    epsilon = get_epsilon(data)
    return gamma * epsilon

def axis_swap(data):
    arr = np.array([list(line) for line in data]).astype(np.int8)
    return arr.swapaxes(0,1)



def main():
    with open("input") as f:
        data = f.read().splitlines()
    print(get_power_rate(data))
    
    temp = axis_swap(data)
    f_count = []
    for row in temp:
        counts = np.bincount(row)
        f_count.append(counts)
    print(np.bincount(axis_swap(data)))
    print(most_f)

if __name__ == "__main__":
    main()
