class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        g_idx = 0
        ans = 0
        for i in s:
            if i >= g[g_idx]:
                ans += 1
                g_idx += 1

            if g_idx >= len(g):
                break
        
        return ans