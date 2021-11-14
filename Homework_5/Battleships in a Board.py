def countBattleships(board):
    def remove_right(b, r, c, max_c):
        while c < max_c and b[r][c] == "X":
            b[r][c] = "."
            c += 1

    def remove_down(b, r, c, max_r):
        while r < max_r and b[r][c] == "X":
            b[r][c] = "."
            r += 1

    count = 0
    rows = len(board)
    columns = len(board[0])
    for row in range(rows):
        for column in range(columns):
            if board[row][column] == "X":
                count += 1
                if column < columns - 1 and board[row][column+1] == "X":
                    remove_right(board, row, column, columns)
                if row < rows - 1 and board[row+1][column] == "X":
                    remove_down(board, row, column, rows)
    return count
