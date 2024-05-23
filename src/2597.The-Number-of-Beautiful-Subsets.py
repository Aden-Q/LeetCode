class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        # we use a set to represent thsi subset so that we can find x + k, x - k efficiently
        res = 0

        def dfs(idx, path):
            nonlocal res

            if idx == len(nums):
                res += 1
                return

            # if we do not include nums[idx]
            dfs(idx+1, path)

            if nums[idx] + k not in path and nums[idx] - k not in path:
                path[nums[idx]] += 1
                dfs(idx+1, path)
                path[nums[idx]] -= 1
                if path[nums[idx]] == 0:
                    del path[nums[idx]]

        dfs(0, Counter())
        # -1 because of the empty set
        return res - 1      
