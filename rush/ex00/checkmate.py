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

def find_king_pos(board):
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "K":
                return (r, c)
            
    return "Fail"
