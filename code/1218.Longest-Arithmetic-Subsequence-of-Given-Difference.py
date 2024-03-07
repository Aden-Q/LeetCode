class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # O(n) dp
        # each entry key -> value is such a pair: key is the entry in the array
        # value is the length of the longest subsequence ending at this index such that the difference is the equal to the given difference
        dp = Counter()
        for num in arr:
            if num - difference not in dp:
                dp[num] = 1
            else:
                dp[num] = dp[num-difference] + 1

        return max(dp.values())
