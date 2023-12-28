class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        min_dist = math.inf
        # we keep track of the last seen index for which wordsDict[idx] is either word1 or word2
        prev_idx = -1
        # a flag to avoid extra string comparison 
        prev_is_word1 = False
        for idx in range(len(wordsDict)):
            word = wordsDict[idx]
            if word == word1 == word2:
                if prev_idx != -1:
                    min_dist = min(min_dist, idx - prev_idx)
                prev_idx = idx
            elif word == word1:
                if prev_idx != -1 and not prev_is_word1:
                    min_dist = min(min_dist, idx - prev_idx)
                prev_idx = idx
                prev_is_word1 = True
            elif word == word2:
                if prev_idx != -1 and prev_is_word1:
                    min_dist = min(min_dist, idx - prev_idx)
                prev_idx = idx
                prev_is_word1 = False
        
        return min_dist