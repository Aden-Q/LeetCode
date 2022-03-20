class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        size = len(nums)
        nums.sort()
        
        def backtracking(nums, start):
            nonlocal path, res
            if len(path) <= size:
                res.append(path[:])
            else:
                return
            i = start
            while i < size:
                path.append(nums[i])
                backtracking(nums, i+1)
                path.pop()
                i += 1
                while i < size and nums[i] == nums[i-1]:
                    i += 1
                
        backtracking(nums, 0)
        return res