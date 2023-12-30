class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False

        # end1: end of s1, exclusive
        # end2: end of s2, exclusive
        # return whether we can interleave s1[:end1] and s2[:end2] to form s3[:end1+end2]
        dp = [[False] * (n+1) for _ in range(m+1)]
        for col in range(n+1):
            dp[0][col] = s3[:col] == s2[:col]

        for row in range(m+1):
            dp[row][0] = s3[:row] == s1[:row]

        for row in range(1, m+1):
            for col in range(1, n+1):
                if s1[row-1] == s3[row+col-1] and dp[row-1][col]:
                        dp[row][col] = True
                if s2[col-1] == s3[row+col-1] and dp[row][col-1]:
                        dp[row][col] = True

        return dp[m][n]
