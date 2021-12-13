import numpy as np

def gobble(filename):
    with open(filename) as f:
        data = [line.strip().split() for line in f]
    return data

def main():
    data = gobble('example')
#    data = np.genfromtxt('example')
    print(data)


if __name__ == "__main__":
    main()
