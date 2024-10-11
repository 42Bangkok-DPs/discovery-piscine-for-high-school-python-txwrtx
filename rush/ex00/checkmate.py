"""
    Add this chat_list for error handling
    char_list = [ 'R', 'B', 'Q', 'P', 'K', '.' ]
"""

directions = {
    'R': [(0, 1), (0, -1), (1, 0), (-1, 0)],
    'B': [(1, 1), (1, -1), (-1, 1), (-1, -1)],
    'Q': [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)],
    'P': [(1, -1), (1, 1)]
}

king_pos = ()

def checkmate(board=""):
    board = board.strip().split('\n')
    for i in board:
        if len(i) != len(board):
            return print("Error")
        
    board = create_board(board)
    king_pos = find_king_pos(board)

    """
        Add this line of code to handle error if 
        there's king more than 1 king and if there's 
        Char that's not in the game just return error
        
        found_king = 0;
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == "K": found_king += 1
    
                if board[row][col] not in char_list:
                    return print("Error")
        if found_king > 1 :
            return print("Error")
    """
    

    """
        Add this lines of code to check if 
        king is equal to None then return Error
    
        if king_pos == None:
        return print("Error")
    """

    for piece, moves in directions.items():
        for move in moves:
            r, c = king_pos
            while True:
                r += move[0]
                c += move[1]
                if 0 <= r < len(board) and 0 <= c < len(board):
                    if board[r][c] == 'K':
                        break
                    if board[r][c] != '.':
                        if board[r][c] == piece:
                            print("Success")
                            return
                        break
                else:
                    break

    print("Fail")
        

def create_board(board):
    return [list(row) for row in board]

# Change to return None to handle if there's no king on the tale
def find_king_pos(board):
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "K":
                return (r, c)
            
    return "Fail"
