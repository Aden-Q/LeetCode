class Num:
    def __init__(self, num):
        self.num = str(num)

    def less_than(self, num1, num2):
        if len(num1) == len(num2):
            return num1 < num2

        min_len = min(len(num1), len(num2))
        if len(num1) > len(num2):
            return self.less_than(num1[:min_len], num2) or (num1[:min_len] == num2 and self.less_than(num1[min_len:], num2))
        
        return self.less_than(num1, num2[:min_len]) or (num1 == num2[:min_len] and self.less_than(num1, num2[min_len:]))

    def __lt__(self, other):
        return self.less_than(self.num, other.num)

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_obj = [Num(num) for num in nums]
        nums_obj.sort(reverse=True)
        res = ''.join([x.num for x in nums_obj])
        # trim leading 0
        res = res.lstrip('0')

        if len(res) == 0:
            return '0'
        return res
