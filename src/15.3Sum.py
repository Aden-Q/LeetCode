class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pivot = 0
        res = []
        nums.sort()

        while pivot < len(nums) - 2:
            left, right = pivot + 1, len(nums) - 1
            target = -nums[pivot]

            while left < right:
                currSum = nums[left] + nums[right]
                if currSum < target:
                    left += 1
                elif currSum > target:
                    right -= 1
                else:
                    res.append([nums[pivot], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    right -= 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
            
            # skip duplicates
            pivot += 1
            while pivot < len(nums) - 2 and nums[pivot] == nums[pivot-1]:
                pivot += 1
        
        return res
