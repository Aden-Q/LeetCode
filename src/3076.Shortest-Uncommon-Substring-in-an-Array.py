class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        n = len(arr)
        ans = [""] * n
        
        def hasCommon(idx, s) -> bool:
            for i in range(n):
                if i == idx:
                    continue
                if arr[i].find(s) >= 0:
                    return True
            
            return False

        for i in range(n):
            candidates = set()
            for left in range(len(arr[i])):
                for right in range(left, len(arr[i])):
                    sub_s = arr[i][left:right+1]
                    if not hasCommon(i, sub_s):
                        candidates.add(sub_s)
            
            if len(candidates) > 0:
                candidates = list(candidates)
                candidates.sort(key = lambda x: (len(x), x))
                ans[i] = candidates[0]

        return ans
