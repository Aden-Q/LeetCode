class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover_right = 0
        idx = 0
        while idx < len(nums) and idx <= cover_right and cover_right < len(nums) - 1:
            if nums[idx] + idx > cover_right:
                cover_right = nums[idx] + idx
            idx += 1
            
        return cover_right >= len(nums) - 1