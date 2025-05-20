class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        # the idea: for each index in nums, check how many query in the give queries array contain this index

        diffArray = [0] * (n + 1)
        for l, r in queries:
            diffArray[l] += 1
            diffArray[r + 1] -= 1

        prefixSum = 0
        for i in range(n):
            # prefixSum calculates how many times we can decrement the current value at most
            prefixSum += diffArray[i]
            if prefixSum < nums[i]:
                return False

        return True
