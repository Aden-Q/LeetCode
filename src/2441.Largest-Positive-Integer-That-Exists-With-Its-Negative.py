class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ans = 0
        for num in nums:
            if -num in nums_set and num > ans:
                ans = num

        return ans if ans > 0 else -1
