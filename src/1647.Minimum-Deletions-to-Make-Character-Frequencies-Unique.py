class Solution:
    def minDeletions(self, s: str) -> int:
        freq = Counter(s)
        sorted_freq = list(freq.values())
        sorted_freq.sort(reverse=True)

        ans = 0
        curr_freq = sorted_freq[0]
        for f in sorted_freq:
            curr_freq = min(f, curr_freq)
            ans += max(0, f - curr_freq)
            curr_freq = max(curr_freq-1, 0)
        
        return ans
