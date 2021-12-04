import numpy as np

class Board:
    def __init__(self, boardState):
        self.BN = boardState
        self.MS = np.zeros((5,5), dtype=int)

    def __repr__(self):
        temp = np.array2string(self.BN, prefix='\n') + '\n' + np.array2string(self.MS, suffix='\n') + '\n'
        return temp
    
    def checkWin(self):
        if (5 in np.sum(self.MS, axis=0)):
            return True
        elif (5 in np.sum(self.MS, axis=1)):
            return True
        else: 
            return False

    def markBoard(self, foo):
        if foo in self.BN:
            x,y = np.where(self.BN == foo)
            self.MS[x,y] = 1

    def roundsToWin(self, nums_list):
        #yes, i realize i could import and use count here, but i'm already using numpy and that's cheating enough.
        count = 0
        for x in nums_list:
            self.markBoard(x)
            count += 1
            if self.checkWin():
                return count
    
    def unmarkedSum(self):
        unmarked = np.where(self.MS == 0)
        return sum(self.BN[unmarked])





def main():
    with open("input") as f:
        data = f.read().splitlines()
    #Pop off the list of random numbers
    num_list = [int(i) for i in data.pop(0).split(',')]
    
    #Yes, i'm reading input file twice cause i can't be arsed to do it properly.
    #Split boardlist into 5x5 np arrays
    boardList = np.genfromtxt("input", dtype=int, skip_header = 2)
    boardList = np.array_split(boardList,len(boardList)/5)
    
    #populate classes, i know there are cleaner ways.
    bL = []
    for B in boardList:
        bL.append(Board(B))
    
    #how many rounds needed for every board to win
    roundsNeeded = []
    for B in bL:
        roundsNeeded.append(B.roundsToWin(num_list))

    #Winning Round Number
    wr = min(roundsNeeded)

    #Winning Board Index
    wi = roundsNeeded.index(wr)

    #Winning Board
    winner = bL[wi]

    print(wr)
    print(winner)
    print(winner.unmarkedSum())
    print(winner.unmarkedSum() * num_list[wr-1])



#    print(bL)
#    print(num_list)
#    print(boardList)


if __name__ == "__main__":
    main()
