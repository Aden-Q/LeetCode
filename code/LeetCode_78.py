class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        
        def backtracking(nums, start):
            res.append(path[:])
            if start > len(nums) - 1:
                return
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtracking(nums, i+1)
                path.pop()
            
        backtracking(nums, 0)
        return res