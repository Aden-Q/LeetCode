class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        table = {}

        for idx, val in enumerate(keyboard):
            table[val] = idx

        res = table[word[0]]
        for i in range(1, len(word)):
            res += abs(table[word[i]] - table[word[i-1]])

        return res