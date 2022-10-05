class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        rows = len(pizza)
        cols = len(pizza[0])
        prefixSum = [[0] * (cols + 1) for _ in range(rows + 1)]
        mod = 10 ** 9 + 7
        
        for i in range(rows):
            for j in range(cols):
                currVal = 1 if pizza[i][j] == 'A' else 0
                prefixSum[i+1][j+1] = prefixSum[i][j+1] + prefixSum[i+1][j] - prefixSum[i][j] + currVal
        
        def getSum(row1, col1, row2, col2):
            nonlocal prefixSum
            if row1 > row2 or col1 > col2:
                return 0
            # Get the range sum of the square with left upper corner (row1, col1) and right lower corner (row2, col2)
            return prefixSum[row2 + 1][col2 + 1] - prefixSum[row1][col2 + 1] - prefixSum[row2 + 1][col1] + prefixSum[row1][col1]
        
        # A state of dp represents the number of ways of cutting pizza
        # starting from (row, col) as a upper-left corner and use c cuts
        # c represents the number of cuts we have performed so far
        @lru_cache(maxsize=None)
        def dp(row, col, c):
            if getSum(row, col, rows - 1, cols - 1) == 0:
                return 0
            if c == k - 1:
                # no more cuts need to perform
                return 1
            
            numWaysOfCut = 0
            # Check whether we can perform a row cut
            for next_row in range(row + 1, rows):
                # Need to guarantee that there is one apple given to a person by performing this cut
                if getSum(row, col, next_row - 1, cols - 1) != 0:
                    numWaysOfCut = (numWaysOfCut + dp(next_row, col, c + 1)) % mod
                
            for next_col in range(col + 1, cols):
                # Need to guarantee that there is one apple given to a person by performing this cut
                if getSum(row, col, rows - 1, next_col - 1) != 0:
                    numWaysOfCut = (numWaysOfCut + dp(row, next_col, c + 1)) % mod
            
            return numWaysOfCut

        return dp(0, 0, 0)