import numpy as np
import numpy.ma as ma
import scipy.ndimage as ndimage

#class Octo:
#    def __init__(self, energy):
#        print(energy)
#        self.energy = int(energy)
#        self.flash = False
#
#    def flash(self):
#        if self.flash == False:
#            self.flash = True
#
#    def step(self):
#        self.energy += 1
#        if self.energy >= 9:
#            self.flash()
#    
#    def __repr__(self):
#        return f'{self.energy} {self.flash}'
#    def __str__(self):
#        return f'{self.energy} {self.flash}'
        
#class Grid:
#    def __init__(self, arr):
#        self.data = arr
#        self.flash_map = np.zeros(arr.shape, dtype=bool)
#
#    def get_neighbors(self, x, y):
#        pass
#    
#    def flash(self):
#        self.flash_map = True if self.data >= 9 else False
#
#    def step(self):
#        pass
#
#    def __repr__(self):
#        return f'{self.data} {chr(10)} {self.flash_map}'
#    def __str__(self):
#        return f'{self.data} {chr(10)} {self.flash_map}'
def flash(arr, can_flash=None):
    if can_flash == None:
        can_flash = np.ones(arr.shape, dtype=bool)
    print(arr, "\n", can_flash)
    for y in arr:
        for x in y:
            print(x, y)
    return ma.masked_greater_equal(arr, 9)

def test(values):
    print(values, type(values))
    return 1


def main():
    data = ma.array([[int(y) for y in x] for x in np.genfromtxt('example',dtype=str, unpack=True)])
    footprint = np.array([[1,1,1], [1,0,1], [1,1,1]])
    flash(data+1)
    #print(list(np.ndenumerate(data)))
    #print(flash(data+1))
    #s = lambda x:x+1
    #print(ndimage.generic_filter(data, s, footprint=footprint, mode='constant', cval=0))

    #results = ndimage.generic_filter(data, test, footprint=footprint, mode='constant', cval=0)
    #print(results)
    #print(data,mask)




if __name__ == "__main__":
    main()
