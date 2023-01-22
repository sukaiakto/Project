import random

num = [0, 0, 0, 0]


def init_board():
    board = []
    for i in range(4):
        board += [["0"] * 4]
    add_num(board, 2)
    return board


def add_num(board, n):
    for i in range(n):
        new_num = str(random.choice([2, 4]))
        random_x = random.randrange(4)
        random_y = random.randrange(4)
        while board[random_y][random_x] != "0":
            random_x = random.randrange(4)
            random_y = random.randrange(4)
        board[random_y][random_x] = new_num


def win(board):
    win_ = False
    for line in board:
        if "2048" in line:
            win_ = True
            break
    return win_


def score(board):
    for i in range(4):
        num[i] = sum(map(int, board[i]))
    return sum(num)


def add(board, i_list, j_list, i_direction, j_direction):
    move = 0
    for i in i_list:
        for j in j_list:
            if board[i][j] == board[i + i_direction][j + j_direction]:
                board[i + i_direction][j + j_direction] = str(
                    int(board[i][j]) + int(board[i + i_direction][j + j_direction]))
                if board[i][j] != 0:
                    move += 1
                board[i][j] = "0"
    return move


def push(board, i_list, j_list, i_direction, j_direction):
    move = 0
    for i in i_list:
        for j in j_list:
            if board[i + i_direction][j + j_direction] == "0":
                board[i + i_direction][j + j_direction] = board[i][j]
                if board[i][j] != 0:
                    move += 1
                board[i][j] = "0"
    return move


def move_direction(board, user_input):
    move = 0
    if user_input == "u":
        i_list, j_list = range(1, 4), range(4)
        i_direction, j_direction = -1, 0
    elif user_input == "d":
        i_list, j_list = range(2, -1, -1), range(4)
        i_direction, j_direction = 1, 0
    elif user_input == "l":
        i_list, j_list = range(4), range(1, 4)
        i_direction, j_direction = 0, -1
    elif user_input == "r":
        i_list, j_list = range(4), range(2, -1, -1)
        i_direction, j_direction = 0, 1

    for i in range(4):
        move += push(board, i_list, j_list, i_direction, j_direction)
    move += add(board, i_list, j_list, i_direction, j_direction)
    for i in range(4):
        move += push(board, i_list, j_list, i_direction, j_direction)

    return move


def check_cell(board, i, j):
    move_i = []
    move_j = []
    board_size = len(board)
    if i > 0:
        move_i.append(-1)
        move_j.append(0)
    if i < (board_size - 1):
        move_i.append(1)
        move_j.append(0)
    if j > 0:
        move_j.append(-1)
        move_i.append(0)
    if j < (board_size - 1):
        move_j.append(1)
        move_i.append(0)
    for k in range(len(move_i)):
        if board[i + move_i[k]][j + move_j[k]] == board[i][j]:
            return True
    return False


def can_move(board):
    board_size = len(board)
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == 0:
                return True
            if check_cell(board, i, j):
                return True
    return False


def lose(board):
    full_table = False
    for elt in board:
        full_table = full_table or ("0" in elt)

    if not full_table:
        return not can_move(board)
    return False


def main(board, user_input):
    if user_input == 'rest':
        return init_board()
    if user_input == 'win':
        for x in range(4):
            for y in range(4):
                board[x][y] = '2048'
    if not lose(board) and not win(board):

        move = move_direction(board, user_input)
        if move != 0:
            add_num(board, 1)
    return board
