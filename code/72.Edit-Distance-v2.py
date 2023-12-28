class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        # find the edit distance of word1[:idx1] and word2[:idx2]
        @cache
        def dfs(idx1, idx2):
            if idx1 == 0:
                return idx2
            if idx2 == 0:
                return idx1
            if word1[idx1-1] == word2[idx2-1]:
                return dfs(idx1-1, idx2-1)

            insert_dist = dfs(idx1, idx2-1)
            delete_dist = dfs(idx1-1, idx2)
            replace_dist = dfs(idx1-1, idx2-1)

            return min(insert_dist, delete_dist, replace_dist) + 1

        return dfs(len(word1), len(word2))
