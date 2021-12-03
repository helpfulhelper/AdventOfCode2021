def counter(data, pred=bool):
    return sum(map(pred, data))




def main():
    with open("input") as f:
        data = [int(i) for i in f.readlines()]
    #print(len(data))
    print( counter(data, ) )
    
if __name__ == "__main__":
    main()

