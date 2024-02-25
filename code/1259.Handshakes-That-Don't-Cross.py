class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        mod = 10 ** 9 + 7

        @cache
        def dp(numPeople) -> int:
            if numPeople == 0:
                return 1
            
            if numPeople == 2:
                return 1
            
            res = 0
            # the last people can shake hands with people 1, 3, 5, ..., last_index - 1
            for shake in range(1, numPeople, 2):
                res += dp(shake - 1) * dp(numPeople - shake - 1)
                res = res % mod

            return res

        return dp(numPeople)
