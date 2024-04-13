class Solution:
    def isArmstrong(self, n: int) -> bool:
        digits = []
        temp_n = n
        while temp_n:
            digits.append(temp_n % 10)
            temp_n = temp_n // 10

        power = len(digits)
        power_sum = 0
        for digit in digits:
            power_sum += digit ** power
        
        return power_sum == n
