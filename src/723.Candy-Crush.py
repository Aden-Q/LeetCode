class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m, n = len(board), len(board[0])
        todo = False
        
        # If we ever did crush operations, we need to make a recursive call
        # to further crush
        for r in range(m):
            # Check each row
            for c in range(n-2):
                if abs(board[r][c]) == abs(board[r][c+1]) == abs(board[r][c+2]) != 0:
                    board[r][c] = board[r][c+1] = board[r][c+2] = - abs(board[r][c])
                    todo = True
        
        for r in range(m-2):
            # Check each row
            for c in range(n):
                if abs(board[r][c]) == abs(board[r+1][c]) == abs(board[r+2][c]) != 0:
                    board[r][c] = board[r+1][c] = board[r+2][c] = - abs(board[r][c])
                    todo = True
        # Gravity step, falling down for each column
        for c in range(n):
            last_row = m - 1
            for r in range(m-1, -1, -1):
                if board[r][c] > 0:
                    board[last_row][c] = board[r][c]
                    last_row -= 1
            for r in range(last_row, -1, -1):
                # Fill in those empty cells
                board[r][c] = 0    
        
        if todo:
            return self.candyCrush(board)
        return board