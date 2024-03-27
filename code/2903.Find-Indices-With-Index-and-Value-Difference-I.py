from sortedcontainers import SortedList

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        sl = SortedList()
        n = len(nums)

        for i in range(indexDifference, n):
            sl.add((nums[i-indexDifference], i-indexDifference))
            if abs(nums[i] - sl[0][0]) >= valueDifference:
                return [i, sl[0][1]]
            if abs(nums[i] - sl[-1][0]) >= valueDifference:
                return [i, sl[-1][1]]

        return [-1, -1]
