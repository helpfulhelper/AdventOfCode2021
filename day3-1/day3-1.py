def matrixify(data):
    temp = []
    for x, line in enumerate(data):
        temp[x] = map(int, str(line))
    return temp
    #return [map(int,str(line)) for line in data]

    
#    temp = [int(x) for x in list(line) for line in data]
#    for row in temp:
#        temp = [int(x) for x in row]
#    return temp
#    return [int(x) for x in temp]

def sum_of_ones(stuff):
    return [sum(x) for x in zip(*stuff)]

def get_gamma(data):
    pass

def get_eps_fast(gamma):
    return ~gamma

def get_power_rate(gamma, eps):
    return gamma * eps


def main():
    with open("input") as f:
        data = f.read().splitlines()
    # Convert the string of "bits" into actual bits
    #    data = [int(bits,2) for bits in data]
    #print(str(bin(data[0])))
    print(matrixify(data))

if __name__ == "__main__":
    main()
