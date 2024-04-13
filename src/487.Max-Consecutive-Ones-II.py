class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # a typical dp problem
        n = len(nums)
        # dp[k][0] represents the maximum number of consecutve 1's ending with nums[k] if we don't flip any 0
        # dp[k][1] represents the maximum number of consecutive 1's ending with nums[k] if we flip exactly 1 0
        first, second = 0, 0
        
        # initilize dp
        if nums[0] == 1:
            first, second = 1, 0
        else:
            first, second = 0, 1
        
        maxOnes = 1
        for i in range(1, n):
            if nums[i] == 0:
                # the sublist ends with 0, no consecutive 1's if we don't flip any 0
                first, second = 0, first + 1
            else:
                # the sublist ends with 1
                first, second = first + 1, second + 1
            maxOnes = max(maxOnes, first, second)
        
        return maxOnes