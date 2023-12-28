class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        # we processing s from left to right
        # idx is the current symbol that we are processing
        # last_char is the last character in the compression sequence
        # last_char_count is the count of the last character in the compression sequence
        # k is the number of symbols still last to delete
        # dp returns the minimum length of the compressed string for s[idx:] when we perform at most k delete operations
        @lru_cache(None)
        def dp(idx, last_char, last_char_count, k) -> int:
            if k < 0:
                return math.inf
            if idx == n or idx >= n-k:
                # base case1: nothing to process, the minimum length of the compressed string is 0
                # base case2: when the number of characters left is less than or equal to k, we can delete everything in this case
                return 0

            # length of the longest compress string if we delete s[idx]
            delete_len = dp(idx+1, last_char, last_char_count, k-1)
            if s[idx] == last_char:
                if last_char_count in (1, 9, 99):
                    keep_len = dp(idx+1, last_char, last_char_count+1, k) + 1
                else:
                    keep_len = dp(idx+1, last_char, last_char_count+1, k)
            else:
                keep_len = dp(idx+1, s[idx], 1, k) + 1

            return min(delete_len, keep_len)

        return dp(0, '', 0, k)