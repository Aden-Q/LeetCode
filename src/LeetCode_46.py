class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        used = []
        
        def backtracking(nums):
            nonlocal path, res, used
            if len(path) == len(nums):
                res.append(path[:])
            for num in nums:
                if num not in used:
                    used.append(num)
                    path.append(num)
                    backtracking(nums)
                    path.pop()
                    used.pop()
            
        backtracking(nums)
        return res