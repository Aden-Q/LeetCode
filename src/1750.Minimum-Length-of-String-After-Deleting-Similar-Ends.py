class Solution:
    def minimumLength(self, s: str) -> int:
        # O(n), simulation
        left, right = 0, len(s) - 1
        while left < right and s[left] == s[right]:
            pivot =s[left]
            while left <= right and s[left] == pivot:
                left += 1
            while left <= right and s[right] == pivot:
                right -= 1

        return right - left + 1
