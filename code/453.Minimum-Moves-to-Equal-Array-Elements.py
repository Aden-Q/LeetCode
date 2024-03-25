class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n = len(nums)
        currSum = sum(nums)
        minVal = min(nums)
        # if k moves, we have increment the mininum value k times
        # so all numbers become minVal + k
        # the sum becomes currSum + (n-1) * k
        # we solve for (minVal + k) * n = currSum + (n-1) * k
        return currSum - minVal * n
