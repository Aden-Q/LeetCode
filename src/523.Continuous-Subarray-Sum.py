class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {}
        d[0] = -1

        prefix = 0
        for idx, num in enumerate(nums):
            prefix += num
            if prefix % k in d:
                last_idx = d[prefix % k]
                if idx - last_idx >= 2:
                    return True
            else:
                d[prefix % k] = idx

        return False
