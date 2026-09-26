class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(9):
            row = []
            col = []

            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in row:
                        return False
                    row.append(board[i][j])

                if board[j][i] != ".":
                    if board[j][i] in col:
                        return False
                    col.append(board[j][i])

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = []

                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        if board[r][c] != ".":
                            if board[r][c] in box:
                                return False
                            box.append(board[r][c])

        return True