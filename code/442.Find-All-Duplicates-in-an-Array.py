class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # We can use the index as the hash key and sign as the hash value as a presence indicator
        ans = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                # seen before
                ans.append(abs(num))
            
            nums[abs(num) - 1] *= -1

        return ans
