class Solution:
    def makePalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        cnt = 0

        while left < right:
            if s[left] != s[right]:
                # yes we must replace exactly one character
                cnt += 1
            if cnt > 2:
                return False
            left += 1
            right -= 1

        return True