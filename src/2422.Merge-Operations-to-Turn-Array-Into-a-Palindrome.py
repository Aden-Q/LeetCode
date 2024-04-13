class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        step = 0
        while left < right:
            if nums[left] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] < nums[right]:
                nums[left+1] += nums[left]
                left += 1
                step += 1
            else:
                nums[right-1] += nums[right]
                right -= 1
                step += 1

        return step
