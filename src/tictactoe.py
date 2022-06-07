NUMBER_OF_SYMBOLS = 9
GRID = 3
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def fill_board(symbols="_________"):
    global board
    index = 0
    for i in range(GRID):
        for j in range(GRID):
            if symbols[index] == 'X' or symbols[index] == 'O':
                board[i][j] = symbols[index]
            index += 1


def print_board():
    global board
    print("-" * NUMBER_OF_SYMBOLS)
    for i in range(GRID):
        print("|", end=" ")
        for j in range(GRID):
            print(board[i][j], end=" ")
        print("|")
    print("-" * NUMBER_OF_SYMBOLS)


def is_plain():
    global board
    res = [column for line in board for column in line if column == "" or column == "_"]
    return len(res) == 0


def is_x_win():
    """X wins"""
    global board
    for i in range(GRID):
        if board[i][0] == "X" and board[i][1] == "X" and board[i][2] == "X":
            return True
        if board[0][i] == "X" and board[1][i] == "X" and board[2][i] == "X":
            return True
    if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        return True
    if board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        return True
    return False


def is_o_win():
    """O wins"""
    global board
    for i in range(GRID):
        if board[i][0] == "O" and board[i][1] == "O" and board[i][2] == "O":
            return True
        if board[0][i] == "O" and board[1][i] == "O" and board[2][i] == "O":
            return True
    if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        return True
    if board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        return True
    return False


def analyze_game(symbols: str):
    output = ''
    if abs(symbols.count("O") - symbols.count("X")) > 1:
        # print("Impossible")
        pass
    elif is_x_win() and is_o_win():
        pass
        # print("Impossible")
    elif is_x_win():
        # print("X wins")
        output = "X"
    elif is_o_win():
        # print("O wins")
        output = "O"
    elif is_plain():
        # print("Draw")
        output = "D"
    else:
        # print("Game not finished")
        pass
    return output


def make_move(move: str = "X"):
    global board
    while True:
        symbols = input()
        if len(symbols.split()) > 1:
            x, y =symbols.split()
            if x.isnumeric() and y.isnumeric():
                x = int(x) - 1
                y = int(y) - 1
                if x < 0 or x > 2:
                    print("Coordinates should be from 1 to 3!")
                elif y < 0 or y > 2:
                    print("Coordinates should be from 1 to 3!")
                elif board[x][y] == "X" or board[x][y] == "O":
                    print("This cell is occupied! Choose another one!")
                else:
                    board[x][y] = move
                    break
            else:
                print("You should enter numbers!")
        else:
            print("You should enter numbers!")


def main():
    fill_board()
    print_board()
    i = 0
    moves = ["X", "O"]
    while True:
        make_move(moves[i % 2])
        print_board()
        i += 1
        if i > 8: # if there is 8 moves, the game is over
            stat = analyze_game("".join(["".join(line) for line in board]))
            if stat == "X":
                print("X wins")
                break
            elif stat == "O":
                print("O wins")
                break
            elif stat == "D":
                print("Draw")
                break


if __name__ == "__main__":
    main()
