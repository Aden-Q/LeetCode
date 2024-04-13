class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        # keep track of the minimum and maximum, so at most 2 elements in the array
        # order: smaller, larger
        candidates = []
        n = len(nums)

        for i in range(indexDifference, n):
            if len(candidates) < 2:
                candidates.append((nums[i-indexDifference], i-indexDifference))
                candidates.sort()
            elif nums[i-indexDifference] > candidates[1][0]:
                candidates[1] = (nums[i-indexDifference], i-indexDifference)
            elif nums[i-indexDifference] < candidates[0][0]:
                candidates[0] = (nums[i-indexDifference], i-indexDifference)

            if abs(nums[i] - candidates[0][0]) >= valueDifference:
                return [i, candidates[0][1]]
            if abs(nums[i] - candidates[-1][0]) >= valueDifference:
                return [i, candidates[-1][1]]

        return [-1, -1]
