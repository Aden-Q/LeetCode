class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_temp = []
        for c in s:
            if c.isalnum():
                s_temp.append(c)
        left, right = 0, len(s_temp) - 1
        while left < right:
            if s_temp[left] != s_temp[right]:
                return False
            left += 1
            right -= 1
        return True