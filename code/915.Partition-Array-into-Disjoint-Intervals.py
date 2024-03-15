class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        # left_max is the maximum element in the left subarray
        left_max = nums[0]
        # curr_max is the running maximum seen so far
        curr_max = nums[0]
        # the right boundary of the left subarray
        right_boundary = 0
        for idx, num in enumerate(nums):
            if num < left_max:
                # this is the time we need to move the boundary
                # we only move it when it's necessary
                right_boundary = idx
                # when we expand the boundary, we need to update left_max
                left_max = curr_max
            # we always need to keep track of the current maximum in the run
            curr_max = max(curr_max, num)

        return right_boundary + 1
