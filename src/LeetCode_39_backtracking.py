class Solution:
    def combinationSum(self, candidates, target: int):
        path = []  # a single solution
        res = []  # a collection of solutions
        
        def backtracking(start, cur_sum):
            nonlocal path
            nonlocal res
            if cur_sum == target:
                # get a solution
                res.append(path[:])
                return
            if cur_sum > target:
                # prune the branch
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtracking(i, cur_sum + candidates[i])  # 重复取
                path.pop()
        
        backtracking(0, 0)
        return res
        
if __name__ == '__main__':
    test = Solution()
    candidates = [2,3,6,7]
    target = 7
    test.combinationSum(candidates, target)