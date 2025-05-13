class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9 + 7

        # dp[i] is the number of occurence of the character i after k transformations, k being dynamic
        dp = [0] * 26

        for c in s:
            dp[ord(c) - ord("a")] += 1

        for _ in range(t):
            dp_next = [0] * 26
            dp_next[0] = dp[25]  # a
            dp_next[1] = (dp[0] + dp[25]) % mod  # b
            for i in range(2, 26):
                dp_next[i] = dp[i - 1]
            dp, dp_next = dp_next, dp

        return sum(dp) % mod
