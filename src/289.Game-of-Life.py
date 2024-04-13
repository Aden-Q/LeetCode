import copy

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def countLive(board, row, col):
            num_live = 0
            # left
            if col - 1 >= 0 and board[row][col-1] == 1:
                num_live += 1
            # right
            if col + 1 < len(board[0]) and board[row][col+1] == 1:
                num_live += 1
            # up
            if row-1 >= 0 and board[row-1][col] == 1:
                num_live += 1
            # down
            if row+1 < len(board) and board[row+1][col] == 1:
                num_live += 1
            # diagnal
            if row-1 >= 0 and col - 1 >= 0 and board[row-1][col-1] == 1:
                num_live += 1
            if row-1 >= 0 and col + 1 < len(board[0]) and board[row-1][col+1] == 1:
                num_live += 1
            if row+1 < len(board) and col-1 >= 0 and board[row+1][col-1] == 1:
                num_live += 1
            if row+1 < len(board) and col+1 < len(board[0]) and board[row+1][col+1] == 1:
                num_live += 1
            return num_live
            
        temp_board = copy.deepcopy(board)
        num_row = len(board)
        num_col = len(board[0])
        for i in range(num_row):
            for j in range(num_col):
                num_live = countLive(board, i, j)
                if board[i][j] == 1:
                    if num_live == 2 or num_live == 3:
                        temp_board[i][j] = 1
                    else:
                        temp_board[i][j] = 0
                else:
                    if num_live == 3:
                        temp_board[i][j] = 1
        # copy back
        for i in range(num_row):
            for j in range(num_col):
                board[i][j] = temp_board[i][j]
            