def print_board(board):
    print("\n".join(map(str, board)))

def check_winner(board):
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2] and board[i][0]!=' ': 
            return True
        if board[0][i]==board[1][i]==board[2][i] and board[0][i]!=' ': 
            return True
    if board[0][0]==board[1][1]==board[2][2] and board[0][0]!=' ': 
        return True
    if board[0][2]==board[1][1]==board[2][0] and board[0][2]!=' ': 
        return True
    return False

def make_move(board, row, col, player):
    if board[row][col]!=' ':
        return False
    board[row][col] = player
    return True

def main():
    board = [[' ']*3 for _ in range(3)]
    player = 'X'
    while True:
        print_board(board)
        print("Player", player, "turn")
        try:
            row, col = map(int, input("Enter the row and column to place your move (1-3): ").split())
            row -= 1
            col -= 1
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid move! Try again.")
                continue
            if not make_move(board, row, col, player):
                print("Invalid move! Try again.")
                continue
            if check_winner(board):
                print_board(board)
                print("Player", player, "wins!")
                break
            player = 'O' if player == 'X' else 'X'
        except ValueError:
            print("Invalid input! Please enter the row and column numbers separated by a space.")
            continue
        except Exception as e:
            print("An error occurred:", e)
            break

if __name__ == "__main__":
    main()