class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        l1 = []
        l2 = []
        for c in s:
            if c == '#' and len(l1) != 0:
                l1.pop()
            elif c != '#':
                l1.append(c)
        for c in t:
            if c == '#' and len(l2) != 0:
                l2.pop()
            elif c != '#':
                l2.append(c)
        return l1 == l2