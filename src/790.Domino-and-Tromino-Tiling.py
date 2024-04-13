class Solution:
    def numTilings(self, n: int) -> int:
        # partially fill the last column (must fill all the columns before the last one)
        dp1 = {1: 0, 2: 2}
        # fully fill the last column
        dp2 = {1: 1, 2: 2}

        # dp2[n] = dp2[n-1] + dp2[n-2] + dp1[n-1]
        # dp1[n] = dp1[n-1] + 2 * dp2[n-2]
        
        # return the number of ways to fill a 2xn board
        def dfs_dp1(n) -> int:
            nonlocal dp1, dp2
            if n in dp1:
                return dp1[n]
            dp1[n] = (dfs_dp1(n-1) + 2 * dfs_dp2(n-2)) % (10 ** 9 + 7)
            return dp1[n]

        def dfs_dp2(n) -> int:
            nonlocal dp1, dp2
            if n in dp2:
                return dp2[n]
            dp2[n] = (dfs_dp2(n-1) + dfs_dp2(n-2) + dfs_dp1(n-1)) % (10 ** 9 + 7)
            return dp2[n]

        return dfs_dp2(n)
