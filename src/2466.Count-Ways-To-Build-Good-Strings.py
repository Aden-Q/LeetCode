class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10 ** 9 + 7
        # returns the number of strings of the given length by following the rules
        @cache
        def dp(length) -> int:
            if length < 0:
                return 0

            if length == 0:
                return 1
            
            # ending with zeros + ending with ones
            return (dp(length - one) + dp(length - zero)) % mod

        ans = 0
        for length in range(low, high+1):
            ans = (ans + dp(length)) % mod

        return ans
