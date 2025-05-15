class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        prev, index = 0, 0
        res = []

        while index < n:
            res.append(words[prev])
            while index < n and groups[index] == groups[prev]:
                index += 1

            prev = index

        return res
