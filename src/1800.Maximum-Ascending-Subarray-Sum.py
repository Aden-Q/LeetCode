class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSum = 0
        currSum = 0
        prev = 0

        for num in nums:
            if num > prev:
                currSum += num
            else:
                currSum = num

            prev = num
            maxSum = max(maxSum, currSum)

        return maxSum
