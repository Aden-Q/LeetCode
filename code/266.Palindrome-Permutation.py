class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # is a permutation of the string can form a palindrome,
        # then the occurrance of characters that appear odd times must be at most 1
        counter = Counter(s)
        res = 0
        for val in counter.values():
            if val % 2 == 1:
                res += 1

        return res <= 1
