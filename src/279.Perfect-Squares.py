class Solution:
    def numSquares(self, n: int) -> int:
        
        @cache
        def dp(n) -> int:
            if n == 0:
                return 0

            i = 1
            res = n
            while i * i <= n:
                res = min(res, 1 + dp(n - i * i))
                i += 1

            return res

        return dp(n)
