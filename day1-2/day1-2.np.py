import numpy as np
from scipy.signal import convolve


def main():
    data = np.genfromtxt('input')
    footprint = [1,1,1]
    windowed = convolve(data,footprint,'valid')
    tot = sum([windowed[i] > windowed[i-1] for i,d in enumerate(windowed)])
    print(tot)
    
if __name__ == "__main__":
    main()

