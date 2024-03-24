class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        max_len = 0
        for i in range(n):
            for j in range(i+1, n):
                counter = Counter(s[i:j+1])
                vals = list(counter.values())
                vals.sort(reverse=True)
                if vals[0] > 2:
                    continue
                max_len = max(max_len, j - i + 1)
                
        return max_len
