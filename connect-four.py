def start():
    #Asks user for how large they want the playing grid to be
    global gridSize
    gridSize = int(input("The grid will be a square, how many rows/columns do you want? (Between 0 and 8)"))

    #Validation: Max grid size of 8x8
    while gridSize < 0 or gridSize > 8:
        gridSize = int(input("Invalid value, how many rows/columns do you want?"))
    
    else:
        #Log gridSize
        print("Grid Size: ",gridSize)

    #Asks user how many tokens needed to win
    global winningNoRows
    winningNoRows = int(input("How many rows do you want to get in order to win?"))

    #Input validation
    while winningNoRows < 0 or winningNoRows > gridSize:
        winningNoRows = int(input("Invalid Input: How many rows do you want to get in order to win?"))

    else:
        print("Winning number of rows: ",winningNoRows)
    
    #Creates array by adding 0 to each row and then adding each row to the array
    global array
    array=[]
    
    for i in range(gridSize):
        row = []

        for i in range(gridSize):
            row.append(0)
        array.append(row)

def grid():
    #Print grid
    for row in array:
        print(row)


def game():
    #Sets limit on maximum number of moves: being max number of spaces on the grid
    maxNoMoves = gridSize * gridSize
    currentMoveNo = 0

    #Dictates which players move it is if the turn is even it is player red's move, if odd then player yellow.
    while currentMoveNo < maxNoMoves:

        if currentMoveNo % 2 ==0:
            currentToken="R"
            print("Current Player Turn: Red")
        
        else:
            currentToken = "Y"
            print("Current Player Turn: Yellow")

        #Adjusted to compliment arrays starting at 0
        currentRow = gridSize -1

        columnChoice = int(input("Which column would you like to put your counter down?"))

        #Validate column choice

        while -1<columnChoice<gridSize:
            columnChoice = int(input("Which column would you like to put your counter down?"))

        #Checks to see if the space is free(dictated by a 0), if not it moves up a row, starting from the bottom row.
        while currentRow>=0:
            if  array[currentRow][columnChoice] ==0:
                array[currentRow][columnChoice] =currentToken
                break

            else:
                currentRow= currentRow-1

        # Reprints grid to show what current game play looks like.
        for row in array:
            print(row)
        currentMoveNo = currentMoveNo+1
        #Checks to see if there is a winner after each turn
        checkWinner(currentRow, columnChoice)

def checkWinner(row, col):
    redCount=1
    yellowCount = 1

    #Check for Red winner
    try:

        while redCount<winningNoRows:
            #Checks the value below
            if array[row+1][col]=="R":
                for i in range(1,winningNoRows):
                    if array[row+i][col]=="R":
                        redCount=redCount+1
        
                    else:
                        break
            
            #Checks thevalue to the left
            if array[row][col-1]=="R":
                for i in range(1,winningNoRows):
                    if array[row][col-i]=="R":
                        redCount=redCount+1
                        
                    else:
                        break
            
            #Checks the value above
            if array[row-1][col]=="R":
                for i in range(1,winningNoRows):
                    if array[row-i][col]=="R":
                        redCount=redCount+1
                        
                    else:
                        break
            
            #Checks the value to right
            if array[row][col+1]=="R":
                for i in range(1,winningNoRows):
                    if array[row][col+i]=="R":
                        redCount=redCount+1
                        
                    else:
                        break


        if redCount>=winningNoRows:
            print("Red wins!")
            quit
            
    except IndexError:
        pass
     
    #Check for Yellow winner

    try:
        while yellowCount<winningNoRows:
            #Checks the value below
            if array[row+1][col]=="Y":
                for i in range(1,winningNoRows):
                    if array[row+i][col]=="Y":
                        yellowCount=yellowCount+1
                    else:
                        break
            
            #Checks the value to the left
            if array[row][col-1]=="Y":
                for i in range(1,winningNoRows):
                    if array[row][col-i]=="Y":
                        yellowCount=yellowCount+1
                        
                    else:
                        break
            
            #Checks the value above
            if array[row-1][col]=="Y":
                for i in range(1,winningNoRows):
                    if array[row-i][col]=="Y":
                        yellowCount=yellowCount+1
                        
                    else:
                        break
            
            #Checks the value to right
            if array[row][col+1]=="Y":
                for i in range(1,winningNoRows):
                    if array[row][col+i]=="Y":
                        yellowCount=yellowCount+1

                    else:
                        break
        
        if yellowCount>=winningNoRows:
            print("Yellow wins!")
            quit

    except IndexError:
        pass


start()
grid()
game()
