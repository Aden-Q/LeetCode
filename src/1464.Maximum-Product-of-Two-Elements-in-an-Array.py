class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # first: largest element seen so far
        # second: second largest element seen so far
        first, second = nums[0], nums[1]
        if first < second:
            first, second = second, first

        for i in range(2, len(nums)):
            if nums[i] > first:
                first, second = nums[i], first
            elif nums[i] > second:
                second = nums[i]
        
        return (first - 1) * (second - 1)
