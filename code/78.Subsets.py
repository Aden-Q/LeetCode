class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def dfs(start, curr):
            if start == n:
                res.append(curr[:])
                return
            # make choices
            # either we append nums[start]
            # or we do not append nums[start]
            dfs(start+1, curr)
            curr.append(nums[start])
            dfs(start+1, curr)
            curr.pop()

        dfs(0, [])
        return res