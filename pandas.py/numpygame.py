import numpy as np

def initialize_board():
    return np.full((3, 3), ' ')

def display_board(board):
    print("   0   1   2")
    for i in range(3):
        print(f"{i}  " + " | ".join(board[i]))
        if i < 2:
            print("  ---+---+---")

def check_winner(board, player):
    # Check rows, columns and diagonals
    for i in range(3):
        if np.all(board[i, :] == player) or np.all(board[:, i] == player):
            return True
    if np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player):
        return True
    return False

def check_draw(board):
    return not np.any(board == ' ')

def make_move(board, row, col, player):
    if board[row, col] == ' ':
        board[row, col] = player
        return True
    else:
        return False

def tic_tac_toe():
    board = initialize_board()
    current_player = 'X'
    while True:
        display_board(board)
        print(f"Player {current_player}'s turn")
        row = int(input("Enter the row (0, 1, or 2): "))
        col = int(input("Enter the column (0, 1, or 2): "))
        if make_move(board, row, col, current_player):
            if check_winner(board, current_player):
                display_board(board)
                print(f"Player {current_player} wins!")
                break
            elif check_draw(board):
                display_board(board)
                print("The game is a draw!")
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move, try again.")

tic_tac_toe()
