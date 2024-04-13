class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        n = len(nums)
        if total_sum % 2 == 1:
            return False

        # a typical dfs problem
        # dfs(start, remain) returns true if there's a subset selected from nums[start:] such that its sum is equal to remain
        @cache
        def dfs(start, remain):
            if remain == 0:
                return True
            if remain < 0 or start >= n:
                return False
            
            # we can make 2 choices: either we include nums[start] or exclude nums[start] in our final answer
            return dfs(start+1, remain) or dfs(start+1, remain-nums[start])

        # we only need to find a subset with sum == total_sum // 2
        return dfs(0, total_sum // 2)
