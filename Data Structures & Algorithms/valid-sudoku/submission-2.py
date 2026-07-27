class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for j in range(len(board)):
            rows = {}
            columns = {}
            for i in range(len(board)):
                if board[j][i] != '.':
                    if board[j][i] not in rows:
                        rows[board[j][i]] = 1
                    else:
                        return False

                if board[i][j] != '.':
                    if board[i][j] not in columns:
                        columns[board[i][j]] = 1
                    else:
                        return False
            square = {}
            for r in range(3):
                for c in range(3):
                    row = (j//3)*3+r
                    col = (j%3)*3+c
                    if board[row][col] != '.':
                        if board[row][col] not in square:
                            square[board[row][col]] = 1
                        else:
                            return False
        return True
        
