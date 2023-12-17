class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        res = 0
        nums.sort()

        for pivot in range(len(nums) - 2):
            left, right = pivot + 1, len(nums) - 1

            while left < right:
                currSum = nums[pivot] + nums[left] + nums[right]
                if currSum < target:
                    # found the upper bound
                    res +=  right - left
                    # check the next sum (no less than the current sum)
                    left += 1
                else:
                    # move the upper bound until we find the strict upper bound
                    right -= 1
        
        return res
