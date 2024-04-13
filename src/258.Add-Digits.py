class Solution:
    def addDigits(self, num: int) -> int:
        res = num
        while len(str(res)) > 1:
            temp_sum = 0
            while num > 0:
                temp_sum += num % 10
                num = num // 10
            res = temp_sum
            num = temp_sum
            
        return res