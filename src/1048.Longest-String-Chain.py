class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def isPredecessor(word1, word2):
            ''' Return True if word1 is a predecessor of word2
            '''
            cnt = 0
            if len(word1) != len(word2) - 1:
                return False
            i = 0
            for j in range(len(word2)):
                if word2[j] == word1[i]:
                    i += 1
                if i == len(word1):
                    return True
            return False
        
        words.sort(key = lambda a : len(a))
        dp = [1] * len(words)
        for i in range(len(words)):
            for j in range(i):
                if isPredecessor(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)