class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        # O(n) time to determine whether p is still a subsequence of s after removals
        def isSubsequence(p, s_list) -> bool:
            idx_p = 0
            idx_s = 0
            while idx_p < len(p) and idx_s < len(s_list):
                if p[idx_p] == s_list[idx_s]:
                    idx_p += 1
                    idx_s += 1
                else:
                    idx_s += 1
            
            return idx_p == len(p)

        # test whether k is a good, we need to find the largest k
        def feasible(k) -> bool:
            s_list = list(s)
            for i in range(k):
                s_list[removable[i]] = ''
            
            return isSubsequence(p, s_list)

        left, right = 0, len(removable) + 1
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                left = mid + 1
            else:
                right = mid
        
        return left - 1
