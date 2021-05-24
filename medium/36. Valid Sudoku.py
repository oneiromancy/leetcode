def isValidSudoku(board):
    d = {}
    keys = range(1, 10)
    
    for i in keys:
        d[i] = ([False] * 9, [False] * 9, [False] * 9)

    for r in range(9):
        for c in range(9):
            # Each row must contain the digits 1-9 without repetition.
            if board[r][c] == '.':
                continue
            elif d[r + 1][0][int(board[r][c]) - 1] is False:
                d[r + 1][0][int(board[r][c]) - 1] = True
            else: 
                return False

            # Each column must contain the digits 1-9 without repetition.
            if board[r][c] == '.':
                continue
            elif d[c + 1][1][int(board[r][c]) - 1] is False:
                d[c + 1][1][int(board[r][c]) - 1] = True
            else: 
                return False

            # Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
            if board[r][c] == '.':
                continue
            elif 0 <= r <= 2 and 0 <= c <= 2:
                if d[1][2][int(board[r][c]) - 1] is False:
                    d[1][2][int(board[r][c]) - 1] = True
                else: 
                    return False
            elif 0 <= r <= 2 and 3 <= c <= 5:
                if d[2][2][int(board[r][c]) - 1] is False:
                    d[2][2][int(board[r][c]) - 1] = True
                else: 
                    return False
            elif 0 <= r <= 2 and 6 <= c <= 8:
                if d[3][2][int(board[r][c]) - 1] is False:
                    d[3][2][int(board[r][c]) - 1] = True
                else: 
                    return False
            elif 3 <= r <= 5 and 0 <= c <= 2:
                if d[4][2][int(board[r][c]) - 1] is False:
                    d[4][2][int(board[r][c]) - 1] = True
                else: 
                    return False
            elif 3 <= r <= 5 and 3 <= c <= 5:
                if d[5][2][int(board[r][c]) - 1] is False:
                    d[5][2][int(board[r][c]) - 1] = True
                else: 
                    return False
            elif 3 <= r <= 5 and 6 <= c <= 8:
                if d[6][2][int(board[r][c]) - 1] is False:
                    d[6][2][int(board[r][c]) - 1] = True
                else: 
                    return False
            elif 6 <= r <= 8 and 0 <= c <= 2:
                if d[7][2][int(board[r][c]) - 1] is False:
                    d[7][2][int(board[r][c]) - 1] = True
                else: 
                    return False
            elif 6 <= r <= 8 and 3 <= c <= 5:
                if d[8][2][int(board[r][c]) - 1] is False:
                    d[8][2][int(board[r][c]) - 1] = True
                else: 
                    return False
            elif 6 <= r <= 8 and 6 <= c <= 8:
                if d[9][2][int(board[r][c]) - 1] is False:
                    d[9][2][int(board[r][c]) - 1] = True
                else: 
                    return False

    return True
            

print(isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
