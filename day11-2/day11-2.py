import numpy as np
from scipy.signal import convolve

footprint = [[1,1,1], [1,0,1], [1,1,1]]

def step(arr):
    #curr will equal step 1 of the process - adding 1 to all values in the provided array
    curr = arr+1
    #temp 
    init = curr
    while True:
        #Create a truth table of all values > 9
        will_flash = curr > 9

        #signal.convolve is what i wanted, not ndimage. boo. 
        #signal.convolve will... convolve in this manner:
        # 'same' indicates it should return an array of the same size as will_flash
        # wherever will_flash is True, will apply footprint at that location
        # this will add 1 to all 8 neighbors.
        # curr becomes our current propogation state - 
        # i.e. our initial step of energy + propogated energy
        # TLDR: instead of searching for neighbors when it flashes, each element asks which of my neighbors are flashing?
        curr = init + convolve(will_flash, footprint, 'same')

        #Test if no change between propagation truth table before and after convolution
        #i.e. we've exhausted the propogation of flashes in the current step
        if (will_flash == (curr > 9)).all():
            #Reusing our truth table of what has flashed, set that points energy to 0.
            curr[will_flash] = 0
            return curr, will_flash.sum()


def main():
    total = 0
    data = np.genfromtxt('input', dtype=int, delimiter=1)
    d = data
    i = 0
    while True:
        d, _ = step(d)
        if (d == (np.zeros(d.shape))).all():
            print(i + 1)
            break
        i += 1
        




if __name__ == "__main__":
    main()
