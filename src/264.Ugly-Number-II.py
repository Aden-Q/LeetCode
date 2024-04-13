class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[1] = 1
        ptr_x, ptr_y, ptr_z = 1, 1, 1
        for i in range(2, n+1):
            dp[i] = min(dp[ptr_x] * 2, dp[ptr_y] * 3, dp[ptr_z] * 5)
            if dp[i] == dp[ptr_x] * 2: ptr_x += 1
            if dp[i] == dp[ptr_y] * 3: ptr_y += 1
            if dp[i] == dp[ptr_z] * 5: ptr_z += 1

        return dp[n]
