class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        mode = nums[1] - nums[0]
        for i in range(2, len(nums)):
            next_mode = nums[i] - nums[i-1]
            if next_mode * mode < 0:
                return False
            # find the first non-zero mode
            if mode == 0:
                mode = next_mode
        return True