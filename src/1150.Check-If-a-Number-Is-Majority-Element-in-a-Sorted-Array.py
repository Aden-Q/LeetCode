class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        idx_left = bisect.bisect_left(nums, target)
        idx_right = bisect.bisect_right(nums, target)

        return idx_right - idx_left > len(nums) / 2
