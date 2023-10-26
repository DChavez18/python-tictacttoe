import random

def main():
    introduction = intro()
    game_mode = selectGameMode()
    board = create_grid()
    pretty = printPretty(board)
    symbol_1, symbol_2 = sym()

    if game_mode == "PvC":
        symbol_2 = "CPU"
    
    count = 0
    winner = None
    
    while count < 9 and not winner:
        pretty = printPretty(board)

        if count % 2 == 0:
            player = symbol_1
        else:
            player = symbol_2

        if player == "CPU":
            print("CPU is thinking...")
            row, column = generateCPUMove(board)
        else:
            printPretty(board)
            row, column = getPlayerMove(board, player)

        while (row > 2 or row < 0) or (column > 2 or column < 0):
            outOfBoard(row, column)
            row, column = getPlayerMove(board, player)

        while board[row][column] != " ":
            filled = illegal(board, row, column, symbol_1, symbol_2)
            row, column = getPlayerMove(board, player)

        board[row][column] = player
        count += 1

        winner = isWinner(board, symbol_1, symbol_2)

    pretty = printPretty(board)
    
    if winner == "Tie":
        print("It's a tie!")
    else:
        print(f"Player {winner} wins!")

def selectGameMode():
    while True:
        mode = input("Select the game mode (1 for Player vs. Player, 2 for Player vs. CPU): ")
        if mode == "1":
            return "PvP"
        elif mode == "2":
            return "PvC"
        else:
            print("Invalid choice. Please select '1' for Player vs. Player or '2' for Player vs. CPU.")

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
    while True:
        symbol_1 = input("Player 1, choose your symbol (X or O): ").upper()
        if symbol_1 == "X" or symbol_1 == "O":
            break
        else:
            print("Invalid choice. Please select 'X' or 'O'.")

    symbol_2 = "X" if symbol_1 == "O" else "O"
    print(f"Player 2, your symbol is {symbol_2}.")
    input("Press enter to continue...\n")
    return symbol_1, symbol_2

def getPlayerMove(board, player):
    print(f"Player {player}, it's your turn.")
    row = int(input("Pick a row (0, 1, or 2): "))
    column = int(input("Pick a column (0, 1, or 2): "))
    return row, column        

def generateCPUMove(board):
    while True:
        row = random.randint(0, 2)
        column = random.randint(0, 2)
        if board[row][column] == " ":
            return row, column

def isWinner(board, symbol_1, symbol_2):
    for row in range(3):
        if (board[row][0] == board[row][1] == board[row][2] == symbol_1) or (board[row][0] == board[row][1] == board[row][2] == symbol_2):
            return symbol_1 if symbol_1 == board[row][0] else symbol_2

    for column in range(3):
        if (board[0][column] == board[1][column] == board[2][column] == symbol_1) or (board[0][column] == board[1][column] == board[2][column] == symbol_2):
            return symbol_1 if symbol_1 == board[0][column] else symbol_2

    if (board[0][0] == board[1][1] == board[2][2] == symbol_1) or (board[0][0] == board[1][1] == board[2][2] == symbol_2):
        return symbol_1 if symbol_1 == board[0][0] else symbol_2

    if (board[0][2] == board[1][1] == board[2][0] == symbol_1) or (board[0][2] == board[1][1] == board[2][0] == symbol_2):
        return symbol_1 if symbol_1 == board[0][2] else symbol_2

    if all(" " not in row for row in board):
        return "Tie"
    return None

def illegal(board, row, column, symbol_1, symbol_2):
    print("This spot is already taken.")

def outOfBoard(row, column):
    print("You can't place your symbol outside the board.")

def printPretty(board):
    print("   0   1   2")
    print("0  " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print("  ---|---|---")
    print("1  " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("  ---|---|---")
    print("2  " + board[2][0] + " | " + board[2][1] + " | " + board[2][2])
    return board

main()

    