from sortedcontainers import SortedList

class Solution:
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        # a typical binary search problem
        mod = 10 ** 9 + 7
        prefix = 0
        all_prefix = SortedList([0])
        ans = 0
        for num in nums:
            if num == 1:
                prefix += 1
            else:
                prefix -= 1
            ans += all_prefix.bisect_right(prefix-1)
            ans %= mod
            all_prefix.add(prefix)
        
        return ans
