class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()
        n = len(nums)

        def dfs(curr):
            nonlocal res
            nonlocal seen
            if len(curr) == n:
                res.append(curr[:])

            # make choices
            for num in nums:
                if num in seen:
                    continue
                curr.append(num)
                # cannot use this element in recursive calls
                seen.add(num)
                dfs(curr)
                curr.pop()
                seen.remove(num)
        
        dfs([])
        return res
