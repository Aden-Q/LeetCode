class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        used = [[0] * n for _ in range(m)]
        # running dfs for each starting position
        # with backtracking
        def dfs(row, col, cur):
            # row: current row index
            # col: current col index
            # cur: current cursor into the word
            # return true is found
            nonlocal used, word, m, n
            if cur == len(word):
                return True
            if row < 0 or row >= m:
                return False
            if col < 0 or col >= n:
                return False
            if used[row][col]:
                return False
            if word[cur] != board[row][col]:
                return False
            # otherwise marked as used and check the neighboring word
            used[row][col] = True
            for d in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                next_row, next_col = row + d[0], col + d[1]
                if dfs(next_row, next_col, cur+1):
                    return True
            used[row][col] = False
            return False
        
        for row in range(m):
            for col in range(n):
                if dfs(row, col, 0):
                    return True
        
        return False