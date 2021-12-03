def whereami(data):
    pos_x, pos_y = 0,0
    for direction, amount in data:
        match direction:
            case 'forward': pos_x += amount
            case 'down': pos_y += amount
            case 'up': pos_y -= amount
    return pos_x, pos_y
    



def main():
    with open("input") as f:
        data = [line.strip().split() for line in f]
        data = [(x,int(y)) for (x,y) in data]

    x,y = whereami (data)
    howfar = x*y
    print( (x,y) )
    print( howfar )
    #print(data)
    
if __name__ == "__main__":
    main()

