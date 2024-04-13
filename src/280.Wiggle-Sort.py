class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return
        
        # starting from index 1, we check the element right before it, first we expect the trend to be nono-decreasing
        # i.e. nums[0] <= nums[1], then we expect the trend to be non-increasing, alternately
        should_increase = True

        for i in range(1, len(nums)):
            if should_increase:
                if nums[i] < nums[i-1]:
                    # we swap those 2 elements to make it non-decreasing
                    nums[i], nums[i-1] = nums[i-1], nums[i]
            else:
                if nums[i] > nums[i-1]:
                    # we swap those 2 elements to make it non-increasing
                    nums[i], nums[i-1] = nums[i-1], nums[i]
            
            should_increase = not should_increase 

        return
