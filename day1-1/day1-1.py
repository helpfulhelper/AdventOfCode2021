
def counter( data ):
    total = 0
    for c, n in zip(data, data[1:]):
        total += c < n
    return total

def main():
    with open("input") as f:
        data = [int(i) for i in f.readlines()]
    #print(len(data))
    print( counter(data) )
    
if __name__ == "__main__":
    main()

