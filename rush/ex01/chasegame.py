board = [0] * 8
col_index = ["a", "b", "c", "d", "e", "f", "g", "h"]
col_map = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
}

info = [
    "K = King",
    "R = Rook",
    "B = Bishop",
    "Q = Queen",
    "N = Knight",
    "P = Pawn",
    "'b' is BLACK TEAM",
    "'w' is WHITE TEAM"
]

black_pieces = {
    "bP": [(7,'a'),(7,'b'),(7,'c'),(7,'d'),(7,'e'),(7,'f'),(7,'g'),(7,'h')],
    "bR": [(8, 'a'), (8, 'h')],
    "bN": [(8, 'b'), (8, 'g')],
    "bB": [(8, 'c'), (8, 'f')],
    "bK": [(8, 'd')],
    "bQ": [(8, 'e')]
}

white_pieces = {
    "wP": [(2,'a'),(2,'b'),(2,'c'),(2,'d'),(2,'e'),(2,'f'),(2,'g'),(2,'h')],
    "wR": [(1, 'a'), (1, 'h')],
    "wN": [(1, 'b'), (1, 'g')],
    "wB": [(1, 'c'), (1, 'f')],
    "wK": [(1, 'd')],
    "wQ": [(1, 'e')]
}

turn = 1;
current_team = "WHITE TEAM"


for i in range(len(board)):
    board[i] = ["  "] * 8

def refresh_board(board):
    print("----------------- CHESS GAME -----------------", end="\n\n")
    print(f"----------------- {current_team} -----------------", end="\n\n")
    print(f"------------------- TURN {turn} -------------------", end="\n\n\n")

    print("  *", end="")
    print("----+" * 8) 
    for i, row in enumerate(board):
        print(8 - i, end=" | ")
        for col in row:

            print(col, end=" | ")

        print(f"     {info[i]}", end="")   
        print()
        print("  *", end="")
        print("----+" * 8) 
    
    print("     ", end="")
    for i in col_index:
        print(i, end="    ")
    print()

def init_board():
    for piece, squares in black_pieces.items():
        for square in squares:
            square = convert_to_table_index(square)
            row, col = square[0], square[1]
            board[row][col] = piece

    for piece, squares in white_pieces.items():
        for square in squares:
            square = convert_to_table_index(square)
            row, col = square[0], square[1]
            board[row][col] = piece

def convert_to_table_index(num):
    return ((8 - num[0]), col_map.get(num[1]))

# def is_valid_move(piece, select_pos, target_pos):
#     if piece[0] == "w":
#         if piece[1] == "P":
#             if target_pos[0] - select_pos[0] == -1 and target_pos[1] == select_pos[1] and board[target_pos[0]][target_pos[1]] == "  ":
#                 return True
#     elif piece[0] == "b":
#         if piece[1] == "P":
#             if target_pos[0] - select_pos[0] == 1 and target_pos[1] == select_pos[1] and board[target_pos[0]][target_pos[1]] == "  ":
#                 return True
#     return False

init_board()
refresh_board(board)

while True:
    piece = str(input("Select which piece do u want to move (Example: 6d) : "))
    target = str(input("Select which square do u want to move to (Example: 6d) : "))

    select_pos = convert_to_table_index((int(piece[0]), piece[1]))
    target_pos = convert_to_table_index((int(target[0]), target[1]))

    if (current_team == "WHITE TEAM" and str(board[select_pos[0]][select_pos[1]]).startswith("b")) \
        or (current_team == "BLACK TEAM" and str(board[select_pos[0]][select_pos[1]]).startswith("w")):
        print("U can't select opponent piece!")
        continue
    
    if board[select_pos[0]][select_pos[1]] == "  ":
        print("U can't select empty square!")
        continue

    if str(board[select_pos[0]][select_pos[1]]).startswith("b") and target_pos[0] == 7:
        break
    elif str(board[select_pos[0]][select_pos[1]]).startswith("w") and target_pos[0] == 0:
        break
    board[target_pos[0]][target_pos[1]] = board[select_pos[0]][select_pos[1]]
    board[select_pos[0]][select_pos[1]] = "  "

    turn += 1
    if current_team  == "WHITE TEAM": current_team = "BLACK TEAM"
    else: current_team = "WHITE TEAM"
    refresh_board(board)
print("\n\n\n")
print(f"                    {current_team} WIN!!!!!!!")
print("\n\n\n")

    # if is_valid_move(board[select_pos[0]][select_pos[1]], select_pos, target_pos):
    #     board[target_pos[0]][target_pos[1]] = board[select_pos[0]][select_pos[1]]
    #     board[select_pos[0]][select_pos[1]] = "  " 
    #     turn += 1
    #     if current_team  == "WHITE TEAM": current_team = "BLACK TEAM"
    #     else: current_team = "WHITE TEAM"
    #     refresh_board(board)
    # else: 
    #     print("Invalid Move!")
    
