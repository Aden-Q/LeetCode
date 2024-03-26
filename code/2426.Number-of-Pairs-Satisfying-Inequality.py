from sortedcontainers import SortedList

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)
        # nums1[i] - nums2[i] <= nums1[j] - nums2[j] + diff
        sl = SortedList()
        ans = 0
        for i in range(n):
            val = nums1[i] - nums2[i]
            sl.add(val)
            pivot = sl.bisect_right(val + diff)
            if diff >= 0:
                ans += pivot - 1
            else:
                ans += pivot
        
        return ans
