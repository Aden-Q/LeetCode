class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # the idea is we sort the input list first
        # then we greedily select the largest element in nums such that
        # the sum of all elements smaller than or equal to it is largest than it
        # and this is the final answer
        n = len(nums)
        nums.sort()
        prefix_sum = nums[0] + nums[1]
        res = -1

        for i in range(2, n):
            if prefix_sum > nums[i]:
                res = prefix_sum + nums[i]
            prefix_sum += nums[i]
        
        return res
