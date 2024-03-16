from sortedcontainers import SortedList

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -inf
        LHS = SortedList()
        LHS.add(nums[0])
        maxRight = [0] * n
        maxRight[-1] = nums[-1]
        for i in reversed(range(n-1)):
            maxRight[i] = max(nums[i], maxRight[i+1])
        
        for i in range(1, n-1):
            num = nums[i]
            leftMaxNumIdx = LHS.bisect_left(num) - 1
            if leftMaxNumIdx >= 0 and maxRight[i] > num:
                ans = max(ans, LHS[leftMaxNumIdx] - num + maxRight[i])
            LHS.add(num)

        return ans
