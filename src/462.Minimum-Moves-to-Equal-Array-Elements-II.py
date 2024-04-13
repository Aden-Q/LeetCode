class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # prefix sum O(nlogn)
        n = len(nums)
        nums.sort()
        totalSum =sum(nums)
        prefixSum = 0
        minMoves = inf
        for idx, num in enumerate(nums):
            currMoves = (idx * num - prefixSum) + (totalSum - prefixSum - (n - idx) * num)
            minMoves = min(minMoves, currMoves)
            prefixSum += num

        return minMoves
