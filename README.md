# Connect Four

Playing as either the red user or the yellow user, players compete to create a row of their colours going up, down, left or right that is equivalent of the chosen winning number of rows.

Language: Python
## Step-by-Step run through of the script
The functions used include: start(), grid(), game() and checkWinner()

### Start Function
1. Creates the gridSize variable and asks the user for how large they want the grid to be.
2. This value is then validated ensuring it sits between 0 and 8, limiting the size of the grid. If the value does not meet this criteria the user is then asked again for an input value until the criteria is met.
3. Grid Size is then printed.
4. User asked for the winning number of rows they want, and is again validated in a similar way in which it has to be bigger than 0 and less than the grid size otherwise the user will be asked for the input again.
5. An array is created for the grid size and filled with 0s to represent empty slots.

### Grid Function
1. Prints the current grid.

### Game Function
1. Sets the max number of moves equal to number of spaces on the grid and sets the current move number to 0 so that while the game is running if the current number of moves exceeds that the game stops.
2. If the current move number is even then it is the red players turn, if odd then it is the yellow players turn.
3. Adjustment is made so that the users row number and array row number are aligned.
4. User is asked which column they want to drop their token down.
5.
6. A check is done to see if the bottom item of that column is 0, if it is then the red token will replace that, otherwise it will check the one above the bottom and so on until an empty slot is found.
7. The grid is reprinted to display the current game situation.
8. Current move count is increased by one
9. checkWinner() is called after each turn to determine whether a winner has been produced or not.

### Check Winner Function
1. Sets counts for redCount and yellowCount, counts which will determine whether there is a winner or not, to one
2. A try catch is used to catch IndexErrors which will occur when a array value that does not exist is checked for "R" or "Y"
3. For each colour a while loop is created that is maintained until the count for that colour is bigger than the winning number of rows.
4. Within each while loop is a check for each direction away from the current token. i.e The token to the left will be checked to see if it's value is "R", if it is it will continue to loop that way, increasing the redCount. Once it has exceeded the winning number of rows the game will end and a winner is declared. The exact same process occurs for the remaining directions (Above, to the right and below) and this also occurs exactly the same but for the yellow player.
```
while yellowCount<winningNoRows:
            #Checks the value below
            if array[row+1][col]=="Y":
                for i in range(1,winningNoRows):
                    if array[row+i][col]=="Y":
                        yellowCount=yellowCount+1
                    else:
                        break
```

### Additional Improvements
As time was limited, many improvements could be made to this program.
1. Logging: A log file could have been created and log each action and variable change made to make it easier in the future to discover where problems occur.
2. More sophisticated validation checks. The validation on the user input was basic, insuring the values lied between certain values. This could be improved by ensuring the user only gave numerical values.
3. Increased range of winner check. Currently you could only win if the direction of the winning row was N,E,S,W. This could be improved by allowing each player to win diagonally (NE,SE, SW, NW).
4. Using a framework or GUI to display the game would improve appearances.
