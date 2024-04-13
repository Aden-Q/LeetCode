class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # p0 is the rightmost position to store 0
        # p2 is the leftmost position to store 2
        p0, p2 = 0, n - 1
        idx = 0

        while idx <= p2:
            if nums[idx] == 0:
                # store at position nums[p0] and increment p0
                nums[p0], nums[idx] = nums[idx], nums[p0]
                # we may need to visit the same idx again
                p0 += 1
                idx += 1
            elif nums[idx] == 2:
                nums[p2], nums[idx] = nums[idx], nums[p2]
                p2 -= 1
            else:
                # check the next candidate
                idx += 1
        