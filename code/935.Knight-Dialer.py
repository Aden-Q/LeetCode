class Solution:
    def knightDialer(self, n: int) -> int:
        # This is a typically DP problem
        # Given that n is sufficiently large, dfs with timeout for sure
        
        # num is the number we are current at, step is the remaining number of steps we can make
        # The dp result is the total number of phone numbers we can dial based on the current state
        @lru_cache(maxsize=None)
        def dp(num, step):
            if step == 0:
                return 1
            if num == 0:
                return (dp(4, step - 1) + dp(6, step - 1)) % (10 ** 9 + 7)
            elif num == 1:
                return (dp(6, step - 1) + dp(8, step - 1)) % (10 ** 9 + 7)
            elif num == 2:
                return (dp(7, step - 1) + dp(9, step - 1)) % (10 ** 9 + 7)
            elif num == 3:
                return (dp(4, step - 1) + dp(8, step - 1)) % (10 ** 9 + 7)
            elif num == 4:
                return (dp(0, step - 1) + dp(3, step - 1) + dp(9, step - 1)) % (10 ** 9 + 7)
            elif num == 5:
                return 0
            elif num == 6:
                return (dp(0, step - 1) + dp(1, step - 1) + dp(7, step - 1)) % (10 ** 9 + 7)
            elif num == 7:
                return (dp(2, step - 1) + dp(6, step - 1)) % (10 ** 9 + 7)
            elif num == 8:
                return (dp(1, step - 1) + dp(3, step - 1)) % (10 ** 9 + 7)
            elif num == 9:
                return (dp(2, step - 1) + dp(4, step - 1)) % (10 ** 9 + 7)
            return 0
        
        res = 0
        for i in range(10):
            res = (res + dp(i, n - 1)) % (10 ** 9 + 7)
        return res