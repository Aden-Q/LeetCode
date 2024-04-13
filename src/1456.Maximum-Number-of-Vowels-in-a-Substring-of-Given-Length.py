class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        candidates = set(['a', 'e', 'i', 'o', 'u'])
        
        counter = 0
        for i in range(k):
            if s[i] in candidates:
                counter += 1

        max_counter = counter

        for i in range(k, len(s)):
            if s[i] in candidates:
                counter += 1
            if s[i-k] in candidates:
                counter -= 1

            max_counter = max(max_counter, counter)

        return max_counter
