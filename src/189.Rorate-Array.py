class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        res = nums[-k:]
        res.extend(nums[:-k])
        for i in range(len(nums)):
            nums[i] = res[i]