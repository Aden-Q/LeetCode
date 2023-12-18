class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # min_first is the smallest element in the array
        # min_second is the second smallest element in the array
        min_first, min_second = math.inf, math.inf
        # max_first is the largest element in the array
        # max_second is the second largest in the array
        max_first, max_second = -math.inf, -math.inf

        for num in nums:
            if num < min_first:
                min_first, min_second = num, min_first
            elif num < min_second:
                min_second = num
            if num > max_first:
                max_first, max_second = num, max_first
            elif num > max_second:
                max_second = num
        
        return max_first * max_second - min_first * min_second
