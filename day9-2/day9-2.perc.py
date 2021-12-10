import numpy as np
from pylab import *
from scipy.ndimage import measurements
from functools import reduce

def main():
    data = np.array([[int(d) for d in str(word)] for word in np.genfromtxt('input', dtype=str)])

    truth_table = np.isin(data, arange(9))
    basins, _ = measurements.label(truth_table)
    basin_areas = measurements.sum(truth_table, basins, index=arange(basins.max() + 1))
    print(int(reduce((lambda a,b: a*b),sort(basin_areas)[-3:])))


if __name__ == "__main__":
    main()
