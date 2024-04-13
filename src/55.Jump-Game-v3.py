class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # O(N) time, O(1) space
        # One-pass linear scan
        farthest = 0
        for i in range(len(nums)-1):
            farthest = max(farthest, i + nums[i])
            if farthest <= i:
                # Stuck
                return False
        return True  