from sortedcontainers import SortedList

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        sl = SortedList()
        ans = 0
        for num in nums:
            ans += len(sl) - sl.bisect_right(num * 2)
            sl.add(num)

        return ans
