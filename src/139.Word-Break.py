class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        from collections import Counter
        word_dict = Counter(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for word in wordDict:
                if i >= len(word):
                    dp[i] = dp[i] or (dp[i-len(word)] and s[i-len(word):i] == word)
        return dp[len(s)]