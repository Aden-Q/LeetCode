class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        max_subset = [nums[0]]

        # returns the largest subset ending at nums[idx] (must use nums[idx])
        @cache
        def dp(idx):
            nonlocal max_subset
            if idx == 0:
                return [nums[idx]]
            
            res = [nums[idx]]
            for i in range(idx-1, -1, -1):
                curr = dp(i)
                if nums[idx] % nums[i] == 0:
                    if len(curr) + 1 > len(res):
                        res = curr.copy()
                        res.append(nums[idx])
            
            if len(res) > len(max_subset):
                max_subset = res
            return res

        dp(len(nums) - 1)

        return max_subset
