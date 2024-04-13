class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        path = []
        
        def backtrack(start):
            nonlocal res, path, s, wordDict
            # End state
            if start == len(s):
                res.append(" ".join(path))
                return
            
            # Make a choice
            for word in wordDict:
                if s[start:start + len(word)] == word:
                    # A match is found
                    path.append(word)
                    # Recursion
                    backtrack(start + len(word))
                    path.pop()
                    
            return
        
        backtrack(0)
        return res