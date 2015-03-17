# define functions

def GetGridRow(aRowLength):
    # draws a single row using |_ for each square
    thisRow = '|_' * (aRowLength)
    # add closing | to row
    thisRow = thisRow + '|'
    return thisRow

def DisplayGrid(aGridSize, aRow):
    # display top of grid using _ as top of each square
    print(' _' * aGridSize)
    # display rows of |_| for each row
    for rowCount in range(aGridSize):
        print(aRow)

def GetGridSize():
    validGrid = False
    while validGrid == False:
        thisGridSize = int(input("Please enter the size of the grid(max 20): "))
        if thisGridSize <= 20:
            validGrid = True
    return thisGridSize

# main program

sizeOfGrid = GetGridSize()
sizeToDraw = GetGridRow(aRow)
DisplayGrid(aGridSize, aRow)
