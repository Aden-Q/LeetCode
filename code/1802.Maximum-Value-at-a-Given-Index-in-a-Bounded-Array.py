class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        
        def calSum(n, index, target):
            # nums[index] = target
            # nums[index - i] = target - i
            # nums[0] = target - index
            # nums[index + i] = target - i
            # i = n - 1 - index
            # nums[n-1] = target - n + 1 + index
            if target - index > 0:
                firstHalf = (target - index  + target) * (index + 1) / 2
            else:
                firstHalf = (1 + target) * (target) / 2 + (index + 1 - target)
            if target - n + 1 + index > 0:
                secondHalf = (target - 1 + target - n + 1 + index) * (n - 1 - index) / 2
            else:
                secondHalf = (1 + target - 1) * (target - 1) / 2 + (n - index - target)
            return int(firstHalf + secondHalf)
        
        left, right = 1, 10 ** 9
        while left <= right:
            mid = (left + right) // 2
            curSum = calSum(n, index, mid)
            if curSum <= maxSum:
                left = mid + 1
            else:
                right = mid - 1
        
        return left - 1