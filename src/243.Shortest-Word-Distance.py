class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        recent_idx1, recent_idx2 = -1, -1
        minDist = math.inf

        for idx in range(len(wordsDict)):
            word = wordsDict[idx]
            if word == word1:
                recent_idx1 = idx
            elif word == word2:
                recent_idx2 = idx
            else:
                continue
            
            if recent_idx1 != -1 and recent_idx2 != -1:
                minDist = min(minDist, abs(recent_idx1 - recent_idx2))
        
        return minDist