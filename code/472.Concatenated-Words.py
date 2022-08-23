class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        hashset = set(words)
        
        # dp[i] represents whether word can be constructed from words
        def dp(word, i, memo):
            nonlocal hashset
            if i == len(word):
                return True
            if memo[i] != 'Unknown':
                return memo[i]
            
            for j in range(i, len(word)):
                # Check whether the prefix word[i:j+1] is in the words list
                if word[i:j+1] in hashset and (i, j+1) != (0, len(word)):
                    # A common prefix is found, check memo
                    if dp(word, j+1, memo):
                        memo[i] = True
                        return memo[i]
                    # Otherwise check the next word
                    
            memo[i] = False
            return memo[i]
        
        res = []
        # A memo for each word
        for word in words:
            memo = ['Unknown'] * len(word)
            if dp(word, 0, memo):
                res.append(word)
        return res