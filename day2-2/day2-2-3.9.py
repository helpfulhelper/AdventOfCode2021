def whereami(data):
    pos_x, pos_y, aim = 0, 0, 0
    for direction, amount in data:
        if direction == 'forward': 
            pos_x += amount
            pos_y += amount*aim
        if direction == 'down': aim += amount
        if direction == 'up': aim -= amount
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

