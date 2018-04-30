# My_Mario_Version_2.py
#
# Marina Martin
# 
#
# CMPT 120
#
# April 2016



import pdb
import random
import sys



#GLOBAL VARIABLES

#Set the variables for the maze size


## Read the file:
try:

    mazeFile = open('InputData_3.txt')

    mazeWidth = int(mazeFile.readline())
    print(mazeWidth)

    mazeHeight = int(mazeFile.readline())
    print(mazeHeight)

    aNumOfRewardingObstacles = int(mazeFile.readline())
    print(aNumOfRewardingObstacles)

    aNumOfExplodingObstacles = int(mazeFile.readline())
    print(aNumOfExplodingObstacles)

    EmptySymbol = mazeFile.readline().strip('\n')
    print("(" + EmptySymbol +")")

    RewardSymbol = mazeFile.readline().strip('\n')
    print(RewardSymbol)

    ExplodingSymbol = mazeFile.readline().strip('\n')
    print(ExplodingSymbol)

    MapRewardSymbol = "RRR"
    MapExplodingSymbol = "EEE"

    MarioSymbol = mazeFile.readline().strip('\n')
    print(MarioSymbol)

    ExitSymbol = mazeFile.readline().strip('\n')
    print(ExitSymbol)

    DashSymbol = mazeFile.readline().strip('\n')
    print(DashSymbol)
    
    leftRightBorder = mazeFile.readline().strip('\n')
    print(leftRightBorder)

# Create the board and the top/bottom frame rows

    GameBoard = [[EmptySymbol for x in range(mazeWidth)] for y in range(mazeHeight)]
    TopBorder = [DashSymbol for x in range(mazeWidth)]
    BottomBorder = [DashSymbol for x in range(mazeWidth)]
 
    marioLocationString = mazeFile.readline()
    marioLocationList = marioLocationString.split()
    marioRow = int(marioLocationList[0])
    marioColumn = int(marioLocationList[1])
    print("mario", marioRow, marioColumn)
    GameBoard[marioRow][marioColumn] = MarioSymbol
    
    for i in range(0, aNumOfRewardingObstacles):
        rewardObstacleLocationString = mazeFile.readline()
        rewardObstacleLocationList = rewardObstacleLocationString.split()
        rewardObstacleRow = int(rewardObstacleLocationList[0])
        rewardObstacleColumn = int(rewardObstacleLocationList[1])
        print("reward", i, rewardObstacleRow, rewardObstacleColumn)
        GameBoard[rewardObstacleRow][rewardObstacleColumn] = MapRewardSymbol

    for i in range(0, aNumOfExplodingObstacles):
        explodingObstacleLocationString = mazeFile.readline()
        explodingObstacleLocationList = explodingObstacleLocationString.split()
        explodingObstacleRow = int(explodingObstacleLocationList[0])
        explodingObstacleColumn = int(explodingObstacleLocationList[1])

        print("exploding", i, explodingObstacleRow, explodingObstacleColumn)
        GameBoard[explodingObstacleRow][explodingObstacleColumn] = MapExplodingSymbol


    x = marioColumn
    y = marioRow

    
    if x < (mazeWidth / 2) and y < (mazeHeight / 2):
                     # Mario is in top left
                     BottomBorder[mazeWidth - 1] = ExitSymbol

    elif x >= (mazeWidth / 2) and y < (mazeHeight / 2):
                     # Mario is top right
                     BottomBorder[0] = ExitSymbol

    elif x < (mazeWidth / 2) and y >= (mazeHeight / 2):
                     # Mario is in bottom left
                     TopBorder[mazeWidth - 1] = ExitSymbol

    elif x >= (mazeWidth / 2) and y >= (mazeHeight / 2):
                    # Mario is bottom right
                     TopBorder[0] = ExitSymbol

    marioScore = aNumOfExplodingObstacles/3

                     
    mazeFile.close()
    

except ValueError:
   print("you screwed up making the game file")




#FUNCTIONS

def init():
   
    print("Welcome to the Mario Maze! \n\n\n")
    return()


def header():

    numHeader = ("      ") #initialize number header (6 spaces)

    for i in range(mazeWidth):
        if i <= 8:
            numHeader = numHeader + str(i+1) + ("  ")#white space is equivilant to 2 spaces
        else:
            numHeader = numHeader + str(i+1) + (" ")#white space is equivilant to 1 spaces
        
    print(numHeader)
    return()


def printBoardAndFrame():

    print("Your score is: ", marioScore)
    topFrame = "     "#5 whitespaces

    for n in range(mazeWidth):
        topFrame += TopBorder[n]

    print(topFrame)

    for y in range(mazeHeight):
        line = ""            
        for x in range(mazeWidth):
            if MapRewardSymbol == GameBoard[y][x]:
                line += RewardSymbol
            elif MapExplodingSymbol == GameBoard[y][x]:
                line += ExplodingSymbol


            else:
                line += GameBoard[y][x]
        if y <= 8:
            print(str(y + 1) + "  | " + line + " | ")       
        else:
            print(str(y + 1) + " | " + line + " | ")

    bottomFrame = "     "#5 whitespaces

    for n in range(mazeWidth):
        bottomFrame += BottomBorder[n]

    print(bottomFrame)
    return()



def printBoard():
    init()
    header()
    printBoardAndFrame()
    return()

             

### MAIN


marioHasNotWonYet = True
timeToExit = False
while((timeToExit == False) and (marioScore > 0) and (marioHasNotWonYet)): 
    printBoard()
    userTypedValidStuff = False
    while (not userTypedValidStuff):
        whatTheyTyped = input("Please enter either the letter 'R' for right, the letter 'L' for left, the letter 'U' for up, the letter 'D' for down and the letter 'X' to exit the game:   ")
        print("(" + whatTheyTyped +")")

        if whatTheyTyped == "X":
            userTypedValidStuff = True
            timeToExit = True

        else:
            targetX = marioColumn
            targetY = marioRow
            print("mario: ", marioRow, marioColumn)
            print("target: ", targetY, targetX)
            if whatTheyTyped == "R":
                print("move right")
                targetX = marioColumn + 1
                userTypedValidStuff = True

            elif whatTheyTyped == "L":
                print("move left")
                targetX = marioColumn - 1
                userTypedValidStuff = True

            elif whatTheyTyped == "U":
                print("move up")
                targetY = marioRow - 1
                userTypedValidStuff = True
                if ((targetY == -1) and (ExitSymbol == TopBorder[marioColumn])):
                    marioHasNotWonYet = False

            elif whatTheyTyped == "D":
                print("move down")
                targetY = marioRow +1 
                userTypedValidStuff = True
                if ((targetY == mazeHeight) and (ExitSymbol == BottomBorder[marioColumn])):
                    marioHasNotWonYet = False

            print("target: ", targetY, targetX)

            # If the target location is on the map...
            if (targetX >= 0 and targetX <= mazeWidth - 1 and targetY >= 0 and targetY <= mazeHeight - 1):

              # Remove Mario from his old location in the map
              GameBoard[marioRow][marioColumn] = EmptySymbol
              whatIsAtTarget = GameBoard[targetY][targetX]
              print("what: ", whatIsAtTarget)
            
              if whatIsAtTarget == EmptySymbol:
                     GameBoard[targetY][targetX] = MarioSymbol
                     marioColumn = targetX
                     marioRow = targetY


              elif whatIsAtTarget == MapRewardSymbol:
                     marioScore = marioScore + 1
                     GameBoard[targetY][targetX] = MarioSymbol
                     marioColumn = targetX
                     marioRow = targetY

              elif whatIsAtTarget == MapExplodingSymbol:
                     marioScore = marioScore - 1
                     GameBoard[targetY][targetX] = MarioSymbol
                     marioColumn = targetX
                     marioRow = targetY

         

      

print("Thank you for playing Mario!")

if not marioHasNotWonYet:
    print("You Win!  Your score is: ", marioScore)
    
elif timeToExit:
    print("Bye!  Peace out.")

else:
    print("Sorry, but you lost.  Please try again soon.")   




