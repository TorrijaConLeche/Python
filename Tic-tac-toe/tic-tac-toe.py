# Simple Tic-tac-toe


grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Playing board

nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Used to compare with the board

turn = "p1"  # Stores the turn


def show_board(board):  # Show the board
    for i in board:
        for j in i:
            print(j, end=" ")
        print()


def toggle_turn(player):  # Toggle turn

    if player == "p1":
        return "p2"
    else:
        return "p1"


# Used to apply changes when a player moves between fields 1-3
def player_movement1(number, grid, turn):
    for i in grid[0]:
        if turn == "p1":
            if i == number:
                ind = grid[0].index(i)
                grid[0][ind] = "X"
        else:
            if i == number:
                ind = grid[0].index(i)
                grid[0][ind] = "O"


# Used to apply changes when a player moves between fields 4-6
def player_movement2(number, grid, turn):
    for i in grid[1]:
        if turn == "p1":
            if i == number:
                ind = grid[1].index(i)
                grid[1][ind] = "X"
        else:
            if i == number:
                ind = grid[1].index(i)
                grid[1][ind] = "O"


# Used to apply changes when a player moves between fields 7-9
def player_movement3(number, grid, turn):
    for i in grid[2]:
        if turn == "p1":
            if i == number:
                ind = grid[2].index(i)
                grid[2][ind] = "X"
        else:
            if i == number:
                ind = grid[2].index(i)
                grid[2][ind] = "O"


def who_plays(turn, name1, name2):  # Show who plays
    if turn == "p1":
        print(f"{name1} plays: ")
    else:
        print(f"{name2} plays: ")


def check_board(grid, nums):  # Check board

    p1_wins = ["X", "X", "X"]
    p2_wins = ["O", "O", "O"]

    # Used to check DRAW
    x = set(grid[0]).intersection(set(nums[0]))  # Row 1: 1-3
    y = set(grid[1]).intersection(set(nums[1]))  # Row 2: 4-6
    z = set(grid[2]).intersection(set(nums[2]))  # Row 3: 7-9

    # Rows
    row1 = grid[0]
    row2 = grid[1]
    row3 = grid[2]
    # Columns
    col1 = [grid[0][0]] + [grid[1][0]] + [grid[2][0]]
    col2 = [grid[0][1]] + [grid[1][1]] + [grid[2][1]]
    col3 = [grid[0][2]] + [grid[1][2]] + [grid[2][2]]
    # Diagonals
    diag1 = [grid[0][0]] + [grid[1][1]] + [grid[2][2]]
    diag2 = [grid[0][2]] + [grid[1][1]] + [grid[2][0]]

    # Check if p1 wins
    if row1 == p1_wins or row2 == p1_wins or row3 == p1_wins\
       or col1 == p1_wins or col2 == p1_wins or col3 == p1_wins\
       or diag1 == p1_wins or diag2 == p1_wins:
        return 1

    # Check if p2 wins
    if row1 == p2_wins or row2 == p2_wins or row3 == p2_wins\
            or col1 == p2_wins or col2 == p2_wins or col3 == p2_wins\
            or diag1 == p2_wins or diag2 == p2_wins:
        return 2

    # Check DRAW
    if len(x) == 0 and len(y) == 0 and len(z) == 0:
        return 0


name1 = input("Player 1 name: ")
name2 = input("Player 2 name: ")

while True:
    show_board(grid)
    while True:

        if check_board(grid, nums) == 0:  # Check the board so if there is a draw we exit
            print("-----------\nDRAW\n-----------")
            exit()

        if check_board(grid, nums) == 1:  # Check the board so if there is a draw we exit
            print(f"------------------\n{name1} (X) wins\n------------------")
            exit()

        if check_board(grid, nums) == 2:  # Check the board so if there is a draw we exit
            print(f"------------------\n{name2} (O) wins\n------------------")
            exit()

        who_plays(turn, name1, name2)

        mov = int(input())

        if mov in grid[0]:
            player_movement1(mov, grid, turn)  # Position between 1-3
            break
        elif mov in grid[1]:
            player_movement2(mov, grid, turn)   # Position between 4-6
            break
        elif mov in grid[2]:
            player_movement3(mov, grid, turn)   # Position between 7-9
            break
        else:
            print(turn, "Please input a valid position\n")

        show_board(grid)

    turn = toggle_turn(turn)
