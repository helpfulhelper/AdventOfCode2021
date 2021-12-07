import numpy as np

def main():
#    data = gobble('example')
    data = np.genfromtxt('example',dtype=int,delimiter=',')
    c = np.arange(data.min(), data.max() + 1)
    
    p1 = [sum([abs(outer-d) for d in data]) for outer in c]
    p2 = [sum([abs(outer-d)*(abs(outer-d)+1)/2 for d in data]) for outer in c]

    print(min(p1), min(p2))

if __name__ == "__main__":
    main()
