class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        lookup_table = set(str(i) for i in range(1, 27))

        # dp[i] is the number of ways to decode s[i:]
        dp_plus_one = 1
        dp_plus_two = 0

        for i in range(n-1, -1, -1):
            dp = 0
            if s[i] == '0':
                dp_plus_one, dp_plus_two = 0, dp_plus_one
                continue
            dp += dp_plus_one
            if i+1 < n and s[i:i+2] in lookup_table:
                dp += dp_plus_two
            dp_plus_one, dp_plus_two = dp, dp_plus_one

        return dp_plus_one
