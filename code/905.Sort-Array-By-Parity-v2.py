class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            parity1 = nums[left] % 2
            parity2 = nums[right] % 2
            if (parity1, parity2) == (1, 0):
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            elif (parity1, parity2) == (0, 0):
                left += 1
            elif (parity1, parity2) == (0, 1):
                left += 1
                right -= 1
            else:
                right -= 1   
        return nums