class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        digits = ["1","2","3","4","5","6","7","8","9"]
        def isValid(board, row, col, val):
            # check columns
            for i in range(9):
                if i != col and board[row][i] == val:
                    return False
            # check rows
            for i in range(9):
                if i != row and board[i][col] == val:
                    return False
            # check 3x3 grid
            block_row_idx = row // 3
            block_col_idx = col // 3
            for i in range(block_row_idx*3, block_row_idx*3+3):
                for j in range(block_col_idx*3, block_col_idx*3+3):
                    if (i, j) != (row, col) and board[i][j] == val:
                        return False
            return True
            
        def backtracking(board) -> bool:
            for row in range(9):
                for col in range(9):
                    if board[row][col] != '.':
                        continue
                    for val in digits:
                        if isValid(board, row, col, val):
                            board[row][col] = val
                            if backtracking(board): return True  
                            board[row][col] = '.'
                    return False
            return True
                
        backtracking(board)
        return board
                