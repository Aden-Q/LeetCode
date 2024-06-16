class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # index into nums
        idx = 0
        # the smallest number that has not been covered yet
        miss = 1
        # the number of patches (we need to return this as the final answer)
        res = 0

        # loop until we cover [1, n] inclusive
        while miss <= n:
            if idx < len(nums) and nums[idx] <= miss:
                # no need to patch
                miss += nums[idx]
                idx += 1
            else:
                # need to patch "miss"
                miss += miss
                res += 1

        return res
