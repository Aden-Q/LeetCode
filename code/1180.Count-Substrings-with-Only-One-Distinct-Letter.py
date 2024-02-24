class Solution:
    def countLetters(self, s: str) -> int:
        window = Counter()
        res = 0
        left, right = 0, 0
        while right < len(s):
            window[s[right]] += 1
            # shrink
            while len(window) > 1:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1

            res += list(window.values())[0]
            right += 1

        return res
