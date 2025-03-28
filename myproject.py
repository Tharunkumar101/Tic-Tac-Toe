def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
def winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
   
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
def is_full(board):
    return all(cell != " " for row in board for cell in row)
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        print_board(board)
        player = players[turn % 2]
        print(f"{player}'s turn. Enter row and column (0-2): ")    
        try:
            row, col = map(int, input().split())
            if board[row][col] == " ":
                board[row][col] = player
                if winner(board, player):
                    print_board(board)
                    print(f"{player} wins!")
                    break
                if is_full(board):
                    print_board(board)
                    print("It's a draw!")
                    break
                turn += 1
            else:
                print("Cell is already occupied. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Enter numbers between 0 and 2.")

if __name__ == "__main__":
    tic_tac_toe()
