class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        if sum(nums) < x:
            return -1

        # map: suffix -> number of elements
        table = {0: 0}
        suffix = 0
        n = len(nums)
        for i in reversed(range(n)):
            suffix += nums[i]
            if suffix > x:
                # we don't need those
                break
            table[suffix] = n - i

        ans = inf
        if x in table:
            ans = table[x]
        
        prefix = 0
        for i in range(n):
            prefix += nums[i]
            if x - prefix > x:
                # we don't need those
                break
            if x - prefix in table:
                ans = min(ans, i+1 + table[x-prefix])
        
        return ans if ans <= n else -1
