class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # last occurrance position
        hash_table = [0] * 26
        for i in range(len(s)):
            hash_table[ord(s[i]) - ord('a')] = i
        res = []
        left = 0
        right = 0
        for i in range(len(s)):
            right = max(right, hash_table[ord(s[i]) - ord('a')])
            if i == right:
                res.append(right - left + 1)
                left = right + 1
        return res