class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        masks = [0] * n
        for i in range(n):
            for c in words[i]:
                masks[i] |= 1 << ord(c) - ord('a')
        max_prod = 0
        for i in range(n):
            for j in range(i+1, n):
                if masks[i] & masks[j] == 0:
                    max_prod = max(len(words[i]) * len(words[j]), max_prod)
        return max_prod