def main():
  introduction = intro()
  board = create_grid()
  pretty = printPretty(board)
  symbol_1, symbol_2 = sym()
  full = isFull(board, symbol_1, symbol_2)

def intro():
  print("Welcome to Tic Tac Toe!")
  print("\n")
  print("The game is played on a grid that's 3 squares by 3 squares.")
  print("Rules: Player 1 and player 2, represented by X and O, take turns "
          "marking the spaces in a 3*3 grid. The player who succeeds in placing "
          "three of their marks in a horizontal, vertical, or diagonal row wins.")
  print("\n")
  input("Press enter to continue...")
  print("\n")

def create_grid():
  print("This is the classic grid:")
  board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
  return board

def sym():
  symbol_1 = input("Player 1, choose your symbol (X or O): ")
  if symbol_1 == "X":
    symbol_2 = "O"
    print("Player 2, your symbol is O.")
  else:
    symbol_2 = "X"
    print("Player 2, your symbol is X.")
  input("Press enter to continue...")
  print("\n")
  return symbol_1, symbol_2

def startGame(board, symbol_1, symbol_2, count):
  if count % 2 == 0:
    player = symbol_1
  elif count % 2 == 1:
    player = symbol_2
  print("Player " + player + ", it's your turn.")
  row = int(input("Pick a row:"
                  "[upper row = 0, middle row = 1, lower row = 2]:"))
  column = int(input("Pick a column:"
                      "[left column = 0, middle column = 1, right column = 2]:"))

  while (row > 2 or row < 0) or (column > 2 or column < 0):
    outOfBoard(row, column)
    row = int(input("Pick a row:"
                    "[upper row = 0, middle row = 1, lower row = 2]:"))
    column = int(input("Pick a column:"
                        "[left column = 0, middle column = 1, right column = 2]:"))

  while (board[row][column] == symbol_1)or (board[row][column] == symbol_2):
    filled = illegal(board, row, column, symbol_1, symbol_2)
    row = int(input("Pick a row:"
                    "[upper row = 0, middle row = 1, lower row = 2]:"))
    column = int(input("Pick a column:"
                        "[left column = 0, middle column = 1, right column = 2]:"))
  if player == symbol_1:
    board[row][column] = symbol_1

  else:
    board[row][column] = symbol_2

  return board

def isFull(board, symbol_1, symbol_2):
  count = 1
  winner = True

  while count < 10 and winner == True:
    gaming = startGame(board, symbol_1, symbol_2, count)
    pretty = printPretty(board)

    if count == 9:
      print("Full board. Game over.")
      if winner == True:
        print("It's a tie!")
  
    winner = isWinner(board, symbol_1, symbol_2, count)
    count += 1
  if winner == False:
    print("Game over.")

  report(count, winner, symbol_1, symbol_2)

def outOfBoard(row, column):
  print("You can't place your symbol outside the board.")

def printPretty(board):
  print(board[0][0] + "|" + board[0][1] + "|" + board[0][2])
  print("-+-+-")
  print(board[1][0] + "|" + board[1][1] + "|" + board[1][2])
  print("-+-+-")
  print(board[2][0] + "|" + board[2][1] + "|" + board[2][2])
  return board

def isWinner(board, symbol_1, symbol_2, count):
  winner = True
  for row in range (0, 3):
    if (board[row][0] == board[row][1] == board[row][2] == symbol_1):
      winner = False
      print("Player" + symbol_1 + "wins!")
    elif (board[row][0] == board[row][1] == board[row][2] == symbol_2):
      winner = False
      print("Player" + symbol_2 + "wins!")
  for column in range (0, 3):
    if (board[0][column] == board[1][column] == board[2][column] == symbol_1):
      winner = False
      print("Player" + symbol_1 + "wins!")
    elif (board[0][column] == board[1][column] == board[2][column] == symbol_2):
      winner = False
      print("Player" + symbol_2 + "wins!")

  if (board[0][0] == board[1][1] == board[2][2] == symbol_1):
    winner = False
    print("Player" + symbol_1 + "wins!")
  elif (board[0][0] == board[1][1] == board[2][2] == symbol_2):
    winner = False
    print("Player" + symbol_2 + "wins!")
  elif (board[0][2] == board[1][1] == board[2][0] == symbol_1):
    winner = False
    print("Player" + symbol_1 + "wins!")
  elif (board[0][2] == board[1][1] == board[2][0] == symbol_2):
    winner = False
    print("Player" + symbol_2 + "wins!")
  return winner

def illegal(board, row, column, symbol_1, symbol_2):
  print("This spot is already taken.")

def report(count, winner, symbol_1, symbol_2):
  if winner == True:
    print("It's a tie!")
  elif count % 2 == 0:
    print("Player" + symbol_1 + "wins!")
  elif count % 2 == 1:
    print("Player" + symbol_2 + "wins!")

main()

    