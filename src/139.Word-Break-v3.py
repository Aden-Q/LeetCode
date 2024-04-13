class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordDict = set(wordDict)
        dp = [False] * (n+1)
        dp[-1] = True

        for start in range(n, -1, -1):
            for end in range(start+1, n+1):
                if s[start:end] in wordDict and dp[end]:
                    dp[start] = True

        return dp[0]