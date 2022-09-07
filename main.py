import random

print("Tic Tac Toe")
print("============")
print("")

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
gameboard = [[1,2,3], [4, 5, 6], [7, 8, 9]]
rows = 3
cols = 3

def printGameBoard():
  for x in range(rows):
    print("\n+---+---+---")
    print("|", end="")
    for y in range(cols):
      print("", gameboard[x][y], end=" |")
  print("\n+---+---+---")


def modifyArray(num, turn):
  num -= 1
  if (num ==0):
    gameboard[0][0] = turn
  elif (num == 1):
    gameboard[0][1] = turn
  elif (num == 2):
    gameboard[0][2] = turn
  elif (num == 3):
    gameboard[1][0] = turn
  elif (num == 4):
    gameboard[1][1] = turn
  elif (num == 5):
    gameboard[1][2] = turn
  elif (num == 6):
    gameboard[2][0] = turn
  elif (num == 7):
    gameboard[2][1] = turn
  elif (num == 8):
    gameboard[2][2] = turn



def checkForWinner(gameBoard):
  if (gameboard[0][0] == "X" and gameboard[0][1] == "X" and gameboard[0][2] == "X"):
    print("Player X wins!!!")
  elif (gameboard[1][0] == "X" and gameboard[1][1] == "X" and gameboard[1][2] == "X"):
    print("Player X wins!!!")
  elif (gameboard[2][0] == "X" and gameboard[2][1] == "X" and gameboard[2][2] == "X"):
    print("Player X wins!!!")
  elif (gameboard[0][0] == "X" and gameboard[1][0] == "X" and gameboard[2][0] == "X"):
    print("Player X wins!!!")
  elif (gameboard[0][1] == "X" and gameboard[1][1] == "X" and gameboard[2][1] == "X"):
    print("Player X wins!!!")
  elif (gameboard[0][2] == "X" and gameboard[1][2] == "X" and gameboard[2][2] == "X"):
    print("Player X wins!!!")
  elif (gameboard[0][0] == "X" and gameboard[1][1] == "X" and gameboard[2][2] == "X"):
    print("Player X wins!!!")
  elif (gameboard[0][2] == "X" and gameboard[1][1] == "X" and gameboard[2][2] == "X"):
    print("Player X wins!!!")

  elif (gameboard[0][0] == "O" and gameboard[0][1] == "O" and gameboard[0][2] == "O"):
    print("Player 0 wins!!!")
  elif (gameboard[1][0] == "O" and gameboard[1][1] == "O" and gameboard[1][2] == "O"):
    print("Player O wins!!!")
  elif (gameboard[2][0] == "O" and gameboard[2][1] == "O" and gameboard[2][2] == "O"):
    print("Player O wins!!!")
  elif (gameboard[0][0] == "O" and gameboard[1][0] == "O" and gameboard[2][0] == "O"):
    print("Player O wins!!!")
  elif (gameboard[0][1] == "O" and gameboard[1][1] == "O" and gameboard[2][1] == "O"):
    print("Player O wins!!!")
  elif (gameboard[0][2] == "O" and gameboard[1][2] == "O" and gameboard[2][2] == "O"):
    print("Player O wins!!!")
  elif (gameboard[0][0] == "O" and gameboard[1][1] == "O" and gameboard[2][2] == "O"):
    print("Player O wins!!!")
  elif (gameboard[0][2] == "O" and gameboard[1][1] == "O" and gameboard[2][2] == "O"):
    print("Player O wins!!!")
  else:
    return "N"


leaveLoop = False
turnCounter = 0

while (leaveLoop == False):
  if (turnCounter % 2 == 0):
    printGameBoard()
    numberPicked = int(input("\nChose a number between 1 and 9: "))
    if (numberPicked > 0 and numberPicked < 10):
      modifyArray(numberPicked, "X")
      board.remove(numberPicked)
      
    else:
     print("Invalid entry please try again.") 
    turnCounter += 1
  
  else:
    while(True):
      cpuChoice = random.choice(board)
      print("\nCpu choice: ", cpuChoice)
      if (cpuChoice in board):
        modifyArray(cpuChoice, "O")
        board.remove(cpuChoice)
        turnCounter += 1
        break

  winner = checkForWinner(gameboard)
  if (winner != "N"):
    print("\nGame Over! Thanks for playing!")



