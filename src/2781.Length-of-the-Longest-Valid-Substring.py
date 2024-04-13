class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        # convert to a set to support O(1) lookup
        forbidden_set = set(forbidden)
        possible_forbidden_len = range(1, 11)
        left = right = 0
        max_length = 0
        # sliding window
        while right < len(word):
            for substr_left in range(right, max(left, right-9) - 1, -1):
                if word[substr_left:right+1] in forbidden_set:
                    left = max(left, substr_left + 1)
                    break
            
            max_length = max(max_length, right - left + 1)
            right += 1

        return max_length
