import numpy as np
from scipy.signal import convolve
from scipy.ndimage import generic_filter

footprint = [[1,1,1], [1,0,1], [1,1,1]]

def step(arr):
    #curr will equal step 1 of the process - adding 1 to all values in the provided array
    curr = arr+1
    #initial state of energy prior to propogation 
    init = curr
    #propogate energy + flashes
    while True:
        #Create a truth of whether a given element will flash (energy > 9)
        will_flash = curr > 9

        #signal.convolve is what i wanted, not ndimage. boo.
        #signal.convolve will... convolve in this manner:
        # 'same' indicates it should return an array of the same size as will_flash
        # the footprint moves over each element, multiplying each cell under the footprint by 1, summing the results of the mult
        # this effectively adds 1 to the current element for every neighbor who will flash
        # curr becomes our current propogation state 
        # i.e. our initial step of energy + propogated energy
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
    #d, b = step(data)
    #step(d)
    for i in range(100):
        d, temp = step(d)
        total += temp
    print(total)



if __name__ == "__main__":
    main()

