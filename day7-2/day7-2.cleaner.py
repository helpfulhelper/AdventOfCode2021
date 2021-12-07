import numpy as np

def main():
    data = np.genfromtxt('example',dtype=int,delimiter=',')

    # c is an array containing a list of all possible positions from the input.
    # we do not have to consider positions outside the minimum or maximum starting points
    # as we can assume any solution is between the min and max
    c = np.arange(data.min(), data.max() + 1)
    
    # p1 finds the optimum position (minimum fuel required) assuming a fixed cost of 1 per movement.
    # so for every possible position (c), we generate a sub-array containing the cost for every starting location d
    # the cost is computed as the absolute value between proposed position c and current location d
    # applying a summation to each sub-array gives us the total cost for each possible position

    p1 = [sum([abs(outer-d) for d in data]) for outer in c]

    # p2 is much the same, but has a cost that inflates per movement. 1 mv = 1 fuel, 2 mv = 2 fuel, 3mv = 3fuel etc.
    # This total cost of each movement can be considered as a sum of consecutive numbers
    # The formula for the sum of consecutive N numbers is: (N/2)*(first number+last number)
    # As our distance to move will always be at least 1 (0 distance simplifies to 0)
    # We can rearrange and simplify to:
    #  ((Distance) * (1 + Distance) / 2) 
    # where distance is the absolute value between current and proposed position
    # The rest follows as in P1.

    p2 = [sum([abs(outer-d)*(abs(outer-d)+1)/2 for d in data]) for outer in c]

    print(f'The optimal fixed cost position is {np.argmin(p1)}, with a cost of {min(p1)}')
    print(f'The optimal inflating cost position is {np.argmin(p2)}, with a cost of {min(p2)}')

if __name__ == "__main__":
    main()
