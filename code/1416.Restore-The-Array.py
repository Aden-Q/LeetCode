class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        # a typical dynamic programming problem
        mod = 10 ** 9 + 7
        # returns the number of ways to print s[start:] such that all integers are in the range [1, k]
        @cache
        def dp(start) -> int:
            if start == len(s):
                # the number of ways to print an empty string is 1
                return 1
            if s[start] == '0':
                # leading zero is invalid
                return 0

            res = 0
            for next_start in range(start+1, len(s) + 1):
                curr_int = int(s[start:next_start])
                if curr_int > k:
                    break
                # print s[start:next_start] + remaining
                res = (res + dp(next_start)) % mod

            return res

        return dp(0)
