def create_new_board():
    return [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ]


def print_board(board):
    width = len(board[0])
    height = len(board)

    for i, row in enumerate(board):
        for j, element in enumerate(row):
            print(element, end='')
            if j < (width - 1):
                print("|", end='')

        if i < (height - 1):
            print()
            print("+".join("-" * width))

    print("\n\n")


def game_finished(board):
    if board[0][0] == board[0][1] == board[0][2] != " ":
        return True
    elif board[1][0] == board[1][1] == board[1][2]!= " ":
        return True
    elif board[2][0] == board[2][1] == board[2][2]!= " ":
        return True
    elif board[0][0] == board[1][0] == board[2][0]!= " ":
        return True
    elif board[0][1] == board[1][1] == board[2][1]!= " ":
        return True
    elif board[0][2] == board[1][2] == board[2][2]!= " ":
        return True
    elif board[0][0] == board[1][1] == board[2][2]!= " ":
        return True
    elif board[0][2] == board[1][1] == board[2][0]!= " ":
        return True
    else:
        return False


def get_input(player, board):
    while True:
        try:
            trekk = input(f"{player} what's your move? ")
            x, y = [int(n) for n in trekk.split(sep=",")]
            if not (0 <= x < len(board[0])):
                print(f"x must be between 0 and {len(board[0])}")
                continue

            if not (0 <= y < len(board)):
                print(f"y must be between 0 and {len(board)}")
                continue
            
            if board[x][y] != " ":
                print("This cell is already taken.")
                continue

            return x, y
        except:
            print("Not a valid move. Please type again.")

            
def full_board(board):
    for row in board:
        for element in row:
            if element == " ":
                return False
    return True


def main():
    board = create_new_board() 
    sign = "X"
    while True:
        name = "player 1" if sign == "X" else "player 2"
        print_board(board)
        x, y = get_input(name, board)
        board[x][y] = sign
        if game_finished(board):
            print(f"{name} you won!")
            break

        if full_board(board):
            print("its a tie!")
            break

        sign = "O" if sign == "X" else "X"
    
    print_board(board)
    print(f"The game is finished.")

    
if __name__ == '__main__':  
    main()
