from sortedcontainers import SortedList

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        # key: value in B
        # value: index of the value in B
        pos_b = [0] * n
        for idx, val in enumerate(nums2):
            pos_b[val] = idx
        
        pre_a = []
        sl = SortedList()
        for num1 in nums1:
            # count how many numbers come before num1 in both arrays
            pre_a.append(sl.bisect_left(pos_b[num1]))
            sl.add(pos_b[num1])

        suf_a = []
        sl.clear()
        for num1 in nums1[::-1]:
            suf_a.append(len(sl) - sl.bisect_left(pos_b[num1]))
            sl.add(pos_b[num1])

        suf_a.reverse()
        ans = 0
        for pre, suf in zip(pre_a, suf_a):
            ans += pre * suf

        return ans
