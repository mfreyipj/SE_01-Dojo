grid = [[15, 2, 1, 12],
        [8, 5, 6, 11],
        [4, 9, 10, 7],
        [3, 14, 13, 0]]

''' # Control grid -> to test the evaluate function
grid = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 0]]
'''
max_number = len(grid)**2 - 1


def printGrid():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end=" ")
        print()


# Get index tuple of a number in the grid
def find(l, elem):
    for row, i in enumerate(l):
        try:
            column = i.index(elem)
        except ValueError:
            continue
        return row, column
    return -1


# Request a number input from the user and evaluate it as a number
def getNumberInput():
    while True:
        try:
            userInput = int(input("Which number would you like to move to the empty field?\n"))
        except:
            print("That's not a real number, try again!\n")
        else:
            if (userInput > 0 and userInput < max_number):
                return userInput
            else:
                print("This number is not part of the grid, try again! \n")



# Evaluate the adjacency of the given number to the empty field by comparing their indexes (0/0 and 0/1 e.g.) and their rows
def evaluateAdjacencyToZero(number):

    # Get the indexes of the number and zero
    i_number = find(grid, number)
    i_zero = find(grid, 0)

    # Check whether the number is in the same row or same column
    sameRow = i_zero[0] == i_number[0]
    sameColumn = i_zero[1] == i_number[1] 


    # Get the sum of the index of both numbers
    # Examples : 0/0 -> 0, 1/1 -> 2
    indexSumZero = i_zero[0] + i_zero[1]
    indexSumNumber = i_number[0] + i_number[1]

    if((indexSumZero - indexSumNumber == 1 or indexSumZero - indexSumNumber == -1) and (sameRow or sameColumn)):
        return True
    else:
        print("The entered number is not adjacent to the empty field!\n")
        return False



# Exchange a given number with the zero in the grid
def exchange_with_zero(number):

    # Get the new indexes of the number and zero
    new_i_zero = find(grid, number)
    new_i_number = find(grid, 0)

    # Exchange the two numbers
    grid[new_i_zero[0]][new_i_zero[1]] = 0
    grid[new_i_number[0]][new_i_number[1]] = number
    
    print("You have successfully moved " + str(number) + " to the empty field!\n")


# Evaluate whether the grid was successfully rearranged
def evaluateGrid(g):
   expected_number = 1   
   for i in range(len(g)):
        for j in range(len(g[i])):
            if int(g[i][j]) == expected_number or expected_number == max_number+1:
                expected_number += 1
            else:
                return False    
   return True


def main():

    # Welcome user
    print("Welcome to the game! \n")
    
    while(evaluateGrid(grid) != True):
        printGrid()
        # request a number to be moved
        number_to_exchange = getNumberInput()
        # if the number is adjacent to the empty field, exchange them
        if evaluateAdjacencyToZero(number_to_exchange):
            exchange_with_zero(number_to_exchange)

    print("You completed the game!")
    quit()    

main()