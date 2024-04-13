class Solution:
    def countGoodSubsequences(self, s: str) -> int:
        mod = 10 ** 9 + 7
        freq_counter = Counter(s)
        max_freq = max(freq_counter.values())
        keys = freq_counter.keys()
        ans = 0
        # every character has a given frequency
        for freq in range(1, max_freq + 1):
            curr = 1
            for key in keys:
                if freq_counter[key] >= freq:
                    curr *= (comb(freq_counter[key], freq) + 1)
                    curr = curr % mod

            # rule out the empty subsequence
            ans = (ans + curr - 1) % mod
        
        return ans
