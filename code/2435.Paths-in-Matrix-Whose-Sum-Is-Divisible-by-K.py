class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        mod = 10 ** 9 + 7
        # for all path sums, we only care about the result mod k
        # returns the number of paths starting from (0, 0) ending at (row, col) with a path sum of target        
        dp = [[0] * (k) for _ in range(n+1)]
        dp_next = [[0] * (k) for _ in range(n+1)]
        for target in range(k):
            dp_next[1][target] = 1 if grid[0][0] % k == target else 0

        for row in range(1, m+1):
            for col in range(1, n+1):
                if row == 1 and col == 1:
                    for target in range(k):
                        dp_next[col][target] = 1 if grid[row-1][col-1] % k == target else 0
                else:    
                    for target in range(k):
                        offset = (target - grid[row-1][col-1]) % k
                        dp_next[col][target] = (dp[col][offset] + dp_next[col-1][offset]) % mod
            # to avoid garbage collector
            dp, dp_next = dp_next, dp

        return dp[n][0]