class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        g_ptr = len(g) - 1
        s_ptr = len(s) - 1
        while g_ptr >= 0 and s_ptr >= 0:
            if s[s_ptr] >= g[g_ptr]:
                # content
                s_ptr -= 1
            g_ptr -= 1
        
        return len(s) - s_ptr - 1