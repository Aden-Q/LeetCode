class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        s1 = 1
        s2 = 2
        for i in range(3, n+1):
            s2, s1 = s1 + s2, s2
        return s2
            