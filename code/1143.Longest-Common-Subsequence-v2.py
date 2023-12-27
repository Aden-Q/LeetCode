class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 2D dp
        m, n = len(text1), len(text2)

        prev = [0] * (n+1)
        curr = [0] * (n+1)

        for row in reversed(range(m)):
            for col in reversed(range(n)):
                if text1[row] == text2[col]:
                    curr[col] = 1 + prev[col+1]
                else:
                    curr[col] = max(prev[col], curr[col+1])
            prev, curr = curr, prev

        return prev[0]