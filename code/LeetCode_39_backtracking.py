class Solution:
    def combinationSum(self, candidates, target: int):
        path = []  # a single solution
        res = []  # a collection of solutions
        
        def backtracking(idx, cur_sum):
            nonlocal path
            nonlocal res
            if cur_sum == target:
                # get a solution
                res.append(path[:])
                return
            if cur_sum > target or idx > len(candidates) - 1:
                # prune the branch
                return
            max_count = (target - cur_sum) // candidates[idx]
            for i in range(max_count+1):
                for j in range(i):
                    path.append(candidates[idx])
                backtracking(idx+1, cur_sum + i * candidates[idx])
                # revert
                for j in range(i):
                    path.pop()
        
        backtracking(0, 0)
        return res
        
if __name__ == '__main__':
    test = Solution()
    candidates = [2,3,6,7]
    target = 7
    test.combinationSum(candidates, target)