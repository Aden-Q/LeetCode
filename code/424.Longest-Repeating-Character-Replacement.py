class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # using sliding window, we keep track of the occurance of the most frequent character in the list
        # the window always keep a substring which can contain the same letter after at most k operations as described
        # let the window size be n, the occurance of the most frequent character be t, then we can perform n - t operations
        # thus we need to make sure n - t <= k inside the window
        left, right = 0, 0
        most_freq = 0
        counter = Counter()

        while right < len(s):
            counter[s[right]] += 1
            most_freq = max(most_freq, counter[s[right]])
            # contract
            if (right - left + 1) - most_freq > k:
                counter[s[left]] -= 1
                # trick here, we don't need to change the frequency
                # if s[left] is the most frequent character, then some other element s[j] has the same
                # frequency given the current window, for which we don't need to update most_freq
                # or counter[s[j]] < counter[s[left]] for all j in [left...right]. We also don't need to
                # update most_freq in this case
                left += 1

            right += 1

        return right - left