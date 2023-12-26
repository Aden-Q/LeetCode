class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # using sliding window, we keep track of the occurance of the most frequent character in the list
        # the window always keep a substring which can contain the same letter after at most k operations as described
        # let the window size be n, the occurance of the most frequent character be t, then we can perform n - t operations
        # thus we need to make sure n - t <= k inside the window
        left, right = 0, 0
        most_freq = 0
        most_freq_char = ''
        counter = Counter()
        res = 0

        while right < len(s):
            counter[s[right]] += 1
            if counter[s[right]] > most_freq:
                most_freq_char = s[right]
                most_freq = counter[s[right]]
            # contract
            if (right - left + 1) - most_freq > k:
                counter[s[left]] -= 1
                # O(26) operation
                # only find a new most frequency when this number change
                if s[left] == most_freq_char:
                    for key, val in counter.items():
                        if val > most_freq:
                            most_freq = val
                            most_freq_char = key
                left += 1

            right += 1

        return right - left