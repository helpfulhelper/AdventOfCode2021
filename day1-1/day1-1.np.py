import numpy as np

def main():
    data = np.genfromtxt('input')
    tot = sum([data[i] > data[i-1] for i,d in enumerate(data)])
    print(tot)
    
if __name__ == "__main__":
    main()

