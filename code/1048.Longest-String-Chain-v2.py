class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # Let L be the maximum length of a single word
        # Let N be the number of words
        # The sorting has a O(L * NlogN) time complexity, O(LN) space
        # The isPred function has a O(L) time complexity
        # The dp has a O(L * N^2) time complexity, O(N) space
        # So overall, if we do not consider the space taken by sorting
        # The time complexity is O(LN(N + logN)) = O(LN^2) and space is O(N)
        
        def isPred(word1, word2) -> bool:
            # This function is used to check whether word1 is a
            # predecessor of word2
            if len(word1) != len(word2) - 1:
                return False
            ptr1 = 0
            ptr2 = 0
            
            while ptr1 < len(word1) and ptr2 < len(word2):
                if word1[ptr1] == word2[ptr2]:
                    ptr1 += 1
                    ptr2 += 1
                else:
                    ptr2 += 1
            
            return ptr1 == len(word1)
        
        words.sort(key = lambda x : len(x))
        # dp[i] represents the length of the longest possible word chain
        # using words[:i+1] including the last word
        dp = [1] * len(words)
        
        for i in range(1, len(words)):
            for j in range(i):
                # Check whether word[j] is a predecessor of word[i]
                if isPred(words[j], words[i]):
                    # If true, then we can concatenate those two words
                    # and form a new chain
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)