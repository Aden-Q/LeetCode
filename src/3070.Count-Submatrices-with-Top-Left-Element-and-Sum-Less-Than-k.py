class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        # 2d prefix sum
        prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for row in range(m):
            for col in range(n):
                prefix_sum[row+1][col+1] = grid[row][col] + prefix_sum[row][col+1] + prefix_sum[row+1][col] - prefix_sum[row][col]
                if prefix_sum[row+1][col+1] <= k:
                    ans += 1
        return ans
