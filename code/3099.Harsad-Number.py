class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        x_temp = x
        sum_digits = 0
        while x_temp:
            sum_digits += x_temp % 10
            x_temp //= 10
        
        if x % sum_digits == 0:
            return sum_digits

        return -1
