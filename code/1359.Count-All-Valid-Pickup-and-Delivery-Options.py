class Solution:
    def countOrders(self, n: int) -> int:
        mod = 10 ** 9 + 7
        def dp(n) -> int:
            if n == 1:
                return 1
        
            # choose from 2n - 1, 2 + 2
            return (dp(n-1) * (comb(2*n-1, 2) + 2*n-1)) % mod

        return dp(n)
