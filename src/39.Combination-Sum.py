class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        # dfs and backtrack
        # recursion_stack represents all the element selected so far in the current resursive call
        # idx represents the starting index to select elements from the candidate list
        def dfs(recursion_stack, remain, idx):
            if remain == 0:
                res.append(recursion_stack[:])
                return

            if idx >= len(candidates):
                # impossible
                return
            
            # make choices
            cnt = 0
            curr = candidates[idx]
            while remain - cnt * curr >= 0:
                recursion_stack.extend([curr] * cnt)
                dfs(recursion_stack, remain - cnt * curr, idx+1)
                for _ in range(cnt):
                    recursion_stack.pop()

                cnt += 1

        dfs([], target, 0)
        return res
