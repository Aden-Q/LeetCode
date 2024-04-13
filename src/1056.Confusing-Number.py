class Solution:
    def confusingNumber(self, n: int) -> bool:
        digits = []
        while n:
            digit = n % 10
            if digit in [2, 3, 4, 5, 7]:
                return False
            digits.append(digit)
            n = n // 10

        lookup_table = {
            6: 9,
            9: 6,
            1: 1,
            0: 0,
            8: 8,
        }
        left, right = 0, len(digits) - 1
        while left <= right:
            if digits[right] != lookup_table[digits[left]]:
                return True
            left += 1
            right -= 1

        return False
